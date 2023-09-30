class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = [-1, -1]
        a[0] = self.second( nums, target, True)
        a[1] = self.second(nums, target, False)
        return a
    

    def second(self, arr, target, isStart):
        targetIndex = -1
        start , end = 0 , len(arr) -1

        while start <= end:
            middle = start + (end - start) // 2

            if arr[middle] == target:
                targetIndex = middle
                if isStart:
                    end = middle - 1
                else:
                    start = middle + 1
            elif target < arr[middle]:
                end = middle - 1
            else:
                start  = middle + 1
        return targetIndex