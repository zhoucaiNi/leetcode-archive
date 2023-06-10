# from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = [set() for _ in range(len(board) *3)]

        for x in range(len(board)):
            for y in range(len(board[0])):
                currVal = board[x][y]
                if currVal in s[x] or currVal in s[9+y] or \
                currVal in s[18+int(x/3) + 3* int(y/3)]:
                    return False
                elif board[x][y] != ".":
                    s[x].add(currVal)
                    s[y+9].add(currVal)
                    s[18+int(x/3) + 3* int(y/3)].add(currVal)
        return True
                    
                
        