# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_head = ListNode(0)
        carry = 0
        current = node_head
        
        while l1 or l2 or carry:
            sum_of_ints = l1.val + carry if l1 else carry
            sum_of_ints += l2.val if l2 else 0
            
            #If x and y are integers, the return value from divmod() is same as (a // b, x % y)
            carry, sum_of_ints = divmod(sum_of_ints, 10)
            current.next = ListNode(sum_of_ints)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return node_head.next
