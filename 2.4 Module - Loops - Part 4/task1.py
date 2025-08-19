#Multiple of 7 in range provided by User

a, b = map(int,input("Enter two numbers (Start - End): ").split())

for i in range(a, b+1):
    if i % 7 == 0:
        print(i)

