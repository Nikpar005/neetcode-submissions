class Solution:
    def trap(self, height: list[int]) -> int:
        # Αν δεν υπάρχουν τούβλα, δεν μαζεύεται νερό
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0
        
        while l < r:
            # Μετακινούμε τον δείκτη που έχει τον μικρότερο "μέγιστο τοίχο"
            if leftMax < rightMax:
                l += 1
                # Ενημερώνουμε τον ψηλότερο τοίχο που έχουμε δει από αριστερά
                leftMax = max(leftMax, height[l])
                # Προσθέτουμε το νερό που παγιδεύεται σε αυτή τη θέση
                water += leftMax - height[l]
            else:
                r -= 1
                # Ενημερώνουμε τον ψηλότερο τοίχο που έχουμε δει από δεξιά
                rightMax = max(rightMax, height[r])
                # Προσθέτουμε το νερό που παγιδεύεται
                water += rightMax - height[r]
                
        return water