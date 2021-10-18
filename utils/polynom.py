from utils.log import Logger


class Polynom:
    def __init__(self, sign:str, factor:int, power:int):
        self.sign = sign
        self.factor = factor
        self.power = power
        self.logger = Logger("Polynom")

    # @property
    # def power(self):
    #     return self.power
