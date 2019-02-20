from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except Exception as e:
        raise e


def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox(executable_path="D:\\Browserdriver\\geckodriver.exe")
    driver.get("http://mol.uat.bwoilmarine.com/mybusiness/#/login")
    driver.maximize_window()
    time.sleep(10)
    username = getElement(driver, "id", "username")
    password = getElement(driver, "id", "password")
    loginButton =getElement(driver, "xpath", '//span[text()="Login"]/..')
    username.send_keys("CargoOwnerMOL@bwoil.com")
    password.send_keys("00000000")
    time.sleep(10)
    loginButton.click()
    time.sleep(10)
    driver.quit()