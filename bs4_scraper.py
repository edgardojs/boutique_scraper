from bs4 import BeautifulSoup as bs
import requests

url = "https://www.superpagespr.com/Searchpg.aspx?nombre=%27Boutiques%27&ciudad=Caguas"

page = requests.get(url)

soup = bs(page.text, 'html.parser')

print(soup.find_all("div", {"class":"right-card"}))