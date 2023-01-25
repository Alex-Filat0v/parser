import time
import timeit
import random
import undetected_chromedriver
from openpyxl import load_workbook
'''
cycles = int(input("Сколько раз тестим?: "))
sr = 0
for j in range(cycles):
    pages_count = 179 #int(input("Сколько страниц на сайте marketcsgo?: "))
    time = 0
    for i in range(1, pages_count + 1):
        time += random.randint(0, 2) * 0.73
    print(f"В этот раз ({j + 1} цикл) суммарно мы потеряли: {time} секунд")
    if time == 0:
        print("Ахуеть как вообще такое возможно ?!?!?!?")
        break
    sr += time
print(f"Среднее время потерь: {sr/cycles}")


pages_count = 179 #int(input("Сколько страниц на сайте marketcsgo?: "))
timer = 1
time = 0
for i in range(1, pages_count + 1):
    time += (5.37 - 0.03 * timer)
    timer += 1
print(time)


#445.531
#477.92999999999995
options = undetected_chromedriver.ChromeOptions().add_argument("--user-data-dir=C:\\Users\\1alex\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = undetected_chromedriver.Chrome(options=options)
driver.get('https://nowsecure.nl')
time.sleep(20)
'''


code = """
import time
import random
cycles = 10000 #int(input("Сколько раз тестим?: "))
sr = 0
for j in range(cycles):
    pages_count = 179 #int(input("Сколько страниц на сайте marketcsgo?: "))
    time = 0
    for i in range(1, pages_count + 1):
        time += random.randint(0, 2) * 0.73
    print(f"В этот раз ({j + 1} цикл) суммарно мы потеряли: {time} секунд")
    if time == 0:
        print("Ахуеть как вообще такое возможно ?!?!?!?")
        break
    sr += time
print(f"Среднее время потерь: {sr/cycles}")
"""
ex = timeit.timeit(code, number=1)

print(ex)

