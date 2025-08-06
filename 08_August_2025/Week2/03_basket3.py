class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced_fruits = 0  
        basket_occupied = [False] * n 
        
        for i in range(n):  
            fruit_placed = False  
            
            for j in range(n): 
                if not basket_occupied[j] and baskets[j] >= fruits[i]:
                    basket_occupied[j] = True 
                    fruit_placed = True
                    break  
            
            if not fruit_placed:
                unplaced_fruits += 1 
                
        return unplaced_fruits
