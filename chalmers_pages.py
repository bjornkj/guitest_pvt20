from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By

class ChalmersPage:
    def __init__(self, driver: Union[webdriver.Chrome, webdriver.Firefox, webdriver.Edge]):
        self.driver = driver

    def click_utbildning(self):
        self.driver.find_element(By.LINK_TEXT, "Utbildning").click()

    def click_forskning(self):
        self.driver.find_element(By.LINK_TEXT, "Forskning").click()

    def click_samverkan(self):
        self.driver.find_element(By.LINK_TEXT, "Samverkan").click()


class ChalmersITProgram(ChalmersPage):
    pass


class ChalmersMainPage(ChalmersPage):
    pass


class ChalmersUtbildning(ChalmersPage):
    def click_program_pa_grundniva(self):
        self.driver.find_element(By.LINK_TEXT, "Program på grundnivå").click()


class ChalmersProgramGrundniva(ChalmersPage):
    def click_uo_data(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Data, IT").click()

    def click_it(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Informationsteknik").click()

