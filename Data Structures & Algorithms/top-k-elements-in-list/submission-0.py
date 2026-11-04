from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Το most_common επιστρέφει λίστα με tuples: [(αριθμός, συχνότητα), ...]
        return [num for num, count in Counter(nums).most_common(k)]