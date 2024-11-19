from selenium.webdriver.common.by import By


class LoginPage():
    txt_email_xpath = '//*[@id="input-email"]'
    txt_password_xpath = '//*[@id="input-password"]'
    btn_login_xpath = '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button'
    msg_myaccount_xpath = "/html/body/main/div[2]/div/div/h2[1]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False

