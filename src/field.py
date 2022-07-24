# Constants
from numpy import empty


own_field_count_starting_area = 4 # Not shared fields
own_field_count_ending_area = 2 # Not shared fields
shared_field_count = 8 # Shared fields
is_double_throw_field = [3, 7, 13] # Fields to throw the dice twice
is_safe_field = 7 # Safe field
player_one = 'player_one' # Player one field marker
player_two = 'player_two' # Player two field marker
player_none = 'empty' # Empty field marker

class Field():
    def __init__(self):
        # Own fields of each player
        self.player_one_own_fields_starting_area = []
        self.player_two_own_fields_starting_area = []
        self.player_one_own_fields_ending_area = []
        self.player_two_own_fields_ending_area = []
        # Shared fields
        self.shared_field = []
        self.init_fields()

    def init_fields(self):
        # Init fields as unused
        for i in range(own_field_count_starting_area):
            self.player_one_own_fields_starting_area.append(player_none)
            self.player_two_own_fields_starting_area.append(player_none)
        for i in range(own_field_count_ending_area):
            self.player_one_own_fields_ending_area.append(player_none)
            self.player_two_own_fields_ending_area.append(player_none)
        for i in range(shared_field_count):
            self.shared_field.append(player_none)
    
    def set_marker(self, player, remove, field_number):
        if player == player_one:
            if field_number < own_field_count_starting_area:
                if remove == True:
                    self.player_one_own_fields_starting_area[field_number] = player_none
                else:
                    self.player_one_own_fields_starting_area[field_number] = player_one
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if remove == True:
                    self.shared_field[field_number - own_field_count_starting_area] = player_none
                else:
                    self.shared_field[field_number - own_field_count_starting_area] = player_one
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                if remove == True:
                    self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = player_none
                else:
                    self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = player_one
        elif player == player_two:
            if field_number < own_field_count_starting_area:
                if remove == True:
                    self.player_two_own_fields_starting_area[field_number] = player_none
                else:
                    self.player_two_own_fields_starting_area[field_number] = player_two
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if remove == True:
                    self.shared_field[field_number + own_field_count_starting_area] = player_none
                else:
                    self.shared_field[field_number - own_field_count_starting_area] = player_two
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                if remove == True:
                    self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = player_none
                else:
                    self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] = player_two
    
    def check_for_collision(self, player, field_number):
        # Return 0 if move not possible
        # Return 1 if move is possible and no player is kicked
        # Return 2 if move is possible and player is kicked
        if player == player_one:
            if field_number < own_field_count_starting_area:
                if self.player_one_own_fields_starting_area[field_number] == player_one:
                    return 0
                else:
                    return 1
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if self.shared_field[field_number - own_field_count_starting_area] == player_one:
                    return 0
                elif field_number == is_safe_field and self.shared_field[field_number - own_field_count_starting_area] == player_two:
                    return 0
                elif self.shared_field[field_number - own_field_count_starting_area] == player_two:
                    return 2
                else:
                    return 1
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                if self.player_one_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == player_one:
                    return 0
                else:
                    return 1
        elif player == player_two:
            if field_number < own_field_count_starting_area:
                if self.player_two_own_fields_starting_area[field_number] == player_two:
                    return 0
                else:
                    return 1
            elif field_number < (own_field_count_starting_area + shared_field_count) and field_number >= own_field_count_starting_area:
                if self.shared_field[field_number - own_field_count_starting_area] == player_two:
                    return 0
                elif field_number == is_safe_field and self.shared_field[field_number - own_field_count_starting_area] == player_one:
                    return 0
                elif self.shared_field[field_number - own_field_count_starting_area] == player_one:
                    return 2
                else:
                    return 1
            elif field_number >= (own_field_count_starting_area + shared_field_count):
                if self.player_two_own_fields_ending_area[field_number - own_field_count_starting_area - shared_field_count] == player_two:
                    return 0
                else:
                    return 1
    
    def move_possible(self, player, pip_count):
        
    def make_move(self, player, from_field, to_field):
        pass