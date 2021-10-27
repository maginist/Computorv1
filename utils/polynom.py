from utils.log import Logger


class Polynom:
    def __init__(self, sign:str, factor:int, power:int, x:bool, line:str):
        self.sign = sign
        self.factor = factor
        self.power = power
        self.x = x
        self.line = line
        self.logger = Logger("Polynom")

    # @property
    # def power(self):
    #     return self.power

    def __repr__(self) -> str:
        pass
