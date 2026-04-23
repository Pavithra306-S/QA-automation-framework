
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
   def __init__(self,driver):
       self.driver = driver

    # locators
   username_input = (By.ID, 'user-name')
   password_input = (By.ID, 'password')
   login_button = (By.ID, 'login-button')
   error_message = (By.CLASS_NAME, 'error-message-container')
   product_page_title = (By.CLASS_NAME, 'title')
   # Actions
   def enter_username(self,username):
       self.driver.find_element(*self.username_input).clear()
       self.driver.find_element(*self.username_input).send_keys(username)

   def enter_password(self,password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

   def click_login(self):
       wait = WebDriverWait(self.driver, 5)
       wait.until(EC.element_to_be_clickable(self.login_button)).click()

   def get_error_message(self):
       wait = WebDriverWait(self.driver, 5)
       error_message = wait.until(EC.presence_of_element_located(self.error_message)).text
       return error_message

   def get_page_title(self):
       return self.driver.find_element(*self.product_page_title).text
