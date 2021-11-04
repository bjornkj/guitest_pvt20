import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from kyh_pages import MainPage, VaraUtbildningar, PvtPage
import pytest
from datetime import datetime, timedelta


class ChromeWithMem(webdriver.Chrome):
    last_element: object

    def find_element(self, *args, **kwargs):
        self.last_element = super(webdriver.Chrome, self).find_element(*args, **kwargs)
        return self.last_element



@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = ChromeWithMem(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://kyh.se/foo")
    driver.add_cookie(
        {'domain': 'kyh.se', 'expiry': int((datetime.today() + timedelta(weeks=4)).timestamp()),
         'httpOnly': False, 'name': 'cookie_notice_accepted', 'path': '/',
         'secure': True, 'value': 'true'})
    yield driver
    driver.quit()


def test_pvt_nav(browser):
    browser.get("https://www.kyh.se")
    kyh_main_page = MainPage(browser)
    kyh_main_page.click_vara_utb_dd()
    kyh_main_page.click_it_in_dd()
    vara_utb = VaraUtbildningar(browser)
    vara_utb.click_gbg()
    time.sleep(2)
    vara_utb.page_down()
    time.sleep(2)
    vara_utb.click_pvt()
    pvt_page = PvtPage(browser)
    assert browser.current_url == "https://kyh.se/utbildningar/teknisk-testare/"


def test_pvt_utb_len(browser):
    browser.get("https://kyh.se/utbildningar/teknisk-testare/")
    pvt_page = PvtPage(browser)
    assert pvt_page.antal_ar == "2 år"


def test_pvt_utb_ort(browser):
    browser.get("https://kyh.se/utbildningar/teknisk-testare/")
    pvt_page = PvtPage(browser)
    pvt_page.page_down()
    assert pvt_page.ort == "asdfas"
