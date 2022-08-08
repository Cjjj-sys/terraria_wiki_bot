import requests
from bs4 import BeautifulSoup
from models.wiki import WikiStruture
from wiki_helper import WikiHelper

class WikiHelper:
    
    def __init__(self, name):
        self.name = name
        url = "https://terraria.wiki.gg/zh/wiki/日耀喷发剑?variant=zh-cn"
        wiki_html = requests.get(url).content
        self.wiki_soup = BeautifulSoup(wiki_html, "html.parser")
        # print(wiki_soup.prettify())
    
    def _get_properties(self) -> WikiStruture.Properties:
        print()
        return WikiStruture.Properties
      
    def get_wiki(self) -> WikiStruture:
        wiki = WikiStruture(self.name)
        wiki.Properties = _get_properties()
        
    