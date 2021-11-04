import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def foo():
    # 1. Starta webläsaren
    # 2. Gå till kyh.se
    # 3. Skriv ut dom cookiers vi redan har
    # 4. Klicka ok cookiefrågan
    # 5. Skriv ut alla cookies igen
    browser = webdriver.Chrome()
    browser.get("https://www.kyh.se")
    old_cookies = browser.get_cookies()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "#cn-accept-cookie").click()
    print("-" * 80)
    new_cookies = browser.get_cookies()
    for cookie in new_cookies:
        if cookie not in old_cookies:
            print(cookie)
    # #cn-accept-cookie
    # 1638604134
    # {'domain': 'kyh.se', 'expiry': 1638604134, 'httpOnly': False, 'name': 'cookie_notice_accepted', 'path': '/', 'secure': True, 'value': 'true'}



def set_cookie():
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get("https://kyh.se/foo")
    browser.add_cookie(
        {'domain': 'kyh.se', 'expiry': int((datetime.datetime.today() + datetime.timedelta(weeks=4)).timestamp()), 'httpOnly': False, 'name': 'cookie_notice_accepted', 'path': '/',
         'secure': True, 'value': 'true'})
    browser.get("https://www.kyh.se")
    time.sleep(5)


if __name__ == '__main__':
    set_cookie()