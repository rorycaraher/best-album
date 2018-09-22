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
print(artist_id)
