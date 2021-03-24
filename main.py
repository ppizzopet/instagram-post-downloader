import requests
import bs4
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, '
                         'like Gecko) Mobile/14G60 Instagram 12.0.0.16.90 (iPhone9,4; iOS 10_3_3; en_US; en-US; '
                         'scale=2.61; gamut=wide; 1080x1920)'}
posurl = input("Enter post url (with https) : ")
page = requests.get(posurl, headers=headers)
soup = bs4.BeautifulSoup(page.content, "html.parser")
imageurl = str(soup.find_all("script", type='text/javascript')[3]).rsplit('src":"')[1].split('","')[0].replace(
    r"\u0026", "&")
f = open(f'{posurl.split("/")[4]}.jpg','wb')
f.write(urllib.request.urlopen(imageurl).read())
f.close()
print("Post downloaded successfully!")
