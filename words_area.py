import random


class WordsArea:
    def __init__(self, words):
        self.all_words = None
        self.random_string_words = ""
        words.insert('1.0', f"{self.random_string_words}")
        words['state'] = 'disabled'

    def get_words(self):
        with open("words_list.txt") as words_list:
            self.all_words = [line.rstrip() for line in words_list]
            random.shuffle(self.all_words)
            for word in self.all_words:
                self.random_string_words += word
                self.random_string_words += " "

    def words_reset(self, words, text):
        words['state'] = 'normal'
        words.delete('1.0', 'end')
        self.get_words()
        words.insert('1.0', f"{self.random_string_words}")
        words['state'] = 'disabled'
        text.delete('1.0', 'end')

