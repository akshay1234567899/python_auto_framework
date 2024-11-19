from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class MyAccountPage:

    lnk_logout_xpath = "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a" #xpath for logout

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        try:
            wait = WebDriverWait(self.driver, 20)  # Increased timeout
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_logout_xpath)))
            element.click()
        except TimeoutException:
            print("Timeout: The logout link was not clickable.")
        except NoSuchElementException:
            print("Error: The logout link was not found.")
