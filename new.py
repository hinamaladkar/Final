from bs4 import BeautifulSoup
import requests as rq
import csv

news = []

url = "http://www.moneycontrol.com/news/stocks-in-news-142-1882-next-188.html"

req = rq.get(url)

soup = BeautifulSoup(req.content, "lxml")

a = soup.find_all("ul","nws_listing")

print(len(a))

b = a[0].find_all("div","ohidden")

for i in b:

    #print i
    #print
    v = i.find_all("a","nws_linkhd")[0].get("href")
    print(v)
    print
    
        
    
    


