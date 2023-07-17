from utility.generic import SeleniumWrapper

register_link = ('link text', 'Register')
male_radio_btn = ('id', 'gender-male')
female_radio_btn = ('id', 'gender-female')
firstname_txt = ('id', 'FirstName')
lastname_txt = ('id', 'LastName')
email_txt = ('id', 'Email')
password_txt = ('id', 'Password')
confirm_password_txt = ('id', 'ConfirmPassword')
register_btn=('id', 'register-button')


class RegistrationPage(SeleniumWrapper):

    def click_register_link(self):  # driver.find_element(*register_link).click()
        self.click_on_element(register_link)

    def select_male_radio_btn(self):  # driver.find_element(*male_radio_btn).click()
        self.click_on_element(male_radio_btn)

    def select_female_radio_btn(self):  # driver.find_element(*female_radio_btn).click()
        self.click_on_element(female_radio_btn)

    def enter_firstname_txt(self, fname):  # driver.find_element(*firstname_txt).send_keys('Chiranth')
        self.enter_txt(firstname_txt, value=fname)

    def enter_lastname_txt(self, lname):  # driver.find_element(*lastname_txt).send_keys('K V')
        self.enter_txt(lastname_txt, value=lname)

    def enter_mail_txt(self, mail):  # driver.find_element(*email_txt).send_keys('chiru22py@gmail.com')
        self.enter_txt(email_txt, value=mail)

    def enter_password_txt(self, pwd):  # driver.find_element(*lastname_txt).send_keys('Python@2022')
        self.enter_txt(password_txt, value=pwd)

    def enter_confirmpassword_txt(self, confirm_pwd):  # driver.find_element(*lastname_txt).send_keys('Python@2022')
        self.enter_txt(confirm_password_txt, value=confirm_pwd)

    def click_register_btn(self):
        self.click_on_element(register_btn)