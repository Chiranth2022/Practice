from pom.login import LoginPage
from utility.config import Config
import pytest

@pytest.mark.login
def test_login(driver_):
    Lp=LoginPage(driver_)
    Lp.select_login_link()
    Lp.enter_username_txt(Config.USERNAME)
    Lp.enter_password_txt(Config.PASSWORD)
    Lp.select_login_btn()
