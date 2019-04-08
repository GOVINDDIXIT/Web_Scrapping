from bs4 import BeautifulSoup


soup = BeautifulSoup(open('sample_table.html'), 'lxml')

# Print soup.prettify()

for tr in soup.find_all('tr'):
	for td in tr.find_all('td'):
		print td.text

		