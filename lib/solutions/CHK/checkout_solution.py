import copy

PRICE_TABLE_AND_OFFERS = {
    "A": {"price": 50, "offer": {"group_size": 3, "price_per_group": 130}},
    "B": {"price": 30, "offer": {"group_size": 2, "price_per_group": 45}},
    "C": {"price": 20, "offer": {}},
    "D": {"price": 15, "offer": {}},
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
        except Exception as e:
            print(f"********* FAILED WITH {e} *********")
            return -1


def validate_checkout(sku):
    valid_inputs = ["A", "B", "C", "D"]
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {input}. Valid inputs = {valid_inputs}")
    return True


def get_total_price(shopping_cart_dict):
    total = 0
    for sku, number_of_items in shopping_cart_dict.items():
        multiplier = copy.deepcopy(number_of_items)  # deepcopy might be overkill
        offer = PRICE_TABLE_AND_OFFERS.get(sku).get("offer")
        if offer:
            group_size = offer.get("group_size")
            price_per_group = offer.get("price_per_group")
            number_of_groups = int(multiplier / group_size)
            total += number_of_groups * price_per_group
            multiplier = multiplier % group_size
        total += PRICE_TABLE_AND_OFFERS[sku]["price"] * multiplier
    return total

