from models.repository import Repository
from tkinter.filedialog import askdirectory

import os

class Repositories:

    options = {}

    @staticmethod
    def extract_repositories(beatiful_soup_object):
        repositories_html_structure = beatiful_soup_object.find(attrs = {'id':'user-repositories-list'}).ul
        no_process_repositories = repositories_html_structure.find_all('li')
        process_repositories = [repository.div.div.h3 for repository in no_process_repositories]
        repositories = [Repository(repository.a.text.strip(), repository.a['href'].strip()) for repository in process_repositories]
        return repositories

    @staticmethod
    def get_repositories(repositories):
        print()
        for index, repository in enumerate(repositories):
            print(f'{index + 1} - {repository.name}: https://github.com{repository.url}')
    
    @staticmethod
    def clone_repository(repository):
        directory_file = askdirectory()
        os.system(f"cd {directory_file} && git clone {repository.url}")