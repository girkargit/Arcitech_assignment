import pytest
import time
from selenium.webdriver.common.by import By
from pageobject.web_element import *
from utilities.baseclass import *
from test_data.testcase_data import *


class TestCreateProfile(BaseClass):
    is_login_page_display = None

    def test_is_home_page_display(self):
        obj = WebElement(self.driver)
        log = self.getLogger()
        flag = self.is_element_displayed(obj.book_demo_option())
        if flag:
            TestCreateProfile.is_login_page_display = True
        log.info("----- %s -----" % self.get_url())
        assert "https://proschool.ai/" == self.get_url()

    def test_login_process(self):
        obj = WebElement(self.driver)
        log = self.getLogger()
        if TestCreateProfile.is_login_page_display:
            print("----- Login page is present -----")
            obj.login_signup_button().click()
            obj.student_profile().click()
            obj.email_input().send_keys("pashtesuraj157@gmail.com")
            obj.password_input().send_keys("Test@123")
            obj.login_button().click()
            log.info("----- Login Successfully -----")
            assert True == self.is_element_displayed(obj.create_profile_text())
        else:
            print("-----No Login page is present -----")

    def test_create_profile(self, getData):
        """
        We can perform negative data testing using excel sheet,
        """
        print(getData)
        obj = WebElement(self.driver)
        log = self.getLogger()
        obj.create_profile_button().click()
        obj.full_name_text().clear()
        obj.full_name_text().send_keys(getData["full_name"])  # Fetch data from excel sheet
        self.static_drop_down(obj.select_grade(), "16")  # Static drop down
        self.static_drop_down(obj.select_gender(), "1")  # Static drop down
        self.static_drop_down(obj.select_lang(), "1")  # Static drop down
        obj.location_text().send_keys("Mum")
        time.sleep(2)
        for i in obj.select_location():
            if "Mumbai" in i.text:
                i.click()
                break
        obj.dob_click().click()
        obj.dob_date_click().click()
        obj.next_click().click()
        time.sleep(5)

    @pytest.fixture(params=Data.getTestData("first_page", "../test_case/arcitech_ai.xlsx"))
    def getData(self, request):
        return request.param
