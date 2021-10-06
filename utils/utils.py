# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: judumay <judumay@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/24 16:45:09 by maginist          #+#    #+#              #
#    Updated: 2021/10/06 14:01:45 by judumay          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def print_error(arg, index, error):
    error_message = {
        0: "Syntax error: Argument is not an equation",
        1: f"Syntax error: The equation is not well formated, {arg}.",
        2: f"Syntax error: bad caractere at index : {index}, you wrote '{arg}'.",
        3: f"Syntax error: forbidden operation on the left side at index: {index}, you wrote '{arg}'.",
        4: f"Syntax error: forbidden operation on the right side at index: {index}, you wrote '{arg}'.",
        5: "Degree of the equation is too high.",
        6: f"{arg}",
    }
    print(error_message.get(error))
    exit()


def abs(nb):
    if nb < 0:
        return (nb * (-1)) + 0
    else:
        return nb + 0


def sqrt(nb):
    x = 1
    y = 0.5 * (x + nb)
    while abs(y - x) > 0.00000001:
        x = y
        y = 0.5 * (x + nb / x)
    return y + 0
