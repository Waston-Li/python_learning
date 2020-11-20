from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs=set()
        n=len(s)
        r,ans=-1,0
        for i in range(n):
            if i!=0:
                hs.remove(s[i-1])
            while r+1<n and s[r+1] not in hs:
                hs.add(s[r+1])
                r+=1

            ans=max(ans,r-i+1)
        return ans




a=Solution().lengthOfLongestSubstring("letter")
print(a)