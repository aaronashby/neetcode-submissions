# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If head is null, return head
        # Initialize currNode to head
        # Initialize prev2 and prev to null
        # While currNode isn't null
        # - If prev isn't null, set prev.next to prev2
        # - Move currNode, prev, and prev2 up one
        # Set prev.next to prev2 once more
        # Return prev
        if not head:
            return head
        
        currNode = head
        prev2 = prev = None
        
        while currNode:
            if prev:
                prev.next = prev2
            prev2 = prev
            prev = currNode
            currNode = currNode.next
        prev.next = prev2
        return prev