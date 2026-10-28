class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        value = ["1","2","3","4","5","6","7","8","9","."]
        for j in range(len(board)):
            check_list=set()
            if len(board) != 9:
                return False
            for n in range(len(board[j])):
                if len(board[j]) != 9:
                    return False 
                else:
                    if board[j][n] not in value:
                        return False
                    if board[j][n] in check_list:
                        return False
                    if board[j][n] not in check_list:
                        if board[j][n] != ".":
                            check_list.add(board[j][n])
                        
        for n in range(9):
            check_list = set()
            for j in range(len(board)):
                if board[j][n] in check_list:
                    return False
                if board[j][n] not in check_list:
                    if board[j][n] != ".":
                        check_list.add(board[j][n])
            



        for j in range(0,len(board),3):
            for n in range(0,len(board[j]),3):
                check_list=set()
                for side in range(3):
                    for side2 in range(3):

                        if board[j+side][n+side2] in check_list:
                            return False
                        else:
                            if board[j+side][n+side2] != ".":
                                check_list.add(board[j+side][n+side2])

        return True

                
