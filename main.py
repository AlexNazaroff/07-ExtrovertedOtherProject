ffPath =="C:\Users\admin.admin2\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe"
os.environ["webdriver.firefox.driver"] = ffPath
driver = webdriver.Firefox(executable_path=ffPath)
driver.get(url)