from typing import Any, Optional, List

from python.utilities import ListNode
import sys


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num_index = max(range(len(nums)), key=nums.__getitem__)
        max_num = nums[max_num_index]
        return (
            max_num_index if all((max_num >= x * 2 for x in nums if x != max_num))
            else -1
        )

print(Solution().dominantIndex([3,6,1,0]))