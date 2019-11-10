from selenium import webdriver
from bs4 import BeautifulSoup
from models.github import Github
from models.repositories import Repository

import os, sys

def main():
    
    PATH = "/usr/bin/chromedriver" if sys.platform == "linux" else \
            os.path.join("Windows", "chromedriver")
    
    login = input()
    password = input()
    driver = webdriver.Chrome()
    
    github = Github(driver, login, password)
    github.connect()
    html_repository = BeautifulSoup(github.html_page(), features="html.parser")
    Repository.extract_html_repositories(html_repository)