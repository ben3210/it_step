lines = []
count = 0

with open("task3_file1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if len(line) > count:
        count = len(line)

print("Length of the longest line:", count - 1) #count - 1: removing extra one character '\n' at the end (two characters, but counts as one since this is a special character for new line)