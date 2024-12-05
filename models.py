import csv
import random
import os

class Word:
    def __init__(self, text, definition, hint):
        self.text = text
        self.definition = definition
        self.hint = hint
        
        self.secret = self.encrypt()

    def encrypt(self):
        return ['__'] * len(self.text)

class Game:
    word = Word('','','')
    lives = ['<3'] * 5
    letters = list("abcdefghijklmnopqrstuvwxyz")
    guessed_letters = []

    last_guess= {'letter': '', 'correct': False}
    invalid_guess = {'letter': '', 'true': False}

    @classmethod
    def set_word(cls):
        with open('words.csv', 'r') as data:
            csv_reader = csv.reader(data, quotechar='"')
            words = list(csv_reader)[1:]

            random_index = random.randint(0, len(words) - 1)
            cls.word = Word(*words[random_index])

    @classmethod
    def play(cls):
        guess = input('\nGuess a letter: ').lower()
        cls.check_guess(guess)
        cls.last_guess['letter'] = guess

    @classmethod
    def check_guess(cls, guess):
        valid = False
        for letter in cls.letters:
            if guess == letter:
                valid = True
                cls.invalid_guess['true'] = False
        if not valid:
            cls.invalid_guess['letter'] = guess
            cls.invalid_guess['true'] = True
            return

        for letter in cls.word.text:
            if guess == letter:
                cls.reveal_letters(guess)
                cls.last_guess['correct'] = True
                cls.letters.remove(guess)
                cls.guessed_letters.append(guess)
                return
        
        cls.last_guess['correct'] = False
        cls.letters.remove(guess)
        cls.guessed_letters.append(guess)
        cls.lives.pop()

    
    @classmethod
    def reveal_letters(cls, letter):
        for index, let in enumerate(cls.word.text):
            if letter == let:
                cls.word.secret[index] = letter

    @classmethod
    def print_array(cls, array):
        print('  '.join(map(str, array)))

    @classmethod
    def display(cls):
        os.system('clear')

        print('Tries: ', end='')
        cls.print_array(cls.lives)

        print(end='\n\n')

        print(f'Remaining guesses: ', end='')
        cls.print_array(cls.letters)
        
        if (cls.guessed_letters != []):
            print(f'Guessed letters: ', end='')
            cls.print_array(cls.guessed_letters)

        print(end='\n\n')

        cls.print_array(cls.word.secret)
        
        print(f'\n\nDefinition: {cls.word.definition}')
        if len(cls.lives) < 3:
            print(f'Hint: {cls.word.hint}')

        if cls.invalid_guess['true']:
            print(f'\nInvalid guess ({cls.invalid_guess['letter']})')
        elif cls.last_guess['letter'] != '':
            print(f'\n{'Correct' if cls.last_guess['correct'] == True else 'Incorrect'} guess! ({cls.last_guess['letter']})')

        if cls.lost():
            print(f'\nYou have lost:(\nThe word was [{cls.word.text}]')
        elif cls.won():
            print(f'\nYou have won!')

    @classmethod
    def lost(cls):
        return len(cls.lives) == 0
    
    @classmethod
    def won(cls):
        for letter in cls.word.secret:
            if letter ==  '__':
                return False
        return True
