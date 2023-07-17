from pom.registration import RegistrationPage
from utility.config import Config
import pytest

data=[('Ciranth','K V','chiru22py@gmail.com','Python@2022','Python@2022'),('chintu',"K",'chinthu22@gmail.com','Chintu@2003','Chintu@2003')]
@pytest.mark.register
@pytest.mark.parametrize("fname, lname, mail, pwd, confirm_pwd",data)
def test_register(fname,lname,mail,pwd,confirm_pwd,driver_):
    try:
        rp = RegistrationPage(driver_)
        rp.click_register_link()
        rp.select_male_radio_btn()
        rp.enter_firstname_txt(fname)
        rp.enter_lastname_txt(lname)
        rp.enter_mail_txt(mail)
        rp.enter_password_txt(pwd)
        rp.enter_confirmpassword_txt(confirm_pwd)

    except Exception as msg:
        from datetime import datetime
        td = datetime.now()
        driver_.save_screenshot(Config.SCREENSHOT_PATH + f"screenshot-{td.day}-{td.month}-{td.year}.jpg")
        raise msg

