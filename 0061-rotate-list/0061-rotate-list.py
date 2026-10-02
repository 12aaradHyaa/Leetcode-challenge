class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            current = current.next
            length += 1


        k = k % length

        if k == 0:
            return head

        current.next = head

        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        return new_head