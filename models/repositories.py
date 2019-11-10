class Repository:

    @staticmethod
    def extract_html_repositories(beatiful_soup_object):
        repositories = beatiful_soup_object.find(attrs = {"class":"list-style-none"})
        print(repositories)

    @staticmethod
    def organize_repositories(repositories):
        print(repositories)