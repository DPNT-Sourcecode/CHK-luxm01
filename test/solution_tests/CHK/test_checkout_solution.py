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
            ("F", 10),  # buy 1, pay for 1
            ("FF", 20),  # buy 2, pay for 2
            ("FFF", 20),  # buy 3, pay for 2
            ("FFFF", 30),  # buy 4, pay for 3
            ("FFFFF", 40),  # buy 5, pay for 4
            ("FFFFFF", 40),  # buy 6, pay for 4
            ("FFFFFFF", 50),  # buy 7, pay for 5
            ("FFFFFFFF", 60),  # buy 8, pay for 56
            ("G", 20),
            ("H", 10),
            ("HHHHH", 45),
            ("HHHHHHHHHH", 80),
            ("I", 35),
            ("J", 60),
            ("K", 80),
            ("KK", 150),
            ("L", 90),
            ("M", 15),
            ("N", 40),
            ("NNNM", 120),
            ("O", 10),
            ("P", 50),
            ("PPPPP", 200),
            ("Q", 30),
            ("QQQ", 80),
            ("R", 50),
            ("RRRQ", 150),
            ("S", 30),
            ("T", 20),
            ("U", 40),
            ("UUU", 120),
            ("UUUU", 120),
            ("V", 50),
            ("VV", 90),
            ("VVV", 130),
            ("W", 20),
            ("X", 90),
            ("Y", 10),
            ("Z", 50),
            ("1", 45),
            # ("SSSTTTXXXYYYZZZ", 225),
            ("STX", 45),
            # ("XYZ", 45),
            # ("STXYZ", 75)
        ],
    )
    def test_checkout_no_error(self, skus, expected):
        assert expected == CheckoutSolution().checkout(skus)

    # @pytest.mark.parametrize(
    #     "skus, expected",
    #     [
    #         ("Ö", -1),
    #         (1, -1),
    #         ("ABCDEFÖ", -1),
    #     ],
    # )
    # def test_checkout_error(self, skus, expected):
    #     # unhappy path returns -1
    #     assert expected == CheckoutSolution().checkout(skus)

    # @pytest.mark.parametrize(
    #     "sku",
    #     [
    #         ("E"),
    #     ],
    # )
    # def test_validate_checkout_raises(self, sku):
    #     with pytest.raises(Exception):
    #         validate_checkout()


