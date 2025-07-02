from solutions.SUM.sum_solution import SumSolution
import pytest

class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum_raises(self):
        with pytest.raises(Exception) as e:
            SumSolution().compute(101, -1)

