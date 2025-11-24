import pytest

from Pageobject.Loginpage import Login
from utilities.read_properties_login import Readconfig
from utilities.Custom_Logger import LogGen

class Test_001_Login:

    url = Readconfig.getapplicationURL()
    valid_username=Readconfig.getvalidusername()
    valid_password=Readconfig.getvalidpassword()
    invalid_username=Readconfig.getinvalidusername()
    invalid_password=Readconfig.getinvalidpassword()
    logs=LogGen.loggen()


    @pytest.mark.regression
    def test_homepage_title(self,setup):
        self.logs.info("*******Test_001_Login*******")
        self.driver=setup
        self.driver.get(self.url)
        act_title=self.driver.title
        if act_title == "TakeStock":
            assert True
        else:
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup): #Login with valid details
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.set_username(self.valid_username)
        self.lp.set_password(self.valid_password)
        self.lp.click_login()
        self.lp.dashboard_header_check()
        assert self.lp.welcome_element.text == "Welcome Super Admin !"

    @pytest.mark.regression
    def test_invalid_login(self,setup): #Login with the username and without password
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.set_username(self.invalid_username)
        self.lp.set_password(self.invalid_password)
        self.lp.click_login()
        self.lp.login_invalid_toast()
        if self.lp.error_login.is_displayed():
            assert True
        else:
            assert False

