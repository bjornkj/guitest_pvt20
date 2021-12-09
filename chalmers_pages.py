from __future__ import annotations

import time
from functools import cache
import datetime
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

    @property
    def url(self) -> str:
        return self.driver.current_url



class ChalmersITProgram(ChalmersPage):
    PROGRAM_TYPE = (By.CSS_SELECTOR, "#first-page > div.program-header > h2")
    TEXT = (By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]')

    @property
    def program_type(self):
        return self.driver.find_element(*ChalmersITProgram.PROGRAM_TYPE).text

    @property
    def text(self):
        return self.driver.find_element(*ChalmersITProgram.TEXT).text


class ChalmersDataProgram(ChalmersPage):
    pass

class ChalmersMainPage(ChalmersPage):
    def go_utbildning(self) -> ChalmersUtbildning:
        self.click_utbildning()
        return ChalmersUtbildning(self.driver)


class ChalmersUtbildning(ChalmersPage):
    def click_program_pa_grundniva(self):
        self.driver.find_element(By.LINK_TEXT, "Program på grundnivå").click()

    def go_program_grundniva(self) -> ChalmersProgramGrundniva:
        self.click_program_pa_grundniva()
        return ChalmersProgramGrundniva(self.driver)


class ChalmersProgramGrundniva(ChalmersPage):
    def click_uo_data(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Data, IT").click()
        return self

    def click_it(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Informationsteknik").click()

    def click_data(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Datateknik").click()

    def go_data(self) -> ChalmersDataProgram:
        self.click_data()
        return ChalmersDataProgram(self.driver)

    def go_it(self) -> ChalmersITProgram:
        self.click_it()
        return ChalmersITProgram(self.driver)


class Person:
    __first_name: str
    __last_name: str
    born = datetime.date

    def __init__(self, first_name, last_name, born):
        self.__first_name = first_name
        self.__last_name = last_name
        self.born = born

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return (datetime.datetime.today().date() - self.born).days

    def say_hello(self):
        print("Hello there")

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} days old"


if __name__ == '__main__':
    # p = Person("Björn", "Kjellgren", datetime.date(1980, 12, 4))
    # print(p.first_name)
    # print(p)
    # #print(p.get_age())
    # print(p.age)
    #
    # def greeter(f):
    #     def inner(*args):
    #         print(f"Hello there, i'm about to run {f.__name__}")
    #         f(*args)
    #         print("Done")
    #     return inner
    #
    # @greeter
    # def foo():
    #     print("Hello")
    #
    # @greeter
    # def bar(n):
    #     print(f"{n}^2 = {n*n}")
    #
    #
    # foo()
    # bar(10)

    def factorial(n):
        if n == 0:
            return 1
        return n*factorial(n-1)

    start = time.process_time_ns()
    print(factorial(100))
    print(factorial(200))
    print(time.process_time_ns() - start)

