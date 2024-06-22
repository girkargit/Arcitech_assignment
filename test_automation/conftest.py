import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def login_setup(request):
    """
    Browsing invoking process and enter mobile number and OTP.
    :return: This function will return driver as a object.
    """
    """
    For updated Selenium no need to give chrom driver path. Need to place chrome driver
    in python default folder.
    """

    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-application-cache")
    service_obj = Service()
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.get('https://proschool.ai/')
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    driver.refresh()
    yield
    time.sleep(2)
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    :return: For capturing screenshot for failed test case
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        with open("logfile.log", "r") as f:
            pytest_html = node.config.pluginmanager.getplugin('html')
            extra = getattr(report, 'extra', [])
            extra.append(pytest_html.extras.text(f.read(), 'Log file'))
            report.extra = extra
