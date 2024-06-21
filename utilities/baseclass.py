import time
import pytest
import logging
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
