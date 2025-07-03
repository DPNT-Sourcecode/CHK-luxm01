from solutions.HLO.hello_solution import HelloSolution
import pytest


class TestHello:
    def test_hello(self):
        assert HelloSolution().hello("Matt") == "Hello, World!"

    @pytest.mark.parametrize(
        "input",
        [
            (1),
        ],
    )
    def test_hello_raises(self, input):
        with pytest.raises(Exception):
            HelloSolution().hello(input)

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("Chloë", "Hello, World!"),
            ("Jean-Paul", "Hello, World!"),
            ("5", "Hello, World!"),
        ],
    )
    def test_hello_doesnt_raise(self, input, expected):
        assert HelloSolution().hello(input) == expected



