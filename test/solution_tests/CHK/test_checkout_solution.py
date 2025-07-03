from solutions.CHK.checkout_solution import CheckoutSolution, validate_checkout
import pytest


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("A", 50),
            ("AA", 100),
            # ("AAA", 130),
            # ("AAAA", 180),
            # ("AAAAAA", 260),
            ("B", 30),
            # ("BB", 45),
            # ("BBB", 75),
            ("C", 20),
            ("CC", 40),
            ("CCC", 60),
            ("D", 15),
            ("DD", 30),
            ("DDD", 45),
            ("ABC", 100),
            # ("ABAAD", 175),
            # ("ABCDABCDABCDABCDABCD", 525),
        ],
    )
    def test_checkout_doesnt_no_error(self, skus, expected):
        assert CheckoutSolution().checkout(skus) == expected

    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("E", -1),
            (1, -1),
            ("ABCDE", -1),
        ],
    )
    def test_checkout_error(self, skus, expected):
        # unhappy path returns -1
        assert CheckoutSolution().checkout(skus) == expected

    @pytest.mark.parametrize(
        "sku",
        [
            ("E"),
        ],
    )
    def test_validate_checkout_raises(self, sku):
        with pytest.raises(Exception):
            validate_checkout()

