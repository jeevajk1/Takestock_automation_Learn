from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    # Locators
    email_id="signin-email"
    password_id="signin-password"
    login_button_xpath="//a[text()='Login']"
    logout_icon_xpath="//a[@title='Logout']"
    logout_alert_box_xpath="//button[text()='Yes']"
    dashboard_header="//center[text()='Welcome Super Admin !']"
    login_invalid_xpath="//div[text()='Login Failed! Please check username and password']"

    def __init__(self,driver):
        self.driver=driver


    def set_username(self,username):
        self.driver.find_element(By.ID,self.email_id).clear()
        self.driver.find_element(By.ID,self.email_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_icon_xpath).click()
        self.driver.find_element(By.XPATH,self.logout_alert_box_xpath).click()

    def dashboard_header_check(self):
        wait = WebDriverWait(self.driver, 10)
        self.welcome_element=wait.until(EC.presence_of_element_located((By.XPATH,self.dashboard_header)))

    def login_invalid_toast(self):
        wait = WebDriverWait(self.driver, 20)
        self.error_login = wait.until(EC.visibility_of_element_located((By.XPATH, self.login_invalid_xpath)))
