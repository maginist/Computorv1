import re
from utils.log import Logger
from utils.polynom import Polynom

class Parsing:
    def __init__(self, vb=False):
        self.vb = vb
        self.logger = Logger("Parsing", self.vb)

    def create_polynom(self, polynom):
        factor_tmp, power_tmp = "", ""
        sign = polynom[0]
        x = False
        polynom = polynom[1:]
        if 'X' in polynom:
            factor_tmp, power_tmp = polynom.split('X', 1)
            power_tmp = 'X' + power_tmp
            x = True
        else:
            factor_tmp = polynom
        factor = re.search(r"^\d+?\.?\d*[*]?$", factor_tmp)
        if factor is None and factor_tmp:
            self.logger.error("factor")
        power = re.search(r"^X[\^][0-9]$|^X$", power_tmp)
        if power is None and power_tmp:
            self.logger.error("power")
        factor = factor.group(0).replace('*', '') if factor else 1
        try:
            factor = int(factor)
        except ValueError:
            factor = float(factor)
        if power and power.group(0) == "X":
            power = 1
        elif power:
            power = int(re.sub(r"[X^]", "", power.group(0)))
        else:
            power = 0
        return sign, factor, power, x

    def create_polylist(self, poly):
        polylist = []
        if poly[0] != "-":
            poly = '+' + poly
        result = re.findall(r"[+-]?[0-9X^.* ]+", poly)
        for poly in result:
            sign, factor, power, x = self.create_polynom(poly)
            polylist.append(Polynom(sign, factor, power, x, poly))
        return polylist

    def cleaning_equation(self, eq):
        eq = re.sub(r"\s+", "", eq)  # del all superfluous space
        eq = eq.replace(r"x", r"X")
        eq = re.sub(r"[+]+", '+', eq)
        eq = re.sub(r"[\^]+", '^', eq)
        eq = re.sub(r"[-]+", '-', eq)
        eq = re.sub(r"[*]+", '*', eq)
        return eq

    def parse_equation(self, eq):
        for i, index in enumerate(eq):
            if index not in "0123456789.+-=* ^Xx":
                self.logger.error_parsing("The equation is not well formated", i, index)
        eq = self.cleaning_equation(eq)
        split = eq.split("=")
        if len(split) != 2:
            self.logger.error("Argument is not an equation.")
        polynomleft = self.create_polylist(eq[:eq.index('=')])
        polynomrigth = self.create_polylist(eq[eq.index('=') + 1:])
        return polynomleft, polynomrigth
