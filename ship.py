class Ship():
    def __init__(self, start_position, end_position, name="ship"):
        self.start_position = start_position
        self.end_position = end_position
        self.name = name
        self.size = self.calculate_size()
        self.damaged_parts = []

    def calculate_size(self):
        if self.start_position[0] == self.end_position[0]: #they are in the same row
            return abs(int(self.start_position[1]) - int(self.end_position[1]))
        else: #same column
            return abs(ord(self.start_position[0]) - ord(self.end_position[0]))

    def is_sunken(self):
        return self.size == len(self.damaged_parts)
