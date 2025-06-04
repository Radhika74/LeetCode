class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        res = ""
        length = len(word) - numFriends+1
        for i in range(0, len(word)):
            temp =word[i:i+length]
            if temp > res :
                res = temp
        return res
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.answerString("abacaba", 3))  # Output: "cab"
    print(solution.answerString("abcde", 2))    # Output: "cde"
    print(solution.answerString("aaaaa", 5))    # Output: "a"