# Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page
# http://the-internet.herokuapp.com/inputs

from selenium import webdriver


class Enter_Alphabets():

    def test(self):
        BaseURL = "http://the-internet.herokuapp.com/inputs"
        driver = webdriver.Chrome(
            executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        try:
            driver.find_element_by_xpath("//input[@type='number']").send_keys("sasd")
        except:
            print("Cannot enter alphabets")


EA = Enter_Alphabets()
EA.test()
