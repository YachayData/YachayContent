import numpy as np


from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import os 

# fecha y nombre del archivo

date = str(datetime.date.today())
folder_name = '../output/' + str(date) 

try:
	os.mkdir(folder_name)
	os.mkdir(folder_name + '/img')
	os.mkdir(folder_name + '/logo')
except:
	pass


header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}


url_name = "https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRFZxYUdjU0JtVnpMVFF4T1JvQ1Ewd29BQVAB?hl=es-419&gl=CL&ceid=CL%3Aes-419"
url = requests.get(url_name, headers=header)


soup = BeautifulSoup(url.text, "html.parser")


profiles = soup.find_all("a", attrs={"class": "WwrzSb"})
	       

images = soup.find_all('img', attrs={"class": "Quavad"})
logos =  soup.find_all('img', attrs={"class": "msvBD zC7z7b"})
names = []
for i in range(10):
	name = profiles[i]['aria-label']
	names.append(name)
	image_url = images[i]['src']
	logo_url = logos[i]['src']
	
	img_data = requests.get(image_url).content
	img_name = folder_name + '/img/' + str(i) + '.webp'
	with open(img_name, 'wb') as handler:
    		handler.write(img_data)
    		
	logo_data = requests.get(logo_url).content
	logo_name = folder_name + '/logo/' + str(i) + '.webp'
	with open(logo_name, 'wb') as handler:
		handler.write(logo_data)

df = pd.DataFrame(names)
df.to_csv(folder_name + '/data.csv', index=False)
