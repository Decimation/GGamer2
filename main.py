import pickle
import pprint
import time
from multiprocessing import freeze_support
from typing import Set

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from http.cookiejar import MozillaCookieJar
from pathlib import Path
import requests


def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if line != '\n' and (not re.match(r'^#', line)):
                line_fields = line.strip().split('\t')
                cookies[line_fields[5]] = line_fields[6]
    return cookies


cj = MozillaCookieJar(r"C:\Users\Deci\Downloads\cookies.txt")
cj.load()

for c in cj:
    pprint.pprint(c)


def main():
    co = ChromeOptions()
    co.add_argument("--no-sandbox")
    # co.add_argument(r"user-data-dir=C:\Users\Deci\AppData\Local\Google\Chrome\User Data")
    co.add_argument("--disable-setuid-sandbox")
    hdl = dict()
    driver = uc.Chrome(headless=False, use_subprocess=False, options=co)
    # driver.get('https://nowsecure.nl')
    # driver.save_screenshot('nowsecure.png')

    driver.get("https://chatgpt.com")

    for cookie in cj:
        pprint.pprint(cookie)
        # Setting domain to None automatically instructs most webdrivers to use the domain of the current window
        # handle
        cookie_dict = {'domain': cookie.domain, 'name': cookie.name, 'value': cookie.value, 'secure': cookie.secure}
        if cookie.expires:
            cookie_dict['expiry'] = cookie.expires
        if cookie.path_specified:
            cookie_dict['path'] = cookie.path
        # driver.add_cookie(cookie_dict={'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain})
        driver.add_cookie(cookie_dict)

    # cookies = pickle.load(open("cookies.pkl", "rba+"))
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    driver.get("https://chatgpt.com")

    # sel = "button"
    # el = driver.find_elements(By.CSS_SELECTOR, sel)
    # # for e in el:
    # #     print(e)
    # print(f"Current url {driver.current_url}")
    # driver.save_screenshot("butt.png")
    # # driver.close()
    wait = WebDriverWait(driver, 60)
    # # Wait until an element with the CSS selector 'button' is located
    # # tg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))
    # # wait.until(EC.presence_of_element_located())
    # tg = [ee for ee in el if ('Log in' in ee.text)][0]
    # # driver.add_cookie()
    # print(tg)
    # tg.click()
    # wait.until(EC.title_contains("Login"))
    # eml = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    # pprint.pprint(eml)
    # eml.click()
    # eml.send_keys("decimation001@gmail.com")
    em = wait.until(EC.presence_of_element_located((By.ID, 'prompt-textarea')))
    em.send_keys("How do I play game\n")
    responses = set()

    while True:
        res = driver.find_elements(By.XPATH, r"//div[@data-message-author-role='assistant']")

        for r in res:
            responses.add(r)
            pprint.pp(r.text)

    driver.implicitly_wait(10000.0)
    driver.quit()


if __name__ == '__main__':
    freeze_support()
    main()
