# import winreg

if __name__ == "__main__":
    #  connecting to key in registry
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    access_key = winreg.OpenKey(
        access_registry, r"SOFTWARE\Microsoft\Windows\CurrentVersion"
    )
    #  accessing the key to open the registry directories under
    for i in range(1024):
        try:
            asubkey_name = winreg.EnumKey(access_key, i)
            asubkey = winreg.OpenKey(access_key, asubkey_name)
            val = winreg.OpenKeyEx(asubkey, "chrome.exe")
            enum = winreg.EnumValue(asubkey, 0)
            print("{}; {}/{}".format(i, asubkey, enum))
        except EnvironmentError:
            pass
