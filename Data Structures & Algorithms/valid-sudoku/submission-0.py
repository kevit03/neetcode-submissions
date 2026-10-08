class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # multidmensional array of strays 
        # check for duplicates (dictionary) in a row, column, 3x3 box 
        # floor divison 

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for m in range(0, 9): 
            for n in range(0, 9): 

                v = board[m][n] 
                if v == ".": 
                    continue 
                elif v in rows[m] or v in cols[n] or v in boxes[(m // 3, n // 3)]:                return False
                else: 
                    rows[m].add(v)
                    cols[n].add(v)
                    boxes[(m // 3,n // 3)].add(v)
        return True 

                

        


