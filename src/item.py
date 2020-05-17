import crayons 
class Item: 
    def __init__(self, name, description):
        self.name = name 
        self.description = description 
    
    def on_picked_item(self, player):
        print(crayons.blue("\n...grabbing" + "."))
        # pass 

    def __str__(self):
        return self.name + ": " + self.description


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value 
        self.picked_up = False 
    
    def on_picked_item(self, player): 
        super().on_picked_item(player)

        if not self.picked_up:
            player.score += self.value 
            print(f"You have received {self.value} points!")
            self.picked_up = True 
    