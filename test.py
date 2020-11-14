from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cm = max(arr1)
        cnt = [0] * (cm+1)
        res = []

        for i in arr1:
            cnt[i] += 1

        for i in arr2:
            res.extend([i] * cnt[i])
            cnt[i] = 0

        for i in range(cm):
            if (cnt[i] > 0):
                res.append(i)
        print(res)


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
result=Solution().relativeSortArray(arr1,arr2)
