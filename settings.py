import pygame
import random
import math

class Setting:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 0, 0, 0 # black
        self.fps = 120
        self.left_padding = 25
        self.right_padding = 100
        self.top_padding = 100

        self.num_in_list = 100
        self.min_num = 0
        self.max_num = 100
        self.lst = self.set_list()

        self.bar_color = [
            (0, 204, 204),
            (102, 255, 255),
            (204, 255, 255)
        ]
        
        self.swap_color1 = (0, 255, 0)
        self.swap_color2 = (255, 0, 0)

        self.title_font = pygame.font.SysFont(None, 30)
        self.font_color = (255, 255, 255)

    
    def set_list(self):
        lst = self._generate_list()
        max_value = max(lst)
        
        self.bar_width = (self.screen_width - self.left_padding - self.right_padding) // len(lst)
        
        # calcuate the relative height of each value to the display area
        self.percent_bar_height = (self.screen_height - self.top_padding) / max_value

        return lst

    def _generate_list(self):
        lst = []
        for _ in range(self.num_in_list + 1):
            num = random.randint(self.min_num, self.max_num)
            lst.append(num)
        
        return lst
