import requests

def add_product(name, price, price_unit):
    response = requests.post(
        'https://prod.pkf-m.ru/parser-api/v1/parser/alros/products/',  # suppliers/
        headers={
            'accept': '*/*',
            'apikey': 'JINSkT6s2CxCVSqkGuUHZMnmwP6tq7',
            'Content-Type': 'application/json'
                 },
        json=[{
            "name": name,
            "price": price,
            "price_unit": price_unit,
            "supplier_id": 772
        }]
    )
    if response.status_code == 200:
        print("Записано в базу")

def clear_database():
    response = requests.delete(
        'https://prod.pkf-m.ru/parser-api/v1/parser/alros/products/',
        headers={
            'accept': '*/*',
            'apikey': 'JINSkT6s2CxCVSqkGuUHZMnmwP6tq7'
        }
    )
    print(response.text)
    print(response)


if __name__ == '__main__':
    name = "test_name_2"
    price = "test_price_2"
    price_unit = "test_price_unit_2"

    add_product(name, price, price_unit)
    # clear_database()
    # headers = {
    #     'accept': '*/*',
    #     'apikey': 'JINSkT6s2CxCVSqkGuUHZMnmwP6tq7',
    #     'Content-Type': 'application/json'
    # }
    # add_product = [{
    #     "name": "test_name",
    #     "price": "test_price",
    #     "price_unit": "test_price_unit",
    #     "supplier_id": 772
    # }]
    #
    # add_products_post = requests.post(
    #     'https://prod.pkf-m.ru/parser-api/v1/parser/alros/products/',
    #     headers=headers,
    #     json=add_product
    # )
    # # addProduct(name, price, price_unit)
    # print(add_products_post.text)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
