import subprocess

program_1 = ["python3", "firebase_csv.py"]
program_2 = ["python3", "uploader2.py"]

process_1 = subprocess.Popen(program_1)
process_2 = subprocess.Popen(program_2)

process_1.wait()
process_2.wait()