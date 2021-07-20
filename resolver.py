# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    resolver.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maginist <maginist@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/20 16:05:36 by maginist          #+#    #+#              #
#    Updated: 2021/07/20 16:05:36 by maginist         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Solver:
    def __init__(self, verbose, fraction, reduce_form, expression, degree):
        self.verbose = verbose
        self.reduce = reduce_form
        self.eq = expression
        self.degree = degree
        self.discriminant = 0
        self.solution = [0.0, 0.0]
        self.fraction = fraction

    # faire attention aux equations canoniques!
