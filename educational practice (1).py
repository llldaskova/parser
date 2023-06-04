#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
from os import system


# In[2]:


url="https://coinmarketcap.com"  
service=Service('.\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
try:
    driver.get(url)
except Exception as e:
    print('Страница не найдена!')
    exit()
main_page = driver.page_source
soup=BeautifulSoup(main_page,"lxml")
soup=soup.find('ul',class_="pagination").find('li',class_="next").find_previous()
driver.close()
driver.quit()
soup=soup.text
count=int(soup)


# In[3]:


base=[]
d_type=[('Name','U20'),('Prise','U20'),('Market Cup','U20')]
count=1
for j in range(count):
    try:
        url_base="https://coinmarketcap.com/?page="+str(j+1)  
        service_base=Service('.\\chromedriver.exe')
        driver_base = webdriver.Chrome(service=service_base)
        driver_base.get(url_base)
        for n in range(1000,8001,1000):
            script="window.scrollTo"
            script=script+'('+str(n)+','+str(n+1000)+')'
            time.sleep(1)
            driver_base.execute_script(script)
        main_page = driver_base.page_source
    except Exception as e:
        print('Страница не найдена!')
        print(url_base)
        print(e)
        continue 
    soup_base=BeautifulSoup(main_page,"lxml")
    driver_base.close()
    driver_base.quit()
    table=soup_base.find('tbody').find_all('tr')
    print(table)
    for i in table:
        try:
            name=i.find('p',class_="sc-4984dd93-0 kKpPOn").text
        except Exception as e:
            name=' '
        try:
            prise=i.find("div",class_="sc-cadad039-0 clgqXO").text
        except Exception as e:
            prise=' '
        try:
            marketCup=i.find("span", class_="sc-edc9a476-1 gqomIJ").text
        except Exception as e:
            marketCup=' '
        base.append((name,prise,marketCup))


# In[4]:


base_res=np.array(base, dtype = d_type)
base_res=np.sort(base_res, order = 'Name')


# In[5]:


def b_found(value):
    mid = len(base_res) // 2
    low = 0
    high = len(base_res) - 1
 
    while base_res[mid][0] != value and low <= high:
        if value > base_res[mid][0]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
 
    if low > high:
        print("No value")
    else:
        for n in range(3):
            print(("%s: %s")%(d_type[n][0],base_res[mid][n]))


# In[ ]:


while 1:
    print("1-показать базу")
    print("2-поиск по базе")
    print("3-выход")
    a=int(input())
    if a==1:
        print(base_res)
    elif a==2:
        value=input()
        b_found(value)
    elif a==3:
        break
    else:
        system("cls")
        continue 
    system("cls")


# In[ ]:




