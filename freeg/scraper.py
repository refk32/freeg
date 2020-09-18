import requests
from bs4 import BeautifulSoup
import json
import tldextract

def extract():
    """ 
    Scrape data on https://isthereanydeal.com/specials/ 
    
    """
    freegames = []
    url = "https://isthereanydeal.com/specials/"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
    }

    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, features="lxml")
    bundle = soup.find_all("div", attrs={"class" : "bundle-row1"})
    for i in bundle :
        
        bundle_title = i.find("div", attrs={"class" : "bundle-title"})
        bundle_tag = i.find("a", attrs={"class" : "bundle-tag"}).text
        
        if bundle_tag == "giveaway" :
            
            time_left = i.find("div", attrs={"class" : "bundle-time"}).text

            if "unknown" in time_left: 
                continue # search only for limited time free games       

            title = str(bundle_title.text).split("-")[0].strip() # extract the game title from whitespaces
            link = bundle_title.find("a", attrs={"href" : True})["href"]
            store = tldextract.extract(link).registered_domain
   
            freegames.append({"title" : title, "link" : link, "store" : store,"time_left" : time_left})
    
    return freegames



if __name__ == "__main__":
    print(extract())
