BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[37m"
END = "\033[0m"


class Logger:
    def __init__(self, type, vb=False):
        self.type = type
        self.vb = vb

    def info(self, message):
        if self.vb is True:
            info = f"{YELLOW}<{self.type}>{END}"
            print(f"{info:24} {message}")

    def warning(self, message):
        print(f"{PURPLE}<{self.type}> Warning: {END}{message}")

    def error(self, message):
        print(f"{RED}<{self.type}> Error: {END:6}{message}")
        exit()

    def error_parsing(self, message, index, arg):
        print(f"{RED}<{self.type}> Error: {END:6}{message} at index : {index}, you wrote '{arg}'.")
        exit()

    def debug(self, message, arg):
        print(f"{GREEN}<{self.type}> debug: {END:6}{message} : {arg}")