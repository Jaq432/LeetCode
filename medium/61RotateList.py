#Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: [ListNode], k: int) -> [ListNode]:
    if not head:
        return head

    # Pointer for the tail
    tail = head

    # Get length of the list
    length = 0
    while tail.next:
        tail = tail.next
        length += 1

    # Tail is now at the end of the list

    # Calculate steps to rotation
    stepsToRot = k % length

    if stepsToRot == 0:
        return head

    # Move the pointer over to the rotation point
    pointer = head
    for _ in range(stepsToRot):
        pointer = pointer.next
    
    # Set the variable for the new head to be the point after the rotation
    # This will be stored so when we remove the end of the original list, we can add this to the front
    newHead = pointer.next

    # Remove the end of the list
    pointer.next = None
    # Put the end of the list onto the front
    tail.next = head

    return newHead