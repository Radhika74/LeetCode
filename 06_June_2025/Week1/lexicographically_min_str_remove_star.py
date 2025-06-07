class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        is_removed = [False] * n
        char_indices = [[] for _ in range(26)]

        for i in range(n):
            if s[i] == '*':
                for j in range(26):
                    if char_indices[j]:
                        last_idx = char_indices[j].pop()
                        is_removed[last_idx] = True
                        break
            else:
                # Track index of the current character
                char_indices[ord(s[i]) - ord('a')].append(i)

        result = []
        for i in range(n):
            if s[i] != '*' and not is_removed[i]:
                result.append(s[i])

        return ''.join(result)