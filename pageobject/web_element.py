from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver):
        self.driver = driver

    # ----- Sign up webelement -----
    login_signup = (By.XPATH, "//a[@class='sign_btn']")

