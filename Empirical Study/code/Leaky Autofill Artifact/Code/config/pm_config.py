class PMConfig(object):
    """ Properties of each password manager
    
    Safari cannot be tested with this tool as it does not allow human operations, thus making it impossible to enter data and also not supporting the method of loading local profiles, therefore we do it manually.

    Args:
        click_ele_properties (dict): Element.rect including x, y, width, and height 
        name (dict): Name of the password manager 
        type (dict): Type of the password manager, including browser, extension, and firefox (as Firefox is different from chromium-based browsers)
        tri_icon (dict): The (x, y) offset to trigger the autofill functionality, which is expected to show the popup window of the autofill functionality 
        drop_icon (dict): The (x, y) offset to click the pop-up window to trigger the password manager to fill the data into web forms
        require_login_time (dict): Time required to complete the log into the password manager and/or enter the test data into the password manager manually. Some PMs require two-step authentication, re-CAPTCHA, or risk-based authentication, thus the number varies between PMs.
        whether_multiple_handles (dict): Whether the form will generate new handles during autofill
        handle_click_ele_xpath (dict): The xpath for processing the new handle  
        whether_alert (dict): Whether the form will generate alert warnings during autofill 
        whether_right_click (dict): Whether the password manager needs right click to autofill. If so, or the autofill functionality needs to be triggered by clicking the icon on the address bar (things may be difficult to handle using Selenium), we wait for some time and do it manually. 
    """
    
    def __init__(self, click_ele_properties: dict) -> None:
        self.cep: dict = click_ele_properties

        one_password: dict = {
            "name": "1password",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1],
            "drop_icon": [0, self.cep["height"]],
            "require_login_time": 20, # Required time for logging into the Password Manager / May vary among different password managers
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": True,
                "whether_right_click": False
            }
        }
        
        lastpass: dict = {
            "name": "lastpass",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1],
            "drop_icon": [0, self.cep["height"]],
            "require_login_time": 60,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": True,
                "handle_click_ele_xpath": "/html/body/div/div/div[3]/div/button[2]",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": True,
                "handle_click_ele_xpath": "/html/body/div/div/div[3]/div/button[2]",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        avira: dict = {
            "name": "avira",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1],
            "drop_icon": [0, self.cep["height"] * 1.75],
            "require_login_time": 60,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        norton: dict = {
            "name": "norton",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1],
            "drop_icon": [0, self.cep["height"] * 3.0],
            "require_login_time": 80,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        bitwarden: dict = {
            "name": "bitwarden",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1],
            "drop_icon": [0, self.cep["height"]],
            "require_login_time": 60,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            },
            "cvv": {
                "whether_multiple_handles": True,
                "handle_click_ele_xpath": "False",
                "whether_alert": False,
                "whether_right_click": True
            }
        }
        
        kaspersky: dict = {
            "name": "kaspersky",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0],
            "drop_icon": [self.cep["width"], self.cep["height"] * 0.1],
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        dashlane: dict = {
            "name": "dashlane",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, self.cep["height"] * 0.1], 
            "drop_icon": [0, self.cep["height"] * 3.0], 
            "require_login_time": 50,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        keeper: dict = {
            "name": "keeper",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 6.0],
            "require_login_time": 60,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            }
        }
        
        multipassword: dict = {
            "name": "multipassword",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, 0], 
            "drop_icon": [self.cep["width"], self.cep["height"]], 
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        truekey: dict = {
            "name": "truekey",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 4.0], 
            "require_login_time": 60,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        roboform: dict = {
            "name": "roboform",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.55, -self.cep["height"] * 0.5], 
            "drop_icon": [self.cep["width"] * 0.75, -self.cep["height"] * 0.5], 
            "require_login_time": 10,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        dualsafe: dict = {
            "name": "dualsafe",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 3.0], 
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        nordpassdesktop: dict = {
            "name": "nordpassdesktop",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 2.0],
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        nordpassextension: dict = {
            "name": "nordpassextension",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 2.0], 
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        expressvpn: dict = {
            "name": "expressvpn",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"]],
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        passbolt: dict = {
            "name": "passbolt",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.475, 0], 
            "drop_icon": [0, self.cep["height"] * 2.0], 
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        protopass: dict = {
            "name": "protopass",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.475, 0], 
            "drop_icon": [self.cep["width"] * 0.25, self.cep["height"] * 2.0], 
            "require_login_time": 40,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        dropbox: dict = {
            "name": "dropbox",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.45, 0], 
            "drop_icon": [0, self.cep["height"] * 2.0], 
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        keepassxc: dict = {
            "name": "keepassxc",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, 0], 
            "drop_icon": [0, self.cep["height"]], 
            "require_login_time": 10,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        zoho_vault: dict = {
            "name": "zoho_vault",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.475, 0], 
            "drop_icon": [self.cep["width"] * 1.0, self.cep["height"] * 3.0],
            "require_login_time": 50,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        enpass: dict = {
            "name": "enpass",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, 0], 
            "drop_icon": [0, self.cep["height"]], 
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        m_autofill: dict = {
            "name": "m_autofill",
            "type": "extension",
            "tri_icon": [self.cep["width"] * 0.1, 0], 
            "drop_icon": [0, self.cep["height"]],
            "require_login_time": 100,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        safeincloud: dict = {
            "name": "safeincloud",
            "type": "extension",
            "tri_icon": [0, 0],
            "drop_icon": [0, self.cep["height"] * 3.0],
            "require_login_time": 20,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": True
            }
        }
        
        icloud: dict = {
            "name": "icloud",
            "type": "extension",
            "tri_icon": [0, 0],
            "drop_icon": [0, self.cep["height"] * 2.0],
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        chrome: dict = {
            "name": "chrome",
            "type": "browser",
            "tri_icon": [0, 0],
            "drop_icon": [self.cep["width"] * 0.25, self.cep["height"] * 0.5],
            "require_login_time": 5,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        edge: dict = {
            "name": "edge",
            "type": "browser",
            "tri_icon": [0, 0],
            "drop_icon": [self.cep["width"] * 0.5, self.cep["height"] * 2.0],
            "require_login_time": 50,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        opera: dict = {
            "name": "opera",
            "type": "browser",
            "tri_icon": [0, 0],
            "drop_icon": [self.cep["width"] * 0.25, self.cep["height"] * 1.0],
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        brave: dict = {
            "name": "brave",
            "type": "browser",
            "tri_icon": [0, 0],
            "drop_icon": [self.cep["width"] * 0.25, self.cep["height"] * 1.0],
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }
        
        firefox: dict = {
            "name": "firefox",
            "type": "firefox",
            "tri_icon": [0, 0],
            "drop_icon": [self.cep["width"] * 0.25, self.cep["height"] * 1.0],
            "require_login_time": 30,
            "login": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "pii": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            },
            "cvv": {
                "whether_multiple_handles": False,
                "handle_click_ele_xpath": "",
                "whether_alert": False,
                "whether_right_click": False
            }
        }

        self.pm_dict: dict = {
            "1password": one_password,
            "lastpass": lastpass,
            "avira": avira, 
            "norton": norton,
            "bitwarden": bitwarden,
            "kaspersky": kaspersky,
            "dashlane": dashlane,
            "keeper": keeper,
            "multipassword": multipassword,
            "truekey": truekey,
            "roboform": roboform,
            "dualsafe": dualsafe,
            "nordpassdesktop": nordpassdesktop,
            "nordpassextension": nordpassextension,
            "passbolt": passbolt,
            "protopass": protopass,
            "expressvpn": expressvpn,
            "dropbox": dropbox,
            "keepassxc": keepassxc,
            "zoho_vault": zoho_vault,
            "enpass": enpass,
            "safeincloud": safeincloud,
            "m_autofill": m_autofill,
            "icloud": icloud,
            "chrome": chrome,
            "edge": edge,
            "opera": opera,
            "brave": brave,
            "firefox": firefox,
            "empty": {}
        }
    
    # return properties of targeted password manager 
    def get_pm_properties(self, pm_name: str) -> dict:
        if pm_name in self.pm_dict:
            return self.pm_dict[pm_name]
        else:
            return self.pm_dict["empty"]