import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
dri_ops = webdriver


def selenium_driver_operator(url) -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_argument(r"C:\Users\shaye\AppData\Local\Google\Chrome\User Data\Default")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    driver.maximize_window()
    driver.get(url)
    return driver


def click_next(driver: webdriver):
    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()


def fill_name(driver: webdriver):
    driver.find_element(By.NAME, "firstName").send_keys("test")
    driver.find_element(By.NAME, "lastName").send_keys("test")
    click_next(driver)


def fill_date(driver: webdriver):
    driver.find_element(By.NAME, "day").send_keys("1")
    Select(driver.find_element(By.ID, "month")).select_by_index("1")
    driver.find_element(By.NAME, "year").send_keys("1990")
    Select(driver.find_element(By.ID, "gender")).select_by_index("1")
    click_next(driver)


def fill_email(driver: webdriver):
    driver.find_element(By.NAME, "Username").send_keys("john.smith.test.trade.1")
    click_next(driver)


def fill_password(driver: webdriver):
    driver.find_element(By.NAME, "Passwd").send_keys("")
    driver.find_element(By.NAME, "PasswdAgain").send_keys("")
    click_next(driver)


url = 'https://accounts.google.com/signup'

a = selenium_driver_operator(url)
fill_name(a)
time.sleep(3)
fill_date(a)
time.sleep(3)
fill_email(a)
time.sleep(3)
fill_password(a)
time.sleep(10)

