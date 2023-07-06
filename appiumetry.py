import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By




desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'emulator-5554'  # Replace with your emulator's device name
desired_caps['automationName'] = 'UiAutomator2'




driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
# Set up desired capabilities

def timer(sec):
    for i in range(1,sec+1):
        time.sleep(1)


def open_Hiya_app():
    driver.activate_app('com.webascender.callerid')
    # driver.find_element(By.ACCESSIBILITY_ID, 'Hiya').click()

def first_time_open():
    driver.find_element(By.ID, 'com.webascender.callerid:id/button_get_started').click()


def enter_number():
    driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("000000")

def click_look_up():
    driver.find_element(By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx'
                        '.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                        '.Button').click()

def exit_driver():
    driver.quit()
# Start the WebDriver

def close_Hiya():
    driver.terminate_app('com.webascender.callerid')

def get_running_appid():
    app_id = driver.current_package
    return app_id
def click_on_keypad():
    driver.find_element(By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android'
                        '.widget.LinearLayout/android.widget.FrameLayout[3]').click()
def set_phone_num():
    driver.find_element(By.ID, 'com.webascender.callerid:id/edittext_phoneNumber').send_keys("123")

def start_loop():
    open_Hiya_app()
    first_time_open()
    enter_number()
    close_Hiya()


start_loop()
exit_driver()


# driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Predicted app: Hiya"]').click()
# driver.find_element(By.ID, 'com.webascender.callerid:id/button_get_started').click()
# driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("123")
# Navigate to a website

# Perform automation tasks
# ...
# Quit the driver
