import time

from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    chk_policy_name = "agree"
    btn_continue_xpath = '/html/body/main/div[2]/div/div/form/div/button'
    text_msg_conf_xpath = "/ html / body / main / div[2] / div / div / h1"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
            self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)


    def setEmail(self, email):
         self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)


    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)


    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()


    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()


        time.sleep(5)


    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None
