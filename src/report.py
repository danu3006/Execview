import csv
import json
from typing import List

from player import Player


class Report:
    __players: List = list()

    # Unique positions for each of the players for dynamic generation.
    __unique_position: List = list()

    # Can be edited to add more ranks and will be added to JSON automatically.
    __ranks: List = ['Gold', 'Silver', 'Bronze']

    def __init__(self, *, csv_file_path: str = ''):
        """ Report generation for Chicago Bulls.

        :param csv_file_path: the absolute or relative path of the CSV file
        :type csv_file_path: str
        """
        self.__csv_file_path = csv_file_path
        self._parse_csv()

    def _parse_csv(self):
        """ Parses the CSV file line by line and creates a `Player` object. The player objects are added into a list
        and sorted using Timsort O(n log n). Each of the players position is added to a unique list for dynamic JSON
        generation.
        """
        try:
            with open(self.__csv_file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    player = Player(data=line)
                    if player.position not in self.__unique_position:
                        self.__unique_position.append(player.position)
                    self.__players.append(player)

                # timsort O(n log n)
                self.__players.sort(key=lambda p: p.ppg, reverse=True)
        except FileNotFoundError as e:
            print(e)

    def to_json(self):
        """ Converts the `self` (report) to a JSON object. """
        avg_height = round(sum(player.height_cm for player in self.__players) / len(self.__players), 1)

        return json.dumps({
            'Players': [player.to_json() for player in self.__players],
            'AveragePPG': round(sum(player.ppg for player in self.__players) / len(self.__players), 2),
            'Leaders': [{self.__ranks[i]: p.full_name, 'PPG': p.ppg} for i, p in enumerate(self.__players[:len(
                self.__ranks)])],
            'Count': {pos: sum(1 for p in self.__players if p.position == pos) for pos in self.__unique_position},
            'AverageHeight': f'{avg_height} cm'
        })
