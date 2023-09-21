import glob
import os

print("Current Working Directory:", os.getcwd())

myfiles = glob.glob("files/*.txt")
print("Files found:", myfiles)

if not myfiles:
    print("No text files found in the 'files' directory.")

for filepath in myfiles:
    try:
        with open(filepath, 'r') as file:
            print(file.read().upper())
    except Exception as e:
        print(f"Error reading {os.path.basename(filepath)}: {e}")
