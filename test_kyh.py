import time

from selenium import webdriver
from kyh_pages import MainPage, VaraUtbildningar, PvtPage
import pytest


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
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
    assert pvt_page.ort == "asdfas"
