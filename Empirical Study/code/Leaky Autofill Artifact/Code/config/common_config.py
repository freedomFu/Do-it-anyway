import sys
from typing import List, Dict


class CommonConfig(object):
    user_name: str = "artifact"
    root_path: str = f"C:\\Users\\{user_name}\\Desktop\\Artifact\\"
    driver_path: str = f"{root_path}\\Driver\\"

    # Used browsers and drivers
    chrome_driver: str = (
        f"{driver_path}\\Chrome.128.0.6613.84\\chromedriver-win64\\chromedriver.exe"
    )
    chrome_path: str = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    chrome_user_profile: str = (
        f"C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data\\"
    )
    chrome_profile_dir: str = f"Default"

    edge_driver: str = (
        f"{driver_path}\\Edge.128.0.2739.42\\edgedriver_win64\\msedgedriver.exe"
    )

    firefox_driver: str = (
        f"{driver_path}\\Firefox.129.0.2\\geckodriver-v0.34.0-win32\\geckodriver.exe"
    )
    firefox_path: str = f"C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    opera_driver: str = (
        f"{driver_path}\\Opera.127.0.6533.120\\chromedriver-win64\\chromedriver.exe"
    )
    opera_path: str = (
        f"C:\\Users\\{user_name}\\AppData\\Local\\Programs\\Opera\\opera.exe"
    )

    brave_driver: str = (
        f"{driver_path}\\Brave.128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
    )
    brave_path: str = (
        "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    )

    # password manager extension
    pm_extension: dict = {
        "1password": "./1Password/aeblfdkhhhdcdjpifhhbdiojplfjncoa/2.23.3_0",
        "lastpass": "./LastPass/hdokiejnpimakedhajhdlcegeplioahd/4.130.2.1_0",
        "avira": "./Avira/caljgklbbfbcjjanaijlacgncafpegll/2.20.0.4570_0",
        "norton": "./Norton/admmjipmmciaobhojoghlmleefbicajg/8.2.0.161_0",
        "bitwarden": "./BitWarden/nngceckbapebfimnlniiiahkandclblb/2024.4.1_0",
        "kaspersky": "./Kaspersky/dhnkblpjbkfklfloegejegedcafpliaa/24.0.128.1_0",
        "dashlane": "./Dashlane/fdjamakpfbbddfjaooikfcpapjohcfmg/6.2418.0_0",
        "keeper": "./Keeper/bfogiafebfohielmmehodmfbbebbbpei/16.8.3_0",
        "multipassword": "./MultiPassword-Password Manager/cnlhokffphohmfcddnibpohmkdfafdli/0.97.4_0",
        "truekey": "./TrueKey/cpaibbcbodhimfnjnakiidgbpiehfgci/4.3.1.9339_0",
        "roboform": "./RoboForm/pnlccmojcmeohlpggmfnbbiapkmbliob/9.5.9.2_0",
        "dualsafe": "./DualSafe/lgbjhdkjmpgjgcbcdlhkokkckpjmedgc/1.4.28_0",
        "nordpassdesktop": "./NordPass desktop app version/fooolghllnmhmmndgjiamiiodkpenpbb/5.15.28_0",
        "nordpassextension": "./NordPass/eiaeiblijfjekdanodkjadfinkhbfgcd/5.15.29_0",
        "expressvpn": "./ExpressVPNKeys/blgcbajigpdfohpgcmbbfnphcgifjopc/2.0.12.715_0",
        "passbolt": "./passbolt/didegimhafipceonhjepacocaffmoppf/4.7.7_0",
        "protopass": "./Proton Pass/ghmbeldphafepmbegfdlkpapadhbakde/1.16.7_0",
        "dropbox": "./Dropbox/bmhejbnmpamgfnomlahkonpanlkcfabg/3.26.0_1",
        "keepassxc": "./KeePassXC-Browser/oboonakemofpalcgghocfoadofidjkkk/1.9.0.4_0",
        "zoho_vault": "./Zoho Vault/igkpcodhieompeloncfnbekccinhapdb/4.0_0",
        "enpass": "./Enpass/kmcfomidfpdkfieipokbalgegidffkal/6.9.3_0",
        "m_autofill": "./Microsoft Autofill/fiedbfgcleddlbcmgdigjgdfcggjcion/2.0.5_0",
        "safeincloud": "./SafeInCloud/lchdigjbcmdgcfeijpfkpadacbijihjl/24.1.0_0",
        "icloud": "./iCloud/pejdijmoenmkgeppbflobdenhhabjlaj/2.2.9_0",
        "chrome": "",
        "edge": "",
        "opera": "",
        "brave": "",
        "firefox": "",
        "safari": "",
    }

    lastpass: str = "./LastPass/hdokiejnpimakedhajhdlcegeplioahd/4.130.2.1_0"
    avira: str = "./Avira/caljgklbbfbcjjanaijlacgncafpegll/2.20.0.4570_0"
    norton: str = "./Norton/admmjipmmciaobhojoghlmleefbicajg/8.2.0.161_0"
    onepassword: str = "./1Password/aeblfdkhhhdcdjpifhhbdiojplfjncoa/2.23.3_0"
    bitwarden: str = "./BitWarden/nngceckbapebfimnlniiiahkandclblb/2024.4.1_0"
    kaspersky: str = "./Kaspersky/dhnkblpjbkfklfloegejegedcafpliaa/24.0.128.1_0"
    dashlane: str = "./Dashlane/fdjamakpfbbddfjaooikfcpapjohcfmg/6.2418.0_0"
    icloud: str = "./iCloud/pejdijmoenmkgeppbflobdenhhabjlaj/2.2.9_0"
    keeper: str = "./Keeper/bfogiafebfohielmmehodmfbbebbbpei/16.8.3_0"
    multipassword: str = (
        "./MultiPassword-Password Manager/cnlhokffphohmfcddnibpohmkdfafdli/0.97.4_0"
    )
    truekey: str = "./TrueKey/cpaibbcbodhimfnjnakiidgbpiehfgci/4.3.1.9339_0"
    roboform: str = "./RoboForm/pnlccmojcmeohlpggmfnbbiapkmbliob/9.5.9.2_0"
    dualsafe: str = "./DualSafe/lgbjhdkjmpgjgcbcdlhkokkckpjmedgc/1.4.28_0"
    nordpass: str = (
        "./NordPass desktop app version/fooolghllnmhmmndgjiamiiodkpenpbb/5.15.28_0"
    )
    expressvpn: str = "./ExpressVPNKeys/blgcbajigpdfohpgcmbbfnphcgifjopc/2.0.12.715_0"
    dropbox: str = "./Dropbox/bmhejbnmpamgfnomlahkonpanlkcfabg/3.26.0_1"
    keepassxc: str = "./KeePassXC-Browser/oboonakemofpalcgghocfoadofidjkkk/1.9.0.4_0"
    nordpass2: str = "./NordPass/eiaeiblijfjekdanodkjadfinkhbfgcd/5.15.29_0"
    nordpass2_newest: str = (
        "./NordPass/newest/eiaeiblijfjekdanodkjadfinkhbfgcd/5.21.9_0"
    )
    passbolt: str = "./passbolt/didegimhafipceonhjepacocaffmoppf/4.7.7_0"
    protopass: str = "./Proton Pass/ghmbeldphafepmbegfdlkpapadhbakde/1.16.7_0"
    m_autofill: str = "./Microsoft Autofill/fiedbfgcleddlbcmgdigjgdfcggjcion/2.0.5_0"
    zoho_vault: str = "./Zoho Vault/igkpcodhieompeloncfnbekccinhapdb/4.0_0"
    enpass: str = "./Enpass/kmcfomidfpdkfieipokbalgegidffkal/6.9.3_0"
    safeincloud: str = "./SafeInCloud/lchdigjbcmdgcfeijpfkpadacbijihjl/24.1.0_0"
