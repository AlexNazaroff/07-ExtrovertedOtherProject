ffPath =="C:\Users\admin.admin2\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe"
os.environ["webdriver.firefox.driver"] = ffPath

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)