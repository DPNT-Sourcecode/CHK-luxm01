class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        validate_checkout(input)

def validate_checkout(input):
    valid_inputs = ["A", "B", "C", "D"]
    if input not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")



