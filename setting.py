class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализация настроек игры"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Параметры корабля
        self.ship_limit = 3
        self.ship_speed = 2.5
        # Параметры снаряда
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # Настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15
        # fleet_direction=1 означает движение вправо, а -1 влево.
        self.fleet_direction = 1
        self.speedup_scale = 1.25
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1
        # score
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points* self.score_scale)