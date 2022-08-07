import requests
from bs4 import BeautifulSoup

class WikiStruture:
    """
    TerrariaWiki的结构,包含物品的名称,ID等...
    """
    type: str
    damage: str
    knock_back: str
    critical_hit: str
    use_speed: str
    proj_speed: str
    tooltip: str
    rarity: str # 稀有率
    cost: str
    research: str
    debuff_name: str
    debuff_tip: str
    debuff_rate: str
    debuff_duration: str
    proj_names: list
    id: str
    buff_id: list
    proj_id: list
    
    version_message: str
    description: str
    content: str
    recipe: str
    note: str
    tip: str
    
    def __init__(self, name):
        self.name = name
    

url = "https://terraria.wiki.gg/zh/wiki/日耀喷发剑?variant=zh-cn"
wiki_html = requests.get(url).content
wiki_soup = BeautifulSoup(wiki_html, "html.praser")
print(wiki_soup.prettify())