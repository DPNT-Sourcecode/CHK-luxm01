from solutions.CHK.checkout_solution import CheckoutSolution, validate_checkout
import pytest


class TestCheckout:
    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("E", 40),
            ("F", 10),  # buy 1, pay for 1
            ("G", 20),
            ("H", 10),
            ("I", 35),
            ("J", 60),
            ("K", 70),
            ("L", 90),
            ("M", 15),
            ("N", 40),
            ("O", 10),
            ("P", 50),
            ("Q", 30),
            ("R", 50),
            ("S", 20),
            ("T", 20),
            ("U", 40),
            ("V", 50),
            ("W", 20),
            ("X", 17),
            ("Y", 20),
            ("Z", 21),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 200),
            ("AAAAAA", 250),
            ("AAAAAAAA", 330),
            ("BB", 45),
            ("BBB", 75),
            ("CC", 40),
            ("CCC", 60),
            ("DD", 30),
            ("DDD", 45),
            ("ABC", 100),
            ("ABAAD", 175),
            ("ABCDABCDABCDABCDABCD", 495),
            ("EE", 80),
            ("EEB", 80),
            ("EEEEBB", 160),
            ("BEBEEE", 160),
            ("ABCDEABCDE", 280),
            ("FF", 20),  # buy 2, pay for 2
            ("FFF", 20),  # buy 3, pay for 2
            ("FFFF", 30),  # buy 4, pay for 3
            ("FFFFF", 40),  # buy 5, pay for 4
            ("FFFFFF", 40),  # buy 6, pay for 4
            ("FFFFFFF", 50),  # buy 7, pay for 5
            ("FFFFFFFF", 60),  # buy 8, pay for 56
            ("HHHHH", 45),
            ("HHHHHHHHHH", 80),
            ("KK", 120),
            ("NNNM", 120),
            ("PPPPP", 200),
            ("QQQ", 80),
            ("RRRQ", 150),
            ("UUU", 120),
            ("UUUU", 120),
            ("VV", 90),
            ("VVV", 130),
            ("1", 45),
            ("STX", 45),
            ("XYZ", 45),
            ("STXYZ", 82),
            ("SSSTTT", 90),
            ("SSSTTTXXXYYYZZZ", 225),
            ("SSSZ", 65),
            ("ZZZS", 65),
            ("STXS", 62)
        ],
    )
    def test_checkout_no_error(self, skus, expected):
        assert expected == CheckoutSolution().checkout(skus)

    @pytest.mark.parametrize(
        "skus, expected",
        [
            ("Ö", -1),
            (1, -1),
            ("ABCDEFÖ", -1),
        ],
    )
    def test_checkout_error(self, skus, expected):
        # unhappy path returns -1
        assert expected == CheckoutSolution().checkout(skus)

    @pytest.mark.parametrize(
        "sku",
        [
            ("ö"),
        ],
    )
    def test_validate_checkout_raises(self, sku):
        with pytest.raises(Exception):
            validate_checkout(sku)
