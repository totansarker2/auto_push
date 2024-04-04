import os
import subprocess
import time
# file1 = subprocess.run(["ls", "-l"])

for i in range(0, 100):
    # script = `{}`
    file1 = subprocess.run(["bash", "script.sh"])
    time.sleep(5)




# print("The exit code was: %d" % file1.returncode)
print("Current Working Directory",os.getcwd())