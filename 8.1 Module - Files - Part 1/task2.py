statistics = []
with open(r"task2.txt", "a+") as file:
    file.seek(0)
    x = file.read()
    file.seek(0)
    lines = file.readlines()
    
    vowels = 0
    consonants = 0
    digits = 0
    for char in x:
        if char in "aieuoAIEUO":
            vowels += 1
        elif char.isalpha() and char not in "aieuoAIEUO":
            consonants += 1
        elif char.isdigit():
            digits += 1

    statistics.append("Number of\n")
    statistics.append(f"Characters: {len(x)}\n")
    statistics.append(f"Lines: {len(lines)}\n")
    statistics.append(f"Vowels: {vowels}\n")
    statistics.append(f"Consonants: {consonants}\n")
    statistics.append(f"Digits: {digits}\n")

    with open("task2_statistics.txt", "w") as f:
        f.writelines(statistics)
    with open("task2_statistics.txt", "r") as f:
        print(f.read())
