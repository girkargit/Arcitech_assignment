import pytest
import time
from pageobject.web_element import *
from utilities.baseclass import *


class TestSignUp(BaseClass):

    def test_landed_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://proschool.ai/" == self.get_url()

    def test_sign_up_process(self):
        log = self.getLogger()
        obj = WebElement(self.driver)
        obj.login_signup_button().click()
        obj.signup_button().click()
        obj.student_profile().click()
        obj.email_input().send_keys("pashtesuraj157@gmail.com")
        obj.password_input().send_keys("Test@123")
        obj.register_action().click()
        obj.confirm_action().click()
        flag = self.otp_verification(obj.otp_six_box())
        if flag:
            obj.confirm_code_verification().click()
        else:
            time.sleep(1)
            obj.resend_code_verification().click()
        log.info("----- Sign up successfully. -----")
        assert True == self.is_element_displayed(obj.create_profile_text())
