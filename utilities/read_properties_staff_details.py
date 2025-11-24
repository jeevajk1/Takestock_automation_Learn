import configparser

config=configparser.RawConfigParser()
config.read(r'C:\Users\jeeva.ss\PycharmProjects\Takestock_uat\Configuration\config.ini')

class Read_Config_Staff:

    @staticmethod
    def get_f_name():
        first_name=config.get('Staff_details','first_name')
        return first_name
    @staticmethod
    def get_staff_password():
        password_staff=config.get('Staff_details','password')
        return password_staff
    @staticmethod
    def get_staff_confirm_password():
        confirm_password=config.get('Staff_details','confirm_password')
        return confirm_password
    @staticmethod
    def get_staff_email():
        staff_email_id=config.get('Staff_details','email')
        return staff_email_id
    @staticmethod
    def get_staff_address_one():
        staff_address_one=config.get('Staff_details','address_one')
        return staff_address_one
    @staticmethod
    def get_staff_city():
        staff_city=config.get('Staff_details','city')
        return staff_city
    @staticmethod
    def get_staff_state():
        staff_state=config.get('Staff_details','state')
        return staff_state
    @staticmethod
    def get_staff_zip_code():
        staff_zip_code=config.get('Staff_details','zip_code')
        return staff_zip_code
    @staticmethod
    def get_staff_category():
        staff_category=config.get('Staff_details','category')
        return staff_category

