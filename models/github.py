from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

class Github:

    def __init__(self, driver, login, password):
        self.driver = driver
        self.login = login
        self.password = password
        self.__url = "https://github.com/login"
    
    def connect(self):
        self.__navegate()
        self.__make_login()
    
    def repositories_url(self):
        url = BeautifulSoup(self.html_page(), features="html.parser")
        url = url.find(attrs={'class':'Header-item position-relative mr-0 d-none d-lg-flex'}).details
        url = url.find(attrs={'class':'dropdown-menu dropdown-menu-sw mt-2'})
        return "https://github.com" + url.find_all('a')[2]['href']
    
    def html_page(self):
        return self.driver.page_source
        
    def __navegate(self):
        self.driver.get(self.__url)

    def __make_login(self):
        self.driver.find_element_by_id("login_field").send_keys(self.login)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_name("commit").click()