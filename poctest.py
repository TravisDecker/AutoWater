import os
import time

while True:
    print("disabling pump")
    os.system("sudo uhubctl -l 1-1 -p 2 -a 0")
    time.sleep(5)
    os.system("sudo uhubctl -l 1-1 -p 2 -a 1")
    time.sleep(10)