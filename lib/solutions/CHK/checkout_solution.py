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
        shopping_cart_dict = {}
        try:
            for sku in skus:
                validate_checkout(sku)
                if shopping_cart_dict.get(sku):
                    shopping_cart_dict[sku] += 1
                else:
                    shopping_cart_dict[sku] = 1
            return get_total_price(shopping_cart_dict)
        except:
            return -1
        
def validate_checkout(sku):
    valid_inputs = ["A", "B", "C", "D"]
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")
    return True

def get_total_price(shopping_cart_dict):
    print(f"shopping_cart_dict ************** {shopping_cart_dict}")
    total = 0
    for k, v in shopping_cart_dict.items():
        total += PRICE_TABLE_AND_OFFERS[k]["price"] * v
    return total




