import utils, settingsTools, locales, os

settings = settingsTools.loadSettings()

locales = locales.Locales()

def searchJDK():
    for file in os.listdir():
        if ("jdk" in file and not os.path.isfile(os.path.join(".", file))):
            utils.setJavaHome(file)
            return True
    jdk = os.environ.get("JAVA_HOME")
    # why tf your jdk points to recycle bin bitch are you retarted
    return jdk is not None and utils.verifyPath(jdk)

def downloadJDK():
    if (not searchJDK() or settings["force_install_jdk"] == True):
        JDK_LINK = settings["jdk_link"]
        JDK_ZIP_NAME = settings["jdk_zip_name"]
        utils.downloadFileAndExtract(JDK_LINK, JDK_ZIP_NAME)
        # Set JAVA_HOME and PATH
        utils.setJavaHome("jdk-14.0.2")
        os.environ["PATH"] = os.environ["PATH"]+";"+os.path.join(os.environ["JAVA_HOME"], "bin")
