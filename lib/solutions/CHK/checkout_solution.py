class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        
        try:
            for sku in skus:
                validate_checkout(sku)
        except:
            return -1
        return 50
        

def validate_checkout(sku):
    valid_inputs = ["A", "B", "C", "D"]
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")


