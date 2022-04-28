#!/usr/bin/env python
# coding: utf-8

# # Question 1 https://www.wikipedia.org/

# In[1]:


get_ipython().system('pip install bs4')

get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://www.wikipedia.org/')
page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[5]:


header_1=soup.find('div',class_="central-textlogo")
header_1.text


# # Question 2 and 3 IMDB'S

# In[6]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies')


# In[7]:


page


# In[8]:


soup = BeautifulSoup(page.content)
soup


# In[9]:


titles=[]

for i in soup.find_all('td',class_="titleColumn"):
    titles.append(i.text)
    
    
titles


# In[10]:


rating=[]

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text)
    
rating


# In[11]:


year=[]
for i  in soup.find_all('span',class_="secondaryInfo"):
        year.append(i.text)
year             


# In[12]:


print(len(titles),len(rating),len(year))


# In[13]:


#data frame

import pandas as pd
df= pd.DataFrame({'Titles':titles,'Rating':rating,'Year':year})
df


# In[14]:


print(df.iloc[0:100])


# # Question 4 https://meesho.com/bags-ladies/pl/p7vbp

# In[15]:


page = requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
page


# In[16]:


soup = BeautifulSoup(page.content)
soup               


# In[17]:


name=[]

for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    name.append(i.text)
name


# In[18]:


price=[]

for i in soup.find_all('h5',class_='Text__StyledText-sc-oo0kvp-0 hiHdyy'):
    price.append(i.text)

price 


# In[19]:


discount=[]
for i in soup.find_all('span',class_="Text__StyledText-sc-oo0kvp-0 lnonyH"):
    discount.append(i.text)

discount    

    


# In[20]:


print(len(name),len(price),len(discount))


# In[21]:


import pandas as pd
df=pd.DataFrame({'Name':name,'Price':price,'Discount':discount})
df


# # Question 5 https://www.icc-cricket.com/rankings/mens/team-rankings/

# In[22]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[23]:


soup = BeautifulSoup(page.content)
soup


# In[24]:


name=[]
for i in soup.find_all('span',class_="u-hide-phablet"):
    name.append(i.text)
name    


# In[25]:


matches=[]
for i in soup.find_all('tr',class_="table-body"):
    matches.append(i.text.split()[3:4])
matches    


# In[26]:


print(len(name),len(matches))


# In[ ]:





# In[27]:


match=soup.find('td',class_="table-body__cell u-center-text")
match.text


# In[ ]:





# In[28]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[29]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Question 7 (https://coreyms.com/)

# In[30]:


page=requests.get('https://coreyms.com/')
page


# In[31]:


soup=BeautifulSoup(page.content)
soup


# In[32]:


heading = []
for i in soup.find_all('h2',class_="entry-title"):
    heading.append(i.text)
heading    


# In[33]:


date=[]
for i in soup.find_all('time',class_="entry-time"):
    date.append(i.text)
date


# In[34]:


content=[]
for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text)
content    


# In[35]:


url=[]
for i in soup.find_all('div',class_="ytp-cued-thumbnail-overlay-image"):
    url.append(i.text)
url    


# In[36]:


print(len(heading),len(date),len(content))


# In[37]:


import pandas as pd
df=pd.DataFrame({'Heading':heading,'Date':date,'Content':content})
df


# # question 8 https://www.nobroker.in/property/sale/hyderabad/Indira%20Nagar?searchParam=W3sibGF0IjoxNy40NDc0NDc1LCJsb24iOjc4LjM1NjkyNzUsInBsYWNlSWQiOiJDaElKZzVwcF9KU1R5enNSaHBYNzU2M2VkX2ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=&radius=2.0&city=hyderabad&locality=Indira%20Nagar

# In[38]:


page =requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,&locality=Jayanagar,&locality=Rajajinagar')
page


# In[39]:


soup=BeautifulSoup(page.content)
soup


# In[40]:


title=[]
for i in soup.find_all('span',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"):
    title.append(i.text)
title    


# In[41]:


location=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"):
    location.append(i.text)
location    


# In[42]:


price=[]
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0"):
    price.append(i.text)
price


# In[43]:


print(len(title),len(location),len(price))


# In[44]:


import pandas as pd
df=pd.DataFrame({'Title':title,'Location':location,'Price':price})
df


# # Quetsion 9 https://www.dineout.co.in/delhi-restaurants/welcome-back

# In[45]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page


# In[46]:


soup=BeautifulSoup(page.content)
soup


# In[47]:


names=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    names.append(i.text)
names   


# In[48]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location    


# In[49]:


rating=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating    


# In[50]:


image=[]
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
image    


# In[51]:


cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
cuisine    


# In[52]:


print(len(names),len(location),len(rating),len(image),len(cuisine))


# In[53]:


import pandas as pd
df=pd.DataFrame({'Names':names,'Location':location,'Rating':rating,'Image':image,'Cuisine':cuisine})
df


# # question 10 https://www.bewakoof.com/women-printed-t-shirts

# In[54]:


page=requests.get('https://www.bewakoof.com/women-plain-t-shirts')
page


# In[55]:


soup=BeautifulSoup(page.content)
soup


# In[56]:


name=[]
for i in soup.find_all('div',class_="productCardBox"):
    name.append(i.text.split()[0:5])
name


# In[57]:


price=[]
for i in soup.find_all('span',class_="discountedPriceText"):    
    price.append(i.text)
price    


# In[58]:


image=[]
for i in soup.find_all('div',style="width: 100%; padding-top: 125%; position: relative; background: rgb(248, 248, 249);"):
    image.append(i.text)
image    


# In[59]:


print(len(name),len(price))
      


# In[60]:


import pandas as pd
df=pd.DataFrame({'Name':name,'Price':price})
df


# In[61]:


print(df.iloc[0:10])

