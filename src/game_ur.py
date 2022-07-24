import field
import dice

field = field.Field()
dices = [dice.Dice(), dice.Dice(), dice.Dice(), dice.Dice()]

class Game_Ur():
    def __init__(self):
        self.is_player_ones_turn = True;
    
    def players_turn(self, starting_field, pip_count):
        #pip_count = self.roll_dices()
        if self.is_player_ones_turn:
            field.make_move(field.player_one, starting_field, pip_count)
        else:
            field.make_move(field.player_two, starting_field, pip_count)
        self.is_player_ones_turn = not self.is_player_ones_turn

    def roll_dices(self):
        result = 0
        for dice in dices:
            result += dice.roll_dice()       
        return result

game = Game_Ur()

while (not field.player_one.has_won() and not field.player_two.has_won()):
    pip_count = 0
    print("Player Ones Turn")
    if input("Roll dice= [y/n]") == 'y':
        pip_count = game.roll_dices()
        print(f"Pip Count: {pip_count}")
    print(field.player_one_own_fields_starting_area)
    print(field.shared_field)
    print(field.player_one_own_fields_ending_area)
    print()
    print(field.player_two_own_fields_starting_area)
    print(field.shared_field)
    print(field.player_two_own_fields_ending_area)
    print()
    starting_field = int(input("Make Move From: "))
    game.players_turn(starting_field, pip_count)