import glob

myfiles = glob.glob("files/*.txt")
print("Found files:")
print(myfiles)

for filepath in myfiles:
    try:
        print(f"Reading file: {filepath}")
        with open(filepath, 'r') as file:
            print(file.read().upper())
    except IOError as e:
        print(f"Error reading {filepath}: {e}")
