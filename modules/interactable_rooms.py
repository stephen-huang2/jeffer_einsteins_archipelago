class Room:
    
    def __init__(self, name:str, key:bool=False, unlocked:bool=False):
        self.name = name
        self.key = key
        self.unlocked = unlocked
    
    def __str__(self):
        return self.name