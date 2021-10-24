#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.


# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# In[4]:


link='https://en.wikipedia.org/wiki/Main_Page'


# In[6]:


page=requests.get(link)
page


# In[10]:


soup=bs(page.content,'html.parser')


# In[27]:


tags=['h1','h2','h3','h4']
for i in soup.find_all(tags):
    print(i.name+'-'+i.text.replace('\n',''))


# In[30]:


#2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame.

get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.imdb.com/chart/top/'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

movies=soup.find_all('td',class_='titleColumn')
rat=soup.find_all('td',class_='ratingColumn imdbRating')
year=soup.find_all('span',class_='secondaryInfo')
movielist=[]
rating=[]
yearr=[]
for i in movies:
    for a in i.find_all('a'):
        movielist.append(i.text.replace('\n',''))
for i in rat:
    for a in i.find_all('strong'):
        rating.append(i.text.replace('\n',''))
for i in year:
    for j in range(0,len(year)):
        yearr.append(i.text.replace('\n',''))


IMDBTOP100=pd.DataFrame({})

IMDBTOP100['movielist']=movielist[:100]
IMDBTOP100['rating']=rating[:100]
IMDBTOP100['year']=year[:100]
IMDBTOP100


# In[3]:


#3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year of release) and make data frame.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.imdb.com/india/top-rated-indian-movies/'

data=requests.get(link)

soup=bs(data.content,'html.parser')

movies=soup.find_all('td',class_='titleColumn')
rating=soup.find_all('td',class_='ratingColumn imdbRating')
year=soup.find_all('span',class_='secondaryInfo')

Movie_Name=[]
Imdb_rating=[]
re_year=[]
for i in movies:
    for j in i.find_all('a'):
        Movie_Name.append(i.text.replace('\n',''))
for i in rating:
    for j in i.find_all('strong'):
        Imdb_rating.append(i.text.replace('\n',''))
for i in year:
    for j in range(0,len(year)):
        re_year.append(i.text.replace('\n',''))

imdb_movies=pd.DataFrame({})

imdb_movies['Movie_Name']=Movie_Name[:100]
imdb_movies['Imdb_rating']=Imdb_rating[:100]
imdb_movies['re_year']=re_year[:100]

imdb_movies


# In[33]:


#4.i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/mens/team-rankings/odi'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

teams=soup.find_all('span',class_='u-hide-phablet')

team=[]
for i in teams:
    team.append(i.text.replace('\n',''))

matches=soup.find_all('td',class_='table-body__cell u-center-text')

match=[]
for i in matches:
    match.append(i.text.replace('\n',''))
match[0:18:2]

points=soup.find_all('td',class_='table-body__cell u-center-text')

point=[]
for i in points:
    point.append(i.text.replace('\n',''))
point[1:19:2]

ratings=soup.find_all('td',class_='table-body__cell u-text-right rating')

rating=[]
for i in ratings:
    rating.append(i.text.replace('\n',''))
rating[0:9]

Top10Rank=pd.DataFrame({})
Top10Rank['Team']=team[1:10]
Top10Rank['Matches']=match[0:18:2]
Top10Rank['Ratings']=rating[0:9]
Top10Rank['Points']=point[1:19:2]
Top10Rank

TopBARank=pd.DataFrame({'Team':['New Zealand'],'Matches':['17'],'Ratings':['121'],'Points':['2054']})
TopBARank

Top10Teams=pd.concat([TopBARank,Top10Rank]).set_index('Team')
Top10Teams


# In[5]:


#4.ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/mens/player-rankings/odi'

data=requests.get(link)

soup=bs(data.content,'html.parser')

player=soup.find_all('td',class_='table-body__cell name')

players=[]
for i in player:
    for j in i.find_all('a'):
        players.append(i.text.replace('\n',''))
players[0:9]

team=soup.find_all('span',class_='table-body__logo-text')

teams=[]
for i in team:
    teams.append(i.text.replace('\n',''))
teams[0:9]

ratings=soup.find_all('td',class_='table-body__cell u-text-right rating')

rating=[]
for i in ratings:
    rating.append(i.text.replace('\n',''))
rating[0:9]

TopBatsmen=pd.DataFrame({})
TopBatsmen['Player Name']=players[0:9]
TopBatsmen['Team']=teams[0:9]
TopBatsmen['Rating']=rating[0:9]
TopBatsmen

Banner=pd.DataFrame({'Player Name':['Baber Azam'],'Team':['Pak'],'Rating':['873']})
Banner

Top10Batsmen=pd.concat([Banner,TopBatsmen]).set_index('Player Name')
Top10Batsmen


# In[6]:


#4.iii) Top 10 ODI bowlers along with the records of their team and rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'

data=requests.get(link)

soup=bs(data.content,'html.parser')

bowler=soup.find_all('td',class_='table-body__cell rankings-table__name name')

bowlers=[]
for i in bowler:
    for j in i.find_all('a'):
        bowlers.append(i.text.replace('\n',''))    

bowlers[0:9]

team=soup.find_all('span',class_='table-body__logo-text')

teams=[]
for i in team:
    teams.append(i.text.replace('\n',''))
    

teams[0:9]

rating=soup.find_all('td',class_='table-body__cell rating')

ratings=[]
for i in rating:
    ratings.append(i.text.replace('\n',''))

ratings[0:9]

TopBowlers=pd.DataFrame({})
TopBowlers['Bowlers']=bowlers[0:9]
TopBowlers['Team']=teams[0:9]
TopBowlers['Ratings']=ratings[0:9]

Banner=pd.DataFrame({'Bowlers':['Trent Boult'],'Team':['NZ'],'Ratings':['737']})

Top10Bowlers=pd.concat([Banner,TopBowlers])
Top10Bowlers.set_index('Bowlers')


# In[7]:


#5.i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/womens/team-rankings/odi'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

team=soup.find_all('span',class_='u-hide-phablet')

teams=[]
for i in team:
    teams.append(i.text.replace('\n',''))
teams[1:10]

match=soup.find_all('td',class_='table-body__cell u-center-text')

matches=[]
for i in match:
    matches.append(i.text.replace('\n',''))
matches[0:20:2]

point=soup.find_all('td',class_='table-body__cell u-center-text')

points=[]
for i in point:
    points.append(i.text.replace('\n',''))
points[1:20:2]

rating=soup.find_all('td',class_='table-body__cell u-text-right rating')

ratings=[]
for i in rating:
    ratings.append(i.text.replace('\n',''))
ratings[0:10]

Topteams=pd.DataFrame({})
Topteams['Teams']=teams[1:10]
Topteams['Matches']=matches[0:20:2]
Topteams['Points']=points[1:20:2]
Topteams['Ratings']=ratings[0:10]

Banner=pd.DataFrame({'Teams':['Australia'],'Matches':['21'],'Points':['3,379'],'Ratings':['161']})

Top10Teams=pd.concat([Banner,Topteams]).set_index('Teams')
Top10Teams



# In[8]:


#5.ii) Top 10 women’s ODI players along with the records of their team and rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

players=soup.find_all('td',class_='table-body__cell name')

player=[]
for i in players:
    for j in i.find_all('a'):
        player.append(i.text.replace('\n',''))
player[0:9]

team=soup.find_all('span',class_='table-body__logo-text')

teams=[]
for i in team:
    teams.append(i.text.replace('\n',''))
teams[0:9]

rating=soup.find_all('td',class_='table-body__cell u-text-right rating')

ratings=[]
for i in rating:
    ratings.append(i.text.replace('\n',''))
ratings[0:9]

Top10Players=pd.DataFrame({})

Top10Players['Name']=player[0:9]
Top10Players['Team']=teams[0:9]
Top10Players['Ratings']=ratings[0:9]

Banner=pd.DataFrame({'Name':['Lizelle Lee'],'Team':['AUS'],'Ratings':['750']})

Top10WomensPlayer=pd.concat([Banner,Top10Players]).set_index('Name')

Top10WomensPlayer


# In[9]:


#5.iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

Name=soup.find_all('td',class_='table-body__cell rankings-table__name name')

Names=[]
for i in Name:
    for j in i.find_all('a'):
        Names.append(i.text.replace('\n',''))
Names[0:9]

team=soup.find_all('span',class_='table-body__logo-text')

teams=[]
for i in team:
    teams.append(i.text.replace('\n',''))
teams[0:9]

rating=soup.find_all('td',class_='table-body__cell rating')

ratings=[]
for i in rating:
    ratings.append(i.text.replace('\n',''))
ratings[0:9]

TopAllRounders=pd.DataFrame({})
TopAllRounders['Player']=Names[0:9]
TopAllRounders['Team']=teams[0:9]
TopAllRounders['Ratings']=ratings[0:9]

Banner=pd.DataFrame({'Player':['Marizanne Kapp'],'Team':['SA'],'Ratings':['372']})

Top10AllRounders=pd.concat([Banner,TopAllRounders]).set_index('Player')
Top10AllRounders


# In[16]:


#6. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The scraped data should include Product Name, Price, Image URL and Average Rating.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.amazon.in/s?k=smartphone+under+20000&rh=n%3A976419031%2Cp_36%3A1318506031&dc&qid=1631345642&rnid=1318502031&ref=sr_nr_p_36_4'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

phone=soup.find_all('span',class_='a-size-medium a-color-base a-text-normal')

phones=[]
for i in phone:
    phones.append(i.text.replace('\n',''))
phones[0:15]

pri=soup.find_all('span',class_='a-price-whole')

price=[]
for i in pri:
    price.append(i.text)
price[0:15]

rat=soup.find_all('span',class_='a-icon-alt')

rating=[]
for i in rat:
    rating.append(i.text)
rating[0:15]

img=soup.find_all('img',class_='s-image')

imageurl=[]
for i in img:
    imageurl.append(i.get('src'))
imageurl[0:15]

Phones=pd.DataFrame({})
Phones['Phones']=phones[0:15]
Phones['Price']=price[0:15]
Phones['Rating']=rating[0:15]
Phones['ImageURL']=imageurl[0:15]
Phones


# In[25]:


#7.Write a python program to scrape house details from mentioned url. It should include house title, location, area, emi and price
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N%20DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8%20iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

Name=soup.find_all('h2',class_='heading-6 font-semi-bold nb__1AShY')

Title=[]
for i in Name:
    Title.append(i.text.replace('\n',''))
Title

loc=soup.find_all('div',class_='nb__2CMjv')

Location=[]
for i in loc:
    Location.append(i.text.replace('\n',''))
Location

Emis=soup.find_all('div',class_='font-semi-bold heading-6')

emi=[]
for i in Emis:
    emi.append(i.text.replace('\n',''))
emi[1:30:3]

len(emi[1:30:3])

are=soup.find_all('div',class_='nb__3oNyC')

Area=[]
for i in are:
    Area.append(i.text.replace('\n',''))
Area

pri=soup.find_all('div',class_='font-semi-bold heading-6')

price=[]
for i in pri:
    price.append(i.text.replace('\n',''))
price[2:30:3]

ListofHouses=pd.DataFrame({})
ListofHouses['Title']=Title
ListofHouses['Location']=Location
ListofHouses['Area']=Area
ListofHouses['EMI']=emi[1:30:3]
ListofHouses['Price']=price[2:30:3]
ListofHouses.set_index('Title')


# In[26]:


#8. Write a python program to scrap the dine details from the given URL.
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.dineout.co.in/delhi-restaurants/buffet-special'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

Res=soup.find_all('div',class_='restnt-info cursor')

Name=[]
for i in Res:
    for j in i.find_all('a',class_='restnt-name ellipsis'):
        Name.append(j.text.replace('\n',''))
Name

loc=soup.find_all('div',class_='restnt-loc ellipsis')

Location=[]
for i in loc:
    Location.append(i.text.replace('\n',''))
Location

cui=soup.find_all('span',class_='double-line-ellipsis')

cuisine=[]
for i in cui:
    cuisine.append(i.text.split('|')[1])
cuisine

rate=soup.find_all('div',class_='restnt-main-wrap clearfix')

rating=[]
for i in rate:
        rating.append(i.text.split('4.3232')[0].replace('In high demand',''))
rating

img=soup.find_all('img',class_='no-img')

img_url=[]
for i in img:
        img_url.append(i.get('data-src'))
img_url

info=pd.DataFrame({})

info['Restaurants']=Name
info['Location']=Location
info['Cuisine']=cuisine
info['Rating']=rating
info['ImageUrl']=img_url
info


# In[28]:


#9.Write a python program to scrape weather details for last 24 hours from the given URL
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://en.tutiempo.net/delhi.html?data=last-24-hours'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

hr=soup.find_all('tr')

hour=[]
for i in hr:
    hour.append(i.text.split('Dr')[0].split('Mi')[0])
hour[14:85:2]


wco=soup.find_all('tr')

wcon=[]
for i in wco:
    for j in i.find_all('span'):
        wcon.append(j.text)
wcon[8:44]
        

len(wcon[8:44])

tem=soup.find_all('td',class_='t Temp')

temp=[]
for i in tem:
    temp.append(i.text)
temp[0:36]

len(temp[0:36])

win=soup.find_all('td',class_='wind')

wind=[]
for i in win:
    wind.append(i.text)
wind[0:36]

hu=soup.find_all('td',class_='hr')

hum=[]
for i in hu:
    hum.append(i.text)
hum[0:36]

pre=soup.find_all('td',class_='prob')

pres=[]
for i in pre:
    pres.append(i.text)
pres[0:36]

Weatherforecast=pd.DataFrame({})
Weatherforecast['Hour']=hour[14:85:2]
Weatherforecast['WeatherCond.']=wcon[8:44]
Weatherforecast['Temp.']=temp[0:36]
Weatherforecast['Wind']=wind[0:36]
Weatherforecast['Humid']=hum[0:36]
Weatherforecast['Pressure']=pres[0:36]
Weatherforecast


# In[29]:


#10.Write a python program to scrape monument name, monument description, image url about top 10 monuments
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/'

data=requests.get(link)
data

soup=bs(data.content,'html.parser')

Name=soup.find_all('p')

Names=[]
for i in Name:
    for j in i.find_all('strong'):
        Names.append(j.text)
Names[0:10]

Des=soup.find_all('p')

desc=[]
for i in Des:
    desc.append(i.text)
desc[5:35:3]

Img=soup.find_all('p')

image=[]
for i in Img:
    for j in i.find_all('img'):
        image.append(j.get('src'))
image[1:20:2]

Top10monuments=pd.DataFrame({})

Top10monuments['Name']=Names[0:10]
Top10monuments['Description']=desc[5:35:3]
Top10monuments['ImageUrl']=image[1:20:2]
Top10monuments.set_index('Name')


# In[ ]:




