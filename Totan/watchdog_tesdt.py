######Import for Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import signal
import subprocess
import time
from random import randint
import os

##### Auto terminate Program
# def alarm_handler(signum, frame):
#     sys.exit("Terminated watchdog")
# signal.signal(signal.SIGALRM, alarm_handler)
# signal.alarm(10)
def exit_program():
    sys.exit()


#### Git Commands
def git_Script():
    print("")
    commit_text = f"a20Tk{0}"
    file1 = subprocess.run(["bash", "script.sh", commit_text])
    value = randint(3, 5)
    time.sleep(value)

class MyEventHandler(FileSystemEventHandler):
    counter = 0
    file_cache = {}
    def on_modified(self, event):
        # print(self.file_cache)
        seconds = int(time.time())
        key = (seconds, event.src_path)
        if key in self.file_cache:
            return
        elif event.is_directory:
            print(event)
            git_Script()
            self.counter+=1
        self.file_cache[key] = True
        
        if self.counter >= 1:
            # os.system('\x03')
            os.kill(os.getpid(), signal.SIGINT)



observer = Observer()
path = "."
observer.schedule(MyEventHandler(), path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



