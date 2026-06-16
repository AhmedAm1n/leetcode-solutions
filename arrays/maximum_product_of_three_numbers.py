# Problem: Maximum Product of Three Numbers
# Difficulty: Easy

from heapq import nlargest, nsmallest
from typing import List

class Solution:

    def productOfThreeNumbers(self, nums: List[int]) -> int:
        top3 = nlargest(3,nums)   
        bottom2 = nsmallest(2,nums)
        return max(top3[0] * top3[1] * top3[2], top3[0] * bottom2[0] * bottom2[1])
