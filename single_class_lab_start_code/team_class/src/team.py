class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, name):
        self.players.append(self.name)

    def has_player(self, name):
        # if name in self.players:
        #     return True
        # else:
        #     return False 

        # either the code below or above works
        return name in self.players

    def play_game(self, game_won):
        if game_won:
            self.points += 3

        
 
