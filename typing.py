import pygame
import sys
import math
import textwrap
import time

from Settings import settings
from Player import player
from Draw import draw
from Keys import keys


class typing:
    """Class to manage overall game assets and behaviours"""
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.settings = settings()
        self.player = player()
        self.draw = draw()
        self.keys = keys()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption(self.settings.CAPTION)
        self.clock = pygame.time.Clock()
        self.time_font = pygame.font.Font('freesansbold.ttf', 60)
        self.text_font = pygame.font.Font('freesansbold.ttf', 20)
        with open ("texts/text.txt") as f:
            contents = f.readlines()
        for n,line in enumerate(contents):
            if line.startswith("line"):
               contents[n] = "\n"+line.rstrip()
            else:
               contents[n]=line.rstrip()
        self.contents = ' '.join(contents)
        self.text_width, self.text_height = self.time_font.size(self.contents)
        self.lines = int(math.ceil(self.text_width / self.settings.WIDTH /2 ))
        self.groups = int(len(self.contents) / self.lines)
        self.line_contents = textwrap.wrap(self.contents, self.groups)
        for n, line in enumerate(self.line_contents):
            if n < len(self.line_contents):
                self.line_contents[n] = self.line_contents[n] + " "
        self.minutes = 0
        self.seconds = 0
        self.ms = 0
        self.typed_letters = []
        self.key_typed = ''

    def run_game(self):
        """Run the game"""
        while True:
            self.clock.tick(self.settings.FPS)
            self.ms += 20
            if self.ms >= 1000:
                self.seconds += 1
                self.ms = 0
            if self.seconds >= 60:
                self.minutes += 1
                self.seconds = 0
            str_minutes = str(self.minutes)
            str_seconds = str(self.seconds)
            str_ms = str(self.ms)
            str_time = f"{str_minutes}:{str_seconds}:{str_ms}"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    for key in self.keys.keys:
                        if event.key == pygame.K_BACKSPACE:
                            try:
                                self.typed_letters.pop()
                            except IndexError as e:
                                self.typed_letters = []
                            break
                        elif event.key == key:
                            self.key_typed = self.keys.keys[key]
                            self.typed_letters.append(self.key_typed)
                            mods = pygame.key.get_mods()
                            if mods == 1 or mods == 2:
                                self.typed_letters.pop()
                                self.key_typed = self.key_typed.upper()
                                self.typed_letters.append(self.key_typed)
                                self.key_typed = ''
                                mods = 0
                                break
                            self.key_typed = ''
                            break

            self.screen.fill(self.settings.bg_col)
            ###Draw itsems here###
            self.draw.draw_timer(self.screen, str_time, self.settings.font_col, self.time_font)
            self.draw.draw_words(self.screen, self.line_contents, self.typed_letters, self.settings.text_col, self.settings.correct_col, self.settings.wrong_col, self.text_font)
            #####################
            pygame.display.flip()
            if len(self.typed_letters) >= len(self.contents):
                break
        self.letters_right, self.wpm, self.typing_percentage, self.text_len, self.minutes = self.player.get_score(self.typed_letters, self.line_contents, self.minutes, self.seconds)

        print (f"You got {self.letters_right} correct out of {self.text_len} in {self.minutes} minutes")
        print (f"You typed at {self.wpm} words per minute on {self.typing_percentage}% accuracy")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    t = typing()
    t.run_game()
