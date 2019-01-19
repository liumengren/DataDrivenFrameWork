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
    driver = webdriver.Firefox(executable_path="D:\\Browserdriver\\geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    print(searchBox.tag_name)
    aList = getElements(driver, "tag name", "a")
    print(len(aList))
    driver.quit()