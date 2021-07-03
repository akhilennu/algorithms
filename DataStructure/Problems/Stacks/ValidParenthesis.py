from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c in mapping:
                if(stack):
                    if(stack.pop() != mapping[c]):
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack


obj = Solution()
a = obj.isValid("()[{]}")
print(a)
