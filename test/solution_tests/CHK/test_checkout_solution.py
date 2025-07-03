from solutions.CHK.checkout_solution import CheckoutSolution, validate_checkout
import pytest


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("A", 50),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 200),
            ("AAAAAA", 250),
            ("AAAAAAAA", 330),
            ("B", 30),
            ("BB", 45),
            ("BBB", 75),
            ("C", 20),
            ("CC", 40),
            ("CCC", 60),
            ("D", 15),
            ("DD", 30),
            ("DDD", 45),
            ("ABC", 100),
            ("ABAAD", 175),
            ("ABCDABCDABCDABCDABCD", 495),
            ("E", 40),
            ("EE", 80),
            ("EEB", 80),
            ("EEEEBB", 160),
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            # ("F", 10),      # buy 1, pay for 1
            # ("FF", 20),     # buy 2, pay for 2
            # ("FFF", 20),    # buy 3, pay for 2
            # ("FFFF", 30),   # buy 4, pay for 3
            ("FFFFF", 40),  # buy 5, pay for 4
            # ("FFFFFF", 30), # buy 6, pay for 4
        ],
    )
    def test_checkout_no_error(self, skus, expected):
        assert expected == CheckoutSolution().checkout(skus) 

    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("Z", -1),
            (1, -1),
            ("ABCDEFZ", -1),
        ],
    )
    def test_checkout_error(self, skus, expected):
        # unhappy path returns -1
        assert expected == CheckoutSolution().checkout(skus) 

    @pytest.mark.parametrize(
        "sku",
        [
            ("E"),
        ],
    )
    def test_validate_checkout_raises(self, sku):
        with pytest.raises(Exception):
            validate_checkout()


