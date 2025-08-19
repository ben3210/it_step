with open("task1_text1.txt") as file:
    file1_lines = [line.replace("\n", "") for line in file]
    with open("task1_text2.txt") as file2:
        file2_lines = [line.replace("\n", "") for line in file2]
        for i in range(len(file1_lines)):
            if file1_lines[i] != file2_lines[i]:
                print(f"First file: Line {i+1}: {file1_lines[i]} \nSecond file: Line {i+1}: {file2_lines[i]}")