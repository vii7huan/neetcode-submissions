# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        #reverse 2nd half
        second = slow.next
        slow.next = None
        pre = None
        while second:
            nxt = second.next
            second.next = pre
            pre,second = second,nxt
        
        #merge
        first, second = head, pre
        while second:
            t1,t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1,t2
