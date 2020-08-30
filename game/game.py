#!/usr/bin/python3

import json
import random


class Game:
    def __init__(self):
        self.answers = 0
        self.right_answers = 0

        self.words = []
        self.words_list = []
        self.random_words_list = []

        self.start = 0
        self.end = 35

        self.pos = 0
        self.round = 0

        self.words_pos = [
            [0, 5, 5],
            [5, 10, 5],
            [10, 15, 5],
            [15, 20, 5],
            [20, 25, 5],
            [25, 30, 5],
            [30, 35, 5],
            [0, 35, 9999]
        ]

        self.load_words()

    def correct_answer(self):
        self.right_answers += 1
        self.answers += 1

    def get_answer(self):
        return self.cur_word[2]

    def get_answer_counts(self):
        return self.right_answers, self.answers

    def get_words(self):
        return self.cur_word[0], self.cur_word[1], self.cur_word[3]

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
        
        self.words_list = self.words[self.start:self.end]

    def randomize_words(self):
        begin = self.words_pos[self.pos][0]
        end = self.words_pos[self.pos][1]
        used_word_list = self.words_list[begin:end]

        while len(self.random_words_list) < len(used_word_list):
            word = random.choice(used_word_list)

            if not word in self.random_words_list:
                self.random_words_list.append(word)

    def set_next_word(self):
        if len(self.random_words_list) == 0:
            self.randomize_words()

            self.round += 1

        if self.round == self.words_pos[self.pos][2]:
            self.round = 0
            self.pos += 1

        self.cur_word = self.random_words_list.pop(0)

    def wrong_answer(self):
        self.answers += 1
