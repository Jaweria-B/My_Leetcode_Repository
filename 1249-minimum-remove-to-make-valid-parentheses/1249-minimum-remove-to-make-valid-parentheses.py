class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        # Identify the indices of parentheses to remove
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Include the remaining unmatched opening parentheses in to_remove
        to_remove.update(stack)

        # Construct the valid string without the characters in to_remove
        result = ''
        for i, char in enumerate(s):
            if i not in to_remove:
                result += char

        return result

