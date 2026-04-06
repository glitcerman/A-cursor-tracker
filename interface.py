import tkinter as tk
import main

def interface(main: main.Main):
    root = tk.Tk()
    root.title("A-mouse-tracker")
    root.geometry("250x275")

    main.root = root
    main.root.configure(bg="#303135")
    
    start_button = tk.Button(
        root, 
        text="Start Logging", 
        command=main.main, bg="#9aa0a6", 
        font=("Arial", 12), 
        relief="flat", 
        borderwidth=2
    )
    start_button.pack(pady=20)
    end_button = tk.Button(
        root, 
        text="Stop Logging", 
        command=main.stop_logging, 
        bg="#9aa0a6", 
        font=("Arial", 12), 
        relief="flat", 
        borderwidth=2
    )
    end_button.pack(pady=10)
    open_button = tk.Button(
        root, 
        text="Open Log", 
        command=main.open_log, 
        bg="#9aa0a6", 
        font=("Arial", 12), 
        relief="flat", 
        borderwidth=2
    )
    open_button.pack(pady=10)
    heatmap_button = tk.Button(
        root, 
        text="Show Heatmap", 
        command=main.show_heatmap, 
        bg="#9aa0a6", 
        font=("Arial", 12), 
        relief="flat", 
        borderwidth=2
    )
    heatmap_button.pack(pady=10)
    quit_button = tk.Button(
        root, 
        text="Quit", 
        command=main.exit_, 
        bg="#ff6262", 
        font=("Arial", 12, "bold"), 
        relief="flat", 
        borderwidth=2
    )
    quit_button.pack(pady=10)
    root.mainloop()