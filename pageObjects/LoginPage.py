# encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class LoginPage(object):
    def __init__(self, driver, sectionname):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemSection(sectionname)
        print(self.loginOptions)

    def getKey(self, optionName):
        try:
            locateType, locatorExpression = self.loginOptions[optionName.lower()].split(">")
            print(locateType, locatorExpression)
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox(executable_path="D:\\Browserdriver\\geckodriver.exe")
    driver.get("http://mol.uat.bwoilmarine.com/mybusiness/#/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    login = LoginPage(driver, "Mol_login")
    login.getKey("loginPage.username").send_keys("CargoOwnerMOL@bwoil.com")
    login.getKey("loginPage.password").send_keys("00000000")
    time.sleep(10)
    login.getKey("loginPage.loginButton").click()
    time.sleep(10)
    driver.quit()