import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

to_dir = "C:/Users/arnav/Downloads"


class a(FileSystemEventHandler):
    def on_created(self,event):
        print({event.src_path} , "has been created")
    def on_modified(self,event):
        print({event.src_path} , "has been modified")

    def on_moved(self,event):
        print({event.src_path} , "has been moved")
    def on_deleted(self,event):
        print({event.src_path} , "has been deleted")            


observer = Observer()
theworkerwhoworks = a()
observer.schedule(theworkerwhoworks, to_dir, recursive=True)
observer.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped. Look outside for Valadmir Putin. He's the one with the gun. You'll know him when you see him. He will make you immortal. He is Russiaeshwar ")
        
