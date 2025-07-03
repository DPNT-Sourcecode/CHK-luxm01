from solutions.CHK.checkout_solution import CheckoutSolution, validate_checkout
import pytest


class TestCheckout:
    @pytest.mark.skip()
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("A", 50),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAAA", 260),
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
            ("ABCDABCDABCDABCDABCD", 525),
        ],
    )
    def test_checkout_doesnt_raise(self, input, expected):
        assert CheckoutSolution().checkout(input) == expected

    @pytest.mark.parametrize(
        "input",
        [
            ("E", -1),
        ],
    )
    def test_checkout_raises(self, input):
        # unhappy path returns -1
        with pytest.raises(Exception):
            CheckoutSolution().checkout(input)

    @pytest.mark.parametrize(
        "input",
        [
            ("E"),
        ],
    )
    def test_validate_checkout_raises(self, input):
        with pytest.raises(Exception):
            validate_checkout()
