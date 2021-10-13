import re
from utils.log import Logger
from utils.polynom import Polynom

def create_polynom(polynom):
    print(polynom)
    factor_tmp, power_tmp = "", ""
    sign = polynom[0]
    polynom = polynom[1:]
    if 'X' in polynom:
        factor_tmp, power_tmp = polynom.split('X', 1)
        power_tmp = 'X' + power_tmp
    else:
        factor_tmp = polynom
    factor = re.search(r"^\d+?\.?\d*[*]?$", factor_tmp)
    print(factor_tmp, factor)
    if factor is None and factor_tmp:
        exit()
    power = re.search(r"^X[\^][0-9]$|^X$", power_tmp)
    print(power_tmp, power)
    if power is None and power_tmp:
        exit()
    factor = factor.group(0).replace('*', '') if factor else 1
    factor = float(factor) 
    if power:
        print(power.group(0))
        power = re.sub(r"[X^]", "", power.group(0))
    power = power if power else 0
    print(power)
    power = int(power)
    return sign, factor, power


def create_polylist(poly):
    polylist = []
    if poly[0] != "-":
        poly = '+' + poly
    result = re.findall(r"[+-]?[0-9X^.* ]+", poly)
    for polynom in result:
        sign, factor, power = create_polynom(polynom)
        polylist.append(Polynom(sign, factor, power))
    return polylist


def cleaning_equation(eq):
    eq = re.sub(r"\s+", "", eq)  # del all superfluous space
    eq = eq.replace(r"x", r"X")
    eq = re.sub(r"[+]+", '+', eq)
    eq = re.sub(r"[\^]+", '^', eq)
    eq = re.sub(r"[-]+", '-', eq)
    eq = re.sub(r"[*]+", '*', eq)
    return eq


def parse_equation(eq):
    logger = Logger("Parsing", True)
    for i, index in enumerate(eq):
        if index not in "0123456789.+-=* ^Xx":
            logger.error_parsing("The equation is not well formated", i, index)
    eq = cleaning_equation(eq)
    split = eq.split("=")
    if len(split) != 2:
        logger.error("Argument is not an equation.")
    polynomleft = create_polylist(eq[:eq.index('=')])
    polynomrigth = create_polylist(eq[eq.index('=') + 1:])
    return polynomleft, polynomrigth
