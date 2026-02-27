class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # flag=True
        # for i in range(9):
        #     for j in range(9):
        #         if flag==False:
        #             break
        #         if board[i][j]!='.':
        #             curr_num=board[i][j]
        #             row=board[0:9][i] # get horizontal row
        #             col = [row[j] for row in board] # get vertical column
                    
        #             i_th=(i//3)*3
        #             j_th=(j//3)*3
        #             # print(i_th)
        #             # print(j_th)
        #             small_board= [row1[j_th:j_th+3] for row1 in board[i_th:i_th+3]]

        #             row_count=row.count(curr_num) # count instance in row
        #             col_count=col.count(curr_num) # count instance in column
        #             flattened_board = [item for sublist in small_board for item in sublist]
        #             small_count = flattened_board.count(curr_num)

        #             #small_count= small_board.count(curr_num)
        #             if row_count>1 or col_count>1 or small_count>1:
        #                 flag=False
                    
        # return flag
        
        rows = set()
        cols = set()
        boxes = set()
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == ".":
                    continue
                
                # Create unique keys
                row_key = (r, num)
                col_key = (c, num)
                box_key = (r // 3, c // 3, num)
                
                # Check duplicates
                if row_key in rows or col_key in cols or box_key in boxes:
                    return False
                
                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)
        
        return True