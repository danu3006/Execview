import csv
import json
from typing import List

from player import Player


class Report:
    __players: List = list()

    def __init__(self, *, csv_file_path: str = ''):
        self.__csv_file_path = csv_file_path
        self._parse_csv()

    def _parse_csv(self):
        try:
            with open(self.__csv_file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    self.__players.append(Player(data=line))
                # timsort O(n log n)
                self.__players.sort(key=lambda p: p.ppg, reverse=True)
        except FileNotFoundError as e:
            print(e)

    def to_json(self):
        return json.dumps({
            'Players': '',
            'AveragePPG': '',
            'Leaders': '',
            'Count': '',
            'AverageHeight': ''
        })
