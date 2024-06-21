from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver):
        self.driver = driver

    # -----Login / Sign up button -----
    login_signup = (By.XPATH, "//a[@class='sign_btn']")

    # ----- Signup button -----
    signup = (By.XPATH, "//a[text()='Sign up']")

    # ----- User details ----
    student = (By.XPATH, "//button[text()='Student']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@name='password']")
    register = (By.XPATH, "//button[text()='Register']")
    confirm = (By.XPATH, "//button[text()='Confirm']")
    otp_box = (By.XPATH, "//div[@label='6-Digit Code']/div/div/input")
    confirm_code = (By.XPATH, "//button[text()='Confirm code']")
    resend_code = (By.XPATH, "//button[text()='Resend code']")

    # ----- Home page -----
    home = (By.XPATH, "//p[text()=' Let's Create Your Student Profile.']")

    def login_signup_button(self):
        return self.driver.find_element(*WebElement.login_signup)

    def signup_button(self):
        return self.driver.find_element(*WebElement.signup)

    def student_profile(self):
        return self.driver.find_element(*WebElement.student)

    def email_input(self):
        return self.driver.find_element(*WebElement.email)

    def password_input(self):
        return self.driver.find_element(*WebElement.password)

    def register_action(self):
        return self.driver.find_element(*WebElement.register)

    def confirm_action(self):
        return self.driver.find_element(*WebElement.confirm)

    def otp_six_box(self):
        lst = self.driver.find_elements(*WebElement.otp_box)
        return lst

    def confirm_code_verification(self):
        return self.driver.find_element(*WebElement.confirm_code)

    def resend_code_verification(self):
        return self.driver.find_element(*WebElement.resend_code)

    def home_text(self):
        return self.driver.find_element(*WebElement.home)