import requests
from bs4 import BeautifulSoup


def get_html(url):
    url = "https://www.avito.ru/taganrog/telefony/samsung?q=sumsung&p=1"
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')

    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def main():
    url = "https://www.avito.ru/taganrog/telefony/samsung?q=sumsung&p=1"
    base_url = "https://www.avito.ru/taganrog/telefony/samsung?"
    page_part = "p="
    query_part = "&q=sumsung"

    html = get_html(url)
    total_pages = get_total_pages(html)

    for i in range(1, total_pages+1):
        url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)


if __name__ == "__main__":
    main()




