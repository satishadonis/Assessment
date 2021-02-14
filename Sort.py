# Write a test to sort the table by the amount due on page http://the-internet.herokuapp.com/tables

from selenium import webdriver
import time

class SortDue():

    def test(self):
        BaseURL = "http://the-internet.herokuapp.com/tables"
        driver = webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(5)
        element_not_sorted = driver.find_elements_by_xpath("//table[@id='table1']//tr/td[4]")

        l= []
        for ele in element_not_sorted:
            l.append(ele.text)

        print("Before clicking on Sort: ", l)

        driver.find_element_by_xpath("//table[@id='table1']//th[4]").click()
        element = driver.find_elements_by_xpath("//table[@id='table1']//tr/td[4]")
        l1= []

        for elem in element:
            l1.append(elem.text)
        print("After clicking on sort", l1)






SD = SortDue()
SD.test()