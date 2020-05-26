# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        front_ptr = back_ptr = head
        prev = None
        
        # Take front_ptr n steps ahead of back_ptr
        for _ in range(n-1):
            front_ptr = front_ptr.next
            if not front_ptr:
                # Length of list is less than n
                return None
        
        
        while front_ptr.next is not None:
            prev = back_ptr
            front_ptr = front_ptr.next
            back_ptr = back_ptr.next

        if prev:
            prev.next = back_ptr.next
        else:
            # the node to remove was the head
            return head.next

        return head


example = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()

result = s.removeNthFromEnd(example, 2)
list_str = ''
while result is not None:
    list_str += str(result.val)
    list_str += '->'
    result = result.next

list_str += 'None'
print(list_str)
        