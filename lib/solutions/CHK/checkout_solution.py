PRICE_TABLE_AND_OFFERS = {
    "A": {"price": 50}, "offer": {3: 130},
    "B": {"price": 30}, "offer": {2: 45},
    "C": {"price": 20}, "offer": {},
    "D": {"price": 15}, "offer": {},
}

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        total = 0
        items = 
        try:
            for sku in skus:
                validate_checkout(sku)
            return 50
        except:
            return -1
        

        

def validate_checkout(sku):
    valid_inputs = ["A", "B", "C", "D"]
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")
    return True







