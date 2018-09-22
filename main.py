import sys
import json
import requests
from bs4 import BeautifulSoup

# ========================================================================
# get the argument
# do a search
# ========================================================================
search_term = sys.argv[1]
search_url = 'https://www.allmusic.com/search/all/' + search_term
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
search_response = requests.get(search_url, headers=headers)

# ========================================================================
# search results
# ========================================================================
search_results = BeautifulSoup(search_response.text, 'html.parser')
first_artist = search_results.findChildren('li', attrs={'class': 'artist'})[0]
artist_link = first_artist.find('a')
tooltip = json.loads(artist_link.attrs['data-tooltip'])
artist_id = tooltip['id']

# ========================================================================
# discography page
# ========================================================================

discography_url = 'https://www.allmusic.com/artist/' + artist_id + '/discography'
discography_response = requests.get(discography_url, headers=headers)
discography_page = BeautifulSoup(discography_response.text, 'html.parser')
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

