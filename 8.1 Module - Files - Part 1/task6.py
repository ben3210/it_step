word = "end"
replace_with = "AAA"
with open("task6.txt", "r") as file:
    content = file.read()
    content = content.replace(word, replace_with)
    with open("task6.txt", "w") as f:
        f.write(content)