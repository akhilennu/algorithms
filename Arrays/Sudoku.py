from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = ['']*9
        b = ['']*9
        for i in range(9):
            r = ''
            for j in range(9):
                val = board[i][j]
                if(val != '.'):

                    tmp = (3*(i//3))+j//3

                    if(val in r or val in c[j] or val in b[tmp]):
                        return False
                    else:
                        r += val
                        c[j] += val
                        b[tmp] += val
        return True


sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
obj = Solution()
sol = obj.isValidSudoku(sudoku)
print(sol)


# for i in range(9):
#     for j in range(9):
#         print((3*int(i/3))+int(j/3), end='|')
#     print()
