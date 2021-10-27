# faire attention aux equations canoniques!
class Solver:
    def __init__(self, verbose, fraction, expression):
        self.verbose = verbose
        self.eq = expression
        self.degree = 0
        self.discriminant = 0
        self.solution = [0.0, 0.0]
        self.fraction = fraction

    def resolve(self, eq, degree):
        self.degree = degree
        
