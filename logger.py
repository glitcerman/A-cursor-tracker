import os, datetime

os.makedirs("logs", exist_ok=True)

log_n = 0
for file in os.listdir("logs"):
    if file.startswith("log_") and file.endswith(".txt") and file != "log_n.txt":
        log_n += 1

def logging(message: str):
    global log_n
    with open(f"logs/log_{log_n}.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} : {message}\n")

def open_log(log_n=log_n):
    with open(f"logs/log_{log_n}.txt", "r") as log_file:
        return log_file.read()