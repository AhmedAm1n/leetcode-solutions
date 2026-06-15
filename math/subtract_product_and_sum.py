# Problem: Subtract the Product and Sum of Digits of an Integer
# Difficulty: Easy

class Solution:
    def subtractProductAndSum(self, n:int) -> int:
        product,total = 1,0
        while n:
            n,v = divmod(n,10)
            product *= v
            total += v
        return product - total
