from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\webDriver\phantomjs\bin\phantomjs.exe' )

driver.get('https://stats.nba.com/players/')

html_doc = driver.page_source

soup =BeautifulSoup(html_doc, 'lxml')

# t = soup.find('div', {'id':'players_traditional'})

# for s in t.find('div', class_='category-body'):
# 	# print(s)
# 	print('\n\n')
# 	print(s.find('tr'))
# 	print('\n\n')
# 	# for tr in s.find_all('tr'):
# 	# 	for td in tr.find('td',class_='category-table__text'):
# 	# 		print td.text 

t = soup.find_all('td', 'category-table__text')
for td in t:
	print(td.text)