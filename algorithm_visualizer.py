# main file
# run this file to execute the programme
import pygame
import sys
import math


from settings import Setting
from algorithms import Algorithm
from button import Button


class Visualizer:
    def __init__(self):
        pygame.init()

        # basic setup
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.algo = Algorithm()
        self.settings = Setting()
        self.start_sort = False
        self.ascending = True
        self.lst = self.settings.lst
        self.speed_key = "Normal"

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.screen_height = self.screen.get_rect().height
        self.screen_width = self.screen.get_rect().width

        # initialize all the control buttons
        self.speed_button = Button(self, self.settings.button_x,
                                   self.settings.speed_button_y,
                                   f"C - Speed: {self.speed_key}")

        self.bubble_sort_button = Button(self, self.settings.button_x,
                                         self.settings.bubble_sort_button_y,
                                         "B - Bubble Sort")

        self.selection_sort_button = Button(self, self.settings.button_x,
                                            self.settings.selection_sort_button_y,
                                            "S - Selection Sort")

        self.insertion_sort_button = Button(self, self.settings.button_x,
                                            self.settings.insertion_sort_button_y,
                                            "I - Insertion Sort")

        self.heap_sort_button = Button(self, self.settings.button_x,
                                       self.settings.heap_sort_button_y,
                                       "H - Heap Sort")

        self.quick_sort_button = Button(self, self.settings.button_x,
                                        self.settings.quick_sort_button_y,
                                        "Q - Quick Sort")

        self.ascending_button = Button(self, self.settings.button_x,
                                       self.settings.ascending_button_y,
                                       "A - Ascending")

        self.descending_button = Button(self, self.settings.button_x,
                                        self.settings.descending_button_y,
                                        "D - Descending")

        self.reset_button = Button(self, self.settings.button_x,
                                   self.settings.reset_button_y,
                                   "R - Reset")

        self.start_button = Button(self, self.settings.button_x,
                                   self.settings.start_button_y,
                                   "Space - Start")

        self.exit_button = Button(self, self.settings.button_x,
                                  self.settings.exit_button_y,
                                  "E - Exit")

    def run_visualizer(self):
        """main event loop"""
        while True:
            self.clock.tick(self.settings.fps[self.speed_key])
            self._update_screen()
            if self.start_sort:
                try:
                    # i, j are the indices of nummbers under swap
                    i, j = next(self.algo_generator)
                    
                    # show the respective bars in different color
                    self._draw_list(swap_color={i: self.settings.swap_color1,
                                                j: self.settings.swap_color2},
                                    clear_bg=True)

                except StopIteration:
                    self.start_sort = False

            self._check_event()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_list()
        self._draw_title()
        self._draw_button()
        pygame.display.flip()

    def _draw_title(self):
        # display sorting algorithm name
        title = self.settings.title_font.render(
            self.algo.algo_name, True, self.settings.font_color)

        self.screen.blit(title, (self.screen_width/2 - title.get_width()/2, 5))

        # display ascending or descending
        second_title = self.settings.title_font.render(f"{'-Ascending-' if self.ascending else '-Descending-'}",
                                                       True, self.settings.font_color)

        self.screen.blit(second_title, (self.screen_width/2 -
                         second_title.get_width()/2, second_title.get_height() + 10))

    def _draw_button(self):
        self.speed_button.draw_button()
        self.bubble_sort_button.draw_button()
        self.selection_sort_button.draw_button()
        self.insertion_sort_button.draw_button()
        self.heap_sort_button.draw_button()
        self.quick_sort_button.draw_button()
        self.ascending_button.draw_button()
        self.descending_button.draw_button()
        self.reset_button.draw_button()
        self.start_button.draw_button()
        self.exit_button.draw_button()

    def _draw_list(self, swap_color={}, clear_bg=False):
        if clear_bg:
            #  clear the display area for bars while sorting
            clear_rect = (
                # paramenters of the display area for bars
                self.settings.left_padding,  # x corodinate
                self.settings.top_padding,  # y corodinate
                self.screen_height - self.settings.left_padding
                - self.settings.right_padding,  # height
                self.screen_width - self.settings.top_padding)  # width

            pygame.draw.rect(self.screen,
                             self.settings.bg_color, clear_rect)

        for i, val in enumerate(self.lst):
            # draw bars to respecent the list
            x = self.settings.left_padding + (i * self.settings.bar_width)
            height = math.floor(val * self.settings.percent_bar_height)
            y = self.screen_height - height
            color = self.settings.bar_color[i % 3]

            if i in swap_color:
                #  show bars under swap in different color
                color = swap_color[i]

            pygame.draw.rect(self.screen, color,
                             (x, y, self.settings.bar_width, height))

        if clear_bg:
            pygame.display.flip()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_keydown_event(self, event):
        if not self.start_sort:
            if event.key == pygame.K_SPACE:
                self.start_sort = True
                self.algo_generator = self.algo.algo_function(
                    self.lst, self.ascending)

            elif event.key == pygame.K_a:
                self.ascending = True

            elif event.key == pygame.K_d:
                self.ascending = False

            elif event.key == pygame.K_i:
                self.algo.change_function(
                    "Insertion Sort", self.algo.insertion_sort)

            elif event.key == pygame.K_b:
                self.algo.change_function("Bubble Sort", self.algo.bubble_sort)

            elif event.key == pygame.K_s:
                self.algo.change_function(
                    "Selection Sort", self.algo.selection_sort)

            elif event.key == pygame.K_h:
                self.algo.change_function("Heap Sort", self.algo.heap_sort)

            elif event.key == pygame.K_q:
                self.algo.change_function("Quick Sort", self.algo.quick_sort)

        if event.key == pygame.K_r:
            # reset the list and stop sorting
            self.lst = self.settings.set_list()
            self.start_sort = False

        elif event.key == pygame.K_e:
            sys.exit()

        elif event.key == pygame.K_c:
            # change fps of the visualizer
            if self.speed_key == "Normal":
                self.speed_key = "Fast"
            elif self.speed_key == "Fast":
                self.speed_key = "Slow"
            elif self.speed_key == "Slow":
                self.speed_key = "Normal"

            self.speed_button._button_tag(f"C - Speed: {self.speed_key}")

    def _check_button(self, mouse_pos):
        bubble_sort_button_clicked = self.bubble_sort_button.rect.collidepoint(
            mouse_pos)
        selection_sort_button_clicked = self.selection_sort_button.rect.collidepoint(
            mouse_pos)
        insertion_sort_button_clicked = self.insertion_sort_button.rect.collidepoint(
            mouse_pos)
        heap_sort_button_clicked = self.heap_sort_button.rect.collidepoint(
            mouse_pos)
        quick_sort_button_clicked = self.quick_sort_button.rect.collidepoint(
            mouse_pos)
        ascending_button_clicked = self.ascending_button.rect.collidepoint(
            mouse_pos)
        descending_button_clicked = self.descending_button.rect.collidepoint(
            mouse_pos)
        reset_button_clicked = self.reset_button.rect.collidepoint(mouse_pos)
        start_button_clicked = self.start_button.rect.collidepoint(mouse_pos)
        exit_button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        speed_button_clicked = self.speed_button.rect.collidepoint(mouse_pos)

        if not self.start_sort:
            if start_button_clicked:
                self.start_sort = True
                self.algo_generator = self.algo.algo_function(
                    self.lst, self.ascending)

            elif ascending_button_clicked:
                self.ascending = True

            elif descending_button_clicked:
                self.ascending = False

            elif insertion_sort_button_clicked:
                self.algo.change_function(
                    "Insertion Sort", self.algo.insertion_sort)

            elif bubble_sort_button_clicked:
                self.algo.change_function("Bubble Sort", self.algo.bubble_sort)

            elif selection_sort_button_clicked:
                self.algo.change_function(
                    "Selection Sort", self.algo.selection_sort)

            elif heap_sort_button_clicked:
                self.algo.change_function("Heap Sort", self.algo.heap_sort)

            elif quick_sort_button_clicked:
                self.algo.change_function("Quick Sort", self.algo.quick_sort)

        if reset_button_clicked:
            self.lst = self.settings.set_list()
            self.start_sort = False

        elif exit_button_clicked:
            sys.exit()

        elif speed_button_clicked:
            # change fps of the visualizer
            if self.speed_key == "Normal":
                self.speed_key = "Fast"
            elif self.speed_key == "Fast":
                self.speed_key = "Slow"
            elif self.speed_key == "Slow":
                self.speed_key = "Normal"

            self.speed_button._button_tag(f"C - Speed: {self.speed_key}")


if __name__ == "__main__":
    v = Visualizer()
    v.run_visualizer()
