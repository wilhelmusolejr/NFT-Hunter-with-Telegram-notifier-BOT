import time
import subprocess
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("Running app.py...")
    subprocess.run(["python", "app.py"])  # Runs app.py
    print("Running every 30 minutes...")
    time.sleep(1800)  # Wait 1800 seconds (30 minutes)