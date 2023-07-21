import pygame.font

from settings import Setting


class Button:
    def __init__(self, algorithm_visualizer, x, y, msg):
        self.screen = algorithm_visualizer.screen
        self.settings = Setting()
        self.height = self.settings.button_height
        self.width = self.settings.button_width
        self.button_color = self.settings.button_color
        self.text_color = self.settings.font_color
        self.font = self.settings.button_font

        self.rect = pygame.Rect(x, y, self.width, self.height)

        self._button_tag(msg)

    def _button_tag(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
