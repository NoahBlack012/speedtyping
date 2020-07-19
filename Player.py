import pygame
from Keys import keys
class player:
    def __init__(self):
        pygame.init()
        self.keys = keys()
        self.wpm_content = []
        with open('texts/text.txt','r') as f:
            for line in f:
                for word in line.split():
                    self.wpm_content.append(word)

    def get_score(self, typed_letters, contents, minutes, seconds):
        def split(word):
            return [char for char in word]
        content = []
        for word in self.wpm_content:
            for char in word:
                content.append(char)
            content.append(" ")
        content.pop()
        letters_right = 0
        letters_wrong = 0
        wpm = 0
        i = 0
        for n, letter in enumerate(content):
            if letter == typed_letters[n]:
                letters_right += 1
        minutes = minutes + (seconds / 60)
        wpm = len(self.wpm_content) / minutes
        wpm = round(wpm, 2)

        typing_percentage = letters_right/len(content) * 100
        typing_percentage = round(typing_percentage, 2)
        return letters_right, wpm, typing_percentage, len(content), round(minutes, 2)
