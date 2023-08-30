contents = ["All carrots are to be sliced "
            "longitudinally.",
            "The carrots were repordely sliced.",
            "I don't love carrots, but they are ok"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)