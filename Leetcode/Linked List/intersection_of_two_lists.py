# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

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
    ## Brute Force
    def _getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_ptr = headA
        

        while a_ptr is not None:
            b_ptr = headB
            while b_ptr is not None:
                if b_ptr is a_ptr:
                    return b_ptr
                b_ptr = b_ptr.next
            a_ptr = a_ptr.next

        return None

    
    ## Hash set
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen_nodes = set()
        a_ptr = headA
        b_ptr = headB

        while a_ptr is not None:
            seen_nodes.add(a_ptr)
            a_ptr = a_ptr.next

        while b_ptr is not None:
            if b_ptr in seen_nodes:
                return b_ptr
            b_ptr = b_ptr.next
            
        return None

inter = ListNode(8)
inter.next = ListNode(4)
inter.next.next = ListNode(5)

a = ListNode(4)
a.next = ListNode(1)
a.next.next = inter

b = ListNode(5)
b.next = ListNode(0)
b.next.next = ListNode(1)
b.next.next.next = inter

res = Solution().getIntersectionNode(a, b)
print(ListNode.to_str(res))