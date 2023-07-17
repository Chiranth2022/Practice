from utility.generic import SeleniumWrapper

login_link=('link text',"Log in")
username_txt=('id','Email')
password_txt=('id','Password')
login_btn=('xpath',"//input[@class='button-1 login-button']")
class LoginPage(SeleniumWrapper):
    def select_login_link(self):
        self.click_on_element(login_link)
    def enter_username_txt(self,username):
        self.enter_txt(username_txt,value=username)
    def enter_password_txt(self,pwd):
        self.enter_txt(password_txt,value=pwd)
    def select_login_btn(self):
        self.click_on_element(login_btn)