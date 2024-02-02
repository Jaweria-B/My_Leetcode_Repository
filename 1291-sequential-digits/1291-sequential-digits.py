class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        minimum = len(str(low))
        maximum = len(str(high))
        number = "123456789"

        for d_cnt in range(minimum, maximum + 1):
            for j in range(0, 9 - d_cnt + 1):
                num = number[j:j + d_cnt]
                num = int(num)
                if low <= num <= high:
                    ans.append(num)

        return ans