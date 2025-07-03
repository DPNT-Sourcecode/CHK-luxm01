from solutions.HLO.hello_solution import HelloSolution
import pytest


class TestHello:
    @pytest.mark.parametrize(
        "name",
        [
            (1),
        ],
    )
    def test_hello_raises(self, name):
        with pytest.raises(Exception):
            HelloSolution().hello(name)

    @pytest.mark.parametrize(
        "name, expected",
        [
            ("John", "Hello, John!"),
            ("Chloë", "Hello, Chloë!"),
            ("Jean-Paul", "Hello, Jean-Paul!"),
            ("5", "Hello, 5!"),
        ],
    )
    def test_hello_doesnt_raise(self, name, expected):
        assert HelloSolution().hello(name) == expected
