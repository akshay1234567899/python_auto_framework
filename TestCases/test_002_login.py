import os
import time

from PageObject.HomePage import HomePage
from PageObject.AccountRegistrationPage import AccountRegistrationPage
from PageObject.LoginPage import LoginPage
from utility import randomeString
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self,setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)

        self.targetpage=self.lp.isMyAccountPageExists()
        time.sleep(5)
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\ScreenShot\\" + "test_login.png")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")
