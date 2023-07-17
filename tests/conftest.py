from selenium import webdriver
import pytest
from utility.config import Config

# @pytest.fixture(params=['chrome','edge'])
@pytest.fixture(params=Config.BROWSER)
def driver_(request):
    browser=request.param
    if browser == "chrome":
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option('detach',True)
        driver = webdriver.Chrome(options=opts)
    elif browser == "edge":
        opts=webdriver.EdgeOptions()
        opts.add_experimental_option('detach',True)
        driver = webdriver.Edge(options=opts)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.quit()