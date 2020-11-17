# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(L1, L2, i):
            if not L1 and not L2 and not i: return None

            s = (L1.val if L1 else 0) + (L2.val if L2 else 0) + i

            p = ListNode(s % 10)

            p.next = dfs(L1.next if L1 else 0, L2.next if L2 else 0, s // 10)

            return p

        return dfs(l1, l2, 0)


