######Import for Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

######Import for Scpriting#####
import subprocess
import time
from random import randint

def git_Script():
    print("")
    commit_text = f"a20Tk{0}"
    value = randint(5, 7)
    file1 = subprocess.run(["bash", "script.sh", commit_text])
    time.sleep(value)

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print(event.src_path, "modified.")
        git_Script()

    def on_created(self, event):
        # print(event.src_path, "created.")
        git_Script()

    def on_moved(self, event):
        # print(event.src_path, "moved to", event.dest_path)
        git_Script()

    def on_deleted(self, event):
        # print(event.src_path, "deleted.")
        git_Script()


observer = Observer()
observer.schedule(MyEventHandler(), ".", recursive=False)
observer.start()
try:
    while observer.is_alive():
        observer.join(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
