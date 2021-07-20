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

from parsing import parse_equation
from resolver import Solver


def main():
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
    args = parser.parse_args()
    try:
        reduce_form = parse_equation(args.expression)
    except Exception as error:
        print(error)
    # try:
    # Solver(args.verbose, args.fraction, args.expression, reduce_form)
    # except Exception as error:
    # print(error)


if __name__ == "__main__":
    main()
