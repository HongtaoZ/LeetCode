

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - 1 - j][i]
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = temp

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])
        print()


if __name__ == "__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r = Solution()
    r.printMatrix(input)
    r.rotate(input)
    r.printMatrix(input)
