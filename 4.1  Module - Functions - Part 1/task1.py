#Printing with different colors using ANSI Escape codes

def bill_gates():
    return """\n\033[90m\"Don't compare yourself with anyone in this world...\033[0m
     \033[91mif\033[0m you \033[91mdo so\033[0m, you are insulting yourself.\033[90m\"\033[0m 
                                                Bill Gates\n"""

print(bill_gates())