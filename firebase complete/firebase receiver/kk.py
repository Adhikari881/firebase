import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import time


# Initialize Firebase app
cred = credentials.Certificate("project.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'newproject111-57407.appspot.com'
})
# Get a reference to the Firebase Storage bucket
bucket = storage.bucket()

# Create a list of already downloaded files
downloaded_files = []

while True:
    try:
        # Get a list of all files in the Firebase Storage bucket
        all_files = bucket.list_blobs()

        # Loop through all files in the bucket
        for file in all_files:
            # Check if the file has already been downloaded
            if file.name not in downloaded_files:
                # Download the file to local PC
                file.download_to_filename('/Users/pc2/Desktop/hacker material/folder/' + file.name)
                # Add the file name to the list of downloaded files
                downloaded_files.append(file.name)
                print('Downloaded file:', file.name)

        # Wait for 10 seconds before checking for new files
        time.sleep(10)

    except Exception as e:
        # Handle any exceptions (e.g. internet connection error)
        print('Error:', e)
        # Wait for 10 seconds before trying again
        time.sleep(10)
