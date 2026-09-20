class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        n = len(B)

        left = 0
        right = m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else A[partitionA - 1]
            minRightA = float('inf') if partitionA == m else A[partitionA]

            maxLeftB = float('-inf') if partitionB == 0 else B[partitionB - 1]
            minRightB = float('inf') if partitionB == n else B[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:

                if (m + n) % 2 == 1:
                    return max(maxLeftA, maxLeftB)

                return (
                    max(maxLeftA, maxLeftB) +
                    min(minRightA, minRightB)
                ) / 2

            elif maxLeftA > minRightB:
                right = partitionA - 1

            else:
                left = partitionA + 1
                