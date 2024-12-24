from typing import Any, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_nodes(values: list[Any]) -> ListNode:
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def to_list(head: Optional[ListNode]) -> list[Any]:
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next
    return res

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

def test_1():
    assert to_list(Solution().mergeNodes(build_nodes(
        [0,3,1,0,4,5,2,0]
    ))) == [4,11]

def test_2():
    assert to_list(Solution().mergeNodes(build_nodes(
        [0,1,0,3,0,2,2,0]
    ))) == [1,3,4] 