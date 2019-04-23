# 1. Получить количество учеников с сайта geekbrains.ru:

import re
import urllib.request
from bs4 import BeautifulSoup as Bs

html = urllib.request.urlopen('https://geekbrains.ru/').read().decode("utf-8")

# a) при помощи регулярных выражений,
total_user = re.findall('<span class="total-users\">Нас уже ([\d\s]+) человек</span>', html)
print(int(total_user.pop().replace(' ', '')))

# b) при помощи библиотеки BeautifulSoup.

s = Bs(html, 'html.parser')
bs_total_user=s.find('span',{'class':'total-users'}).text
print(int(re.sub('\D*', '', bs_total_user)))
