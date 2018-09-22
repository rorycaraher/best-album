import sys
from bs4 import BeautifulSoup

# ========================================================================
# discography page
# ========================================================================
discography_page = BeautifulSoup(open('robert-wyatt.html'), 'html.parser')
picks = discography_page.findChildren('tr', attrs={"class": "pick"})
artist = soup.title.text.split('|')[0].strip()
print(artist)

album_list = []
for pick in picks:
	album_list.append(pick.findChildren('td', attrs={"class": "title"})[0].text.strip())


print("You should listen to: ")
for album in album_list:
	print(album)

