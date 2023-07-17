from utility.wait_module import wait_


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait_
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait_
    def enter_txt(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    def accept_alert(self):
        self.driver.switch_to.alert().accept()