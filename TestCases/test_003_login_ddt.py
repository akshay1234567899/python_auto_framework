import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.HomePage import HomePage
from PageObject.AccountRegistrationPage import AccountRegistrationPage
from PageObject.LoginPage import LoginPage
from PageObject.MyAccountPage import MyAccountPage
from utility import randomeString, XLUtils
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen


class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    # Path to Excel file
    path = os.path.abspath(os.curdir) + "\\TestData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Initialize Page Objects
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        # Get total number of rows in Excel sheet
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info(f"Total Rows in Excel: {self.rows}")

        # List to track test statuses
        lst_status = []   #store the result of execution

        # Loop through the Excel data
        for r in range(2, self.rows + 1):
            self.hp.clickMyAccount()

            # Wait for the "Login" link to be clickable
            try:
                login_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
                )
                login_link.click()
            except Exception as e:
                self.logger.error(f"Error while locating the Login link: {str(e)}")
                lst_status.append('Fail')
                continue

            # Read data from Excel
            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.logger.info(f"Testing with Email: {self.email}, Password: {self.password}, Expected: {self.exp}")

            # Perform login actions
            self.lp.setEmail(self.email)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)

            self.lp.clickLogin()
            time.sleep(2)


            # Validation
            time.sleep(2)  # Optional: Reduce sleep time for faster execution
            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage:
                    self.logger.info("Login Successful - Test Passed")
                    lst_status.append('Pass')
                    time.sleep(2)
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()
                    time.sleep(2)
                else:
                    self.logger.error("Login Failed - Test Failed")
                    lst_status.append('Fail')
                    time.sleep(2)
            elif self.exp == 'Invalid':
                if self.targetpage:
                    self.logger.error("Login should have failed, but it succeeded - Test Failed")
                    lst_status.append('Fail')
                    time.sleep(2)
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()
                    time.sleep(2)
                else:
                    self.logger.info("Login Failed as expected - Test Passed")
                    lst_status.append('Pass')
                    time.sleep(2)

            # Adding a slight delay to ensure stability
            time.sleep(2)
            print("The final list is: ", lst_status, flush=True)
            self.logger.info(f"The final list of test statuses: {lst_status}")
        # Close the browser
        self.driver.close()

        # Final validation of all test cases
        if "Fail" not in lst_status:
            self.logger.info("All data-driven tests passed.")
            assert True
        else:
            self.logger.error("One or more data-driven tests failed.")
            assert False

        self.logger.info("******* End of test_003_login_Datadriven **********")

