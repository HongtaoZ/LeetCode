class Solution:
    def findLength(self, A, B) -> int:
        dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        len_max = 0
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    dp[j][i] = dp[j-1][i-1]+1
                    if len_max < dp[j][i]:
                        len_max = dp[j][i]
        return len_max


if __name__ == "__main__":
    algo = Solution()
    A = [1, 5, 6]
    B = [4, 5, 6, 7]
    print(algo.findLength(A, B))
