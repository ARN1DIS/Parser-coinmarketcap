import requests
from bs4 import BeautifulSoup as BS

url = 'https://coinmarketcap.com'
cripta_list = []

def parse(url):
    responce = requests.get(url)
    soup = BS(responce.content, 'html.parser')
    cripta = soup.find_all('tr')
    if cripta != []:
        cripta_list.extend(cripta)
    
    count = len(cripta_list) - 1
    count_2 = 1
    while count_2 <= count:
        try:
            data = cripta_list[count_2]
            name = data.find('p', {'class':"sc-1eb5slv-0 iworPT"}).text
            all_cmc_link = data.find_all('a', {'class':'cmc-link'})
            price_long = all_cmc_link[1]
            price = price_long.find('span').text
            print(f"{name} цена: {price}")
            count_2 += 1
        except:
            data = cripta_list[count_2]
            name = data.find('a', {'class':"cmc-link"}).text 
            all_span = data.find_all('span')
            price_long = all_span[5].text
            print(f"{name} цена: {price_long}")
            count_2 += 1
    

            

parse(url)


