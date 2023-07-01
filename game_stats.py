class GameStats:
    """Track stats for alien invation"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self._reset_stats()
        self._load_highscore()

        #start alien invation in an inactive state
        self.game_active = False

    # high score in init instead of reset because we dont want to reset high score
    def _load_highscore(self):
        """load highscore from txt file"""
        with open('highscore.txt', 'r') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0
    
    def _reset_stats(self):
        """initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1