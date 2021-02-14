# c) Assert form validation functionality Post entering a dummy username and password on
# http://the-internet.herokuapp.com/login

from selenium import webdriver

class InvalidUserPwd():

    def test(self):
        BaseURL = "http://the-internet.herokuapp.com/login"
        driver= webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").send_keys("abcdkjh")
        driver.find_element_by_id("password").send_keys("oksdfsdf")
        driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']").click()
        element = driver.find_element_by_xpath("// div[@class ='flash error']")
        assert element.text == " Your username is invalid!"

IU = InvalidUserPwd()
IU.test()