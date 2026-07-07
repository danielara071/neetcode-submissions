# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        #reverse
        slow.next = None
        prev = None
        while second:
            nextt = second.next
            second.next = prev
            prev = second
            second = nextt
        second = prev
        curr = head
        while second:
            tmp = curr.next
            tmp2 = second.next
            curr.next = second
            second.next = tmp
            curr = tmp
            second = tmp2
        


