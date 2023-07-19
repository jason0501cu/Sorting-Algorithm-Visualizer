import pygame
import sys
import math

from settings import Setting


class Visualizer:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        


    
    def run_visualizer(self):
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(self.settings.fps)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_list()
        pygame.display.flip()

    
    def _draw_list(self):
        lst = self.settings.lst

        for i, val in enumerate(lst):
            x = self.settings.left_padding + (i * self.settings.bar_width)
            height = math.floor(val * self.settings.percent_bar_height)
            y = self.screen_height - height
            color = self.settings.bar_color[i % 3]


            pygame.draw.rect(self.screen, color, (x, y, self.settings.bar_width, height))

    
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    v = Visualizer()
    v.run_visualizer()