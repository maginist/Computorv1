
import argparse
from utils.parsing import parse_equation
from utils.reduce_polynom import reduce
from utils.utils import create_polynom

def computor(eq, verbose, fraction, graphic, debug):
    before, after = parse_equation(eq)
    create_polynom(before, after)
    eq = reduce(before, after, verbose, debug)


def parsing():
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
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="Debug informations.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parsing()
    computor(args.expression, args.verbose, args.fraction, args.graphic, args.debug)
