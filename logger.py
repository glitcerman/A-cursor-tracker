import os, datetime

os.makedirs("logs", exist_ok=True)

if not os.path.exists("logs\\log_n.txt"):
    log_n = 0
    with open("logs\\log_n.txt", "w") as f:
        f.write(str(log_n))
else:
    with open("logs\\log_n.txt", "r") as f:
        content = f.read().strip()
        log_n = int(content) if content else 0
    with open("logs\\log_n.txt", "w") as f:
        f.write(str(log_n + 1))

def logging(message: str):
    global log_n
    with open(f"logs\\log_{log_n}.txt", "a") as log_file:  # "a" au lieu de "w+"
        log_file.write(f"{datetime.datetime.now()} : {message}\n")

def open_log(log_n=log_n):
    with open(f"logs\\log_{log_n}.txt", "r") as log_file:
        return log_file.read()