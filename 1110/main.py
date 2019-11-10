'''
https://leetcode-cn.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left = 0
        right = len(height) - 1
        res = 0
        # 记录左右边最大值
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1 
        return res