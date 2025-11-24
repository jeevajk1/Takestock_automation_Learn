from Pageobject.Loginpage import Login
from utilities.read_properties_login import Readconfig
from utilities.Custom_Logger import LogGen
from utilities import XLutils
import pytest
from selenium.webdriver.common.by import By

class Test_001_DDT_Login:
    path="C:/Users/jeeva.ss/PycharmProjects/Takestock_uat/Testdata/name_list.xlsx"
    sheet="Sheet1"
    login_error="// div[text() = 'Login Failed! Please check username and password']"
    url = Readconfig.getapplicationURL()
    logs=LogGen.loggen()

    rowcount=XLutils.getRowCount(path,sheet)
    testdata=[]
    for r in range(2,rowcount+1):
        username=XLutils.readData(path,sheet,r,1)
        password=XLutils.readData(path,sheet,r,2)
        testdata.append((username,password))
        print(testdata)



    def test_valid_login_ddt(self, setup,username,password,test): #Login with valid details
        print(f"Login with{username},{password}")
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.set_username(username)
        self.lp.set_password(password)
        self.lp.click_login()
        # self.lp.dashboard_header_check()
        if self.lp.welcome_element.text == "Welcome Super Admin !":
            assert self.lp.welcome_element.is_displayed(),"Login Success"
        else:
            assert self.driver.find_element(By.XPATH,self.login_error).text,"Login Failed"
        self.driver.close()


    # def test_invalid_login(self,setup): #Login with the username and without password
    #     self.driver=setup
    #
    #     self.driver.get(self.url)
    #     self.lp=Login(self.driver)
    #     self.lp.set_username(self.invalid_username)
    #     self.lp.set_password(self.invalid_password)
    #     self.lp.click_login()
    #     self.lp.login_invalid_toast()
    #     if self.lp.error_login.is_displayed():
    #         assert True
    #     else:
    #         assert False
