# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
- The relative order inside both the even and odd groups should remain as it was in the input.
- The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @staticmethod
    def to_str(list_head):
        if list_head is None or list_head.val is None:
            return "(empty)"
        _str = f"{list_head.val}"

        list_node = list_head
        while list_node.next is not None:
            _str += f" -> {list_node.next.val}"
            list_node = list_node.next
        return _str

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        
        odd_ptr = odd_head
        even_ptr = even_head

        while odd_ptr.next is not None and even_ptr.next is not None:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next

            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next

       
        odd_ptr.next = even_head

        return odd_head

list_head = ListNode(1)
liptr = list_head
for i in range(2, 9):
    liptr.next = ListNode(i)
    liptr = liptr.next 

res = Solution().oddEvenList(list_head)
print(ListNode.to_str(res))

list_head_2 = ListNode(2)
liptr = list_head_2
for j in [1,3,5,6,4,7]:
    liptr.next = ListNode(j)
    liptr = liptr.next 

res = Solution().oddEvenList(list_head_2)
print(ListNode.to_str(res))