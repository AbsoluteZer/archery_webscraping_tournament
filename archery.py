import requests
from bs4 import BeautifulSoup

def scrape_tournament_names(soup:BeautifulSoup):
    # print(soup.find_all('td'))
    names=soup.find_all("td",class_="column3")
    return names

def scrape_tournament_dates(soup:BeautifulSoup):
    # print(soup.find_all('td'))
    dates=soup.find_all("td",class_="column7")
    return dates

def scrape_tournament_place(soup:BeautifulSoup):
    # print(soup.find_all('td'))
    places=soup.find_all("td",class_="column6")
    return places

def main(year:int):
    url = f"https://ianseo.net/TourList.php?Year={year}&countryid=MAS&comptime=&timeType=local"
    response = requests.get(url)
    print(response)
    response.raise_for_status()  # Raise an exception for HTTP errors
    soup = BeautifulSoup(response.content,"html.parser")
    names=scrape_tournament_names(soup)
    dates=scrape_tournament_dates(soup)
    places=scrape_tournament_place(soup)
    tournament_details:list[dict[str,str]]=[]
    for x in range(len(names)):
        name=names[x].get_text()
        date=dates[x].get_text()
        place=places[x].get_text()
        tournament_details.append({"name":name,"date":date,"place":place})

    return {"year":year,"lists":tournament_details,"count":len(tournament_details)}


    



