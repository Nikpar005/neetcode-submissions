from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # Κλειδί: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Αγνοούμε τα κενά κελιά
                if val == ".":
                    continue
                
                # Αν ο αριθμός υπάρχει ήδη στη γραμμή, στήλη ή στο 3x3 κουτί -> Άκυρο
                if (
                    val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]
                ):
                    return False
                
                # Καταχώρηση του αριθμού στα αντίστοιχα sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True