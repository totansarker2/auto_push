# import os
import subprocess
import time
from random import randint


# file1 = subprocess.run(["ls", "-l"])


i = 0
while(True):
    # script = `{}`
    commit_text = f"a20Tk{i}"
    value = randint(3, 7)
    file1 = subprocess.run(["bash", "script.sh", commit_text])
    time.sleep(value)
    i+=1


#

# print("The exit code was: %d" % file1.returncode)
# print("Current Working Directory",os.getcwd())