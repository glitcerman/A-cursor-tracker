import logger
import interface
import os
import heatmap
import pyautogui as pag
import threading
import tkinter as tk

class Main:
    def __init__(self):
        logger.logging("Program initialized")
        print("Don't close this window, there's messages here.")
        self.continue_logging = False
        self._thread = None
        self.root = None
        
    def main(self):
        if self.continue_logging:
            return
        self.continue_logging = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        while self.continue_logging:
            position = pag.position()
            logger.logging(f"Mouse position: {position}")
            print(f"Mouse position: {position}")
    
    def stop_logging(self):
        self.continue_logging = False
        logger.logging("Logging stopped")

    def exit_(self):
        self.stop_logging()
        if self._thread is not None:
            self._thread.join()
        if self.root:
            self.root.quit()
    def show_heatmap(self):
        log_file = f"logs/log_{logger.log_n}.txt"
        if os.path.exists(log_file):
            heatmap.generate(log_file)
        else:
            print("No log file found to generate heatmap.")
    def open_log(self):
        log_file = f"logs/log_{logger.log_n}.txt"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                log_content = f.read()
            log_window = tk.Toplevel(self.root)
            log_window.title("Log Content")
            log_window.geometry("400x300")
            text_widget = tk.Text(log_window, wrap=tk.WORD)
            text_widget.insert(tk.END, log_content)
            text_widget.config(state=tk.DISABLED)
            text_widget.pack(expand=True, fill=tk.BOTH)
        else:
            print("No log file found to open.")

if __name__ == "__main__":
    main = Main()
    interface.interface(main)