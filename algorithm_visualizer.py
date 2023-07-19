import pygame
import sys
import math


from settings import Setting
from algorithms import Algorithm


class Visualizer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        
        self.settings = Setting()
        self.start_sort = False
        self.ascending = True
        self.lst = self.settings.lst
        self.algo = Algorithm()
        
         
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        self.screen_height = self.screen.get_rect().height
        self.screen_width = self.screen.get_rect().width
        
    def run_visualizer(self):
        
        while True:
            self.clock.tick(self.settings.fps)
            self._update_screen()
            if self.start_sort:
                try:
                    i, j = next(self.algo_generator)
                    self._draw_list(swap_color={i: self.settings.swap_color1,
                                                j: self.settings.swap_color2}, 
                                    clear_bg=True)

                except StopIteration:
                    self.start_sort = False
          
            self._check_event()
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_list()
        pygame.display.flip()
        
        
    def _draw_list(self, swap_color={}, clear_bg=False):
        if clear_bg:
            clear_rect = (
                    self.settings.left_padding,
                    self.settings.top_padding,
                    self.screen_height - self.settings.left_padding \
                    - self.settings.right_padding,
                    self.screen_width - self.settings.top_padding)

            pygame.draw.rect(self.screen,
                         self.settings.bg_color, clear_rect)
        
        
        for i, val in enumerate(self.lst):
            x = self.settings.left_padding + (i * self.settings.bar_width)
            height = math.floor(val * self.settings.percent_bar_height)
            y = self.screen_height - height
            color = self.settings.bar_color[i % 3]

            if i in swap_color:
                color = swap_color[i]



            pygame.draw.rect(self.screen, color, (x, y, self.settings.bar_width, height))
        
        if clear_bg:
            pygame.display.flip()
        

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_SPACE and not self.start_sort:
                self.start_sort = True
                self.algo_generator = self.algo.algo_function(self.lst, self.ascending)
            
            elif event.key == pygame.K_r:
                self.lst = self.settings.set_list()
    
                self.start_sort = False
            
            elif event.key == pygame.K_a:
                self.ascending = True
            
            elif event.key == pygame.K_d:
                self.ascending = False

            
if __name__ == "__main__":
    v = Visualizer()
    v.run_visualizer()