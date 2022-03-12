class Scoreboard:

    def __init__(self):
        self.home_score = 0
        self.away_score = 0
        self.down = 1
        self.half = 1

    def end_half(self):
        self.half = 2

    def end_game(self):
        self.half = 0
