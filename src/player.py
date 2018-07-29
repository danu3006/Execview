class Player:

    # So multiple `Player` objects of the same player is not generated in memory. As we will not be editing any of
    # the attributes.
    __slots__ = ['id', 'position', 'number', 'country', 'first_name', 'last_name', 'height', 'weight', 'university',
                 'ppg']

    def __init__(self, *, data: list = ''):
        """ A player object converted from a CSV line.

        :param data: a list of data representing the player
        :type data: list
        """
        try:
            self.id: int = data[0]
            self.position: str = data[1]
            self.number: int = data[2]
            self.country: str = data[3]

            name = data[4].split(', ')
            self.first_name: str = name[0]
            self.last_name: str = name[1]

            self.height: str = data[5]
            self.weight: int = data[6].split(' ')[0]
            self.university: str = data[7]
            self.ppg: float = float(data[8])
        except IndexError as e:
            print(e)

    @property
    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @property
    def height_cm(self):
        height = self.height.split(' ')
        foot_to_cm = 30.48
        inch_to_cm = 2.54
        return int(height[0]) * foot_to_cm + int(height[2]) * inch_to_cm

    def to_json(self):
        """ Converts `self` (player) to a JSON object. """
        return {
            "Id": self.id,
            "Position": self.position,
            "Number": self.number,
            "Country": self.country,
            "Name": self.full_name,
            "Height": self.height,
            "Weight": f'{self.weight} lb',
            "University": self.university,
            "PPG": self.ppg
        }
