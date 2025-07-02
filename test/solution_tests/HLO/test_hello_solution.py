from solutions.HLO.hello_solution import HelloSolution
import pytest

class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("Matt") == "Hello, Matt!"