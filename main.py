import logger
import time
import interface
import tkinter as tk
import pyautogui as pag
import threading

class Main:
    def __init__(self):
        logger.logging("Program initialized")
        self.continue_logging = False
        self._thread = None
        self.root = None  # sera défini après la création de la fenêtre
        
    def main(self):
        if self.continue_logging:
            return
        self.continue_logging = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        while self.continue_logging:
            time.sleep(1)
            position = pag.position()
            logger.logging(f"Mouse position: {position}")
    
    def stop_logging(self):
        self.continue_logging = False
        logger.logging("Logging stopped")

    def exit_(self):
        self.stop_logging()
        if self._thread is not None:
            self._thread.join()
        if self.root:
            self.root.quit()

if __name__ == "__main__":
    main = Main()
    interface.interface(main)