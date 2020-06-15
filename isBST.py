f = lambda t: t and  f(t.left) + [t.value] + f(t.right) or []
isBST = lambda t: sorted({*f(t)}) == f(t)
