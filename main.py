from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import *
import undetected_chromedriver
import time
import pyautogui
import settings


# Функция для парсинга сайта lis-skins.ru
def parse_content_from_lisskins(content, a_number, b_number, c_number):

    # Парсим сайт, получая из него данные о названии скина, его качестве и цене
    soup = BeautifulSoup(content, "lxml")
    skins_info = soup.find_all(class_="name-inner")
    skins_quality = soup.find_all(class_="name-exterior")
    price_info = soup.find_all("div", class_="price")

    # Открываем excel таблицу, куда будем записывать полученные данные
    excel_file = "list.xlsx"
    file_load = load_workbook(excel_file)
    file_list = file_load['data']

    # Заводим переменную, потому что не все скины имеют качество, а нам нужно совместить название скина и его качество
    _number_of_quality = 0

    # Перебираем все данные и записываем их в таблицу excel
    for i in range(len(skins_info)):
        item = skins_info[i].text.strip()
        if "Capsule" in item or "Case" in item or "Package" in item or "Sticker" in item or "Tag" in item or "Graffiti" in item or "Music" in item or "Sir" in item or "SEAL" in item or "Warfare" in item or "Nationale" in item or "SWAT" in item or "Romanov" in item or "Crew" in item or "Professionals" in item or "FBI" in item or "Sabre" in item or "TACP" in item or "Slingshot" in item or "NZSAS" in item or "Primeiro" in item or "Street" in item or "SAS" in item or "KSK" in item or "Tool" in item or "Enforcer" in item or "Soldier | Phoenix" in item or "Pin" in item or "Pack" in item or "Challengers" in item or "Legends" in item or "Patch" in item or "Pass" in item or "Contenders" in item:
            file_list[f'A{a_number}'] = item
            price = price_info[i].text.strip()
            price = float(price.replace(" ", ""))
            file_list[f'B{b_number}'] = price
            a_number += 1
            b_number += 1
            c_number += 1

        else:
            item = skins_info[i].text.strip() + " " + skins_quality[_number_of_quality].text.strip()
            file_list[f'A{a_number}'] = item
            price = price_info[i].text.strip()
            price = float(price.replace(" ", ""))
            file_list[f'B{b_number}'] = price
            _number_of_quality += 1
            a_number += 1
            b_number += 1
            c_number += 1

    # Сохраняем и закрываем таблицу
    file_load.save(excel_file)
    file_load.close()

    # Возвращаем строку таблицы, на которой остановилась запись, чтобы начать со следующей строки
    return a_number


# Функция для парсинга сайта market.csgo.com
def parse_content_from_csmarket(content):

    # Парсим сайт, получая из него данные о названии скина и цене
    soup = BeautifulSoup(content, "lxml")
    skins_info = soup.find_all(class_="name")
    prices_info = soup.find_all(class_="price")

    # Открываем excel таблицу, куда будем записывать полученные данные
    excel_file = "list.xlsx"
    file_load = load_workbook(excel_file)
    file_list = file_load['data']

    # Перебираем данные, если совпадение есть в таблице, то записываем наши данные в таблицу excel
    for i in range(len(skins_info)):
        skin_from_site = skins_info[i].text.strip()
        for j in range(2, table_length):
            if skin_from_site == file_list[f"A{j}"].value:
                price = prices_info[i].text.strip()
                price = float(price.replace(" ", ""))
                price_now = file_list[f"D{j}"].value
                if (price_now is None) or (price < float(price_now)):
                    file_list[f'D{j}'] = price

    # Сохраняем и закрываем таблицу
    file_load.save(excel_file)
    file_load.close()


if __name__ == '__main__':

    # Задаем начальные строки таблицы, с которых будем записывать данные
    table_length = 2
    a_number = 2
    b_number = 2
    c_number = 2

    # Задаем кол-во страниц на сайте, парсим каждую страницу
    for id_page in settings.COUNT_OF_PAGES_IN_LISSKINS:
        driver = webdriver.Chrome()
        driver.get(settings.BASE_URL_LISSKINS.format(id_page))
        content = driver.page_source
        table_length = parse_content_from_lisskins(content, a_number, b_number, c_number)
        a_number, b_number, c_number = table_length+1, table_length+1, table_length+1

    # Задаем кол-во страниц на сайте, парсим каждую страницу
    for id_page in settings.COUNT_OF_PAGES_IN_MARKETCSGO:
        driver = undetected_chromedriver.Chrome()
        driver.get(settings.BASE_URL_MARKETCSGO.format(id_page))
        # Тайм слипы нужны потому что на сайте стоит проверка на бота, а чтобы она прошла требуется некотрое время,
        # обычно это 5 секунд.
        time.sleep(5)
        # Движение мыши нужно для того чтобы переключить язык сайта на английский, так как на первом сайте
        # название скинов на английском. Если просто попробовать зайти на английскую версию сайта, то там
        # цена будет в долларах, а нам нужна в рублях.
        pyautogui.moveTo(800, 120, 0.3)
        pyautogui.moveTo(800, 160, 0.2)
        pyautogui.click()
        time.sleep(0.2)
        content = driver.page_source
        driver.close()
        parse_content_from_csmarket(content)
