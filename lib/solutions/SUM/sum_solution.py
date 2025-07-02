
class SumSolution:
    
    def compute(self, x, y):
        check_valid_input(x)
        check_valid_input(y)
        return x + y


def check_valid_input(input):
    valid_input = 0 <= input <= 100
    if not valid_input:
        raise Exception(f"Invalid input {input}. Inputs must be between 0 and 100")

    




