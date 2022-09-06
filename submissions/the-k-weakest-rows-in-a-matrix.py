class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        # Get the indexes of all rows in the matrix
        rows = list(range(len(mat)))
        
        # Evaluate the strength of each row
        evaluations = dict()
        for i in rows:
            row = mat[i]
            # Count the number of soldiers in the row
            soldiers = 0
            for element in row:
                if element == 1:
                    soldiers += 1
                else:
                    break
            evaluations[i] = (soldiers, i)
            
        print(evaluations)
            
        # Sort the rows using selection sort
        for i in range(len(rows)):
            smallest = i
            # Find the index of the smallest element between i and the last item
            for j in range(i, len(rows)):
                if evaluations[rows[j]] < evaluations[rows[smallest]]:
                    smallest = j
            # Swap the smallest element into place
            rows[i], rows[smallest] = rows[smallest], rows[i]
                
        # Select the first k rows
        output = rows[:k]
        
        return output
                    
