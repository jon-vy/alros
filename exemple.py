def start():
    urls = [{'url': 'https://www.russteels.ru/catalog/truby_svarnye_kruglye/', 'pages': 53},
            {'url': 'https://www.russteels.ru/catalog/truby_besshovnye/', 'pages': 51},
            {'url': 'https://www.russteels.ru/catalog/truboprovodnaya_armatura_nerzhaveyushchaya/', 'pages': 31},
            {'url': 'https://www.russteels.ru/catalog/sortovoy_prokat_nerzhaveyushchiy/', 'pages': 8},
            {'url': 'https://www.russteels.ru/catalog/listovoy_prokat_nerzhaveyushchiy/', 'pages': 4},
            {'url': 'https://www.russteels.ru/catalog/armatura_pishchevaya_nerzhaveyushchaya/', 'pages': 44},
            {'url': 'https://www.russteels.ru/catalog/komplektuyushchie_dlya_ograzhdeniy/', 'pages': 8},
            {'url': 'https://www.russteels.ru/catalog/svarochnye_materialy/', 'pages': 1}]
    for url in urls:
        p1 = Thread(target=get_pages, args=[url, ])
        p1.start()
    for _ in urls:
        p1.join()


if name == 'main':
    headers_auth = {
        'apikey': 'mLaAl2gbUeTPYMAoSn0LjI3n8RVz3D'
    }
    r = requests.delete('https://prod.pkf-m.ru/parser-api/v1/parser/specsteel/products/', headers=headers_auth)
    print(f'Delete last products: {r.text}')
    links = []
    asession = AsyncHTMLSession()
    print(f'{str(datetime.datetime.now())}: Getting page links!')
    start()
    print(f'{str(datetime.datetime.now())}: Links ready!')
    print(f'{str(datetime.datetime.now())}: Getting parse pages!')
    products = []
    start_parse_page(links)
    print(f'{str(datetime.datetime.now())}: Pages parsed!')
    # print(products)
    add_supplier_payload = {'name': 'Специальные Стали и Сплавы',
                            'city': 'Москва',
                            'contacts': 'Косарев Артём 7(495) 775-55-22 доб. 304, 7(925) 611-46-18 KosarevA@russteels.ru',
                            'address': 'Щелково',
                            'notes': '',
                            'raiting': 0}
    add = requests.post('https://prod.pkf-m.ru/parser-api/v1/parser/specsteel/supplier/', headers=headers_auth,
                        json=add_supplier_payload)
    print(f'Check supplier: {add.text}')
    supplier_id = json.loads(add.text)['supplier']['id']
    print(len(products))
    while products:
        add_products = []
        len(products)
        for product in products[0:5000]:
            # products.remove(product)
            add_products.append({
                "name": product['name'],
                "price": str(product['price']).replace('руб. / м', ''),
                "price_unit": product['price_unit'],
                "supplier_id": supplier_id
            })
            products.remove(product)
            print(len(products))
        add_products_post = requests.post('https://prod.pkf-m.ru/parser-api/v1/parser/specsteel/products/',
                                          headers=headers_auth, json=add_products)
        print(print(f'Products add: {add_products_post.text}'))