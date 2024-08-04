class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "]":"[]", "}":"{"}

        for p in s:
            if p in closeToOpen:
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append()
        
        return True if not stack else False
    
    # T - O(n) S - O(n)