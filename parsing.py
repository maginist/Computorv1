# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maginist <maginist@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/20 15:53:34 by maginist          #+#    #+#              #
#    Updated: 2021/07/20 15:53:34 by maginist         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from global_var import (
    _OPERATORS,
    _OPERATORS_PRIORITY,
    _SIGN,
    _COMMA,
    _OPEN_PARENTHESES,
    _CLOSING_PARENTHESES,
)


def parse_equation(expression):
    print(expression)
