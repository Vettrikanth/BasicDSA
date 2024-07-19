# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.
# Example 1:
# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

# Example 2:
# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.

from collections import Counter
from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        e=[i for i in nums if i % 2 == 0]
        e.sort()
        if not e:
            return -1
        s=Counter(e)
        max_count=max(s.values())
        print("max value=",max_count)
        for key,val in s.items():
            if (val>=max_count):
                return key
        
        return -1

s=Solution()
ans=s.mostFrequentEven([2,10000,10000,10000,2])
ans1=s.mostFrequentEven([0,1,2,2,4,4,1])
ans2=s.mostFrequentEven([29,47,21,41,13,37,25,7])
ans3=s.mostFrequentEven([1000])
print()
print("ans=",ans)
print("ans1=",ans1)
print("ans2=",ans2)
print("ans3=",ans3)



