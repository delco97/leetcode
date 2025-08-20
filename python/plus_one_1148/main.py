from typing import Any, Optional, List

from python.utilities import ListNode
import sys

def plusOne(digits: List[int]) -> List[int]:
    num = sum(
        (x * (10 ** (len(digits) - 1 - idx))
        for idx, x in enumerate(digits)),
        0
    )
    return [int(x) for x in str(num + 1)]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return plusOne(digits)