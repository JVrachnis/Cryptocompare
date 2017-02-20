from urllib.request import *
import json
import datetime
import time
userinputdate =str(int(time.mktime(datetime.datetime.strptime(input("day/month/year \n'in numbers like 00/00/0000':"), "%d/%m/%Y").timetuple())))
userinputcoins = input("input the coins you like to find \n exaple BTC/XNC:").split("/")
coinlisthttps = urlopen("https://www.cryptocompare.com/api/data/coinlist/").read().decode('utf-8').replace("XNC\t", "XNC")
coinlistdata = json.loads(coinlisthttps)["Data"]
coinlistdata = [w.replace("\t","") for w in coinlistdata]
for coin in userinputcoins:
    if coin in coinlistdata:
        print(coin + ":")
        coinpricehistoricalhttps = urlopen("https://www.cryptocompare.com/api/data/pricehistorical?fsym="+coin+"&tsyms=EUR&ts="+userinputdate).read().decode('utf-8')
        coinpricehistoricaldata = json.loads(coinpricehistoricalhttps)["Data"]
        if coinpricehistoricaldata != []:
            print(coinpricehistoricaldata[0]["Price"])
        else:
            print(coin + " does not have any data")
    else:
        print(coin + " does not exist")
