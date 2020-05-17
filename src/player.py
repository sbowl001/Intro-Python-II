# Write a class to hold player information, e.g. what room they are in
# currently.
import crayons 
class Player:
    def __init__(self, name, room, items= []):
        self.name = name 
        self.room = room
        self.score = 0
        self.items = items
        
    def __str__(self):
        return f'{self.name} is in {self.room}'

    
    def get(self, item):
        self.items.append(item)
        self.room.items.remove(item)
        

    def drop(self, item):
        self.room.items.append(item)
        self.items.remove(item)
        # item.on_drop()