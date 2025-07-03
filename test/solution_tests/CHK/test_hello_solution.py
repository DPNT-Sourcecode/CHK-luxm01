from solutions.CHK.checkout_solution import CheckoutSolution
import pytest


class TestCheckout:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("", ""),
        ],
    )
    def test_checkout_doesnt_raise(self, input, expected):
        assert CheckoutSolution().checkout(input) == expected

    @pytest.mark.parametrize(
        "input",
        [
            (""),
        ],
    )
    def test_checkout_raises(self, input):
        with pytest.raises(Exception):
            CheckoutSolution().checkout(input)


