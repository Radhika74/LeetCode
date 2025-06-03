from collections import deque

class MaximumCandiesYouCanGetFromBoxes:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        visited = [False] * n
        locked_boxes = set()
        processing = deque()
        
        for box in initialBoxes:
            if status[box] == 1:
                visited[box] = True
                processing.append(box)
            else:
                locked_boxes.add(box)
        
        res = 0
        
        while processing:
            curr = processing.pop()
            res += candies[curr]
            
            for key in keys[curr]:
                status[key] = 1
                if key in locked_boxes:
                    visited[key] = True
                    locked_boxes.remove(key)
                    processing.append(key)
            
            for box in containedBoxes[curr]:
                if visited[box]:
                    continue
                if status[box] == 1:
                    visited[box] = True
                    processing.append(box)
                else:
                    locked_boxes.add(box)
        
        return res


# Example usage:
if __name__ == "__main__":
    solution = MaximumCandiesYouCanGetFromBoxes()
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 16
