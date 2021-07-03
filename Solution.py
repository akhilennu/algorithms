from typing import List

# To be used when solving problems on LC


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0
        while(i < j):
            t1 = (j-i)*min(height[i], height[j])
            print(height[i], height[j])
            print(i, j, height[i+1], height[j-1], area, t1)
            if(height[i+1] > height[j-1]):
                i += 1
            else:
                j -= 1

            area = max(area, t1)
        return area


# "".split(sep=' ', maxsplit=1)
obj = Solution()
a = obj.maxArea([1, 3, 2, 5, 25, 24, 5])
print(a)
