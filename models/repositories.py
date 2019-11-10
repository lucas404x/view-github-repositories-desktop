class Repositories:

    @staticmethod
    def extract_repositories(beatiful_soup_object):
        repositories_html_structure = beatiful_soup_object.find(attrs = {'id':'user-repositories-list'}).ul
        no_process_repositories = repositories_html_structure.find_all('li')
        process_repositories = [repository.div.div.h3 for repository in no_process_repositories]
        repositories = [(repository.a.text.strip(), repository.a['href'].strip()) for repository in process_repositories]
        return repositories

    @staticmethod
    def get_repositories(repositories):
        print()
        for name, url in repositories:
            print(f'{name} -> https://github.com/lucas404x{url}')