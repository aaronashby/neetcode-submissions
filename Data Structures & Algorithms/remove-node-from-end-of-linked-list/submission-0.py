# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node
        # Initialize left pointer to dummy node
        # Initialize right pointer to be n + 1 nodes away from left (because we want the node before the one to delete)
        # Move both up until right reaches the end, update left's next to right's prev
        # Return dummy.next
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        for i in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next