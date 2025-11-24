from selenium import webdriver
import pytest
# from selenium.webdriver.chrome.options import Options
#
# options=options()
# options.add_arguments("--browser")
# driver=webdriver.Chrome(options=options)

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        raise Exception(" Unsupported Browser! ")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


