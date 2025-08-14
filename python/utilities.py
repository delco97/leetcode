from typing import Any


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

def to_list(head: ListNode | None) -> list[Any]:
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next
    return res