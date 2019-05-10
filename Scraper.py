from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os, ssl

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

#need to specify breed and add to end of url
link = 'https://www.greenfieldpuppies.com/akita-puppies-for-sale/'
link2= 'https://www.pets4homes.co.uk/dog-breeds/chihuahua/#CharacteristicsSection'
link3= 'https://dogtime.com/dog-breeds/golden-retriever#/slide/1'
link4= 'http://www.vetstreet.com/dogs/cavapoo'

req = Request(url=link, headers=headers) 
html = urlopen(req, timeout=5).read()
req2 = Request(url=link2, headers=headers) 
html2 = urlopen(req2, timeout=5).read()
req3 = Request(url=link3, headers=headers) 
html3 = urlopen(req3, timeout=5).read()
req4 = Request(url=link4, headers=headers) 
html4 = urlopen(req4, timeout=5).read()

soup = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')
soup3 = BeautifulSoup(html3, 'html.parser')
soup4 = BeautifulSoup(html4, 'html.parser')

activityLevel=soup.find('span', 'trait').getText()
print("Acitivity Level: "+activityLevel)

aloneString = soup2.find_all('span',class_='ratingText')[8].getText()
length = len(aloneString)
alone= aloneString[length-4:length-1]
print("Tolerates alone: "+alone)

exerciseString = soup2.find_all('span',class_='ratingText')[1].getText()
length = len(exerciseString)
exercise= exerciseString[length-4:length-1]
print("Exercise Needs: "+exercise)

allergies=soup4.find("div",class_="desktop-experience tablet-experience").table.tr.find_all("td")[5].span.getText()[0]
print("Allergies: "+allergies)

costString = soup2.find_all('span',class_='ratingText')[7].getText()
length = len(costString)
cost= costString[length-4:length-1]
print("Cost: "+cost)

kidFriendly = soup.find_all('span', 'trait')[4].getText()
print("Kid friendly: "+kidFriendly)

react=soup4.find("div",class_="desktop-experience tablet-experience").table.find_all("tr")[2].find_all("td")[5].span.getText()[0]
print("Home reaction: "+react)

sizeString = soup2.find_all('span',class_='ratingText')[0].getText()
length = len(sizeString)
size= sizeString[length-4:length-1]
print("Size: "+size)

trainability = soup.find_all('span', 'trait')[2].getText()
print("Trainability: "+trainability)

weather=soup3.find_all("div",class_="characteristic-star-block")[5].div.getText()
print("Tolerates cold weather: "+weather)

groomString = soup2.find_all('span',class_='ratingText')[4].getText()
length = len(groomString)
groom= groomString[length-4:length-1]
print("Grooming Needs: "+groom)





