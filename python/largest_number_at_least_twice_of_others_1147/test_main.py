from .main import Solution

def test_1():
    """
    Input: nums = [3,6,1,0]
    Output: 1
    Explanation: 6 is the largest integer.
    For every other number in the array x, 6 is at least twice as big as x.
    The index of value 6 is 1, so we return 1.
    """
    assert Solution().dominantIndex(
        [3,6,1,0]
    ) == 1

def test_2():
    """
    Input: nums = [1,2,3,4]
    Output: -1
    Explanation: 4 is less than twice the value of 3, so we return -1.
    """
    assert Solution().dominantIndex(
        [1,2,3,4]
    ) == -1