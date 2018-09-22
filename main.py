import sys
import json
import urllib.request
from bs4 import BeautifulSoup

# ========================================================================
# search results
# ========================================================================
search_results = BeautifulSoup(open('search.html'), 'html.parser')
first_artist = search_results.findChildren('li', attrs={'class': 'artist'})[0]
artist_link = first_artist.find('a')
tooltip = json.loads(artist_link.attrs['data-tooltip'])
artist_id = tooltip['id']

# ========================================================================
# discography page
# ========================================================================
discography_page = BeautifulSoup(open('robert-wyatt.html'), 'html.parser')
picks = discography_page.findChildren('tr', attrs={"class": "pick"})
artist = discography_page.title.text.split('|')[0].strip()

album_list = []
for pick in picks:
	album_list.append(pick.findChildren('td', attrs={"class": "title"})[0].text.strip())

# ========================================================================
# output
# ========================================================================
print(artist + ', eh? You should start with: ')
for album in album_list:
	print(album)

