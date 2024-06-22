from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, driver):
        self.driver = driver

    # -----Login / Sign up button -----
    login_signup = (By.XPATH, "//a[@class='sign_btn']")
    book_demo = (By.XPATH, "//a[text()='Book a Demo']")

    # ----- Signup button -----
    signup = (By.XPATH, "//a[text()='Sign up']")
    login = (By.XPATH, "//button[text()='Login']")
    login_action = (By.XPATH, "//a[text()='Login']")

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
    create_profile = (By.XPATH, "//button[text()='Create Profile']")

    # ----- User info -----
    full_name = (By.XPATH, "(//input[@placeholder='Full name'])[3]")
    location = (By.XPATH, "(//input[@placeholder='Enter a location'])[3]")
    grade_select = (By.ID, "gendar-select-feild")
    gender_select = (By.XPATH, "(//select[@name='gender'])[3]")
    lang_select = (By.XPATH, "(//select[@name='language'])[3]")
    location_slect = (By.XPATH, "//div//div[@class='pac-item']")
    dob_calender = (By.XPATH, "(//input[@placeholder='MM:DD:YYYY'])[3]")
    dob_date = (By.XPATH , "(//div[@class='rdtPicker'])[3]/div/table/tbody/tr[1]/td[5]")
    next = (By.XPATH, "(//button[text()='Next'])[3]")

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

    def register_action_option(self):
        return WebElement.register

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

    def book_demo_option(self):
        return WebElement.book_demo

    def login_button(self):
        return self.driver.find_element(*WebElement.login)

    def login_action_perform(self):
        return self.driver.find_element(*WebElement.login_action)

    def create_profile_button(self):
        return self.driver.find_element(*WebElement.create_profile)

    def create_profile_text(self):
        return WebElement.create_profile

    def full_name_text(self):
        return self.driver.find_element(*WebElement.full_name)

    def location_text(self):
        return self.driver.find_element(*WebElement.location)

    def select_grade(self):
        return self.driver.find_element(*WebElement.grade_select)

    def select_gender(self):
        return self.driver.find_element(*WebElement.gender_select)

    def select_lang(self):
        return self.driver.find_element(*WebElement.lang_select)

    def select_location(self):
        lst = self.driver.find_elements(*WebElement.location_slect)
        return lst

    def dob_click(self):
        return self.driver.find_element(*WebElement.dob_calender)

    def dob_date_click(self):
        return self.driver.find_element(*WebElement.dob_date)

    def next_click(self):
        return self.driver.find_element(*WebElement.next)