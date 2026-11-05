class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Φτιάχνουμε μια λίστα με 1, ίση σε μέγεθος με το nums.
        res = [1] * len(nums)
        
        # 1ο Πέρασμα: Από αριστερά προς τα δεξιά
        prefix = 1
        for i in range(len(nums)):
            # Πρώτα αποθηκεύουμε το προηγούμενο γινόμενο
            res[i] = prefix
            # Μετά ενημερώνουμε το prefix για τον επόμενο αριθμό
            prefix *= nums[i]
            
        # 2ο Πέρασμα: Από δεξιά προς τα αριστερά
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Ξεκινάμε από το τέλος, πάμε μέχρι το 0, με βήμα -1
            # Πολλαπλασιάζουμε αυτό που ήδη είχε το res με το postfix
            res[i] *= postfix
            # Ενημερώνουμε το postfix για τον επόμενο (προς τα αριστερά) αριθμό
            postfix *= nums[i]
            
        return res