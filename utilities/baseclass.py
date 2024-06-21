import time
import pytest
import logging
import inspect
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("login_setup")
class BaseClass:

    def is_element_displayed(self, txt, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(txt))
            return element.is_displayed()
        except Exception as e:
            return False

    def get_url(self):
        return self.driver.current_url

    def otp_verification(self, lst):
        try:
            wait = WebDriverWait(self.driver, 90)
            val = wait.until(lambda driver: all(box.get_attribute("value") for box in lst))
            print("OTP verification successful")
            return True
        except TimeoutException:
            print("Timeout waiting for OTP verification")
            return False

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

