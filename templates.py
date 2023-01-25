for id_page in settings.COUNT_OF_PAGES_IN_MARKETCSGO:
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:\\Users\\1alex\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = undetected_chromedriver.Chrome(options=options)
    driver.get(settings.BASE_URL_MARKETCSGO.format(id_page))

# на случай если нужно будет постоянно автоматически переключать язык на английский
# pyautogui.moveTo(800, 120, 0.3)
# pyautogui.moveTo(800, 160, 0.3)
# pyautogui.click()
# options.add_argument("accept-lang=en")

#file_list[f'C{c_number}'] = round(price * 1.045, 2)

#file_list[f'E{j}'] = round(price * 0.9025, 4)

#        нужно как-то попытаться сократить этот список
#        if item in ["Capsule", "Case", "Package", "Sticker", "Tag", "Graffiti", "Music", "Sir", "SEAL", "Warfare", "Nationale", "SWAT", "Romanov", "Crew", "Professionals", "FBI", "Sabre", "TACP", "Slingshot", "NZSAS", "Primeiro", "Street", "SAS", "KSK", "Tool", "Enforcer", "Soldier | Phoenix", "Pin", "Pack", "Challengers", "Legends", "Patch", "Pass", "Contenders"]:


def parse_content_from_steam(content):

    soup = BeautifulSoup(content, "lxml")

    skins_info = soup.get("div", "data-hash-name")
    print(skins_info)
    #prices_info = soup.find_all(class_="price")

    excel_file = "list.xlsx"
    file_load = load_workbook(excel_file)
    file_list = file_load['data']

#    for id_page in settings_steam.PAGES_NAME:
#        print(id_page)
#        driver = webdriver.Chrome()
#        driver.get(settings_steam.BASE_URL.format(id_page))
#        content = driver.page_source
#        parse_content_from_steam(content)

# options = undetected_chromedriver.ChromeOptions().add_argument("--user-data-dir=C:\\Users\\1alex\\AppData\\Local\\Google\\Chrome\\User Data\\Default")