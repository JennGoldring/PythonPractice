filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# content = ["Hello", "Hello", "Hello"]
# for content, filename in zip(content, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)
#
for filename in filenames:
    with open(f"../files/{filename}", 'w') as file:
        file.write("Hello again")

