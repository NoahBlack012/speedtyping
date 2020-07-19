from Settings import settings
import pygame
class draw:
    def __init__(self):
        self.settings = settings()
        with open ("texts/text.txt") as f:
            contents = f.readlines()
        for n,line in enumerate(contents):
            if line.startswith("line"):
               contents[n] = "\n"+line.rstrip()
            else:
               contents[n]=line.rstrip()
        self.contents = ' '.join(contents)
        pygame.font.init()

    def draw_end_text(self, screen, message_1, message_2, col, font):
        m_1 = font.render(message_1, False, col)
        m_2 = font.render(message_2, False, col)
        screen.blit(m_1, (int(self.settings.WIDTH / 30), int(self.settings.HEIGHT / 4)))
        screen.blit(m_2, (int(self.settings.WIDTH / 30), int(self.settings.HEIGHT / 2)))
    def draw_words(self, screen, text, typed_letters, col, correct_col, wrong_col, font):
        def split(word):
            return [char for char in word]
        display_letters = []
        y = 100
        i = 0
        for line in text:
            x = int(self.settings.WIDTH / 4)
            display_letters = []
            str_display_letters = []
            letters = split(line)
            letters.append(" ")
            for letter in line:
                try:
                    if self.contents[i] == typed_letters[i]:
                        display_letters.append(font.render(str(letter), False, correct_col))
                        str_display_letters.append(str(letter))
                        if self.contents[i] == " ":
                            display_letters.pop()
                            str_display_letters.pop()
                            display_letters.append(font.render(str("_"), False, correct_col))
                            str_display_letters.append("_")
                    elif self.contents[i] != typed_letters[i]:
                        display_letters.append(font.render(str(letter), False, wrong_col))
                        str_display_letters.append(str(letter))
                        if self.contents[i] == " ":
                            display_letters.pop()
                            str_display_letters.pop()
                            display_letters.append(font.render(str("_"), False, wrong_col))
                            str_display_letters.append("_")
                except IndexError as e:
                    display_letters.append(font.render(str(letter), False, col))
                    str_display_letters.append(str(letter))
                i += 1
            for n, letter in enumerate(display_letters):
                screen.blit(letter, (x, y))
                self.text_width, self.text_height = font.size(str_display_letters[n])
                x += self.text_width
            y += 50

    def draw_timer(self, screen, time, col, font):
        display_time = font.render(str(time), False, col)
        screen.blit(display_time, (int(self.settings.WIDTH/2 - self.settings.WIDTH/10), int(self.settings.HEIGHT/30)))
