import sys
from collections import deque
from itertools import combinations as cb
si = sys.stdin.readline


def main():
    n, m = [int(e) for e in si().split()]
    pos, board = [], []
    for i in range(n):
        row = [int(e) for e in si().split()]
        board.append(row)
        for j in range(n):
            if row[j] == 2:
                pos.append((i, j))

    def surr(x, y): return [(i, j)for i, j in (
        (x+1, y), (x-1, y), (x, y+1), (x, y-1))if n > i > -1 < j < n]

    virus, ret, flag = [i for i in range(len(pos))], 50*50+1, True
    cbs = cb(virus, m)
    for el in cbs:
        t, q, vq, mx = 0, deque(), deque(), 0
        visited = [[False for _ in range(n)]for _ in range(n)]
        cost = [[0 for _ in range(n)]for _ in range(n)]

        for e in el:
            visited[pos[e][0]][pos[e][1]] = True
            q.append(pos[e])

        def finished(n):
            nonlocal visited, board
            for i in range(n):
                for j in range(n):
                    if board[i][j] != 1 and not visited[i][j]:
                        return False
            return True

        while q:
            curr = q.popleft()
            nxts = surr(curr[0], curr[1])
            currcost = cost[curr[0]][curr[1]]
            for nxt in nxts:
                if not visited[nxt[0]][nxt[1]] and board[nxt[0]][nxt[1]] != 1:
                    visited[nxt[0]][nxt[1]] = True
                    cost[nxt[0]][nxt[1]] = 1+currcost
                    q.append(nxt)
                    if not board[nxt[0]][nxt[1]]:
                        mx = max(mx, cost[nxt[0]][nxt[1]])

        if not finished(n):
            flag = True and flag
        else:
            flag = False
            ret = min(ret, mx)
    if flag:
        print(-1)
    else:
        print(ret)


if __name__ == '__main__':
    main()
