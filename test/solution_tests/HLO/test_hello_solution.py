from solutions.HLO.hello_solution import HelloSolution
import pytest

class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("Matt") == "Hello, Matt!"
    
    def test_hello_raises(self):
        with pytest.raises(Exception):
            HelloSolution().hello(1)

    @pytest.mark.parametrize("input, expected",
        [
            ("Chloë", "Hello, Chloë!"),
            ("Jean-Paul", "Hello, Jean-Paul!"),
            (5, "Hello, 5"),
        ]

    )
    def test_hello_doesnt_raise(self, input, expected):
        assert HelloSolution().hello(input) == expected


