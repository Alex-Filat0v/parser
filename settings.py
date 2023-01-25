BASE_URL_MARKETCSGO = 'https://market.csgo.com/?t=all&p={}&sd=desc'

pages_count = int(input("Сколько страниц на сайте marketcsgo?: "))

COUNT_OF_PAGES_IN_MARKETCSGO = [0] * pages_count

for i in range(0, pages_count):
    COUNT_OF_PAGES_IN_MARKETCSGO[i] = i + 1


BASE_URL_LISSKINS = 'https://lis-skins.ru/market/csgo/?page={}'

pages_count = int(input("Сколько страниц на сайте lis-skins?: "))

COUNT_OF_PAGES_IN_LISSKINS = [0] * pages_count

for i in range(0, pages_count):
    COUNT_OF_PAGES_IN_LISSKINS[i] = i + 1