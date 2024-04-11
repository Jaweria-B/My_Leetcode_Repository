class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # List to store the digits
        numStack = []
        
        # Iterating through each digit in the number
        for digit in num:
            # While there are remaining removals (k) and the stack is not empty and the current digit is smaller than the top of the stack
            while k > 0 and numStack and digit < numStack[-1]:
                # Remove digits from the stack
                numStack.pop()
                k -= 1
            # Push the current digit to the stack
            numStack.append(digit)
        
        # After iterating through the number, if there are still remaining removals, remove digits from the stack
        while k > 0 and numStack:
            numStack.pop()
            k -= 1

        # Construct the result string by popping digits from the stack
        temp = ""
        while numStack:
            temp += numStack.pop()
        # Reverse the result string to get the correct order
        temp = temp[::-1]

        # Remove leading zeros and construct the final result
        result = ""
        foundNonZero = 0
        for digit in temp:
            if digit == '0' and foundNonZero == 0:
                continue
            else:
                result += digit
                foundNonZero = 1
        # If the result is empty, return "0"
        if not result:
            result = '0'
        return result