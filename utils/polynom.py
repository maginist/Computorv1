from utils.log import Logger


class Polynom:
    def __init__(self, sign, factor, power):
        print(sign, factor, power)
        self.sign = sign
        self.factor = factor
        self.power = power
        self.logger = Logger("Polynom")

    # @property
    # def power(self):
    #     return self.power
