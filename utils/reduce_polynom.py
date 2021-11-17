from utils.log import Logger
from utils.polynom import Polynom



def reduce_x_power(before, final):
    power = 0
    for i in before:
        if power < i.power:
            power = i.power
    while power > -1:
        x_factor = 0.0
        for i, poly in enumerate(before):
            if poly.power == power and poly.x == True:
                if poly.sign == '-':
                    x_factor = x_factor + float(poly.factor * -1)
                else:
                    x_factor = x_factor + float(poly.factor)
        if x_factor > 0:
            sign = '+'
        else:
            sign = '-'
            x_factor = x_factor * -1
        if power > 0 and x_factor != 0:
            final.append(Polynom(sign, x_factor, power, True, sign + str(x_factor) + "X^" + str(power) ))
        if power == 0 and x_factor != 0:
            final.append(Polynom(sign, x_factor, 0, False, sign + str(x_factor)))
        power = power - 1


def vb_display(before, real_before, phase):
    result = ""
    for i in before:
        if i == before[0] and i.line[0] != '-':
            result = i.line[1:] + ' '
        else:
            result = result + i.line[0] + ' ' + i.line[1:] + ' '
    if phase == 2:
        for i in real_before:
            if i.x is False:
                result = result + i.line[0] + ' ' + i.line[1:] + ' '
    result = result + "= 0"
    if phase == 1:
        print("First step of reducted equation (Get all the polynom on one side) :", result)
    if phase == 2:
        print("Second step of reducted equation (Get all the x in one single polynom by power) :", result)
    if phase == 3:
        print("Third step of reducted equation (Get only one real for the equation) : ", result)
    print('')

def add_or_min(poly, number, sign):
    if sign == '+':
        number = number + float(poly)
    else:
        number = number - float(poly)
    if number < 0:
        sign = '-'
    else:
        sign = '+'
    return number, sign

def get_real(before, final):
    real = 0.0
    sign = ""
    for i, poly in enumerate(before):
        if poly.x is False:
            real, sign = add_or_min(poly.factor, real, poly.sign)
    for i, poly in enumerate(final):
        if poly.x is False:
            real, sign = add_or_min(poly.factor, real, poly.sign)
            del final[i]
    if real < 0:
        real = real * -1
    real = round(real, 3)
    if real != 0:
        final.append(Polynom(sign, real, 0, False, sign + str(real) ))


def reduce(before, after, vb, debug):
    logger = Logger("Reduce", debug)
    for i in after:
        if i.factor != 0:
            if i.sign == '+':
                i.sign = '-'
                i.line = i.line.replace('+', '-')
            elif i.sign == '-':
                i.sign = '+'
                i.line = i.line.replace('-', '+')
            before.append(i)
    final = []
    if vb is True:
        vb_display(before,0, 1)
    reduce_x_power(before, final)
    if vb is True:
        vb_display(final, before, 2)
    get_real(before, final)
    if vb is True:
        vb_display(final,0, 3)
    if debug:
        for i in final:
            print("after: ", i.x, i.sign, i.factor, i.power, "line = ", i.line)
    return final