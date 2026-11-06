class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Προσπερνάμε μη αλφαριθμητικούς χαρακτήρες από αριστερά
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Προσπερνάμε μη αλφαριθμητικούς χαρακτήρες από δεξιά
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # Σύγκριση χαρακτήρων (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1

        return True

    # Custom συνάρτηση ελέγχου μέσω ASCII (όπως την κάνει ο NeetCode)
    def alphaNum(self, c: str) -> bool:
        return (
            ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9')
        )