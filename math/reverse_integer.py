class Solution:

    def reverse(self, x: int) -> int:

        ans = 0

        mi, mx = -(2**31), 2**31 - 1

        while x:

            y = x % 10

            if x < 0 and y > 0:
                y -= 10

            ans = ans * 10 + y
            x = (x - y) // 10

        if ans < mi or ans > mx:
            return 0

        return ans
