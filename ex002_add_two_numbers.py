# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def get_value_from_node(self, node: ListNode) -> int:
        if node:
            return node.val
        return 0
    
    def get_next_node(self, node: ListNode) -> ListNode:
        if node:
            return node.next
        return None
    
    def add_ints_with_carry(self, l1: int, l2: int, carry: int) -> (int, int):
        sum_of_ints = l1 + l2 + carry
        carry = 0
        
        if sum_of_ints >= 10:
            sum_of_ints %= 10
            carry = 1
        
        return sum_of_ints, carry
        
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_nodes = []
        i, j = l1, l2
        carry = 0
        
        while i or j:
            sum_of_ints, carry = self.add_ints_with_carry(
                self.get_value_from_node(i),
                self.get_value_from_node(j),
                carry
            )
            
            list_nodes.append(ListNode(sum_of_ints))
            
            i = self.get_next_node(i)
            j = self.get_next_node(j)
            
        if carry > 0:
            list_nodes.append(ListNode(counter))
        
        for i in range(1, len(list_nodes)):
            list_nodes[i - 1].next = list_nodes[i]
        
        return list_nodes[0]
