#!/usr/bin/python3

import json
import random


class Game:
    def __init__(self):
        self.answers = 0
        self.right_answers = 0

        self.words = []

        self.load_words()

        self.start = 0
        self.end = len(self.words)

    def correct_answer(self):
        self.right_answers += 1
        self.answers += 1

    def get_answer(self):
        return self.cur_word[2]

    def get_answer_counts(self):
        return self.right_answers, self.answers

    def get_words(self):
        return self.cur_word[0], self.cur_word[1]

    def load_words(self, file: str = "lang/en_to_fi.json"):
        with open(file, "r") as json_file:
            data = json.load(json_file)

            for word in data['words']:
                source = word['source']
                pron = word['pronounce']
                target = word['target']
                word_class = word['word_class']

                word_dict = [source, pron, target, word_class]
                self.words.append(word_dict)

    def set_next_word(self):
        self.cur_word = random.choice(self.words[self.start:self.end])

    def wrong_answer(self):
        self.answers += 1
