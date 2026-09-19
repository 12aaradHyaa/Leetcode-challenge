class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values and carry
            total = val1 + val2 + carry

            # New digit
            carry = total // 10
            digit = total % 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move ahead
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next