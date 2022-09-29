from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url, regex="", search_string=""):
        self.url = url
        self.regex = regex
        self.search_string = search_string


x = Scrape("google.de", search_string="hea")
print(x.search_string)


def check_if_exists():

    return False
