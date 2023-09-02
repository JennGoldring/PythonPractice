files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    with open(f"../files/{file}", 'r') as f:
        content = f.read()
        print(content)

