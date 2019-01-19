from pageObjects import LoginPage


class LoginAction(object):
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            login.getKey("loginPage.username").send_keys(username)
            login.getKey("loginPage.password").send_keys(password)
            login.getKey("loginPage.loginButton").click()
        except Exception as e:
            raise e