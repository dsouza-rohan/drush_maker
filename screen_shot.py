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

    def open_firefox(self, url_open, target):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Navigate to the application home page
        self.driver.get(url_open)
        pyautogui.hotkey('COMMAND', 'i')
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        time.sleep(1)

        self.full_screen_capture(target, 1)
        time.sleep(1)
        self.driver.quit()

    def full_screen_capture(self, target, secs):
        # fullscreen
        time.sleep(secs)
        pyautogui.screenshot(target)
        time.sleep(secs)

    def take_ss(self):
        self.open_firefox("https://www.example.nl")

        self.full_screen_capture('/Users/rohandsouza/Desktop/omniture.JPEG', 5)
        self.driver.quit()


# ss = ScreenShot
# ss.take_ss(ScreenShot())
