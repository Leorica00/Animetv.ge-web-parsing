import time
import requests
import csv
from bs4 import BeautifulSoup
import random


file = open("animes.csv", "w", encoding="utf-8_sig", newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(["სათაური ქართულად", "სათაური", "სურათის URL"])

for i in range(1, 8):
    url = f"https://animetv.night-city.online/page/{i}/"
    r = requests.get(url)
    res = r.text
    soup = BeautifulSoup(res, "html.parser")
    soup_sub = soup.find("div", id="dle-content")
    all_animes = soup_sub.find_all("div", class_="movie-item")
    for anime in all_animes:
        img_url = "https://animetv.night-city.online" + anime.a.img.attrs.get("src")
        img_url.replace("original", "")
        title_bar_translate = anime.find("div", class_="movie-item__title")
        anime_name_translate = title_bar_translate.text
        title_bar = anime.find("div", class_="movie-item__meta ws-nowrap")
        anime_name = title_bar.span.text
        file_obj.writerow([anime_name_translate, anime_name, img_url])
    time.sleep(random.randint(15, 20))
    #
file.close()
