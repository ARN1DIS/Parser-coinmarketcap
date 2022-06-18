import requests
from bs4 import BeautifulSoup as BS

url = 'https://coinmarketcap.com'
cripta_list = []
up_or_down = None
def parse(url):
    global up_or_down
    responce = requests.get(url)
    soup = BS(responce.content, 'html.parser')
    cripta_block = soup.find_all('tr')
    if cripta_block != []:
        cripta_list.extend(cripta_block)
    
    count = len(cripta_list) - 1
    count_2 = 1
    while count_2 <= count:
        try:
            data = cripta_list[count_2]
            #name of cryptocurrency
            name = data.find('p', {'class':"sc-1eb5slv-0 iworPT"}).text
            #price of cryptocurrency
            all_cmc_link = data.find_all('a', {'class':'cmc-link'})
            price_long = all_cmc_link[1]
            price = price_long.find('span').text
            #up/down per 24 hours in percent
            value = data.find('span', {'class':"sc-15yy2pl-0 hzgCfk"}).text
            #mark up or down
            check = data.find('span', {'class':"icon-Caret-up"})
            if(check != None):
                up_or_down = "+"
            else:
                up_or_down = "-"
            print(f"{name} цена: {price} возросла/упала = {up_or_down}{value}")
            count_2 += 1
        except:
            data = cripta_list[count_2]
            name = data.find('a', {'class':"cmc-link"}).text 
            all_span = data.find_all('span')
            price = all_span[5].text
            print(f"{name} цена: {price}")
            count_2 += 1
    

            

parse(url)


