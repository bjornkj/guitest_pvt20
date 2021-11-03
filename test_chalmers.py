import time

import pytest
from datetime import datetime
from selenium import webdriver


from chalmers_pages import ChalmersMainPage, ChalmersUtbildning, ChalmersITProgram, ChalmersProgramGrundniva


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def test_nav_to_it(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    main_page.click_utbildning()
    utbildningar = ChalmersUtbildning(browser)
    utbildningar.click_program_pa_grundniva()
    program_grundniva = ChalmersProgramGrundniva(browser)
    program_grundniva.click_uo_data()
    program_grundniva.click_it()
    it_prog = ChalmersITProgram(browser)
    assert browser.current_url == 'https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Informationsteknik.aspx'