#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
from urllib.parse import urlparse, urlsplit
from bs4 import BeautifulSoup
from lxml import html
import re

import pandas as pd


# In[39]:


def get_page(url: str) -> str:
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        "Host": "vk.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        # "Cookie": "remixlang=3; remixstid=25589131_940b885dd48d674edb; remixlhk=0503354f21dd3f5835; remixflash=0.0.0; remixscreen_depth=24; remixscreen_orient=1; remixgp=713b46362f9a99290800916311d50259; remixdt=0; tmr_reqNum=6; tmr_lvid=1a7e92e1551969ad583b54cdfd8afd6b; tmr_lvidTS=1581605399827; tmr_detect=0%7C1581618248327; remixsts=%7B%22data%22%3A%5B%5B1581619443%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619441862%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619455%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619453866%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619467%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619465869%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619479%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619477871%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619491%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619489874%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619503%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619501876%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619515%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619513879%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619527%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619525882%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619539%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619537885%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619551%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619549888%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619563%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619561891%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619575%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619573893%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619587%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9001%2C%22last%22%3A1581619585895%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619599%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619597896%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619611%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9000%2C%22last%22%3A1581619609897%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619623%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9001%2C%22last%22%3A1581619621898%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619635%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619633901%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619647%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619645904%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619659%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619657907%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619671%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619669909%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619683%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9001%2C%22last%22%3A1581619681911%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619695%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9001%2C%22last%22%3A1581619693912%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619707%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619705915%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619719%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619717917%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619731%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619729919%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619743%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619741923%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619755%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9003%2C%22last%22%3A1581619753926%2C%22options%22%3A%7B%7D%7D%7D%5D%2C%5B1581619767%2C%22time_spent%22%2C%7B%22profile%22%3A%7B%22full%22%3A9002%2C%22last%22%3A1581619765928%2C%22options%22%3A%7B%7D%7D%7D%5D%5D%2C%22uniqueId%22%3A730444401%7D",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }
    r = requests.get(url, headers=headers)
    return r.text


def save_page(url: str, folder: str):
    content = get_page(url)    
    uid = urlparse(url).path.aplit("/")[-1]
    with open(f"{folder}/{uid}.html", w) as f:
        f.write(content)
        
def get_birthyear(content: str) -> int:
    soup = BeautifulSoup(content)
    f_tags = soup.find_all('a')
    birthyear = ""
    for tag in f_tags:
        if re.search(r'byear', str(tag)):
            birthyear = int(tag.contents[-1].split(" ")[0])
            break
    return birthyear

def get_followers_num(content: str) -> int:
    soup = BeautifulSoup(content)
    f_tags = soup.find_all('div', {'class': 'count'})
    if len(f_tags) == 3:
        return int(f_tags[0].contents)
    else:
        raise Exception("Wrong number of counts fielss")
        
def scrapdata(content: str) -> (int, int):
    return get_birthyear(content), get_followers_num(content)

