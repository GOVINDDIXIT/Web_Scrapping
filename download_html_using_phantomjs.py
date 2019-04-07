from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\webDriver\phantomjs\bin\phantomjs.exe' )

driver.get('http://python.org')

html_doc = driver.page_source

print html_doc