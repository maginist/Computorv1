from utils.utils import get_irreductible_fraction, abs
class Solver:
    def __init__(self, verbose:bool, fraction:bool, expression:str, degree:int):
        self.verbose = verbose
        self.eq = expression
        self.degree = degree
        self.discriminant = 0
        self.solution = [0.0, 0.0]
        self.fraction = fraction

    def degree_two(self, a, b, c):
        d = b**2 - (4*a*c)
        d = round(d, 3)
        if self.verbose == True:
            print(f"\na = {a}, b = {b}, c = {c}, Δ = {d}\n")
        if d > 0:
            r_delta = d ** 0.5
            self.solution[0] = (-b + r_delta)/ (2 * a)
            self.solution[1] = (-b - r_delta)/ (2 * a)
            self.solution[0] = round(self.solution[0], 3)
            self.solution[1] = round(self.solution[1], 3)
            print("The discriminant is positive, so there is two solutions.")
            if self.verbose is True:
                print(f"\na = {a}, b = {b}, c = {c}, Δ = {d}\nx1 = -b + √Δ / 2a\nx2 = -b - √Δ / 2a")
                print(f"x1 = {-b} + {r_delta}/ 2 * {a}\nx2 = {-b} - {r_delta}/ 2 * {a}")
                print(f"x1 = {self.solution[0]} & x2 = {self.solution[1]}")
            if self.fraction:
                if self.solution[0] > 0 and self.solution[1] > 0:
                    fraction1 = get_irreductible_fraction(self.solution[0])
                    fraction2 = get_irreductible_fraction(self.solution[1])
                    print(f"The solutions in irreductible fraction are : x1 = {fraction1}, x2 = {fraction2}")
                else:
                    print("\n One or more number in the solutions is negative, no fraction is possible.")
            print(f"The solutions are x1 = {self.solution[0]} & x2 = {self.solution[1]}.")
        elif d == 0:
            self.solution[0] = -b/ (2 * a)
            print("The discriminant is equal to 0, so there is just one solution.")
            if self.verbose is True:
                print(f"\na = {a}, b = {b}, c = {c}\nx1 = -b / 2 * a\n")
                print(f"x1 = {-b} / 2 * {a}\n")
                print(f"x = {self.solution[0]}")
            if self.fraction:
                if self.solution[0] > 0:
                    fraction1 = get_irreductible_fraction(self.solution[0])
                    print(f"\nThe solution in irreductible fraction is : x = {fraction1}")
                else:
                    print("\nThe solution is negative, no fraction is possible.")
            print(f"The solution is x = {self.solution[0]}.")
        elif d < 0:
            print("The discriminant is negative, so there is two complexes solutions.")
            if self.verbose is True:
                print(f"a = {a}, b = {b}, c = {c}, Δ = {d}\nx1 = -b + i√|Δ| / 2 * a \nx2 = -b - i√|Δ| / 2 * a")
            if self.fraction is True:
                print("\nWe can't convert the complexes solutions in irreductibles fractions.")
            print(f"\nThe two solutions are :\nx1 = ({-b} - i√{abs(d)}) / {2 * a}\nx2 = ({-b} + i√{abs(d)}) / {2 * a}")

    def degree_one(self, a, b):
        res = -b/a
        res = round(res, 3)
        if self.verbose is True:
            print("\nEquation of first degree = ax + b = 0")
            print(f"a = {a}, b = {b}")
            print(f"x = -b/a : x = {-b}/{a}\n")
        if self.fraction:
            if res > 0:
                fraction = get_irreductible_fraction(res)
                print(f"The solution in irreductible fraction is : x = {fraction}")
            else:
                print("\nThe solution is negative, no fraction is possible.")
        print(f"The solution is : x = {res}")

    def resolve(self):
        a, b, c = 0, 0, 0
        for i in self.eq:
            sign = 1 if i.sign == "+" else -1
            if i.power == 2:
                a = i.factor * sign
            elif i.power == 1:
                b = i.factor * sign
            elif i.power == 0:
                c = i.factor * sign
        if self.degree == 0:
            if c == 0:
                print ("Infinity of solutions.")
            else:
                print("There is no solution for this equation.")
        elif self.degree == 1:
            self.degree_one(b, c)
        elif self.degree == 2:
            self.degree_two(a, b, c)