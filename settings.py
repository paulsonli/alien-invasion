class Settings:
    """a class to store all settings for alien invasion"""
    def __init__(self):
        """initialize the game's static settings."""
        #any settings that change throughout the game should be placed in dynamic settings so it can be reset
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3 #how many lives

        #bullet settings
        self.bullet_width = 3 #default 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 2 #default 2

        # alien settings
        self.fleet_drop_speed = 10
        self.fleet_rows = 6 # smaller number = more rows. 12 = 1 row, 10 = 2 rows, 8 = 3 rows 6 = 4 rows. move code to init dynamic settings if changing from lvl up 


        # how quickly the game speeds up 
        self.speedup_scale = 1.1
        #how quickly the alien point value increase
        self.score_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = .25 # default .25
        self.bullet_speed = .5 # default .5
        self.alien_speed = .25 # default .25

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        

    