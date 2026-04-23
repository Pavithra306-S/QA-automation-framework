from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #     locators
    add_to_cart_button = (By.ID,"add-to-cart-sauce-labs-backpack")
    cart_button = (By.CLASS_NAME,"shopping_cart_link")
    cart_quantity = (By.CLASS_NAME,"shopping_cart_badge")

    def click_add_to_cart_button(self):
        self.wait.until(
            EC.visibility_of_element_located(self.add_to_cart_button)
        )
        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def click_cart_button(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.cart_button)
        )

        # Scroll (important for headless)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Use JS click (most reliable)
        self.driver.execute_script("arguments[0].click();", element)

        # 🔥 Wait for actual navigation
        self.wait.until(EC.url_contains("cart"))

    def check_cart_quantity(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_quantity)).text

