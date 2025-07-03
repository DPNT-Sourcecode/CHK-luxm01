from solutions.CHK.checkout_solution import CheckoutSolution
import pytest


class TestCheckout:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("A", 50),
            ("AA", 100)
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAAA", 260)
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
            ("ABCDABCDABCDABCDABCD", 230+120+100+)
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
        # unhappy path returns -1
        with pytest.raises(Exception):
            CheckoutSolution().checkout(input)




