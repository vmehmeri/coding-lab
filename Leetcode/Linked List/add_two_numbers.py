# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ptr = l1
        l2_ptr = l2
        sum_head = ListNode(None)
        sum_ptr = sum_head

        carry = 0
        while l1_ptr is not None or l2_ptr is not None:
            if l1_ptr is None:
                current_sum = l2_ptr.val + carry
            elif l2_ptr is None:
                current_sum = l1_ptr.val + carry
            else: 
                current_sum = l1_ptr.val + l2_ptr.val + carry

            if current_sum > 9:
                carry = 1
                current_sum = current_sum % 10
            else:
                carry = 0

            sum_ptr.next = ListNode(current_sum)
            
            if l1_ptr is not None:
                l1_ptr = l1_ptr.next
            if l2_ptr is not None:
                l2_ptr = l2_ptr.next
            sum_ptr = sum_ptr.next


        if carry != 0:
            sum_ptr.next = ListNode(carry)

        return sum_head.next

s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(ListNode.to_str(s.addTwoNumbers(l1, l2)))