# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        dummy = ListNode(0)
        pointer = head
        second_pointer = dummy

        if pointer == None:
            return None

        while pointer is not None:
            stack.append(pointer.val)
            pointer = pointer.next

        for i in range(len(stack)):
            second_pointer.next = ListNode(stack.pop())
            second_pointer = second_pointer.next

        return dummy.next