with open("johny.txt", "a") as file:
    x = file.write("Johny Johny\nYes Papa")

with open("johny.txt") as file:
    x = file.read()
    print(x)