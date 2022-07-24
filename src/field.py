from turtle import begin_fill
import player

# Constants
# Field
own_field_count_starting_area = 4 # Not shared fields
own_field_count_ending_area = 2 # Not shared fields
shared_field_count = 8 # Shared fields
# Field status
is_double_throw_field = [3, 7, 13] # Fields to throw the dice twice
is_safe_field = 7 # Safe field
field_to_begin = -1 # Starting point for ununsed stones
# Moves
move_not_possible = 'invalid move'
move_possible = 'valid move'
move_kicking_player = 'valid move: player kicked'
move_finishing = 'valid move: stone finished'

class Field():
    def __init__(self):
        # Player
        self.player_one = player.Player()
        self.player_two = player.Player()
        self.player_none = 'empty'
        # Own fields of each player
        self.player_one_own_fields_starting_area = []
        self.player_two_own_fields_starting_area = []
        self.player_one_own_fields_ending_area = []
        self.player_two_own_fields_ending_area = []
        # Shared fields
        self.shared_field = []
        # Init fields
        self.init_fields()

    def init_fields(self):
        # Init fields as unused
        for i in range(own_field_count_starting_area):
            self.player_one_own_fields_starting_area.append(self.player_none)
            self.player_two_own_fields_starting_area.append(self.player_none)
        for i in range(own_field_count_ending_area):
            self.player_one_own_fields_ending_area.append(self.player_none)
            self.player_two_own_fields_ending_area.append(self.player_none)
        for i in range(shared_field_count):
            self.shared_field.append(self.player_none)
    
    def set_marker(self, player, remove, field_number):
        if player == self.player_one:
            if field_number < own_field_count_starting_area:
                if remove == True:
                    self.player_one_own_fields_starting_area[field_number] = self.player_none
                else:
                    self.player_one_own_fields_starting_area[field_number] = self.player_one
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if remove == True:
                    self.shared_field[field_number - own_field_count_starting_area] = self.player_none
                else:
                    self.shared_field[field_number - own_field_count_starting_area] = self.player_one
            elif field_number >= (own_field_count_starting_area + shared_field_count) and field_number < (own_field_count_starting_area + shared_field_count + own_field_count_ending_area):
                if remove == True:
                    self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = self.player_none
                else:
                    self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = self.player_one
        elif player == self.player_two:
            if field_number < own_field_count_starting_area:
                if remove == True:
                    self.player_two_own_fields_starting_area[field_number] = self.player_none
                else:
                    self.player_two_own_fields_starting_area[field_number] = self.player_two
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if remove == True:
                    self.shared_field[field_number + own_field_count_starting_area] = self.player_none
                else:
                    self.shared_field[field_number - own_field_count_starting_area] = self.player_two
            elif field_number >= (own_field_count_starting_area + shared_field_count) and field_number < (own_field_count_starting_area + shared_field_count + own_field_count_ending_area):
                if remove == True:
                    self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = self.player_none
                else:
                    self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = self.player_two
    
    def check_for_collision(self, player, field_number):
        # Return 0 if move not possible
        # Return 1 if move is possible and no player is kicked
        # Return 2 if move is possible and player is kicked
        # Return 3 if move is possible and player finishes one stone
        if player == self.player_one:
            if field_number < own_field_count_starting_area:
                if self.player_one_own_fields_starting_area[field_number] == self.player_one:
                    return move_not_possible
                else:
                    return move_possible
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if self.shared_field[field_number - own_field_count_starting_area] == self.player_one:
                    return move_not_possible
                elif field_number == is_safe_field and self.shared_field[field_number - own_field_count_starting_area] == self.player_two:
                    return move_not_possible
                elif self.shared_field[field_number - own_field_count_starting_area] == self.player_two:
                    return move_kicking_player
                else:
                    return move_possible
            elif field_number >= (own_field_count_starting_area + shared_field_count) and field_number < (own_field_count_starting_area + shared_field_count + own_field_count_ending_area):
                if self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == self.player_one:
                    return move_not_possible
                else:
                    return move_possible
            elif field_number == (own_field_count_starting_area + own_field_count_ending_area + shared_field_count):
                self.player_two.add_point()
                return move_finishing
            else:
                return move_not_possible
        elif player == self.player_two:
            if field_number < own_field_count_starting_area:
                if self.player_two_own_fields_starting_area[field_number] == self.player_two:
                    return move_not_possible
                else:
                    return move_possible
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if self.shared_field[field_number - own_field_count_starting_area] == self.player_two:
                    return move_not_possible
                elif field_number == is_safe_field and self.shared_field[field_number - own_field_count_starting_area] == self.player_one:
                    return move_not_possible
                elif self.shared_field[field_number - own_field_count_starting_area] == self.player_one:
                    return move_kicking_player
                else:
                    return move_possible
            elif field_number >= (own_field_count_starting_area + shared_field_count) and field_number < (own_field_count_starting_area + shared_field_count + own_field_count_ending_area):
                if self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == self.player_two:
                    return move_not_possible
                else:
                    return move_possible
            elif field_number == (own_field_count_starting_area + own_field_count_ending_area + shared_field_count):
                self.player_two.add_point()
                return move_finishing
            else:
                return move_not_possible
    
    def is_own_stone(self, player, field_number):
        if player == self.player_one:
            if field_number < own_field_count_starting_area:
                return self.player_one_own_fields_starting_area[field_number] == player
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                return self.shared_field[field_number - own_field_count_starting_area] == player
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                return self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == player
        elif player == self.player_two:
            if field_number < own_field_count_starting_area:
                return self.player_two_own_fields_starting_area[field_number] == player
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                return self.shared_field[field_number - own_field_count_starting_area] == player
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                return self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == player
        
        return False
    
    def is_move_possible(self, player, pip_count, starting_field):
        if starting_field != field_to_begin:
            return self.is_own_stone(player, starting_field) and (starting_field + pip_count) <= (own_field_count_starting_area + own_field_count_ending_area + shared_field_count) and self.check_for_collision(player, (starting_field + pip_count)) != move_not_possible
        else:
            return player.has_new_stone() and (starting_field + pip_count) <= (own_field_count_starting_area + own_field_count_ending_area + shared_field_count) and self.check_for_collision(player, (starting_field + pip_count)) != move_not_possible

    def make_move(self, player, starting_field, pip_count):
        if self.is_move_possible(player, pip_count, starting_field):
            if starting_field != field_to_begin:
                self.set_marker(player, True, starting_field)
            else:
                player.use_new_stone()
            if self.check_for_collision(player, (starting_field + pip_count)) == move_kicking_player:
                if player == self.player_one:
                    self.player_two.return_kicked_stone()
                elif player == self.player_two:
                    self.player_one.return_kicked_stone()
            self.set_marker(player, False, (starting_field + pip_count))
            return True
        else:
            return False
    
    def can_player_make_move(self, player, pip_count):
        if self.is_move_possible(player, pip_count, field_to_begin):
            return True
        for i in range(own_field_count_starting_area):
            if self.is_move_possible(player, pip_count, i):
                return True
        for i in range(shared_field_count + own_field_count_starting_area):
            if self.is_move_possible(player, pip_count, i):
                return True
        for i in range(shared_field_count + own_field_count_starting_area + own_field_count_ending_area):
            if self.is_move_possible(player, pip_count, i):
                return True
        
        return False

field = Field()
print(field.player_one_own_fields_starting_area)
print(field.shared_field)
print(field.player_one_own_fields_ending_area)
print()
print(field.player_two_own_fields_starting_area)
print(field.shared_field)
print(field.player_two_own_fields_ending_area)
print()

field.make_move(field.player_one, -1, 2)
field.make_move(field.player_one, -1, 4)
field.make_move(field.player_one, -1, 6)
field.make_move(field.player_two, -1, 8)
field.make_move(field.player_one, -1, 8)
print(field.can_player_make_move(field.player_one, 1))

print(field.player_one_own_fields_starting_area)
print(field.shared_field)
print(field.player_one_own_fields_ending_area)
print()
print(field.player_two_own_fields_starting_area)
print(field.shared_field)
print(field.player_two_own_fields_ending_area)
print()