# Constants
number_of_stones = 7
points = 0

class Player():
    def __init__(self):
        # List with all stones
        # True if used - False if not used
        self.stones_in_use = []
        self.init_stones()
    
    def init_stones(self):
        # Init the List as 'all stones unused'
        for i in range(number_of_stones):
            self.stones_in_use.append(False)
    
    def has_new_stone(self):
        # If the stone list has a unused stone return True else return False
        for i in range(number_of_stones):
            if self.stones_in_use[i] == False:
                return True
        return False
    
    def use_new_stone(self):
        # If a stone is unused set is as used
        # Return 1 if succesful else return -1
        if self.has_new_stone() == True:
            for i in range(number_of_stones):
                if self.stones_in_use[i] == False:
                    self.stones_in_use[i] = True
                    return 1
        return -1
    
    def return_kicked_stone(self):
        # Get a used stone and set a used stone in the list as unused
        # Return 1 if succesful else return -1
        for i in range(number_of_stones):
            if self.stones_in_use[i] == True:
                self.stones_in_use[i] = False
                return 1
        return -1
    
    def has_won(self):
        return points == number_of_stones
    
    def add_point(self):
        points += 1