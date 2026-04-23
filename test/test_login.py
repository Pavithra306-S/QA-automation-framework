import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("username,password,expected_error",
                          [
                              ("","secret_sauce", "Username is required"),
                              ("standard_user","", "Password is required"),
                              ("","","Username is required"),
                              ("wronguser","wrongpassword","Username and password do not match any user in this service")

                          ])

def test_login_error_cases(driver,username,password,expected_error):
    driver.refresh()
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    error = login_page.get_error_message()
    print(error)

    assert expected_error in error

def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    title = login_page.get_page_title()
#     validate success
    assert "Products" in title

def test_add_to_cart_function(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    title = login_page.get_page_title()
    #     validate success
    assert "Products" in title
    product_page = ProductPage(driver)
    product_page.click_add_to_cart_button()

    quantity = product_page.check_cart_quantity()

    assert quantity == '1'

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    title = login_page.get_page_title()
    #     validate success
    assert "Products" in title
    product_page = ProductPage(driver)
    product_page.click_add_to_cart_button()

    quantity = product_page.check_cart_quantity()

    assert quantity == '1'

    product_page.click_cart_button()
    cart_page = CartPage(driver)
    cart_page_title = cart_page.get_cart_page_title()
    assert cart_page_title =="Your Cart"
    item_name = cart_page.get_item_in_cart()
    assert item_name == "Sauce Labs Backpack"
    cart_page.remove_item_from_cart()

    assert cart_page.is_cart_empty() is True



# if __name__ == "__main__":
#         test_login_empty_username()


