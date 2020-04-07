def pipesGame(state):
    fail = []
    row, col = len(state), len(state[0])
    times = numpy.full((row,col), float('inf'))
    target = set()
    d = {'1':[(1,0),(-1,0)],'2':[(0,1),(0,-1)],'3':[(0,1),(1,0)],'4':[(0,-1),(1,0)],\
        '5':[(0,-1),(-1,0)],'6':[(0,1),(-1,0)],'7':[(0,1),(0,-1),(1,0),(-1,0),]}
    state = numpy.array(state)
    def valid(x,y,symbol = None):
        return  0<=x<row and 0<= y <col and ('1' <= state[x][y] <= '9' or symbol and symbol.upper() == state[x][y])

    def find(x, y, symbol):
        d[symbol] = []
        for i,j in (0,1),(1,0),(-1,0),(0,-1):
            if valid(x+i,y+j):
                for m,n in d[state[x+i][y+j]]:
                    if m + i == 0 and n+j == 0:
                        d[symbol].append((i,j))
    def dfs(m, x, y, symbol, time):
        queue = [(m, x, y, time)]
        while queue:
            m, x, y, time = queue.pop(0)
            times[x,y] = min(times[x,y],time)
            f = 0
            if state[x][y] == symbol.upper():
                target.add((x,y))
                continue
            if state[x][y] == '7':
                direction = [(0,1),(0,-1)] if m == 0 else [(1,0),(-1,0)]
            else:
                direction = d[state[x][y]]
            for i,j in direction :
                if valid(x+i,y+j,symbol) and not visited[x+i][y+j]:
                    f = 1
                    visited[x+i,y+j] = 1 if state[x+i][y+j] != symbol.upper() else 0
                    queue.append((i, x+i, y+j, time+1))
            if not f:
                fail.append([x,y])
                return 0
        return 1

    count = 0
    check = []
    for i in range(row):
        for j in range(col):
            if 'a' <= state[i][j] <= 'z':
                count += 1
                visited = numpy.zeros((row, col))
                find(i, j, state[i][j])
                if d.get(state[i][j], 0):
                    k = dfs(-1, i, j, state[i][j], 0)
                    check.append(k)
                else:
                    check.append(0)
                    times[i][j] = 0
    for x,y in target:
        times[x, y] = float('inf')
    if all(check):
        return len(times[times < float('inf')]) - count
    else:
        if not fail:
            return len(times[times < float('inf')]) - count
        max_time = min(times[x,y] for x,y in fail)
        return -len(times[times <= max_time]) + count
