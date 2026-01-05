class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        neg_count = 0
        mini = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total_sum += abs(matrix[i][j])

                if matrix[i][j] < 0:
                    neg_count += 1
                
                mini = min(mini, abs(matrix[i][j]))
            
        if neg_count%2 == 1:
            total_sum -= 2*mini
        
        return total_sum