import pygame
class settings:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        end_font = pygame.font.Font('freesansbold.ttf', 30)
        self.WIDTH = 1000
        self.HEIGHT = 600
        self.CAPTION = "Speed Typing"
        self.bg_col = (100, 100, 100)
        self.FPS = 50
        self.font_col = (0, 0, 0)
        self.text_col = (0, 0, 0)
        self.correct_col = (0, 255, 0)
        self.wrong_col = (255, 0, 0)
        self.play_again_x = int(self.WIDTH / 3)
        self.play_again_y = int(self.HEIGHT / 2)
        width, height = end_font.size("Play Again")
        self.play_again_width = int(width + 50)
        self.play_again_height = int(height + 20)
        
