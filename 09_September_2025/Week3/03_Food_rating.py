import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2c = {}
        self.f2r = {}
        self.c2h = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.f2c[f] = c
            self.f2r[f] = r
            if c not in self.c2h:
                self.c2h[c] = []
            heapq.heappush(self.c2h[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.f2c[food]
        self.f2r[food] = newRating
        heapq.heappush(self.c2h[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        h = self.c2h[cuisine]
        while h:
            r, f = h[0]
            if -r == self.f2r[f]:
                return f
            heapq.heappop(h)
        return ""
        