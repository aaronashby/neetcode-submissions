"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # initialize hash map containing (original node -> copied node) pairs
        # go through original list and add (original node -> new list node) to map
        # go through list again
        # - each copied node's next = map[head.next]
        # - each copied node's random = map[head.random]
        # return dummy.next
        copies = {}
        copies[None] = None
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        dummy = Node(0, copies[head])
        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next
        return dummy.next