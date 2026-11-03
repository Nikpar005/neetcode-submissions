class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                # Αντί για leftMax = max(leftMax, height[l])
                if height[l] >= leftMax:
                    leftMax = height[l]  # Νέο ρεκόρ τοίχου, άρα δεν μαζεύει νερό
                else:
                    water += leftMax - height[l] # Παγιδεύει νερό
            else:
                r -= 1
                # Αντί για rightMax = max(rightMax, height[r])
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    water += rightMax - height[r]
                    
        return water