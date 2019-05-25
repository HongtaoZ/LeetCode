"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisors = [1]
        i_max = num
        i = 2

        while i * i <= num and i < i_max:
            if num % i == 0:
                divisors.append(i)
                i_max = num / i
                divisors.append(i_max)
            i = i + 1

        if num == sum(set(divisors)):
            return True
        return False


if __name__ == "__main__":
    algo = Solution()
    for i in range(1, 30):
        print(i, algo.checkPerfectNumber(i))
