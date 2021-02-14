# Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page '
# http://the-internet.herokuapp.com/notification_message_rendered

from selenium import webdriver

class EnterAlphabets():

    def test(self):
        BaseURL = "http://the-internet.herokuapp.com/notification_message_rendered"
        driver = webdriver.Chrome(executable_path='C:\Personal\Interview\Automation\Drivers\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(5)
        loop = driver.find_element_by_link_text("Click here")
        message = driver.find_element_by_xpath("//div[@id='flash']").text

        for i in message == "Action successful":
            if i == message

