import re
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

def generate(log_path: str):
    screen_w, screen_h = pyautogui.size()
    positions = []

    with open(log_path, "r") as f:
        for line in f:
            match = re.search(r"Mouse position: Point\(x=(-?\d+), y=(-?\d+)\)", line)
            if match:
                x, y = int(match.group(1)), int(match.group(2))
                positions.append((x, y))

    if not positions:
        print("No mouse positions found in log file.")
        return

    xs = [p[0] for p in positions]
    ys = [p[1] for p in positions]

    heatmap, xedges, yedges = np.histogram2d(
        xs, ys,
        bins=[screen_w // 10, screen_h // 10],
        range=[[0, screen_w], [0, screen_h]]
    )

    plt.figure(figsize=(10, 6))
    plt.imshow(
        heatmap.T,
        origin="upper",
        extent=[0, screen_w, screen_h, 0],
        cmap="hot",
        interpolation="gaussian",
        aspect="auto"
    )
    plt.colorbar(label="Fréquence")
    plt.title("Heatmap du curseur")
    plt.xlabel("X (px)")
    plt.ylabel("Y (px)")
    plt.tight_layout()
    plt.show()