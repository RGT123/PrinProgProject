from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

link = 'https://www.greenfieldpuppies.com/'
link2 = 'https://www.petfinder.com/search/dogs-for-adoption/us/tx/round-rock/?distance=Anywhere'
link3= 'https://barkavenuepuppies.com/havanese/'
link4= 'https://www.puppyspot.com/puppies-for-sale/breed/french-bulldog/puppy/598245?puppy_index=0'
link5= 'https://www.petlandflorida.com/pet/detail/akita/pembroke-pines/2284231/'


req = Request(url=link, headers=headers, timeout=5) 
html = urlopen(req).read()
req2 = Request(url=link2, headers=headers, timeout=5) 
html2 = urlopen(req2).read()
req3 = Request(url=link3, headers=headers, timeout=5) 
html3 = urlopen(req3).read()
req4 = Request(url=link4, headers=headers, timeout=5) 
html4 = urlopen(req4).read()
req5 = Request(url=link5, headers=headers, timeout=5) 
html5 = urlopen(req5).read()

soup = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')
soup3 = BeautifulSoup(html3, 'html.parser')
soup4 = BeautifulSoup(html4, 'html.parser')
soup5 = BeautifulSoup(html5, 'html.parser')

#print(soup.prettify())
