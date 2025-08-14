from typing import Any, Optional

from python.utilities import ListNode
import sys


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        res = ListNode(0, None)
        res_current = res
        while current:
            if current.val == 0 and current.next:
                res_current.next = ListNode(0, None)
                res_current = res_current.next
            else:
                res_current.val += current.val
            current = current.next
        return res

print(Solution().mergeNodes(None))  # None