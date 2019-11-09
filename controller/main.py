from selenium import webdriver
from bs4 import BeautifulSoup
from model.github import Github
from model.repositories import Repository

def main():
    
    PATH = "/usr/bin/chromedriver"
    
    login = input()
    password = input()
    driver = webdriver.Chrome(executable_path=PATH)
    
    github = Github(driver, login, password)
    github.connect()
    # html_repository = BeautifulSoup(github.html_page(), features="html.parser")
