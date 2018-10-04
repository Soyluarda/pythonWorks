import requests
import json

globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

request = requests.get(globalURL)
data = request.json()
globalMarketCap = data["total_market_cap_usd"]


#menu
print()
print("Welcome my CoinMarket")
print("Global cap of all cryptocurrencies $"+ str(globalMarketCap))
print("Enter 'all' or name of 'crypto'(i.e bitcoin to see name of top 100 currencies or a spesific currency)")
print()
choice = input("Your choice: ")

if choice == "all":
    request = requests.get(tickerURL)
    data = request.json()
    for x in data:
        ticker = x['symbol']
        price = x['price_usd']

        print (ticker + ":\t\s" + price)
    print()

else:
    tickerURL += '/'+choice+'/'
    request = requests.get(tickerURL)
    data = request.json()

    ticker = data[0]['symbol']
    price = data[0]['price_usd']

    print(ticker + ':\t\s'+ price)
    print()
