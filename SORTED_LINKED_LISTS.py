# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList():
    def __init__(self):
        self._head = None
        

    def add_sorted(self, val):
        new_node = ListNode(val)
        current = self._head
      
        if self._head is None or self._head.val >= val:
            new_node.next = self._head
            self._head = new_node
        
        else:
            while current.next is not None and self._head.val < val:
                current = current.next
            new_node.next = current.next
            current.next = new_node
                
        
      
    def values(self):
        values = []
        
        if self._head is None:
            raise ValueError('Empty')
        
        current = self._head
        
        while current is not None:
            values.append(current.val)
            current = current.next
        return values
            

list1 = [1,2,4]
list2 = [1,3,4]

linked_list = LinkedList()

for i in list1 + list2:
    linked_list.add_sorted(i)
    
print(linked_list.values())