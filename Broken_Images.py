# a) Assert Broken images http://the-internet.herokuapp.com/broken_images

from selenium import webdriver
import requests

driver= webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/broken_images")
links=[]
links= driver.find_elements_by_css_selector("img")

for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

    if(requests.head(link.get_attribute('href')).status_code==200):
        print("Valid link")
    else:
        print("Invalid link")