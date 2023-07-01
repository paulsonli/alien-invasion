import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """a class to replort scoring info"""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prep the scoreboard images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn the score into a rendereed image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "SCORE: " + "{:,}".format(rounded_score) # adds a comma inbetween numbers
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) # true for anti aliasing
        

        # display score at the top center of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.centerx = self.screen_rect.centerx
    
    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, - 1) # round the score to nearest 10
        high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #high score at the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        # self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.right = self.screen_rect.right - 20 # put the high score at the top right of the screen
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """turn the level into a rendered image"""
        level_str = "LVL: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.high_score_rect.right
        self.level_rect.top = self.high_score_rect.bottom + 10
        
    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image_scaled = pygame.transform.scale(ship.image, (20, 40))
            ship.rect.x = 10 + ship_number * ship.rect.width # 10px from the left of screen with the padding
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw score, level and ship to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

        
