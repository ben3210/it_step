a, b = map(int,input("Enter two numbers (Start - End): ").split())

all = []
multiples7 = []
multiples5 = 0

for i in range(a, b+1, 1):

    all.append(i)

    if i % 5 == 0:
        multiples5 += 1

    if i % 7 == 0:
        multiples7.append(i)
        
print("All numbers in the range: ", all)
print("All numbers (descending order): ", all[::-1])
print("Multiples of 7: ", multiples7)
print("How many numbers are multiples of 5? : ", multiples5)



