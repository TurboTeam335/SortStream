import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from config import category_mapping, LOG_LEVEL

# Setup logging
logging.basicConfig(filename=os.path.expanduser('~/Downloads/sortstream.log'), level=LOG_LEVEL, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Ignore temporary or hidden files
        if event.src_path.split('/')[-1].startswith('.'):
            return
        # Base folder for sorted files (inside Downloads)
        base_folder = os.path.expanduser('~/Downloads/')

        file_path = event.src_path
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()

        # Determine the category of the file
        destination_subfolder = None
        for category, extensions in category_mapping.items():
            if file_extension in extensions:
                destination_subfolder = os.path.join(base_folder, category)
                break

        if not destination_subfolder:
            destination_subfolder = os.path.join(base_folder, 'Others')

        # Move the file to the destination folder within Downloads
        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)
        new_file_path = self.generate_new_file_path(destination_subfolder, file_path)
        try:
            shutil.move(file_path, new_file_path)
            logging.info(f'Moved {file_path} to {new_file_path}')
        except Exception as e:
            logging.error(f'Error moving file {file_path} to {new_file_path}: {e}')
            raise  

    def generate_new_file_path(self, destination_folder, original_file_path):
        file_base_name = os.path.basename(original_file_path)
        file_name, file_extension = os.path.splitext(file_base_name)
        counter = 1
        new_file_path = os.path.join(destination_folder, file_base_name)

        while os.path.exists(new_file_path):
            new_file_name = f"{file_name}_{counter}{file_extension}"
            new_file_path = os.path.join(destination_folder, new_file_name)
            counter += 1

        return new_file_path

def start_monitoring(path_to_watch):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    path_to_watch = os.path.expanduser('~/Downloads/')
    start_monitoring(path_to_watch)
