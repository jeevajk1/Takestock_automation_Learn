import time

import pytest

from Pageobject.Staff_add import Staff
from testCase.test_login import Test_001_Login
from utilities.read_properties_staff_details import Read_Config_Staff


class Test_002_staff:
    first_name=Read_Config_Staff.get_f_name()
    password=Read_Config_Staff.get_staff_password()
    confirm_password=Read_Config_Staff.get_staff_confirm_password()
    email_id=Read_Config_Staff.get_staff_email()
    address_one=Read_Config_Staff.get_staff_address_one()
    city=Read_Config_Staff.get_staff_city()
    state=Read_Config_Staff.get_staff_state()
    zip_code=Read_Config_Staff.get_staff_zip_code()
    category=Read_Config_Staff.get_staff_category()

    @pytest.mark.regression
    def test_staff_redirect(self,setup):
        self.login=Test_001_Login()
        self.login.test_valid_login(setup)
        self.staff=Staff(setup)
        self.staff.staff_module_select()
        if self.staff.staff_title.is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_staff_add_btn_click(self,setup):
        self.login=Test_001_Login()
        self.login.test_valid_login(setup)
        self.staff=Staff(setup)
        self.staff.staff_module_select()
        self.staff.staff_add_button_click()

    @pytest.mark.regression
    def test_staff_details(self,setup):
        self.login=Test_001_Login()
        self.login.test_valid_login(setup)
        self.staff=Staff(setup)
        self.staff.staff_module_select()
        self.staff.staff_add_button_click()
        self.staff.enter_staff_details(self.first_name,self.password,self.confirm_password,self.email_id,self.address_one,self.city,self.state,self.zip_code,self.category)
        self.staff.click_staff_save_btn()
        if self.staff.success_toast.is_displayed():
            assert True
        else:
            assert False, "Success toast is not captured"


