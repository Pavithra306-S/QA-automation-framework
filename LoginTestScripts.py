from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_error_test(driver,username,password,expected_error_msg):

    test_pass_msg = "TEST CASE PASS"
    test_fail_msg = "TEST CASE FAIL"
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    login = driver.find_element(By.ID, 'login-button')
    login.click()
    # Wait for error msg
    wait = WebDriverWait(driver, 10)
    error_message_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container')))
    error = error_message_container.text
    print(error)

    assert expected_error_msg in error, test_fail_msg
    print(test_pass_msg)


driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()

login_error_test(driver,"","secret_sauce","Username is required")
driver.refresh()
login_error_test(driver,"standard_user","","Password is required")

driver.quit()