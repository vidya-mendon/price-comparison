import simplejson

if __name__ == '__main__':
    price_data = None
    price = []
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = simplejson.loads(price_data)

for d in json_price_data:
            price.append({'name': d['name'], 'price': float(d['amazon_price']), 'url': d['amazon_url']})
            price.append({'name': d['name'], 'price': float(d['walmart_price']), 'url': d['walmart_url']})
            price.append({'name': d['name'], 'price': float(d['ebay_price']), 'url': d['ebay_url']})

            minPricedItem = min(price, key=lambda x: x['price'])
            print(price_data)
            print('=================')
            price = []

