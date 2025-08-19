find = "python"
count = 0
with open("task3_file1.txt", "r") as file:
    content = file.read()
    words = content.lower().split()
    for word in words:
        if word == find:
            count += 1
    print(count)