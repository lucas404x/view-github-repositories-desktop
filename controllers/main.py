from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from models.github import Github
from models.repositories import Repositories
from time import sleep

import sys
import requests

PATH = "/usr/bin/chromedriver" if sys.platform == "linux" else "C:\Windows\chromedriver"
options = Options()
options.add_argument("--headless")

login = input("Your username or email: ")
password = input("Your password: ")

driver = webdriver.Chrome(executable_path=PATH, options=options)

github = Github(driver, login, password)
github.connect()
repositories_page_html = requests.get(github.repositories_url()).content
repositories_page_html = BeautifulSoup(repositories_page_html, features="html.parser")
repositories = Repositories.extract_repositories(repositories_page_html)
Repositories.get_repositories(repositories)