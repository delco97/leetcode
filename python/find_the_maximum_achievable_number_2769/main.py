import math
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

def test_1():
    assert Solution().theMaximumAchievableX(4, 1) == 6

def test_1():
    assert Solution().theMaximumAchievableX(3, 2) == 7