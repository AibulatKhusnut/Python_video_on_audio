import requests
from bs4 import BeautifulSoup

def parse_ss():
    response = requests.get('https://www.binance.com/ru/price/top-gaining-crypto')
    soup = BeautifulSoup(response.content,'html.parser')
    data = soup.find('a',{'href': '/ru/price/felix-token/'}).text
    return data


if __name__ != '__main__':
    pass
else:
    print('Dogecoint rate:', parse_ssr())