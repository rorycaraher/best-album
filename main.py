import sys
import json
import requests
from bs4 import BeautifulSoup

# ========================================================================
# get the argument
# set headers so the query doesn't get rejected!
# ========================================================================
search_term = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# ========================================================================
# do a search
# ========================================================================
search_url = 'https://www.allmusic.com/search/all/' + search_term
search_response = requests.get(search_url, headers=headers)

# ========================================================================
# search results
# ========================================================================
search_results = BeautifulSoup(search_response.text, 'html.parser')
first_artist = search_results.find('li', attrs={'class': 'artist'})
artist_link = first_artist.find('a')
tooltip = json.loads(artist_link.attrs['data-tooltip'])
artist_id = tooltip['id']

# ========================================================================
# discography page
# ========================================================================
discography_url = 'https://www.allmusic.com/artist/' + artist_id + '/discography'
discography_response = requests.get(discography_url, headers=headers)
discography_page = BeautifulSoup(discography_response.text, 'html.parser')
artist = discography_page.title.text.split('|')[0].strip()
picks = discography_page.findChildren('tr', attrs={"class": "pick"})

# ========================================================================
# output
# ========================================================================
if picks:
	album_list = []
	for pick in picks:
		album_list.append(pick.findChildren('td', attrs={"class": "title"})[0].text.strip())

	print(artist + ', eh? You should start with: ')
	for album in album_list:
		print(album)
else:
	print('Not sure where to start with ' + artist + '...')
