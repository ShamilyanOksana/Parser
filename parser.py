import requests
from bs4 import BeautifulSoup



def get_html():
    url = "https://www.avito.ru/taganrog/telefony/samsung?q=sumsung&p=1"
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')

    total_pages = pages.split('=')[1].split('&')[0]








def main():
    # https: // www.avito.ru / taganrog / telefony / samsung?q = sumsung & p = 1

if __name__ == "__mail__":
    main()




