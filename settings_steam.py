BASE_URL = 'https://steamcommunity.com/market/search?appid=730#p{}_popular_desc'

pages_count = int(input("Сколько страниц на сайте steam?: "))

PAGES_NAME = [0] * pages_count

for i in range(0, pages_count):
    PAGES_NAME[i] = i + 1
