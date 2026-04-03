import tkinter as tk
import main

def interface(main: main.Main):
    root = tk.Tk()
    root.title("Mouse Position Logger")
    root.geometry("250x200")

    main.root = root  # on transmet la root à main ici, après sa création

    start_button = tk.Button(root, text="Start Logging", command=main.main)
    start_button.pack(pady=20)
    end_button = tk.Button(root, text="Stop Logging", command=main.stop_logging)
    end_button.pack(pady=10)
    quit_button = tk.Button(root, text="Quit", command=main.exit_)
    quit_button.pack(pady=10)
    root.mainloop()