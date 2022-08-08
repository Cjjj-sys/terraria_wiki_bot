class WikiStruture:
    """
    TerrariaWiki的结构,包含物品的名称,ID等...
    """
    class Properties:
        display_name: str
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
    
    class Content:
        version_message: str
        description: str
        recipe: str
        note: str
        tip: str
    
    def __init__(self, name):
        self.name = name
    
