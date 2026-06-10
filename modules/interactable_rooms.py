class Room:
    
    def __init__(self, name:str, key:bool=False, unlocked:bool=False, key_type:str = "Key"):
        self.name = name
        self.key = key
        self.unlocked = unlocked
        self.key_type = key_type
    
    def __str__(self):
        return self.name