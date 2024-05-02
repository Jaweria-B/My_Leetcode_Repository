class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1

        # Initialize a set to keep track of seen numbers
        seen = set()

        for num in nums:
            abs_num = abs(num)

            # If the absolute value is greater than the current answer
            # and its negation was seen before,
            # update the answer
            if abs_num > ans and -num + 1024 in seen:
                ans = abs_num
            # Mark the current number as seen
            seen.add(num + 1024)

        return ans