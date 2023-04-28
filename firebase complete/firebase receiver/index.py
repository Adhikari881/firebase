import os
import firebase_admin
from firebase_admin import credentials, storage
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Initialize Firebase app
cred = credentials.Certificate("project.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'newproject111-57407.appspot.com'
})

bucket = storage.bucket()

# Create a directory to store the downloaded files
if not os.path.exists('downloaded_files'):
    os.makedirs('downloaded_files')

# Define a function to download a file from Firebase Storage
def download_file(blob):
    filename = os.path.join('downloaded_files', blob.name)
    blob.download_to_filename(filename)
    print(f'Downloaded {filename}')

# Define a class to watch for new files in the bucket
class FirebaseStorageWatcher(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the new file is in the Firebase Storage bucket
        blob = bucket.get_blob(os.path.basename(event.src_path))
        if blob:
            download_file(blob)

# Download all existing files in the bucket
files = bucket.list_blobs()
for file in files:
    download_file(file)

# Watch for new files in the bucket
observer = Observer()
observer.schedule(FirebaseStorageWatcher(), 'downloaded_files')
observer.start()

try:
    while True:
        # Keep the program running
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()













# # Initialize Firebase Storage client
# bucket = storage.bucket()

# # Get a list of files in Firebase Storage
# files = bucket.list_blobs()

# # Print the names of the files
# for file in files:
#     print(file.name)
