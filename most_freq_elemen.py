# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array

from collections import Counter
from typing import List

class Solution:
    def findmostfrq(self,nums:List[int])->int:
        s=Counter(nums)
        l=len(nums)
        for key,value in s.items():
            if (value>l//2):
                return key


s=Solution()
a1=s.findmostfrq([2,2,1,1,1,2,2])
a2=s.findmostfrq([3,2,3])
a3=s.findmostfrq([100,45,100,100,9,6,45])
a4=s.findmostfrq([100,45,100,100,9,6,45,100,100,100])
print(a1)
print(a2)
print(a3)
print(a4)