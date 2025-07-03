import copy

BUY_N_SKUS_FOR_P = {"skus": "STXYZ", "number": 3, "price": 45, "code": "1"}



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
    "G": {"price": 20, "offers": []},
    "H": {
        "price": 10,
        "offers": [
            {"group_size": 10, "price_per_group": 80},
            {"group_size": 5, "price_per_group": 45},
        ],
    },
    "I": {"price": 35, "offers": []},
    "J": {"price": 60, "offers": []},
    "K": {"price": 80, "offers": [{"group_size": 2, "price_per_group": 150}]},
    "L": {"price": 90, "offers": []},
    "M": {"price": 15, "offers": []},
    "N": {"price": 40, "offers": [{"group_size": 3, "freebie": "M"}]},
    "O": {"price": 10, "offers": []},
    "P": {"price": 50, "offers": [{"group_size": 5, "price_per_group": 200}]},
    "Q": {"price": 30, "offers": [{"group_size": 3, "price_per_group": 80}]},
    "R": {"price": 50, "offers": [{"group_size": 3, "freebie": "Q"}]},
    "S": {"price": 30, "offers": []},
    "T": {"price": 20, "offers": []},
    "U": {"price": 40, "offers": [{"group_size": 3, "freebie": "U"}]},
    "V": {
        "price": 50,
        "offers": [
            {"group_size": 3, "price_per_group": 130},
            {"group_size": 2, "price_per_group": 90},
        ],
    },
    "W": {"price": 20, "offers": []},
    "X": {"price": 90, "offers": []},
    "Y": {"price": 10, "offers": []},
    "Z": {"price": 50, "offers": []},
    "1": {"price": 45, "offers": []}
}

BUY_N_SKUS_FOR_P = {"skus": "STXYZ", "number": 3, "price": 45}


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

    # apply buy n skus for p
    relevant_skus = {}
    for sku, number_of_items in shopping_cart_dict.items():
        if sku in BUY_N_SKUS_FOR_P["skus"]:
            relevant_skus[sku] = {"quantity": number_of_items, "price": PRICE_TABLE_AND_OFFERS[sku]["price"]}
    relevant_skus_sorted_by_price = dict(sorted(relevant_skus.items(), key=lambda item: item[1]['price'], reverse=True))
    
    for sku, quantity_price in relevant_skus_sorted_by_price:

    if relevant_skus:
        print(f"\n******************* relevant_skus_sorted_by_price:\n{relevant_skus_sorted_by_price}")

    # remove free items from cart
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
                            if running_total_pay_for == group_size + 1:
                                items_to_deduct += 1
                                running_total_pay_for = 0
                        shopping_cart_dict[freebie] -= items_to_deduct
                    else:
                        shopping_cart_dict[freebie] -= number_of_groups
                        if shopping_cart_dict[freebie] < 0:
                            shopping_cart_dict[freebie] = 0

    # apply bulk discounts
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





