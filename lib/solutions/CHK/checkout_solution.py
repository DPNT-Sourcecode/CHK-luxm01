price_table_and_offers = {
    "A": {"price": 50}, "offer": {3: 130},
    "B": {"price": 30}, "offer": {2: 45},
    "C": {"price": 20}, "offer": {},
    "D": {"price": 15}, ""
}

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        try:
            for sku in skus:
                validate_checkout(sku)
                print(f"VALID: {sku}")
        except:
            print(f"IN EXCEPT BLOCK {skus}")
            return -1
        return 50

        

def validate_checkout(sku):
    valid_inputs = ["A", "B", "C", "D"]
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")
    return True






