with open("task3_file1.txt", "r") as file1:
    lines = file1.readlines()
    lines.pop()
    with open("task3_file2.txt", "w") as file2:
        file2.writelines(lines)