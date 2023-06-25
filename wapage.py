import time
import base64
import selenium
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options











locator = {"serch" : (By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'),
           "msg" : (By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')}
inp_xpath_search = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

shift_start = "06:00:00"
shift_ends = "13:00:00"
time_to_send_msg = ["07:30:00","09:00:00","10:30:00","12:00:00","13:30:00","11:08:30"]


contact = "You"
text = "Hey, this message was sent using Selenium"



def timer(sec):
    for i in range(1,sec+1):
        time.sleep(1)
        print(i)

def open_page():
    options = Options()
    options.add_argument("--profile-directory=Default")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    timer(10)
    imgstring = driver.find_element(By.CLASS_NAME, "_2I5ox").screenshot_as_base64
    imgdata = base64.b64decode(imgstring)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    img = Image.open('some_image.jpg')
    img.show()
    input("scan_QR_code")
    return driver


def send_msg(driver):
    timer(2)
    driver.find_element(*locator["serch"]).send_keys(contact+Keys.ENTER)
    timer(2)
    input_box = driver.find_element(*locator["msg"])
    timer(1)
    input_box.send_keys(text + Keys.ENTER)
    timer(15)

def run_app():
    driver = open_page()
    while (shift_start < time.asctime().split(" ")[3] < shift_ends ):
        if time.asctime().split(" ")[3] in time_to_send_msg:
            send_msg(driver)
        else:
            print("wait till we can send msg")
            pass
    return driver


driver = run_app()
driver.quit()









input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
driver.quit()