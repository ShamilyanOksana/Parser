import requests
from bs4 import BeautifulSoup


class Phone:

    pass


def get_html(url):
    url = "https://www.avito.ru/taganrog/telefony/samsung?q=sumsung&p=1"
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')

    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def print_information(all_info):
    all_info.sort(key=lambda phone: phone.price)
    for info in all_info:
        print(info.title)
        print(info.url)
        print(info.price)
        print(info.currency)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='description')
    count = 0
    for ad in ads:
        all_info.append(Phone())
        all_info[count].title = get_title(ad)
        all_info[count].url = get_link(ad)
        pre_price = get_price(ad)
        all_info[count].price = pre_price[0]
        all_info[count].currency = pre_price[1]
        count+=1
    return all_info


def get_title(current_ads):
    try:
        title = current_ads.find('a', class_='item-description-title-link').get('title')
        return title
    except Exception:
        pass


def get_link(current_ads):
    try:
        link = "https://www.avito.ru" + current_ads.find('a', class_='item-description-title-link').get('href')
        return link
    except Exception:
        pass


def get_price(current_ads):

    try:
        price = current_ads.find('div', class_='about').text.split(' ')[2:]
        if price[0].isdigit() and price[1].isdigit():
            currency = price[2]
            price = int(price[0])*1000 + int(price[1])

        else:
            currency = price[1]
            price = int(price[0])
        return [price, currency]
    except Exception:
        pass


def main():
    url = "https://www.avito.ru/taganrog/telefony/samsung?q=sumsung&p=1"
    base_url = "https://www.avito.ru/taganrog/telefony/samsung?"
    page_part = "p="
    query_part = "&q=sumsung"

    html = get_html(url)
    total_pages = get_total_pages(html)

    # for i in range(1, total_pages+1):
    for i in range(1, 2):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        all_info = get_page_data(html)
        print_information(all_info)

all_info = []

if __name__ == "__main__":
    main()
