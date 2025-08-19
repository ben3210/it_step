#ENGLISH-FRENCH DICTIONARY APPLICATION
import os
import msvcrt

def add_data(data_list, info, data):
    os.system('cls')
    print(f"\033[30;47m Adding New {data} \033[0m\n")
    new_data = {} 
    for i in info:
        is_empty_data = True
        while is_empty_data:
            new_data[i] = input(f"{i.replace("_", " ").title()}: ")
            is_empty_data = new_data[i].isspace() or new_data[i] == ""
    data_list.append(new_data)
    print(f"\033[32mNew {data} Added Successfully\033[0m")


def delete_data(data_list, info, data):
    os.system('cls')
    print(f"\033[30;47m Deleting {data} \033[0m\n")
    name = input("Word (english): ")#change........................................................................
    for dat in data_list:
        if dat[info[0]] == name:
            data_list.remove(dat)
            print(f"\033[32m{data} Deleted Successfully\033[0m")
            break
    else:
        print(f"\033[91m{data} not Found!\n(Hint: Type word correctly - Case Sensitive)\033[0m")#change..................................................
    

def search_data(data_list, info, data):
    os.system('cls')
    print(f"\033[30;47m Searching {data} \033[0m\n")
    
    is_empty_search = True
    while is_empty_search:
        search = input("Search (word - english): ")#change........................................................................
        is_empty_search = search.isspace() or search == ""
    dat = [n for n in data_list if search.lower() in n[info[0]].lower()]
    print(f"\033[32mSearch Results({len(dat)}):\033[0m")    

    for person in dat:
        person_name = person[info[0]]
        i = 0
        highlighted = ""
        while i < len(person_name):
            slice = person_name[i:i+len(search)]
            if slice.lower() == search.lower():
                highlighted += f"\033[33m{slice}\033[0m"
                i += len(search)
            else:
                highlighted += f"\033[34m{person_name[i]}\033[0m"
                i += 1
        if highlighted != "": person_name = highlighted

        for i in info:
            if i == info[0]: print(f"{i.replace("_", " ").title()}: {person_name}")
            else: print(f"{i.replace("_", " ").title()}: \033[34m{person[i]}\033[0m")
        print("-" * 30)
    if len(dat) == 0 : print(f"\033[91m{data} not Found!\033[0m")


def replace_data(data_list, info, data):
    os.system('cls')
    print(f"\033[30;47m Replacing {data} \033[0m\n")
    name = input("Word (english): ")#change........................................................................
    for dat in data_list:
        if dat[info[0]] == name:
            print("\033[34mEnter new Data:\033[0m")
            for i in info:
                dat[i] = input(f"{i.replace("_", " ").title()}: ")
            print(f"\033[32m{data} Replaced Successfully\033[0m")
            break
    else:
        print(f"\033[91m{data} not Found!\n(Hint: Type name correctly - Case Sensitive)\033[0m")


#Additional Function to Display all data stored in Dictionary
def display_data(data_list, info):
    os.system('cls')
    print(f"\033[30;47m List of {data}s({len(data_list)}) \033[0m\n")
    for dat in data_list:
        for i in info:
            print(f"{i.replace("_", " ").title()}: {dat[i]}")
        print("-" * 40)





english_french_words = [
    {
        "english": "apple",
        "french": "pomme"
    },
    {
        "english": "book",
        "french": "livre"
    },
    {
        "english": "house",
        "french": "maison"
    },
    {
        "english": "car",
        "french": "voiture"
    },
    {
        "english": "water",
        "french": "eau"
    },
    {
        "english": "sun",
        "french": "soleil"
    },
    {
        "english": "school",
        "french": "école"
    },
    {
        "english": "friend",
        "french": "ami"
    }
]


os.system('cls')
info = ["english", "french"]#change........................................................................
data = "Word"#change........................................................................

print("\033[1;37;44m Welcome - ENGLISH-FRENCH DICTIONARY APPLICATION \033[0m")#change........................................................................
app_running = True

while app_running:
    
    print("\033[30;47m Main Menu \033[0m\n")
    print(f"Press number in brackets for:\n(1) Add {data} \n(2) Delete {data} \n(3) Search {data} \n(4) Replace {data} \n(5) Show all {data}s \n(0) Exit Application\n")
        
    #try/except to catch error in case user types Special keys (arrows, function keys)that are not directly decodable
    try:
        user = msvcrt.getch().decode()
    except: 
        os.system('cls')
        continue

    if user == '0': app_running = False
    elif user == '1': add_data(english_french_words, info, data); os.system('pause')
    elif user == '2': delete_data(english_french_words, info, data); os.system('pause')
    elif user == '3': search_data(english_french_words, info, data); os.system('pause')
    elif user == '4': replace_data(english_french_words, info, data); os.system('pause')
    elif user == '5': display_data(english_french_words, info); os.system('pause')
    else: print("\033[91mInvalid Input! \n(Hint: Numerical Input | Type 0 - 5)\033[0m"); os.system('pause')
    os.system('cls')