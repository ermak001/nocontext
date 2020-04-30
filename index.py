from bs4 import BeautifulSoup
import urllib.request
import os

def get_html(url):                                                       # Открываем
    response = urllib.request.urlopen(url)                               # код
    return(response.read())                                              # страницы

def parse(html):
    soup = BeautifulSoup(html, 'lxml')                                  # открываем html в супе
    table = soup.find_all('div',{'class':'AdaptiveMedia-singlePhoto'})  # сортировка по диву и классу
    for i in table:
        x = i.find('img')['src']
        urllib.request.urlretrieve(x, r'memes_pars\о' + x[-8:])
        print('save')
def main():
    parse(get_html('https://twitter.com/neighbours_wifi'))               # Запуск программы

if __name__ == '__main__':
    main()
