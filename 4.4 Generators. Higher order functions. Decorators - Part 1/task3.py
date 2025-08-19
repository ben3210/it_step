def show_line(symbol, function_to_call):
    return function_to_call(symbol)

def vertical(symbol):
    for i in range(5):
        print(symbol)
    
def horizontal(symbol):
    for i in range(5):
        print(symbol, end = " ")

symbol = input("Symbol: ")
line =  int(input("Type 1 - vertical 2 - horizontal: "))

if line == 1:
    show_line(symbol, vertical)

if line == 2:
    show_line(symbol, horizontal)