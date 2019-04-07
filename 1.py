from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\Users\govin\OneDrive\Desktop\web_scrappping\chromedriver.exe' )

driver.get('http://python.org')

html_doc = driver.page_source

print html_doc