import configparser

config= configparser.RawConfigParser()
config.read(r'C:\Users\jeeva.ss\PycharmProjects\Takestock_uat\Configuration\config.ini')

class Readconfig:
    @staticmethod
    def getapplicationURL():
        application_url=config.get('Login_info','url')
        return application_url

    @staticmethod
    def getvalidusername():
        valid_name=config.get('Login_info','valid_username')
        return valid_name

    @staticmethod
    def getvalidpassword():
        valid_password=config.get('Login_info','valid_password')
        return valid_password

    @staticmethod
    def getinvalidusername():
        invalid_name=config.get('Login_info','invalid_username')
        return invalid_name

    @staticmethod
    def getinvalidpassword():
        invalid_password=config.get('Login_info','invalid_password')
        return invalid_password
