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
        self.play_x = int(self.settings.WIDTH / 4)
        self.play_y = int(self.settings.HEIGHT / 4)
        self.play_width = int(self.settings.WIDTH / 2)
        self.play_height = int(self.settings.HEIGHT / 2)

    def draw_start_text(self, screen, col, font, hover):       
        if hover:
            message = font.render("Play", False, col)
            pygame.draw.rect(screen, col, (self.play_x, self.play_y, self.play_width, self.play_height), 5)
            screen.blit(message, (self.play_x + 150, self.play_y + 100))
        else:
            message = font.render("Play", False, self.settings.bg_col)
            pygame.draw.rect(screen, col, (self.play_x, self.play_y, self.play_width, self.play_height))
            screen.blit(message, (self.play_x + 150, self.play_y + 100))

    def draw_end_text(self, screen, message_1, message_2, col, font, hover):
        m_1 = font.render(message_1, False, col)
        m_2 = font.render(message_2, False, col)
        screen.blit(m_1, (int(self.settings.WIDTH / 30), int(self.settings.HEIGHT / 8)))
        screen.blit(m_2, (int(self.settings.WIDTH / 30), int(self.settings.HEIGHT / 4)))
        
        if hover:
            m_3 = font.render("Play Again", False, col)
            pygame.draw.rect(screen, col, (self.settings.play_again_x, self.settings.play_again_y, self.settings.play_again_width, self.settings.play_again_height), 5)
            screen.blit(m_3, (self.settings.play_again_x + 15, self.settings.play_again_y + 10))
        else:
            m_3 = font.render("Play Again", False, self.settings.bg_col)
            pygame.draw.rect(screen, col, (self.settings.play_again_x, self.settings.play_again_y, self.settings.play_again_width, self.settings.play_again_height))
            screen.blit(m_3, (self.settings.play_again_x + 15, self.settings.play_again_y + 10))

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
