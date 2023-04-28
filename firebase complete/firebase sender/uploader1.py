import os
import pyrebase,time

# Configure the Pyrebase object with your Firebase project configuration
config = {
    "apiKey": "AIzaSyAYogdcpk9dv49B0SQH4DCkCxlmmsJoTgs",
  "authDomain": "newproject111-57407.firebaseapp.com",
  "databaseURL": "https://newproject111-57407-default-rtdb.firebaseio.com",
  "projectId": "newproject111-57407",
  "storageBucket": "newproject111-57407.appspot.com",
  "messagingSenderId": "446078313372",
  "appId": "1:446078313372:web:0fe94d6bce11690a581e59"
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
directory_to_watch = '/home/pi/Desktop/firebase/upload'

# Use the os package to monitor the directory for new files
while True:
    
    for filename in os.listdir(directory_to_watch):
        time.sleep(60)     # Wait for 1 minute before checking the directory again
        if filename.endswith('.csv'): # Change this condition to match the file extension you want to upload
            file_path = os.path.join(directory_to_watch, filename)
            upload_and_delete_file(file_path)
        else:
            pass
     
