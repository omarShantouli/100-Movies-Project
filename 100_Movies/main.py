from bs4 import BeautifulSoup
import requests
import html
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select(selector="h3")
movies.reverse()
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for m in movies:
        t = html.unescape(m.getText())
        file.write(f"{t}\n")
