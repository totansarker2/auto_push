# import os
import subprocess
import time
from random import randint

value = randint(0, 10)
# file1 = subprocess.run(["ls", "-l"])



while(True):
    # script = `{}`
    file1 = subprocess.run(["bash", "script.sh"])
    time.sleep(5)




# print("The exit code was: %d" % file1.returncode)
# print("Current Working Directory",os.getcwd())