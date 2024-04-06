# import os
import subprocess
import time
from random import randint


# file1 = subprocess.run(["ls", "-l"])


i = 0
while(True):
    # script = `{}`
    commit_text = f"{i}th commit"
    value = randint(3, 5)
    file1 = subprocess.run(["bash", "script.sh", "commit_text"])
    time.sleep(value)




# print("The exit code was: %d" % file1.returncode)
# print("Current Working Directory",os.getcwd())