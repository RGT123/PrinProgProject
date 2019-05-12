from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from Dog import doggie
import os, ssl
import threading

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
           'Connection': 'Close'
           }

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

breeds = ['Golden Retriever','akita','Rottweiler','Pomeranian',
          'chihuahua','Yorkshire terrier','Poodle','Dachshund',
          'schnoodle','Pomsky', 'shih tzu','Labrador Retriever',
          'Siberian Husky','German Shepherd','boxer','Australian shepherd',
          'Great dane','Doberman pinscher','Cavalier king charles spaniel'
]

dogs={}

def generateAttributes(index):
    breed=breeds[index].replace(' ','-').lower()
    link = 'https://www.greenfieldpuppies.com/'
    link2= 'https://www.pets4homes.co.uk/dog-breeds/'
    link3= 'https://dogtime.com/dog-breeds/'
    link4= 'http://www.vetstreet.com/dogs/'

    if breed == 'poodle':
        link+='standard-poodle-puppies-for-sale/'
    elif breed == 'labrador-retriever':
        link+='yellow-'+breed+'-puppies-for-sale/'
    else:
        link+=breed+'-puppies-for-sale/'
    if breed == 'doberman-pinscher':
        link2+='dobermann/#CharacteristicsSection'
    else:
        link2+=breed+'/#CharacteristicsSection'
    link3+=breed
    link4+=breed
    if breed == 'german-shepherd':
        link3+='-dog'
        link4+='-dog'
    
    req = Request(url=link, headers=headers) 
    html = urlopen(req, timeout=10).read()
    req2 = Request(url=link2, headers=headers) 
    html2 = urlopen(req2, timeout=10).read()
    req3 = Request(url=link3, headers=headers) 
    html3 = urlopen(req3, timeout=10).read()
    req4 = Request(url=link4, headers=headers) 
    html4 = urlopen(req4, timeout=10).read()
 
    soup = BeautifulSoup(html, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')
    soup3 = BeautifulSoup(html3, 'html.parser')
    soup4 = BeautifulSoup(html4, 'html.parser')
    
    activityLevel=soup.find('span', 'trait').getText()

    aloneString = soup2.find_all('span',class_='ratingText')[8].getText()
    length = len(aloneString)
    alone= aloneString[length-4:length-1]

    exerciseString = soup2.find_all('span',class_='ratingText')[1].getText()
    length = len(exerciseString)
    exercise= exerciseString[length-4:length-1]

    allergies=soup4.find("div",class_="desktop-experience tablet-experience").table.tr.find_all("td")[5].span.getText()[0]

    costString = soup2.find_all('span',class_='ratingText')[7].getText()
    length = len(costString)
    cost= costString[length-4:length-1]
    
    kidFriendly = soup.find_all('span', 'trait')[4].getText()
    
    react=soup4.find("div",class_="desktop-experience tablet-experience").table.find_all("tr")[2].find_all("td")[5].span.getText()[0]
    
    sizeString = soup2.find_all('span',class_='ratingText')[0].getText()
    length = len(sizeString)
    size= sizeString[length-4:length-1]
    
    trainability = soup.find_all('span', 'trait')[2].getText()

    weather=soup3.find_all("div",class_="characteristic-star-block")[5].div.getText()
    
    groomString = soup2.find_all('span',class_='ratingText')[4].getText()
    length = len(groomString)
    groom= groomString[length-4:length-1]
    
    obj = doggie(activityLevel,
                 alone,
                 exercise,
                 allergies,
                 cost,
                 kidFriendly,
                 react,
                 size,
                 trainability,
                 weather,
                 groom
                )
    dogs["breed{0}".format(index)]=obj
    
def main():

    try:
        threads = [threading.Thread(target=generateAttributes, args=(x,)) for x in range(0,len(breeds))]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            
        #for x in range(0,len(breeds)):
          #  print(breeds[x])
           # dogs["breed{0}".format(x)].printinfo()
        #print(dogs)
    except ConnectionError as e:
        print("Connection Error.\n")
        print(str(e))
    except TimeoutError as e:
        print("Timeout Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")
    except Exception as e:    
        print("General Error")
        print(str(e))
if __name__ == "__main__":
    main()