# import os
import subprocess
import time
from random import randint


# file1 = subprocess.run(["ls", "-l"])



while(True):
    # script = `{}`
    value = randint(0, 5)
    file1 = subprocess.run(["bash", "script.sh"])
    time.sleep(value)




# print("The exit code was: %d" % file1.returncode)
# print("Current Working Directory",os.getcwd())