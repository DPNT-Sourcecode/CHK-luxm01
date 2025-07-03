import copy

PRICE_TABLE_AND_OFFERS = {
    "A": {
        "price": 50,
        "offers": [
            {"group_size": 5, "price_per_group": 200},
            {"group_size": 3, "price_per_group": 130},
        ],
    },
    "B": {"price": 30, "offers": [{"group_size": 2, "price_per_group": 45}]},
    "C": {"price": 20, "offers": []},
    "D": {"price": 15, "offers": []},
    "E": {"price": 40, "offers": [{"group_size": 2, "freebie": "B"}]},
    "F": {"price": 10, "offers": [{"group_size": 2, "freebie": "F"}]},
| "G": {"price"20    |                        |
| "H": {"price"10    | 5H for 45, 10H for 80  |
| "I": {"price"35    |                        |
| "J": {"price"60    |                        |
| "K": {"price"80    | 2K for 150             |
| "L": {"price"90    |                        |
| "M": {"price"15    |                        |
| "N": {"price"40    | 3N get one M free      |
| "O": {"price"10    |                        |
| "P": {"price"50    | 5P for 200             |
| "Q": {"price"30    | 3Q for 80              |
| "R": {"price"50    | 3R get one Q free      |
| "S": {"price"30    |                        |
| "T": {"price"20    |                        |
| "U": {"price"40    | 3U get one U free      |
| "V": {"price"50    | 2V for 90, 3V for 130  |
| "W": {"price"20    |                        |
| "X": {"price"90    |                        |
| "Y": {"price"10    |                        |
| "Z": {"price"50    |                        |
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
            print(f"\n\n********* FAILED WITH {e} *********\n\n")
            return -1


def validate_checkout(sku):
    valid_inputs = PRICE_TABLE_AND_OFFERS.keys()
    if sku not in valid_inputs:
        raise Exception(f"Invalid input: {sku}. Valid inputs = {valid_inputs}")
    return True


def get_total_price(shopping_cart_dict):
    total = 0

    # first pass, remove free items from cart
    for sku, number_of_items in shopping_cart_dict.items():
        multiplier = copy.deepcopy(number_of_items)  # deepcopy might be overkill
        offers = PRICE_TABLE_AND_OFFERS.get(sku).get("offers")
        for offer in offers:
            group_size = offer.get("group_size")
            number_of_groups = int(multiplier / group_size)
            freebie = offer.get("freebie")
            if freebie:
                amount_of_freebie_items_in_cart = shopping_cart_dict.get(freebie)
                if amount_of_freebie_items_in_cart:
                    if freebie == sku:
                        items_to_deduct = 0
                        running_total_pay_for = 0
                        for i in range(amount_of_freebie_items_in_cart):
                            running_total_pay_for += 1
                            if running_total_pay_for == 3:
                                items_to_deduct += 1
                                running_total_pay_for = 0
                        shopping_cart_dict[freebie] -= items_to_deduct
                    else:
                        shopping_cart_dict[freebie] -= number_of_groups
                        if shopping_cart_dict[freebie] < 0:
                            shopping_cart_dict[freebie] = 0

    # second pass, apply bulk discounts
    for sku, number_of_items in shopping_cart_dict.items():
        multiplier = copy.deepcopy(number_of_items)  # deepcopy might be overkill
        offers = PRICE_TABLE_AND_OFFERS.get(sku).get("offers")
        if offers:
            for offer in offers:
                group_size = offer.get("group_size")
                price_per_group = offer.get("price_per_group")
                number_of_groups = int(multiplier / group_size)
                if price_per_group:
                    total += number_of_groups * price_per_group
                    multiplier = multiplier % group_size
        total += PRICE_TABLE_AND_OFFERS[sku]["price"] * multiplier
    return total

