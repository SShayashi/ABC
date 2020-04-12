from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = {}
        prev, now = head, head.next
        d[prev.val] = 1
        while now:
            if d.get(now.val, "no") == "no":
                d[now.val] = 1
                prev = now
                now = now.next
                continue
            else:
                # 既にあるのでリンクから外す
                prev.next = now.next
                now = now.next
        return head
