# faire attention aux equations canoniques!
class Solver:
    def __init__(self, verbose, fraction, expression):
        self.verbose = verbose
        self.reduce_form = ""
        self.eq = expression
        self.natural = ""
        self.degree = 0
        self.discriminant = 0
        self.solution = [0.0, 0.0]
        self.fraction = fraction

    def solver_eq(self, reduce_form):
        self.reduce_form = reduce_form
        print(self.expression)
