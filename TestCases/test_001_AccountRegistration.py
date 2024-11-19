import os
import time

from PageObject.HomePage import HomePage
from PageObject.AccountRegistrationPage import AccountRegistrationPage
from utility import randomeString
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()  # get value from .ini file
    logger = LogGen.loggen()

    def test_account_reg(self, setup):
        self.logger.info("*** Test_001_AccReg started ***")
        self.driver = setup
        self.logger.info("Launching browser")

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("Entering registration details...")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")

        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("test@123")
        time.sleep(2)

        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        time.sleep(5)

        self.confmsg = self.regpage.getconfirmationmsg()
        self.logger.info(f"Confirmation message received: {self.confmsg}")

        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account Registration Test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.error("Account Registration Test Failed")
            screenshot_path = os.path.abspath(os.curdir) + "\\ScreenShot\\test_account_reg.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            self.driver.close()
            assert False

        self.logger.info("*** Test_001_AccReg Ended ***")
