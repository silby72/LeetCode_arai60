class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        old_node = head
        
        while old_node is not None:
            temp = old_node.next
            old_node.next = new_node
            new_node = old_node
            old_node = temp

        return new_node