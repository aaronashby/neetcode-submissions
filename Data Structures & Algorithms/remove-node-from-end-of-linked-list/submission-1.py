# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Do one pass to find length of list
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        # Do another pass to get nth node from the end and set prev's next to curr's next
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        for i in range(length - n):
            curr = curr.next
            prev = prev.next
        prev.next = curr.next
        # Return dummy.next
        return dummy.next