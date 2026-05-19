class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        solutionMatrix = []
        
        solutionMatrix = self.moveRight(self, 0, 0, len(matrix[0]), matrix, solutionMatrix)

        return solutionMatrix
    
    def moveRight(self, index: int, start: int, end: int, matrix: list[list[int]], solutionMatrix: list[int]) -> list[int]:
        if start < end:
            for k in range(start, end):
                solutionMatrix.append(matrix[index][k])

            index += 1
        
            solutionMatrix = self.moveDown(self, end - 1, index, len(matrix) - index + 1, matrix, solutionMatrix)
        
        return solutionMatrix
    
    def moveDown(self, index: int, start: int, end: int, matrix: list[list[int]], solutionMatrix: list[int]) -> list[int]:
        if start < end:
            for k in range(start, end):
                solutionMatrix.append(matrix[k][index])

            index -= 1

            solutionMatrix = self.moveLeft(self, end - 1, index, len(matrix[0]) - index - 3, matrix, solutionMatrix)

        return solutionMatrix

    def moveLeft(self, index: int, start: int, end: int, matrix: list[list[int]], solutionMatrix: list[int]) -> list[int]:
        if start > end:
            for k in range(start, end, -1):
                solutionMatrix.append(matrix[index][k])

            index -= 1

            solutionMatrix = self.moveUp(self, end + 1, index, len(matrix) - index - 2, matrix, solutionMatrix)

        return solutionMatrix

    def moveUp(self, index: int, start: int, end: int, matrix: list[list[int]], solutionMatrix: list[int]) -> list[int]:
        if start > end:
            for k in range(start, end, -1):
                solutionMatrix.append(matrix[k][index])

            index += 1

            solutionMatrix = self.moveRight(self, end + 1, index, len(matrix[0]) - index, matrix, solutionMatrix)

        return solutionMatrix

def main():
    s = Solution
    solutionMatrix = s.spiralOrder(s, [[1,2,3],[4,5,6],[7,8,9]])

    print(solutionMatrix)

main()