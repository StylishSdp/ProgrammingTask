class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        n = len(digits)

        def bfs(s, step):
            if step == n:
                res.append(s)
                return

            for i in alpha[digits[step]]:
                bfs(s + i, step + 1)

        bfs('', 0)
        return res