import json
from pathlib import Path
from colorama import Fore

json_file = Path("betting_journal.json")

def load_bet(json_file):
    if not json_file.exists():
        return[]
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return []

def save_bet(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def add_bet(bets):

    print("-------------------------")

    sports = input("Sport Name: ").capitalize().strip()
    team = input("Team Name: ").capitalize().strip()
    while True:
        try:
            amount = float(input("Bet Amount: "))
            break
        except ValueError:
            print("Enter Number")

    while True:
        result = input("W/L: ").upper().strip()
        if result not in ['W', 'L']:
            print("Enter 'w' or 'l'.")
        else:
            break

    while True:
        try:
            wl_amount = float(input("Win/Loss Amount: "))

            if result == 'W' and wl_amount < 0:
                print("Win should be positive")
                continue 

            if result == 'L' and wl_amount > 0:
                print("Loss should be negative")
                continue 

            break 

        except ValueError:
            print("Enter Number")

    print("-------------------------")

    new_bet = {
        "Sports" : sports,
        "Team" : team,
        "Bet Amount" : amount,
        "Result" : result,
        "Win/Loss Amount" : wl_amount
    }

    print("\n+++ Bet Added Successfully +++\n")

    bets.append(new_bet)

def show_bet(bets):

    print("--------------------------------")
    print("1 Seach with Sports Name")
    print("2 Search with Team Name")
    print("3 View All")
    print("--------------------------------")
    

    while True:
        try:
            user = int(input("Enter (1-3): "))
            if user == 1:
                sports_name = input("Enter Sports Name: ").strip().capitalize()

                found = False

                for bet in bets:
                    if bet["Sports"] == sports_name:
                        print (bet)
                        found = True
        
                if not found:
                    print("No Bets Found")


            elif user == 2:
                team_name = input("Enter Team Name: ").strip().capitalize()

                found = False

                for bet in bets:
                    if bet["Team"] == team_name:
                        print(bet)
                        found = True

                if not found:
                    print("No Bets Fouond")

            elif user == 3:
                with open (json_file, 'r') as f:
                    content = f.read().strip()

                    if not content:
                        print("No Habits Yet!")
                        return
        
                    data = json.loads(content)

                    print(json.dumps(data, indent=4))

            else:
                print("Enter Number")

            break
        except ValueError:
            print("Invalid Option")

def main():
    bets = load_bet(json_file)

    while True:
        print("*****************")
        print("1 Add Bet")
        print("2 Show Bet")
        print("3 Exit")
        print("*****************")

        while True:
            try:
                user = int(input("Enter Number: "))
                break
            except ValueError:
                print("Invalid Option")

        if user == 1:
            add_bet(bets)
            save_bet(json_file, bets)

        elif user == 2:
            show_bet(bets)

        else:
            break

main()