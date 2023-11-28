# C:\Users\Admin\Documents\AHMFaultDecoder-4.6i
import pyautogui
import time


class OpenApp:
    def __int__(self):
        pass
    def minimize_ide_open_app(self) -> object:
        time.sleep(1)
        pyautogui.click(1771, 22)
        time.sleep(1)
        pyautogui.doubleClick(292, 327)

if __name__=="__main__":
    open_app = OpenApp()
    open_app.minimize_ide_open_app()
