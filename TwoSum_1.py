import pytest
from typing import List

class TwoSum:
    def __init__(self):
        self.map = {}

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if complement in self.map:
                return [self.map[complement], i]
            self.map[num] = i
        raise ValueError("No two sum solution")

# Tests
def test_two_sum_case1():
    solution = TwoSum()
    assert solution.twoSum([2,7,11,15], 9) == [0, 1]

def test_two_sum_case2():
    solution = TwoSum()
    assert solution.twoSum([3,2,4], 6) == [1, 2]

def test_two_sum_case3():
    solution = TwoSum()
    assert solution.twoSum([3,3], 6) == [0, 1]

def test_two_sum_no_solution():
    solution = TwoSum()
    with pytest.raises(ValueError):
        solution.twoSum([1,2,3], 10)

if __name__ == "__main__":
    pytest.main([__file__])