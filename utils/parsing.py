import re
from utils.log import Logger


def check_x(polylist, logger):
    for i in polylist:
        if i[0] == '*':
            logger.error("A multiplicator is not well formated.")
        for index in range(len(i)):
            if index != len(i) - 1 and i[index] == ' ':
                logger.error("A polynom is not well formated.") 
            if i[index] == 'X' and index + 1 is True:
                if i[index + 1] != '^' and i[index + 1] != ' ':
                    logger.error("A polynom is not well formated.")


def check_float(polylist, logger):
    for i in polylist:
        floater = 0
        for index in range(len(i)):
            if i[index] == ".":
                floater = floater + 1
                if index - 1 not in range(len(i)) or i[index - 1].isdigit() is False:
                    logger.error("A float is not well formated.")
                if index + 1 not in range(len(i)) or i[index + 1].isdigit() is False:
                    logger.error("A float is not well formated.")
            if floater > 1:
                logger.error("Invalid float.")


def check_degree(polylist, logger):
    tmp = ""
    for i in polylist:
        if "^" in i:
            tmp = tmp + i
    power = re.findall(r"[X]\^[\d]+", tmp)
    for i in power:
        degree = int(i[i.index("^") + 1:])
        if degree > 2:
            logger.error("Degree of the equation is too high.")


def check_power(polylist, logger):
    for i in polylist:
        if "^" in i:
            power = 0
            for index in range(len(i)):
                if i[index] == "^":
                    if i[index - 1] != 'X' and i[index - 1].isdigit() is False:
                        logger.error("A power is not well formated.")
                    power = power + 1
                    if index + 1 not in range(len(i)) or i[index + 1].isdigit() is False:
                        logger.error("A power is not well formated.")
                if power > 1:
                    logger.error("You can't use more than one power on a polynom.")


def check_separator(poly, side, logger):
    sign = 1
    if poly[0] == " ":
        poly = re.sub(r"(^ )", "", poly)
    if poly[0] == "*":
        logger.error(poly[0], 0, side)
    if poly[0] == "+":
        poly = re.sub(r"^\+", "", poly)
    if side == 3:
        polylen = len(poly) - 2
    else:
        polylen = len(poly) - 1
    if poly[polylen] in "+-*":
        if side == 3:
            logger.error_parsing("forbidden operation on the left side ", polylen, poly[polylen])
        else:
            logger.error_parsing("forbidden operation on the right side ", polylen, poly[polylen])
    polylist = re.split(r"[+*-][^X]", poly)
    separator = re.findall(r"[+*-][^X^]", poly)
    if poly[0] == "-":
        polylist = re.split(r"[+*-][^X]", poly)[1:]
        sign = 0
    for i in polylist:
        if i == "":
            logger.error("The equation is not well formated, do not use more than 1 operator within arguments.")
    if len(separator) + sign != len(polylist):
        logger.error("The equation is not well formated,do not use more than 1 operator within arguments.")
    return polylist


def check_poly(poly, side, logger):
    polylist = check_separator(poly, side, logger)
    check_power(polylist, logger)
    check_float(polylist, logger)
    check_degree(polylist, logger)
    check_x(polylist, logger)
    if poly[0] != '-':
        poly = "+" + poly
    polylist = re.findall(r"([+*-] [\d]*[.]?[\d]*[*]?[X]?[\^]?[0-2]?)", poly)
    return polylist


def parse_equation(expression):
    logger = Logger("Parsing", True)
    before, after = None, None
    expression = re.sub(r"(.)?([+-])(.)", r"\g<1> \g<2> \g<3>", expression)  # add space within +-
    expression = re.sub(
        r"(\d+)?([+*-])([^xX][\d+]?)", r"\g<1> \g<2> \g<3>", expression
    )  # add space within all operator except '*X'
    expression = re.sub(r"(.)?([\^])(.)", r"\g<1> \g<2> \g<3>", expression)  # add space within ^
    expression = re.sub(
        r"(\d+)?([\^])([\d+]?)", r"\g<1> \g<2> \g<3>", expression
    )  # add space within all power
    expression = re.sub(r"\s+", " ", expression)  # del all superfluous space
    expression = re.sub(r"(\s\^\s)", "^", expression)  # del space within ^ and all
    if expression[0] == " ":
        expression = re.sub(r"(^ )", "", expression)
    expression = expression.replace(r"x", r"X")
    split = expression.split("=")
    if len(split) != 2:
        logger.error("Argument is not an equation.")
    before = split[0]
    after = split[1]
    for i, index in enumerate(expression):
        if index not in "0123456789.+-=* ^X":
            print(index)
            logger.error_parsing("The equation is not well formated", i, index)
    polynomleft = check_poly(before, 3, logger)
    polynomrigth = check_poly(after, 4, logger)
    return polynomleft, polynomrigth
