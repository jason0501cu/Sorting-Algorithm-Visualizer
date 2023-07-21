import pygame
import random


class Setting:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = 0, 0, 0
        self.fps = {"Slow": 30, "Normal": 60, "Fast": 120}
        self.left_padding = 25
        self.right_padding = 100
        self.top_padding = 100

        self.nums_in_list = 100
        self.min_num = 0
        self.max_num = 100
        self.lst = self.set_list()

        self.bar_color = [
            (0, 204, 204),
            (102, 255, 255),
            (204, 255, 255)
        ]

        self.swap_color1 = (255, 128, 128)
        self.swap_color2 = (0, 204, 0)

        self.title_font = pygame.font.SysFont(None, 30)
        self.font_color = (255, 255, 255)

        self.button_font = pygame.font.SysFont(None, 20)
        self.button_color = (0, 102, 102)
        self.button_width = 130
        self.button_height = 25
        self.button_x = self.screen_width - self.bar_width - 130

        self.speed_button_y = 100

        self.bubble_sort_button_y = 200
        self.button_interval = self.button_height + 30
        self.selection_sort_button_y = self.bubble_sort_button_y + self.button_interval
        self.insertion_sort_button_y = self.selection_sort_button_y + self.button_interval
        self.heap_sort_button_y = self.insertion_sort_button_y + self.button_interval
        self.quick_sort_button_y = self.heap_sort_button_y + self.button_interval

        self.ascending_button_y = self.quick_sort_button_y + self.button_interval
        self.descending_button_y = self.ascending_button_y + self.button_interval

        self.exit_button_y = self.screen_height - 50
        self.start_button_y = self.exit_button_y - self.button_interval
        self.reset_button_y = self.start_button_y - self.button_interval

    def set_list(self):
        # set the values for visualize the list
        lst = self._generate_list()
        max_value = max(lst)

        self.bar_width = (self.screen_width -
                          self.left_padding - self.right_padding) // len(lst)

        # based on max value in the list,
        # calcuate the relative height of each value to the display area
        self.percent_bar_height = (
            self.screen_height - self.top_padding) / max_value

        return lst

    def _generate_list(self):
        lst = []
        for _ in range(self.nums_in_list + 1):
            num = random.randint(self.min_num, self.max_num)
            lst.append(num)

        return lst
