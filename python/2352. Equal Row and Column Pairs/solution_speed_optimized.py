class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Count the occurrences of rows in the grid
        row_count = Counter(tuple(row) for row in grid)
        
        n = len(grid)
        count = 0
        
        # Check columns, form them as tuples and compare with the rows
        for col in zip(*grid):
            count += row_count[tuple(col)]
        
        return count
