ans = 0
def dfs(t):
    global ans
    if t is None: return
    if t.left and t.left.left is None and t.left.right is None:
        ans += t.left.value
    dfs(t.left)
    dfs(t.right)
        
def leftLeavesSum(t):
    global ans
    ans = 0
    dfs(t)
    return ans
