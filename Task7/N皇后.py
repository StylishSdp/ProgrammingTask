def totalNQueens(n):
    def solve(answer, n, i):
        if i == n:
            res.append(answer)
            return

        for j in range(n):
            if j in cols or i + j in pie or i - j + n in na:
                continue

            cols.append(j)
            pie.append(i + j)
            na.append(i - j + n)

            answer[i] = j
            solve(answer, n, i + 1)

            cols.pop()
            pie.pop()
            na.pop()


    cols = []
    pie = []
    na = []
    res = []
    solve([0] * n, n, 0)
    return len(res)

print(totalNQueens(4))


