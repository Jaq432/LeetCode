# Definition for singly-linked list. 
class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            addTwoAndCarry = val1 + val2 + carry
            carry = addTwoAndCarry // 10
            value = addTwoAndCarry % 10

            current.next = ListNode(value)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


class Solution:
    def addTwoNumbers(self, l1, l2):

        # Dummy node acts as the starting point of our result list.
        # This simplifies logic so we don't need special handling
        # for the head of the result list.
        dummy = ListNode(0)

        # 'current' will move along the result list as we build it.
        current = dummy

        # carry stores the value that needs to be carried over
        # when a digit sum exceeds 9.
        carry = 0

        # Continue looping while:
        # - l1 still has nodes
        # - OR l2 still has nodes
        # - OR we still have a carry value left
        while l1 or l2 or carry:

            # If l1 exists, take its value, otherwise use 0
            v1 = l1.val if l1 else 0
            # If l2 exists, take its value, otherwise use 0
            v2 = l2.val if l2 else 0

            # Add both digits plus the carry from the previous step
            total = v1 + v2 + carry

            # Compute the new carry (anything above 9)
            # gets the 10s place
            carry = total // 10

            # The digit to store in the node is the ones-place
            digit = total % 10

            # Create a new node with this digit and attach it
            # to the result list
            current.next = ListNode(digit)
            # Move the current pointer forward
            current = current.next

            # Move l1 forward if possible
            if l1:
                l1 = l1.next

            # Move l2 forward if possible
            if l2:
                l2 = l2.next

        # dummy.next points to the actual start of the result list
        return dummy.next
    
