import os
import subprocess
# file1 = subprocess.run(["ls", "-l"])
file1 = subprocess.run(["bash", "script.sh"])

# print("The exit code was: %d" % file1.returncode)
print("Current Working Directory",os.getcwd())