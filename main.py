import time
from multiprocessing import freeze_support
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from undetected_chromedriver import ChromeOptions
from selenium import webdriver


def main():
    co = ChromeOptions()
    # co.add_argument("--no-sandbox")
    # co.add_argument("--disable-setuid-sandbox")
    hdl = dict()
    driver = uc.Chrome(headless=False, use_subprocess=False, options=co)
    # driver.get('https://nowsecure.nl')
    # driver.save_screenshot('nowsecure.png')
    driver.get("https://chatgpt.com")

    sel = "button"
    el = driver.find_elements(By.CSS_SELECTOR, sel)
    for e in el:
        print(e)
    print(f"Current url {driver.current_url}")
    driver.save_screenshot("butt.png")
    # driver.close()
    wait = WebDriverWait(driver, 10)
    # Wait until an element with the CSS selector 'button' is located
    # element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))
    # wait.until(EC.presence_of_element_located())
    tg = [ee for ee in el if ('Log in' in ee.text)]
    print(tg)

    driver.quit()


if __name__ == '__main__':
    freeze_support()
    main()
