from level_objects import PlainLevelObject

class Player(PlainLevelObject):
    def __init__(self):
        super().__init__("🐰")
        self.items = []
        
    def get_item(self, name: str):
        self.items.append(name)
        
    def has_item(self, name: str):
        return self.items.count(name) > 0
    
    def remove_item(self, name: str):
        if(self.has_item(name)):
            self.items.remove(name)