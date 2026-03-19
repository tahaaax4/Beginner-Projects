import os
import requests 
import json
from pathlib import Path
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()


store_coin = Path("store_coin.json")

def get_data():
    url = "https://openapiv1.coinstats.app/coins"
    API_KEY = os.getenv("API_KEY")

    header = {
        "X-API-KEY" : API_KEY
    }

    response = requests.get(url , headers = header)
    if response.status_code == 200:
        data = response.json()
        return data
        
    else:
        print("API ERROR!")

def save_data(data):

    cleaned_data = []

    for coin in data["result"]:
        coin_info = {
            "Rank" : coin['rank'],
            "Symbol" : coin['symbol'],
            "Price" : f"${round(coin['price'], 3)}",
            "24 Change" : coin['priceChange1d']
            
        }
        cleaned_data.append(coin_info) 

    with open(store_coin, 'w') as f:
        json.dump(cleaned_data, f, indent=4)   

def load_data(store_coin):

    if not store_coin.exists():
        return []
    
    try:
        with open(store_coin, 'r') as f:
            data = json.load(f)
            return data
        
    except json.JSONDecodeError:
        return []

def search_coin(coins):

    user = input("Enter Symbol: ").upper()

    found = False

    for coin in coins:
        if coin["Symbol"] == user:

            change_val = coin["24 Change"]

            if change_val >= 0:
                change_val = Fore.GREEN + str(change_val) + "%" + Fore.RESET
            else:
                change_val = Fore.RED + str(change_val) + "%" + Fore.RESET

            print(f"""
                    Rank   : {coin["Rank"]}
                    Symbol : {coin["Symbol"]}
                    Price  : {coin["Price"]}
                    24h %  : {change_val}
                """)
            
            found = True
            break
    if not found:
        print(f"No Match for this Symbol '{user}'")

def top_coin(coins):

    print(f"{'Rank':<6} {'Symbol':<8} {'Price':<10} {'Change':<8}")  #Format Align Left < 10 Space
    print("------------------------------------")     

    for coin in coins[:10]:

        rank = coin["Rank"]
        symbol = coin["Symbol"]
        price = coin["Price"]
        change = coin["24 Change"]

        if change >= 0:
            change_str = Fore.GREEN + f"{change}%" + Fore.RESET
        else:
            change_str = Fore.RED + f"{change}%" + Fore.RESET

        print(f"{rank:<6} {symbol:<8} {price:<10} {change_str:<8}")

def top_gainers(coins):

    print(f"{'Rannk':<6} {'Symbol':<8} {'Price':<10} {'Change':<8}")
    print("------------------------------------")  

    coins.sort(key = lambda coin : coin['24 Change'], reverse = True)

    for i, coin in enumerate(coins[:10], start=1):
        rank = i
        symbol = coin["Symbol"]
        price = coin["Price"]
        change = coin["24 Change"]

        print(f"{rank:<6} {symbol:<8} {price:<10} {change:<8}")

def top_losers(coins):

    print(f"{'Rannk':<6} {'Symbol':<8} {'Price':<10} {'Change':<8}")
    print("------------------------------------")  

    coins.sort(key = lambda coin : coin['24 Change'], reverse = False)

    for i, coin in enumerate(coins[:10], start=1):
        rank = i
        symbol = coin["Symbol"]
        price = coin["Price"]
        change = coin["24 Change"]

        print(f"{rank:<6} {symbol:<8} {price:<10} {change:<8}")
        
def view_all(coins):

    for coin in coins:
        print(f"""
                    Rank   : {coin["Rank"]}
                    Symbol : {coin["Symbol"]}
                    Price  : {coin["Price"]}
                    24h %  : {coin["24 Change"]}
                """)
        
def main():

    coins = load_data(store_coin)

    while True:
        print("--------------------")
        print("1 Refresh Data")
        print("2 Search Coin")
        print("3 Top Coin")
        print("4 Top Gainers")
        print("5 Top Losers")
        print("6 View All")
        print("7 Exit")
        print("--------------------")

        try:
            user = int(input("Enter Number: "))

            if user == 1:
                data = get_data()
                save_data(data)
                
                

            elif user == 2:
                search_coin(coins)

            elif user == 3:
                top_coin(coins)

            elif user == 4:
                top_gainers(coins)

            elif user == 5:
                top_losers(coins)
            
            elif user == 6:
                view_all(coins)
            
            elif user == 7:
                print("BYE!")
                break

            else:
                print("Invalid Input")

        except ValueError:
            print("Enter Number.")

main()
