
# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


#pyautogui
import pyautogui

class Bot(WebBot):


    def searchForro(self):
        try:
            
            pyautogui.click(428,97, duration=2)

            self.wait(400)
            self.paste('Os melhores forró de Manaus')

            self.wait(200)
            pyautogui.click(941,100, duration=1)

            self.wait(2000)
            pyautogui.click(424,506, duration=2)
        
        except Exception as ex:
           print(f'Erro no elemento {ex}')

    def action(self, execution=None):
        
       
        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to change the default Browser to Firefox
        self.browser = Browser.CHROME

        # Uncomment to set the WebDriver path
        self.driver_path = r"C:/Program Files/chromedriver_win32/chromedriver.exe"

        # Opens the selfCity website.
        self.browse("https://www.youtube.com.br")

        self.maximize_window()
        self.wait(4000)
        # Implement here your logic...
        self.searchForro()

        # Wait 3 seconds before closing
        self.wait(4000000)

        # Finish and clean up the Web Browser
        # You MUST invoke the stop_browser to avoid
        # leaving instances of the webdriver open
        self.stop_browser()

        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
