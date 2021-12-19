import threading

import requests
from bs4 import BeautifulSoup
from lxml import html
import time
from url import url
from api import add_product, clear_database

def pars(Url):
    # print(f"ссылка на станицу каталога {Url}")
    try:  # получаю пагинацию этой станицы
        p = requests.get(Url)
        pagenation = html.fromstring(p.text)
        pagen = pagenation.xpath("//div[@class='module-pagination']/span/a[@href]")
        pag = pagen[len(pagen)-1].attrib['href'].split('=')[1]
    except: pag = 1
    # print(f"страниц в разделе {pag}")

    for i in range(int(pag)):  # Парс страниц согластно пагинации
        p = requests.get(Url, params=f"PAGEN_1={i+1}")
        # print(f"{Url}?PAGEN_1={i+1}")
        table = html.fromstring(p.text)
        tbody = table.xpath("//td[@class='title-tbl-sect']/a/text()")

        # проверка на наличие
        a = BeautifulSoup(p.text, 'html.parser')
        class_quant = a.find_all('ul', class_='quant')
        for j in range(len(tbody)):
            try:
                availability = class_quant[j].contents[1].attrs['class'][0]  # проверка на наличие
                title = tbody[j].split('\u2003')[0]
                price = table.xpath("//a[@class='price_el']/@data-price")[j].split(' / ')[0]
                price_unit = table.xpath("//a[@class='price_el']/@data-price")[j].split(' / ')[1]
                # add_product(title, price, price_unit)
                print(f"{title} | {price} | {price_unit}")
            except: pass  # Нет в наличии ничего не делаю

if __name__ == '__main__':
    start = time.monotonic()
    #clear_database()
    # print(f"сколько строк в url {len(url)}")
    thr_list = []
    for i in range(len(url)):
        thr = threading.Thread(target=pars, args=(url[i],))  # создал поток
        thr_list.append(thr)
        thr.start()

    for i in thr_list:
        i.join()
    end = time.monotonic()
    result_time = end - start
    # r_t = time.strftime("%H:%M:%S", time.gmtime(result_time))
    print(f"Время работы: {result_time}")
    # input('Нажмите Enter для выхода\n')

