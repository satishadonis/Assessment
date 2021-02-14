# b) Assert forgot password success message on the page http://the-internet.herokuapp.com/forgot_password

from selenium import webdriver


class ForgotPassword():

    def test(self):
        BaseURL = "http://the-internet.herokuapp.com/forgot_password"
        driver= webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Enter the Email in text field

        driver.find_element_by_id("email").send_keys("sa.g.com")
        driver.find_element_by_id("form_submit").click()
        driver.implicitly_wait(5)
        element = driver.find_element_by_xpath("//div[@id='content']")
        assert element.text == "Your e-mail's been sent!"
        # print(driver.find_element_by_xpath("//div[@id='content']").text)



fp = ForgotPassword()
fp.test()