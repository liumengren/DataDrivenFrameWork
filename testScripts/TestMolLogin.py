# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from time import sleep
from util.Log import *
import traceback


excelObj = ParseExcel()
excelObj.loadWorkBook(dataFilePath)


def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver =webdriver.Chrome(executable_path="D:\\Browserdriver\\chromedriver.exe", chrome_options=chrome_options)
    driver.get("http://www.baidu.com")
    sleep(3)
    return driver


def testMail():
    try:
        userSheet = excelObj.getSheetByName("账号")
        isExecuteUser = excelObj.getColumn(userSheet, account_isExecute)
        dataBookColumn = excelObj.getColumn(userSheet, account_dataBook)
        for idx, i in enumerate(isExecuteUser[1:]):
            if i.value == "y":
                userRow = excelObj.getRow(userSheet, idx+2)
                userName = userRow[account_username-1].value
                password = str(userRow[account_password-1].value)
                print(userName, password)
                driver = launchBrowser()
                LoginAction.login(driver, userName, password)
                sleep(3)
                dataBookName = dataBookColumn[idx+1].value
                print(dataBookName)
                contactPersonSheet = excelObj.getSheetByName(dataBookName)
                isExecuteData = excelObj.getColumn(contactPersonSheet, contacts_isExecute)
                contactNum = 0
                isExecuteNum = 0
                for idy, data in enumerate(isExecuteData[1:]):
                    if data.value == "y":
                        isExecuteNum += 1
                        contactPersonRow = excelObj.getRow(contactPersonSheet, idy+2)
                        contactPersonName = contactPersonRow[contacts_contactPersonName-1].value
                        print(contactPersonName)

    except Exception as e:
        raise e


if __name__ == '__main__':
    testMail()