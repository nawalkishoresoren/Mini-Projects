import random

num_range = {
    1: (1,10),
    2: (10,50),
    3: (50,100)
}
class Generator:
    def __init__(self,level:int):
        self.level = level

    def generate_random(self):
        return random.randint(*num_range[self.level])
    
