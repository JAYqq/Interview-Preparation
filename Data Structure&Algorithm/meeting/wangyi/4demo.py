def maxValue(self, grid: List[List[int]]) -> int:
    def bfs():
        while queue:
            cur = queue.popleft()
            if cur[0] == m-1 and cur[1] == n-1:
                self.ans = max(self.ans, cur[2])
            for item in dire:
                nd = [cur[0]+item[0], cur[1]+item[1]]
                if nd[0] < m and nd[0] >= 0 and nd[1] < n and nd[1] >= 0:
                    nd.append(cur[2]+grid[nd[0]][nd[1]])
                    queue.append(tuple(nd))
    queue = collections.deque()
    dire = [(0, 1), (1, 0)]
    self.ans = -1
    m, n = len(grid), len(grid[0])
    queue.append((0, 0, grid[0][0]))
    bfs()
    return self.ans
