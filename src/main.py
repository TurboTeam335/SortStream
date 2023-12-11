import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # This function is called when a file is created
        print(f'File {event.src_path} has been created')

        # Here you can add the logic to sort the file into a specific folder based on file type


def start_monitoring(path_to_watch):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Specify the directory to monitor
    # Example: path_to_watch = '/Users/YourUsername/Downloads'
    path_to_watch = '/Users/Daniel/Downloads/'
    start_monitoring(path_to_watch)
