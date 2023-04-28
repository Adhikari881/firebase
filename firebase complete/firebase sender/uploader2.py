import os
import pyrebase,time
from queue import Queue

# Configure the Pyrebase object with your Firebase project configuration
config = {
      'apiKey': "AIzaSyDsgxpOrGxEPnShj4Mi-PRXu0_lLmJT96k",
  'authDomain': "pressure-sensor-38714.firebaseapp.com",
  'databaseURL': "https://pressure-sensor-38714-default-rtdb.firebaseio.com",
  'projectId': "pressure-sensor-38714",
  'storageBucket': "pressure-sensor-38714.appspot.com",
  'messagingSenderId': "928002848156",
  'appId': "1:928002848156:web:69748cb2db8d3c89bc4459",
  'measurementId': "G-X4T3LW5Q4W"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Define a function to upload a file to Firebase Storage, and delete it after upload
def upload_and_delete_file(file_path):
    filename = os.path.basename(file_path)
    storage.child(filename).put(file_path)
    os.remove(file_path)
    print(f'File {filename} uploaded to Firebase Storage and deleted from local directory.')

# Define the directory to monitor for new files
src_dir = '/Users/pc2/Documents/office/firebase complete/firebase sender/upload'
transfer_queue = Queue()

# Use the os package to monitor the directory for new files
while True:
    # Get list of CSV files in source directory, sorted by modification time
    csv_files = sorted([os.path.join(src_dir, f) for f in os.listdir(src_dir) if f.endswith(".csv")], key=os.path.getmtime)
    
    # Add files to transfer queue, ensuring only latest 3 files remain in source directory
    for file_path in csv_files[:-3]:
        transfer_queue.put(file_path)
    csv_files = csv_files[-3:]
    
     # Transfer files in queue
    while not transfer_queue.empty():
        file_path = transfer_queue.get()
        upload_and_delete_file(file_path)
    
    

