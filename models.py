import csv
import random

class Word:
    def __init__(self, text, definition, hint):
        self.text = text
        self.definition = definition
        self.hint = hint
        
        self.secret = self.encrypt()

    def encrypt(self):
        return list('_' * len(self.text))

# word = Word('tree', 'a tall green plant', 'starts with t')

class Game:
    word = None

    @classmethod
    def set_word(cls):
        with open('words.csv', 'r') as data:
            csv_reader = csv.reader(data, quotechar='"')
            words = list(csv_reader)[1:]

            random_index = random.randint(0, len(words) - 1)
            cls.word = words[random_index]

Game.set_word()
print(Game.word)
