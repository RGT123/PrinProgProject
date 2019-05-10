from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os, ssl

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

#need to specify breed and add to end of url
#link = 'https://www.greenfieldpuppies.com/'
link = 'https://www.greenfieldpuppies.com/akita-puppies-for-sale/'
link2= 'https://www.petlandflorida.com/pet/detail/akita/pembroke-pines/2284231/'
#link2 = 'https://www.petfinder.com/search/dogs-for-adoption/us/tx/round-rock/?distance=Anywhere'
#link3= 'https://barkavenuepuppies.com/havanese/'
#link4= 'https://www.puppyspot.com/puppies-for-sale/breed/french-bulldog/puppy/598245?puppy_index=0'
#link5= 'https://www.petlandflorida.com/pet/detail/akita/pembroke-pines/2284231/'


req = Request(url=link, headers=headers) 
html = urlopen(req, timeout=5).read()
req2 = Request(url=link2, headers=headers) 
html2 = urlopen(req2, timeout=5).read()
#req3 = Request(url=link3, headers=headers) 
#html3 = urlopen(req3, timeout=5).read()
#req4 = Request(url=link4, headers=headers) 
#html4 = urlopen(req4, timeout=5).read()
#req5 = Request(url=link5, headers=headers) 
#html5 = urlopen(req5, timeout=5).read()

soup = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')
#soup3 = BeautifulSoup(html3, 'html.parser')
#soup4 = BeautifulSoup(html4, 'html.parser')
#soup5 = BeautifulSoup(html5, 'html.parser')
# =============================================================================
activityLevel=soup.find('span', 'trait').getText()
kidFriendly = soup.find_all('span', 'trait')[4].getText()
trainability = soup.find_all('span', 'trait')[2].getText()

div_container = soup2.find('div', class_='container container--reduce container-fluid-sm detail').div.section.div  
print(div_container)

#div3=div2.find('div', class_ ='row')
#div4=div3.find_all('div')[1]
#div5=div4.div.div
#alone=div5.find('div',class_ = 'progress')[2]['aira-valuenow'].string
print("Acitivity Level: "+activityLevel)
#print(alone)

print("Kid friendly: "+kidFriendly)
print("Trainability: "+trainability)