import random
import string
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Staff:
    # Locator for Staff page
    staff_menu="//span[text()='Staff']"
    staff_page_title="//h6[text()='Staff List']"
    staff_add_button_xpath="//span[text()='Add Staff']"
    staff_details_header_path="//h6[text()='Add Staff']"
    staff_success_toast_path="//div[normalize-space(text())='Staff added Successfully!']"
    # Staff details
    first_name_path="//input[@name='first_name']"
    password_path="//input[@name='password']"
    confirm_password_path="//input[@name='confirm_password']"
    email_path="//input[@name='email']"
    address_path="//textarea[@name='address_one']"
    city_path="//input[@name='city']"
    state_field_path="(//div[@class='ant-select-selector'])[1]"
    zip_code_path="//input[@name='zip_code']"
    category_field_path="(//div[@class='ant-select-selector'])[2]"
    status_field_path="(//div[@class='ant-select-selector'])[3]"
    save_staff_btn_path="//span[text()='Add Staff']"
    state_value_path="//div[@title='California']"
    category_value_path="//div[@title='Admin']"




    def __init__(self,driver):
        self.driver=driver

    def staff_module_select(self):
        self.driver.find_element(By.XPATH,self.staff_menu).click()
        wait=WebDriverWait(self.driver,20)
        self.staff_title=wait.until(EC.presence_of_element_located((By.XPATH,self.staff_page_title)))

    def staff_add_button_click(self):
        wait = WebDriverWait(self.driver, 20)
        self.staff_add_btn= wait.until(EC.presence_of_element_located((By.XPATH, self.staff_add_button_xpath)))
        self.driver.find_element(By.XPATH,self.staff_add_button_xpath).click()

    def enter_staff_details(self,f_name,password_1,password_2,email,address,city,state,zipcode,category):
        wait_actions=ActionChains(self.driver)
        wait=WebDriverWait(self.driver,20)
        self.staff_d_page=wait.until(EC.presence_of_element_located((By.XPATH,self.staff_details_header_path)))
        self.driver.find_element(By.XPATH,self.first_name_path).send_keys(f_name)
        self.driver.find_element(By.XPATH,self.password_path).send_keys(password_1)
        self.driver.find_element(By.XPATH,self.confirm_password_path).send_keys(password_2)
        self.driver.find_element(By.XPATH,self.email_path).send_keys(email)
        self.driver.find_element(By.XPATH,self.address_path).send_keys(address)
        self.driver.find_element(By.XPATH,self.city_path).send_keys(city)

        # Hidden dropdown value select option for state ----Method one---
        # self.driver.find_element(By.XPATH,self.state_field_path).click()
        # drop_option=self.driver.find_element(By.XPATH,self.state_value_path)
        # drop_option.click()

        # Hidden dropdown value select option for state ----Method Two---
        wait_actions=ActionChains(self.driver)
        state_field=self.driver.find_element(By.XPATH,self.state_field_path)
        wait_actions.move_to_element(state_field).click().perform()
        # self.state_value = wait.until(EC.presence_of_element_located((By.XPATH, self.category_value_path)))
        wait_actions.send_keys(state+Keys.ENTER).perform()
        # Hidden dropdown value select option for state ----Method three---
        # state_field=self.driver.find_element(By.XPATH, self.state_field_path)
        # state_field.click()
        # state_field.send_keys("California")
        # state_field.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.zip_code_path).send_keys(zipcode)
        # Hidden dropdown for category
        category_button_down = self.driver.find_element(By.XPATH, self.category_field_path)
        wait_actions.move_to_element(category_button_down).click().perform()
        self.category_value = wait.until(EC.presence_of_element_located((By.XPATH, self.category_value_path)))
        wait_actions.send_keys(category+Keys.ENTER).perform()
        # actions.move_to_element(self.driver.find_element(By.XPATH, self.category_value_path)).click().perform()


    def click_staff_save_btn(self):
        action=ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        save_button_down=self.driver.find_element(By.XPATH,self.save_staff_btn_path)
        action.move_to_element(save_button_down).click().perform()
        self.driver.find_element(By.XPATH,self.save_staff_btn_path).click()
        self.success_toast = wait.until(EC.visibility_of_element_located((By.XPATH, self.staff_success_toast_path)))


def random_generator(size=6,char=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for i in range(size))





