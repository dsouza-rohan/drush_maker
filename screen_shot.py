import time
import pyautogui
from selenium import webdriver


class ScreenShot:
    """Simple ScreenShot utility class"""

    driver = ""

    def __init__(self):
        print("ScreenShot--start")

    def __del__(self):
        print("ScreenShot--done")

    def open_firefox(self, url_open):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Navigate to the application home page
        self.driver.get(url_open)
        pyautogui.hotkey('COMMAND', 'i')
        pyautogui.press('up')
        pyautogui.press('up')

    def full_screen_capture(self, target):
        # fullscreen
        time.sleep(5)
        pyautogui.screenshot(target)
        time.sleep(5)

    def take_ss(self):
        self.open_firefox("https://www.pfizer.nl")

        self.full_screen_capture('/Users/rohandsouza/Desktop/omniture.JPEG')
        self.driver.close()


ss = ScreenShot
ss.take_ss(ScreenShot())
