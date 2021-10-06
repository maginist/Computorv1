# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maginist <maginist@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/20 15:53:32 by maginist          #+#    #+#              #
#    Updated: 2021/07/20 15:53:32 by maginist         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from .utils.parsing import parse_equation
from .utils.reduce_polynom import reduce


def computor(eq, verbose, fraction, graphic):
    before, after = parse_equation(eq)
    eq = reduce(before, after)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolver of polynomial equations.")
    parser.add_argument(
        "expression",
        type=str,
        help="Input an unique string well formated as the equation (ex: 3*X^2 + 4*X^1 = 1*X^1 + 2)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Show verbose and steps of resolution",
    )
    parser.add_argument(
        "-f",
        "--fraction",
        action="store_true",
        default=False,
        help="Show result in irreducible fraction",
    )
    parser.add_argument(
        "-g",
        "--graphic",
        action="store_true",
        default=False,
        help="Show the equation in function",
    )
    args = parser.parse_args()
    computor(args.expression, args.verbose, args.fraction, args.graphic)
