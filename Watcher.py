import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class Watcher:
    #r means raw string and makes sure "\" don't mess with python strings
    DIRECTORY_TO_WATCH = r"C:\Users\Admin\Downloads"

    #Watcher classes constructor
    def __init__(self, control):
        self.observer = Observer()
        self.control = control

    def run(self):
        event_Handler = EventHandler(self.control)

        #tells watchdog to watch directory and let handler deal with it
        self.observer.schedule(event_Handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        finally:
            self.observer.stop()
            self.observer.join()

    def scan_existing_files(self):
        for file_name in os.listdir(self.DIRECTORY_TO_WATCH):
            #only pdf files
            if not file_name.endswith(".pdf"):
                continue

            #yield returns value, but pauses where function stopped
            #unlike return, which returns value, but ends the function
            yield os.path.join(self.DIRECTORY_TO_WATCH, file_name)


#Todo: The Logger should take care of printing or logging changes

def on_createddd(event):
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    try:
        #buffer time for file to be written
        time.sleep(1)

        #Calls out change and executes the external script
        print(f"{BLUE}New file detected!{RESET}")
        return True
        #subprocess.run(["python", self.script_to_run], check=True)

    except FileNotFoundError:
        print(f"{RED}File not found!{RESET}")
    except PermissionError:
        print(f"{RED}Permission denied!{RESET}")
    except Exception as e:
        print(f"{RED}Error processing file {e}!{RESET}")


class EventHandler(FileSystemEventHandler):
    def __init__(self, control):
        self.control = control

    def on_created(self, event):
        #watcher waits for 2 seconds for the file to be fully created, then tells control.
        #Otherwise, classify will try open with pdfplumber when the file isn't there yet.
        time.sleep(1)
        if not event.is_directory:
            self.control.file_created(event.src_path)



