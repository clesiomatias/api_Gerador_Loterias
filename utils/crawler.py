# -*- coding: utf-8 -*-
import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup


def Crawler(tipo):
    ssl._create_default_https_context = ssl._create_unverified_context #Parando de conferir os certificados SSL

    html=urlopen(f'https://www.sorteonline.com.br/{tipo}/resultados')
    bs = BeautifulSoup(html, 'html.parser')

    resultados= bs.find_all('div',{'class':'result-default'})
    linhas=[]
    for i in resultados:
        if i.findChildren('ul',{'class':''}):           
            linhas.append(i.find_all('li',{'class':'bg'}))    
            linhas.append(i.find_all('div',{'class':'time-coracao'}))    
    r=[]
    for j in linhas:
        for n in j:
            for h in n:
                if str(h) not in '<i class="lnr lnr-heart color"></i>'and str(h)not in '<span class="lnr lnr-calendar-full color"></span>':
                    r.append(str(h))    
        

    return r


