from selenium import webdriver

import requests

class Github:

    def __init__(self, driver, login, password):
        self.driver = driver
        self.login = login
        self.password = password
        self.__url = "https://github.com/login"
    
    def connect(self):
        self.__navegate()
        self.__make_login()
        
    def __navegate(self):
        self.driver.get(self.__url)

    def __make_login(self):
        self.driver.find_element_by_id("login_field").send_keys(self.login)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_name("commit").click()
    
    def html_page(self):
        return requests.get(self.driver.current_url).content