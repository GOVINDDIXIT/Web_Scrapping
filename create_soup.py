from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\webDriver\phantomjs\bin\phantomjs.exe' )

driver.get("https://python.org")

html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')

print soup.prettify()

driver.quit()