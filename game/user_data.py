#!/usr/bin/python3

import datetime
import json
from pathlib import Path
from os import mkdir, path

homepath = str(Path.home())


class UserData:
    def __init__(self):
        self.user_file = homepath + "/.local/share/voc_game/user.json"

        self.begin_pos = 0
        self.end_pos = 35

    def get_user_pos(self):
        return self.begin_pos, self.end_pos

    def load_user_data(self):
        week_total = 0
        total = 0

        past_date = ""

        if path.isfile(self.user_file):
            with open(self.user_file, "r") as json_file:
                data = json.load(json_file)

                past_date = data['past_date']
                week_total = data['week_total']
                total = data['total']

                self.begin_pos = data['begin_pos']
                self.end_pos = data['end_pos']

                json_file.close()
            
            today_date = datetime.datetime.today()
            if past_date != today_date.strftime("%Y-%m-%d"):
                self.begin_pos += 35
                self.end_pos += 35

        return week_total, total

    def save_user_data(self, total_week, total):
        json_data = {}

        json_data['past_date'] = datetime.datetime.today().strftime("%Y-%m-%d")
        json_data['week_total'] = total_week
        json_data['total'] = total
        json_data['begin_pos'] = self.begin_pos
        json_data['end_pos'] = self.end_pos

        if not path.isdir(homepath + "/.local/share/voc_game"):
            mkdir(homepath + "/.local/share/voc_game")

        with open(self.user_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
