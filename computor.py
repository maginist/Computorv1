
import argparse
from utils.resolver import Solver
from utils.reduce_polynom import reduce
from utils.utils import get_degree, display_graph
from utils.parsing import Parsing


def computor(eq, verbose, fraction, graphic, debug):
    parsing = Parsing(verbose)
    before, after = parsing.parse_equation(eq)
    if debug:
        for i in before:
            print("before: ", i.x, i.sign, i.factor, i.power, "line = ", i.line)
    eq = reduce(before, after, verbose, debug)
    degree = get_degree(eq)
    solver = Solver(verbose, fraction, eq, degree)
    solver.resolve()
    if graphic is True:
        display_graph(solver.eq)


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
        help="Show steps of resolution",
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
