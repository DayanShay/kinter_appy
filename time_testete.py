from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
def timer(sec):
    for i in range(1,sec+1):
        time.sleep(1)
        print(i)

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\shaye\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.co.il")





timer(20)