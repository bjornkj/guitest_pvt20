import time
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from chalmers_pages import ChalmersMainPage, ChalmersUtbildning, ChalmersProgramGrundniva, ChalmersITProgram

RESOLUTIONS2 = ((1920, 1080), (1440, 900))
RESOLUTIONS = ((1920, 1080),)




@pytest.fixture(params=RESOLUTIONS, scope="module")
def browser(request):
    x, y = request.param
    browser = webdriver.Chrome()
    browser.set_window_position(0, 0)
    browser.set_window_size(x, y)
    yield browser
    browser.quit()


@pytest.fixture
def it_prog_old(browser):
    browser.get('https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Informationsteknik.aspx')
    return browser

@pytest.fixture
def it_prog(browser):
    browser.get('https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Informationsteknik.aspx')
    return ChalmersITProgram(browser)


@pytest.fixture
def chalmers_se_old(browser):
    browser.get("https://www.chalmers.se")
    return browser


@pytest.fixture
def chalmers_se(browser):
    browser.get("https://www.chalmers.se")
    return ChalmersMainPage(browser)


def test_cont_it_hp(it_prog):
    assert it_prog.program_type == "300 hp (civilingenjör)"


def test_cont_it_utb_inneh(it_prog):
    assert "Utbildningens innehåll" in it_prog.text


def test_cont_ant_platser(it_prog):
    assert "Antal platser 120" in it_prog.text


def test_nav_main_to_it(chalmers_se):
    utbildning = chalmers_se.go_utbildning()
    program_grundniva = utbildning.go_program_grundniva()
    program_grundniva.click_uo_data()
    it_p = program_grundniva.go_it()

    assert it_p.driver.current_url == 'https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Informationsteknik.aspx'

def test_nav_again(chalmers_se):
    assert chalmers_se.go_utbildning().go_program_grundniva().click_uo_data().go_it().url ==\
           'https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Informationsteknik.aspx'


def test_nav_main_to_data(chalmers_se_old):
    ChalmersMainPage(chalmers_se_old).click_utbildning()
    ChalmersUtbildning(chalmers_se_old).click_program_pa_grundniva()
    ChalmersProgramGrundniva(chalmers_se_old).click_uo_data()
    ChalmersProgramGrundniva(chalmers_se_old).click_data()
    assert chalmers_se_old.current_url == 'https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/Datateknik.aspx'



# Hur många saker gör testet?
# 1. Testar en navigationsväg til IT-programmet
# 2. Testar innehåll på IT-sidan
# 3. Testar innehåll på IT-sidan
# 4. Testar innehåll på IT-sidan
# 5. Stänger browsern


def cookies():
    browser = webdriver.Chrome()
    browser.get("https://www.chalmers.se")
    for cookie in browser.get_cookies():
        print(cookie)

    browser.quit()


if __name__ == '__main__':
    cookies()

# TODO Exempel på hur vi kan skapa olika typer av rapporter. Ex: html eller xml
# TODO Exempel på hur vi kan spara skärmdumpar och ha med i våra testrapporter
# TODO Ange path till webdriver executables, depreciation waring med strängargument
# TODO Hantering av cookies, hur kan vi exempelvis undvika att behöva klicka accept varje test
# TODO Länk till page objects -> kurssidan
# TODO Hur hanterar vi tester av länkar, vad gör vi assert på
