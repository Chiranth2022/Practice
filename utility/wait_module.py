from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_(func):
    def wrapper(*args, **kwargs):
        instance,locator=args
        wait_object=WebDriverWait(instance.driver,timeout=5,)
        wait_object.until(EC.visibility_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper