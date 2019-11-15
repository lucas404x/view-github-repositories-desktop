from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from getpass import getpass
from models.github import Github
from models.repositories import Repositories

import os, sys
import requests

SO = sys.platform
PATH = "drivers/chromedriver_linux" if SO == "linux" else "drivers\chromedriver_windows"
options = Options()
options.add_argument("--headless")

login = input("Your username or email: ")
password = getpass("Your password: ")

driver = webdriver.Chrome(executable_path=PATH, options=options)

github = Github(driver, login, password)
github.connect()
repositories_page_html = requests.get(github.repositories_url()).content
repositories_page_html = BeautifulSoup(repositories_page_html, features="html.parser")
repositories = Repositories.extract_repositories(repositories_page_html)

while True:
    Repositories.get_repositories(repositories)
    option = int(input("Choose a repository to clone: ")) - 1
    if option < 0 or option >= len(repositories):
        break
    Repositories.clone_repository(repositories[option])
    os.system("clear" if SO == "linux" else "cls")

print("Finish him!")