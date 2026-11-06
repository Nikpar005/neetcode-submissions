from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        # Κάνουμε iterate στο numSet (όχι στο nums) για να αποφύγουμε διπλότυπα!
        for n in numSet:
            # Ελέγχουμε αν το n είναι η αρχή μιας ακολουθίας
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest