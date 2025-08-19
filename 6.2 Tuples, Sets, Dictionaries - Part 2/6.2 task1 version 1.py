import os

def add_player(players_list):
    os.system('cls')
    print("\033[30;47mAdding Player\033[0m\n")
    name = input("Full Name: ")
    height = int(input("Height (in cm): "))
    players_list[name] = height
    print(f"\033[32mPlayer Added Successfully\033[0m")


def delete_player(players_list):
    os.system('cls')
    print("\033[30;47mDeleting Player\033[0m\n")
    name = input("Full Name: ")
    try: del players_list[name]; print(f"\033[32mPlayer Deleted Successfully\033[0m")
    except: print("\033[91mPlayer not Found!\n(Hint: Type full name correctly and start names with Capital Letters)\033[0m")
    

def search_player(players_list):
    os.system('cls')
    print("\033[30;47mSearching Player\033[0m\n")
    name = input("Name: ")
    #allowing user to enter a part of name or single name and still be able to search (powerful search)
    #user can enter first name or a segment of the name and get the full details of the player. if multiple results, display all of them
    found_player = [player for player in players_list if name.lower() in player.lower()]
    print(f"\033[32mSearch Results({len(found_player)}):\033[0m")
    for i in found_player:
        print(f"Full Name: \033[34m{i}\033[0m")
        print(f"Height: \033[34m{players_list[i]}\033[0m")
    if len(found_player) == 0 : print("\033[91mPlayer not Found!\033[0m")


def replace_player(players_list):
    os.system('cls')
    print("\033[30;47mReplacing Player\033[0m\n")
    name = input("Full Name: ")
    new_name = input("New Full Name: ")
    new_height = int(input("New Height (in cm): "))
    try: del players_list[name]; players_list[new_name] = new_height; print(f"\033[32mPlayer Replaced Successfully\033[0m")
    except: print("\033[91mPlayer not Found!\n(Hint: Type full name correctly and start names with Capital Letters)\033[0m")


#Additional Function to Display all data stored in Dictionary
def display_data(players_list):
    os.system('cls')
    print(f"\033[30;47mList of Players({len(players_list)})\033[0m\n")
    print("Name --> Height\n")
    for name, height in players_list.items():
        print(name, "-->", height, "cm")
    print("")





basketball_players = {
    "Michael Jordan": 198,
    "LeBron James": 206,
    "Stephen Curry": 188,
    "Kobe Bryant": 198,
    "Shaquille O'Neal": 216,
    "Kevin Durant": 208,
    "Giannis Antetokounmpo": 211,
    "Tim Duncan": 211,
    "Magic Johnson": 206,
    "Larry Bird": 206
}

print("\033[37;44mWelcome - BASKETBALL PLAYERS APPLICATION\033[0m")
app_running = True

while app_running:
    
    print("\033[30;47mMain Menu\033[0m\n")
    user = int(input("Type number in brackets for:\n(1) Add Player \n(2) Delete Player \n(3) Search Player \n(4) Replace Player \n(5) Show all Players \n(0) Exit Application\n"))
    
    if user == 0: app_running = False
    elif user == 1: add_player(basketball_players); os.system('pause')
    elif user == 2: delete_player(basketball_players); os.system('pause')
    elif user == 3: search_player(basketball_players); os.system('pause')
    elif user == 4: replace_player(basketball_players); os.system('pause')
    elif user == 5: display_data(basketball_players); os.system('pause')
    else: print("\033[91mInvalid Input! \n(Hint: Type 0 - 5)\033[0m"); os.system('pause')
    os.system('cls')