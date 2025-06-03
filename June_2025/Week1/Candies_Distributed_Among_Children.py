
class DistributeCandiesAmongChildrenII:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit) + 1):
            rem = n - i
            if rem > 2 * limit:
                continue
            lower = max(rem - limit, 0)
            upper = min(limit, rem)
            ans += (upper - lower + 1)
        return ans

# Example usage
if __name__ == "__main__":
    solution = DistributeCandiesAmongChildrenII()
    print(solution.distributeCandies(5, 2))
