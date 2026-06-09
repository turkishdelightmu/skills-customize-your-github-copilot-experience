# Starter code for File Handling and Error Handling

try:
    file = open("sample.txt", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("The file was not found.")
finally:
    file.close()

# TODO: Add a prompt for user input and write to notes.txt
