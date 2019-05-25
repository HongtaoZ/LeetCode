# Time:  O(n^2)
# Space: O(n^2)


class Solution(object):
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # if the string is empty or just 1 charater, then return 0 directly.
        if len(s) == 0 or len(s) == 1:
            return 0
        # lookup[i][j] indicate if s[i:j] is a palindrome
        lookup = [[False for j in range(len(s))] for i in range(len(s))]
        # generate a list which contains how many splits needed for mincut[i:]
        mincut = [len(s) - 1 - i for i in range(len(s) + 1)]

        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)
        return mincut[0]


if __name__ == "__main__":
    sol = Solution()
    print("abc,return=", sol.minCut("abba"))  # 2
    print("a,return=", sol.minCut("a"))  # 0
    print("abb,return=", sol.minCut("abb"))  # 1
    print("aaabaa,return=", sol.minCut("aaaabaac"))  # 2
