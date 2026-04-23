from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    item_in_cart =(By.CLASS_NAME,"inventory_item_name")
    remove = (By.ID,"remove-sauce-labs-backpack")
    cart_items = (By.CLASS_NAME,"cart_item")
    cart_page_title = (By.CLASS_NAME,"title")


    def get_cart_page_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_page_title)).text

    def get_item_in_cart(self):
        return self.wait.until(EC.presence_of_element_located(self.item_in_cart)).text
    def remove_item_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.remove)).click()

    def is_cart_empty(self):
        self.wait.until(lambda d: len(d.find_elements(*self.cart_items)) == 0)
        return True