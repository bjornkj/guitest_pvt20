import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Union


class KyhPage:
    driver: Union[webdriver.Chrome, webdriver.Firefox, webdriver.Edge]

    def __init__(self, driver):
        self.driver = driver

    def page_up(self):
        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_UP)

    def page_down(self):
        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)


class MainPage(KyhPage):
    def click_vara_utb_dd(self):
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/nav[1]/div[1]/button").click()

    def click_it_in_dd(self):
        self.driver.find_element(By.LINK_TEXT, "IT").click()


class VaraUtbildningar(KyhPage):
    def click_gbg(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Göteborg')]")))
        button.click()

    def click_pvt(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Programvarutestare")))
        link.click()


class PvtPage(KyhPage):
    @property
    def antal_ar(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/section[2]/section[1]/div[2]/div[2]/ul/li[2]/span').text

    @property
    def ort(self) -> str:
        element = self.driver.find_element(By.XPATH, '//*[@id="content"]/section[2]/section[1]/div[2]/div[2]/ul/li[1]/span')
        return element.text



def main():
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get("https://kyh.se/utbildningar/teknisk-testare/")

    pvt_page = PvtPage(browser)

    print(f"Utbildningstid {pvt_page.antal_ar}, plats {pvt_page.ort}")


if __name__ == '__main__':
    main()
