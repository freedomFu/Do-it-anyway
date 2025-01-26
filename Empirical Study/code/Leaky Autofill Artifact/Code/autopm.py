import os
import random
import time
import argparse
from datetime import datetime
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.chrome.service import Service as CService
from selenium.webdriver.edge.options import Options as EOptions
from selenium.webdriver.edge.service import Service as EService
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.firefox.service import Service as FService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import psutil
import win32api
import win32con
import loguru

from config.common_config import CommonConfig
from config.pm_config import PMConfig
from config.form_config import FormConfig
from utils.util import Utils

""" AutoPM class aims to initiate Selenium, start a browser instance (with Password Manager extensions). With human's assistance, this semi-automatic tool can trigger the autofill functionality of password managers (most of our tested password managers).
"""
class AutoPM(object):
    """ Initializes Selenium with Targeted PMs (Extensions are located in Chrome browser)

    Args:
        - name (str): Name of the tested password manager.
        - is_local (bool): whether browser instance is the locally-installed browser, default False. We suggest the autofill functionality testers use the Selenium-generated browsers to avoid the influence of locally-installed browsers. (However, in some cases, PMs require risk-based authentication, where we could not login successfully in Selenium-generated browsers).
    """
    def __init__(self, name: str = "", is_local: bool = False):
        self.name = name
        # self.extension = extension
        # Whether we should wait for some time for users to login. As the Selenium accesses varies web pages, we just need to login once for one test.
        self.wait_time: bool = False
        self.logger = loguru.logger
        
        try:
            # Relative Path to the tested PM extension. If the string is empty string, the PM name is expected to be a browser-based PM. 
            self.extension = CommonConfig.pm_extension[self.name]
        except KeyError:
            self.logger.error(f"Unknown key: {self.name}")
            exit(0)
        
        if name == "chrome": # Chrome browser-based PM
            options = COptions()
            service = CService(CommonConfig.chrome_driver)
            options.binary_location = CommonConfig.chrome_path
            if is_local: 
                options.add_argument("--user-data-dir=" + CommonConfig.chrome_user_profile)
                options.add_argument("--profile-directory=" + CommonConfig.chrome_profile_dir)
                options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
            self.driver = webdriver.Chrome(service=service, options=options)
        elif name == "edge": # Edge browser-based PM
            options = EOptions()
            service = EService(CommonConfig.edge_driver)
            self.driver = webdriver.Edge(service=service, options=options)
        elif name == "firefox": # Firefox browser-based PM
            options = FOptions()
            service = FService(CommonConfig.firefox_driver)
            options.binary_location = CommonConfig.firefox_path
            self.driver = webdriver.Firefox(service=service, options=options)
        elif name == "opera": # Opera browser-based PM 
            options = COptions()
            service = CService(CommonConfig.opera_driver)
            options.binary_location = CommonConfig.opera_path
            options.add_experimental_option("w3c", True)
            self.driver = webdriver.Chrome(service=service, options=options)
        elif name == "brave": # Brave browser-based PM
            options = COptions()
            service = CService(CommonConfig.brave_driver)
            options.binary_location = CommonConfig.brave_path
            self.driver = webdriver.Chrome(service=service, options=options)
        else: # extensions in chrome browser
            options = COptions()
            options.add_argument("--disable-cache")
            if is_local: # Local browser instance and user profile are initiated (For Chrome in the Artifact)
                options.binary_location = CommonConfig.chrome_path
                options.add_argument("--user-data-dir=" + CommonConfig.chrome_user_profile)
                options.add_argument("--profile-directory=" + CommonConfig.chrome_profile_dir)
                options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
            if self.extension != "":
                options.add_argument("--load-extension=" + CommonConfig.root_path + "/Extension/" + self.extension)
            service = CService(CommonConfig.chrome_driver)
            self.driver = webdriver.Chrome(service=service, options=options)
        
        
        self.dpr = self.driver.execute_script("return window.devicePixelRatio")
        self.logger.info(f"The current DPR is {self.dpr}.")
        if self.dpr != 1:
            self.logger.warning("The current DPR is not 1, which could lead to our test failure.")
        self.action = ActionChains(self.driver)
        # start a webpage with 1920 * 1080
        self.driver.set_window_size(1920, 1080)
        # self.driver.get("https://example.com")
        # time.sleep(100)
    
    """ Create directories for each password manager

    Args:
        type_name (str): Name of the directory type, e.g., screenshots, logs, and results
        pm_name (str): Name of the password manager
    """
    def create_dir(self, type_name: str, pm_name: str) -> None:
        folder_name = f"./{type_name}/{pm_name}/"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    
    """ Test specific password managers with specific form types

    Args:
        form_type (str): 
        is_self (str): 
    """
    def test_webpage_list(
        self,
        form_type: str,
        is_self: bool = True
    ) -> None:
        info: str = "<input> element is concealed" if is_self is True else "<input>'s ancestor <div> element is concealed"
        self.logger.success(f"=========[BEGIN-{info}]==============")
        self.logger.add(f"./logs/{self.name}/{self.name}_{form_type}_{is_self}.log")
        form_properties: dict = FormConfig.get_form_properties(form_type)
        test_site_dict: dict = form_properties["list_page"]
        simple_page_dict: dict = form_properties["simple_page"]
        if is_self:
            info_dict = test_site_dict["self"]
            simple_page = simple_page_dict["self"]
        else:
            info_dict = test_site_dict["parent"]
            simple_page = simple_page_dict["parent"]
        
        # Get the rect info of the click trigger element
        click_element_id: str = form_properties["click_ele_id"]
        self.logger.info("Accessing the original webpage to get the [rect] info of the click element.")
        self.driver.get(info_dict["original"])
        click_ele: WebElement = self.driver.find_element(By.ID, value=form_properties["click_ele_id"])
        click_ele_rect: dict = click_ele.rect
        # click_ele_rect: dict = {key: value * self.dpr for key, value in click_ele_rect.items()}
        click_ele_rect: dict = {key: value for key, value in click_ele_rect.items()}
        pm_config = PMConfig(click_ele_properties=click_ele_rect) # Get the PM properties from password manager configs.
        pm_info: dict = pm_config.get_pm_properties(self.name)
        # print(pm_info)
        
        self.driver.get(simple_page)
        # Wait for some time to store the data or log into the PM
        if self.wait_time is False:
            time.sleep(pm_info["require_login_time"])
            self.wait_time = True

        results: dict = {}

        for k in info_dict:
            name: str = k
            url: str = info_dict[k]
            try:
                ret: bool = self.test_one_webpage(
                    tech_name=name,
                    url=url,
                    pm_info=pm_info,
                    form_type=form_type
                )
                results[k] = ret
                # Clear the Cache
                if self.name != "chrome" and self.extension != "":
                    self.driver.get("chrome://settings/clearBrowserData")
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, value='/html/body/settings-ui').send_keys(Keys.TAB)
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, value='/html/body/settings-ui').send_keys(Keys.ENTER)
                else:
                    pass
            except Exception as e:
                self.logger.error(str(e))
                self.logger.error(f"An error happens: {self.name}--{name}--{url}")
                continue
            time.sleep(random.randint(1, 2))
        self.logger.success(f"=========[END-{info}]==============")
        now = datetime.now()
        time_str = now.strftime("%Y%m%d_%H%M%S")
        with open(f"./results/{self.name}/[{form_type}]_results_{time_str}.txt", "w") as f:
            for k, v in results.items():
                value = 1 if v is True else 0 
                f.write(f"{k},{value}\n")
    
    """ Test one webpage for autofill functionality in filling forms with hidden fields. Researchers may need to change the code below to satisfy their needs. The main functionality of this function includes:
        - Trigger the autofill functionality of the password manager.
        - Click the autofill pop-up window, triggering the PM to fill in the form in the webpage. 
        - Record the filled results.
    Args:
        tech_name (str): element concealment technology 
        url (str): the corresponding URL 
        pm_info (str): the corresponding PM information / properties
        form_type (str): form type, login, pii, pii-email, cvv 
    """
    def test_one_webpage(
        self,
        tech_name: str,
        url: str,
        pm_info: str,
        form_type: str
    ) -> bool:
        # get the checked fields to determine whether fields are filled
        form_properties: dict = FormConfig.get_form_properties(form_type)
        if form_properties is None:
            self.logger.error("Wrong form type [login, pii, pii-email cvv] inputted.")
            return None
        check_value_id_list: list = form_properties["check_value_list"]
        sensitive_value_list: list = form_properties["sensitive_value_list"]
        # 0. Create directories for storing screenshots, logs and results
        self.create_dir(type_name="screenshots", pm_name=self.name)
        self.create_dir(type_name="logs", pm_name=self.name)
        self.create_dir(type_name="results", pm_name=self.name)

        # 1. Get the current window process, this is especially important for browser-based PMs
        main_process = psutil.Process(self.driver.service.process.pid)
        # get the pid of Chrome main process (the first of all chrome processes)
        main_process_pid = main_process.children(recursive=True)[0].pid
        # self.logger.info(f"The current process is {main_process_pid}")
        # Get the window processes. As the browser just begins, there should be only a single window
        # self.logger.info(f"Current handle: {Utils.get_hwnds_by_pid(main_process_pid)}")
        
        # 2. Access the tested link: url
        self.driver.get(url)
        # Wait for loading
        time.sleep(random.randint(1, 2))
        self.driver.refresh()
        time.sleep(random.randint(1, 2))
        # Get the current handle
        main_window_handle = self.driver.current_window_handle
        # [Screenshot] for page loading
        self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_page_loading_{form_type}.png")
        time.sleep(random.randint(1, 2))
        
        # # 3. Test whether the PM autofills the fields on page loading
        # if tech_name == "original":
        #     # on page load - check flag
        #     on_page_load_flag: bool = False
        #     check_value_list: List[str] = []
        #     for i in check_value_id_list:
        #         check_value: str = self.driver.execute_script(f"return document.getElementById('{i}').value;")
        #         check_value_list.append(check_value)
        #     for i in check_value_list:
        #         if i != "":
        #             self.logger.info("Autofill on page load")
        #             on_page_load_flag = True
        #             break
        #     if on_page_load_flag is False:
        #         self.logger.info("Nothing filled on page load")
        #     time.sleep(0.5)
        
        # 3. Click the clicked element to trigger the PM autofill pop-up window 
        click_ele: WebElement = self.driver.find_element(By.ID, value=form_properties["click_ele_id"])
        click_ele_rect: dict = click_ele.rect
        
        # Click other place to lose focus, and then come back to focus
        self.action.move_to_element(click_ele).move_by_offset(
            click_ele_rect["width"], 0
        ).click().perform()
        self.action.move_to_element(click_ele).perform() # re-focus
        self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_click_element_field_focus_{form_type}.png")
        time.sleep(random.randint(1, 2))
        
        pm_type: str = pm_info["type"]
        trigger_icon: list = pm_info["tri_icon"]
        drop_icon: list = pm_info["drop_icon"]
        pm_form_property = pm_info[form_type]
        
        if pm_type == "browser":
            self.action.move_to_element(click_ele).click().perform() # the autofill overlay is the module of the browser itself
            time.sleep(random.randint(1, 2))
            self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_pm_icon_click_{form_type}.png")
            # When the password manager window pop up, a new window process will generate. Note that the window does not belong to the web DOM but the browser, I fail to locate it by selenium
            # Now the variable should contain two elements. And need to switch to the process.
            hwnds_after_click = Utils.get_hwnds_by_pid(main_process_pid)
            # self.logger.info(f"The current handle is {hwnds_after_click}")
            # the first one is the password manager generated pop-up windows
            hwnd_pm = hwnds_after_click[0]
            mk_position = win32api.MAKELONG(int(drop_icon[0]), int(drop_icon[1]))
            win32api.SendMessage(hwnd_pm, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, mk_position)
            win32api.SendMessage(hwnd_pm, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, mk_position)
            time.sleep(random.randint(1, 2))
        elif pm_type == "extension":
            # e.g., Bitwarden, Keeper's pii and cvv
            if pm_form_property["whether_right_click"]:
                # move a bit far to right-click, and wait for sometime to conduct the right click
                self.action.move_to_element(click_ele)
                self.action.move_by_offset(click_ele_rect["width"], click_ele_rect["height"]).context_click().perform()
                time.sleep(10)
            else:
                pm_icon_x = trigger_icon[0]
                pm_icon_y = trigger_icon[1]
                icon_x = drop_icon[0]
                icon_y = drop_icon[1]
                
                self.action.move_to_element(click_ele).move_by_offset(pm_icon_x, pm_icon_y).click().perform()
                self.logger.info("Click the PM icon to Trigger the Password Manager")
                time.sleep(random.randint(1, 2))
                self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_pm_icon_click_{form_type}.png")
                # self.logger.info(self.driver.window_handles)
                # Move to the rendered overlay and click it to get the data filled
                self.action.move_to_element(click_ele).move_by_offset(icon_x, icon_y).click().perform()
                self.logger.info("Click the drop menu to fill the data.")
                time.sleep(random.randint(1, 2))
                
                # Clicking the overlay may generate a new pop-up window, e.g., 1Password
                if pm_form_property["whether_multiple_handles"]:
                    all_windows_handles: list = self.driver.window_handles
                    if len(all_windows_handles) > 1:
                        for windows_handle in all_windows_handles:
                            if windows_handle != main_window_handle:
                                self.driver.switch_to.window(windows_handle)
                                break
                        self.driver.find_element(By.XPATH, value=pm_form_property["handle_click_ele_xpath"]).click()
                        self.driver.switch_to.window(main_window_handle)

                time.sleep(random.randint(1, 2))

                # Clicking the overlay may generate an alert dialog
                if pm_form_property["whether_alert"]:
                    try:
                        alert = self.driver.switch_to.alert
                        alert.accept()
                    except Exception as e:
                        self.logger.error(e)
            
            self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_pm_autofill_{form_type}.png")

        elif pm_type == "firefox":
            self.action.move_to_element(click_ele).click().perform() # the autofill overlay is the module of the browser itself
            if form_type == "pii":
                self.action.move_to_element(click_ele).click().perform()
            time.sleep(random.randint(1, 2))
            self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_pm_icon_click_{form_type}.png")
            self.action.move_to_element(click_ele).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(random.randint(1, 2))
            self.driver.save_screenshot(f"./screenshots/{self.name}/[{tech_name}]_after_pm_autofill_{form_type}.png")

        # 4. get the filled data
        check_filled_value_list: List[str] = []
        checked_sensitive_value_list: List[str] = []
        for i in check_value_id_list:
            check_value: str = self.driver.execute_script(f"return document.getElementById('{i}').value;")
            check_filled_value_list.append(check_value)
            if i in sensitive_value_list:
                checked_sensitive_value_list.append(check_value)

        if tech_name != "original":
            for i in check_filled_value_list:
                self.logger.info(f"Hidden technique {tech_name} test for PM {self.name} - {i}")
        else:
            for i in check_filled_value_list:
                if i != "":
                    self.logger.info(f"Test original origin successfully - {i}")
        for i in checked_sensitive_value_list:
            if i != "":
                return True
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Testing autofill functionality")
    parser.add_argument('--pm_name', type=str, help='[The name of the tested password manager]')
    parser.add_argument('--form_type', type=str, help='[login, pii, cvv， pii-email(for keeper)]')
    parser.add_argument('--is_input', type=int, help='[0 for False, 1 for True]')
    parser.add_argument('--is_local', type=int, help='[0 for False, 1 for True]')
    args = parser.parse_args()
    is_self: bool = True if args.is_input == 1 else False
    is_local: bool = True if args.is_local == 1 else False
    
    # CommonConfig.m_autofill
    auto_pm = AutoPM(name=args.pm_name, is_local=is_local)
    auto_pm.test_webpage_list(form_type=args.form_type, is_self=is_self)