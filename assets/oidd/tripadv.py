import requests
from bs4 import BeautifulSoup

base_url = 'https://www.tripadvisor.com/'  ## we need this to join the links later ##
main_page = 'https://www.tripadvisor.com/Attractions-g60795-Activities-c49-oa{}-Philadelphia_Pennsylvania.html#FILTERED_LIST'
links = {}

## get the initial page to find the number of pages ##
r = requests.get(main_page.format(0))
soup = BeautifulSoup(r.text, "html.parser")
## select the last page from the list of pages ('a', {'class':'pageNum taLnk'}) ##
last_page = max([ int(page.get('data-offset')) for page in soup.find_all('a', {'class':'pageNum taLnk'}) ])

## now iterate over that range (first page, last page, number of links), and extract the links from each page ##
for i in range(0, last_page + 30, 30):
    page = main_page.format(i)
    soup = BeautifulSoup(requests.get(page).text, "html.parser") ## get the next page and parse it with BeautifulSoup ##  
    ## get the hrefs from ('div', {'class':'listing_title'}), and join them with base_url to make the links ##
    vals = [ base_url + link.find('a').get('href') for link in soup.find_all('div', {'class':'listing_title'}) ]
    for val in vals:
      links[val] = 0

for link in list(links): 
    print(link)