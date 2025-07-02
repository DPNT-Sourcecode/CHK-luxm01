from solutions.HLO.hello_solution import HelloSolution
import pytest

class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("Matt") == "Hello, Matt!"
    
    def test_hello_raises(self):
        with pytest.raises(Exception):
            HelloSolution().hello(1)
