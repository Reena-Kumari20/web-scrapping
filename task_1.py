from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup
r=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(r.text,"html.parser")
def main():
    div=soup.find('div',class_='lister')
    tbody=div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')
    rank_list=[];movie_name=[];release_year=[];ratings=[];urls=[]
    for tr in trs:
        ranks=tr.find('td',class_='titleColumn').get_text().strip()
        rank=''
        for i in ranks:
            if '.' not in i:
                rank=rank+i
            else:
                break
        rank_list.append(rank)
        name=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(name)
        year=tr.find('td',class_="titleColumn").span.get_text()
        release_year.append(year)
        rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        ratings.append(rating)
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://wwwimdb.com"+link
        urls.append(movie_link)
    movies_list=[]
    dictionary={}
    i=0
    while i<len(rank_list):
        dictionary["position"]=rank_list[i]
        dictionary["name"]=movie_name[i]
        dictionary["year"]=int(release_year[i][1:5])
        dictionary["rating"]=ratings[i]
        dictionary["urls"]=urls[i]
        movies_list.append(dictionary.copy())
        #print(dictionary)      
        i+=1
    with open("task1.json","w") as f:
        json.dump(movies_list,f,indent=4)
    return movies_list
scrapping=main()
# pprint(scrapping)
# main()