from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from models.github import Github
from models.repositories import Repositories

import sys
import getpass
import requests

PATH = "drivers/chromedriver_linux" if sys.platform == "linux" else "drivers\chromedriver_windows"
options = Options()
options.add_argument("--headless")

login = input("Your username or email: ")
password = getpass.getpass("Your password: ")

driver = webdriver.Chrome(executable_path=PATH, options=options)

github = Github(driver, login, password)
github.connect()
repositories_page_html = requests.get(github.repositories_url()).content
repositories_page_html = BeautifulSoup(repositories_page_html, features="html.parser")
repositories = Repositories.extract_repositories(repositories_page_html)
Repositories.get_repositories(repositories)