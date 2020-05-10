def maximalAllowableSubarrays(a, maxSum):
    n = len(a)
    right_sum = a[n-1]
    right_index = n - 1
    ans = []
    ans.append(right_index)
    for j in range(n-2, -1, -1):
        right_sum += a[j]
        while right_sum > maxSum:
            right_sum -= a[right_index]
            right_index -= 1
        ans.append(right_index)
    return ans[::-1]
