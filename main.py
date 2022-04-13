from locale import currency
from httplib2 import Response
from requests import get
from pprint import PrettyPrinter

BASE_URL="https://free.currconv.com"
MY_API= "570b1a3db8efe2efe421"

printer= PrettyPrinter()

def get_currencies():
    endpoint = f"/api/v7/currencies?apiKey={MY_API}"

    url= BASE_URL + endpoint
    data = get(url).json()["results"]
    
    data = list(data.items())
    data.sort()
    
    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id}- {name} - {symbol}")
        
        
def exchange_rate(currency1, currency2): 
    endpoint = f"/api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={MY_API}"
    url= BASE_URL + endpoint
    response = get(url)   
    
    data = response.json()
    
    if len(data) == 0:
        print("check currencies entered")
        return
    
    rate =   list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    
    return rate 

def convert(currency1, currency2, amount):
    rate =exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try: 
        amount= float(amount)
    except:
        print("Enter valid amount.")  
        return
    
    converted_amount = rate * amount 
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount 

def main():
    currencies= get_currencies()
    
    print("Welcome to the currency converter.Select any of the below commands.")
    print("List- Lists the different type of currencied")
    print("convert- converts from one currency to another")
    print("Rate- get the exchange rate of the currencies")
 
    while True:
        command = input("Enter any of the above or (q to quit)").lower()
          
        if command =="q":
              break
        elif command == "List":
              print_currencies(currencies)
        elif  command =="convert":
              currency1 = input("Enter the currency that you have: ").upper()
              amount = input(f"Enter an amount in {currency}: ")
              currency2 = input ("Enter a currency to convert to: ").upper() 
              convert(currency1, currency2, amount) 
        elif command == "rate":
              currency1 =input("Enter the currency that you have: ").upper()
              currency2 = input("Enter the currency that you want to convert to: ").upper()
              exchange_rate(currency1, currency2)
        else:
            print("Invalid entry")      
main()            