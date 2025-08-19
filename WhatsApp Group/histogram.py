#Task (Histogram): Mon 28 July, 2025
names = ["Alice", "Bob", "Charlie", "Alice", "David", "Emily", "Bob", "Frank", "Grace", "Emily", "Hannah", "Isaac", "Charlie", "Jack", "Grace"]
dict = {}

for name in names:
    count = 0
    for i in range(len(names)):
        if names[i] == name:
            count += 1
    dict[name] = count

print("Names and number of times they are repeated:")
for name in dict:
    print(f"{name} : {dict[name]}")