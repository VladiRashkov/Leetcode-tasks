from typing import List, Optional


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def pairSum(self, head: Optional[ListNode]):
        # ListNode(4) ListNode(2) ListNode(3) ListNode(3)
        second_half = self.split_linked_list(head)
        reversed_second_half = self.reverse_second_half(second_half)

        max_twin_sum = 0
        first_half = head

        while first_half and reversed_second_half:
            twin_sum = first_half.val + reversed_second_half.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            
            first_half = first_half.next
            reversed_second_half = reversed_second_half.next
        
        return max_twin_sum

    def split_linked_list(self, head:Optional[ListNode]):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        
        second_half = slow.next
        slow.next = None
        
        return second_half
    
    def reverse_second_half(self, head:Optional[ListNode]):
        prev = None
        current = head
        
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        
        
    
    
def list_to_linked_list(values: List[int]):
    if values is None:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
    

def linked_list_to_list(head: Optional[ListNode]):
    if head is None:
        return head
    
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
        
    return result

solution = Solution()
values = list_to_linked_list([4,2,2,3])
result = solution.pairSum(values)
print(result)