class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.game_score = ""
        self.temp_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            self.game_is_even()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.score_is_more_than_three()
        else:
            self.game_is_going()
        return self.game_score


    def game_is_even(self):
        if self.player1_score == 0:
            self.game_score = "Love-All"
        elif self.player1_score == 1:
            self.game_score = "Fifteen-All"
        elif self.player1_score == 2:
            self.game_score = "Thirty-All"
        else:
            self.game_score = "Deuce"
    
    def score_is_more_than_three(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            self.game_score = "Advantage player1"
        elif minus_result == -1:
            self.game_score = "Advantage player2"
        elif minus_result >= 2:
            self.game_score = "Win for player1"
        else:
            self.game_score = "Win for player2"
    
    def game_is_going(self):
        for i in range(1, 3):
            if i == 1:
                self.temp_score = self.player1_score
            else:
                self.game_score = self.game_score + "-"
                self.temp_score = self.player2_score

            if self.temp_score == 0:
                self.game_score = self.game_score + "Love"
            elif self.temp_score == 1:
                self.game_score = self.game_score + "Fifteen"
            elif self.temp_score == 2:
                self.game_score = self.game_score + "Thirty"
            elif self.temp_score == 3:
                self.game_score = self.game_score + "Forty"