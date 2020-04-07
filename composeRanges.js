function composeRanges(nums) {
    let res = []
    for (n of nums.sort((a, b) => a - b)) {
        if (!res.length) {
            res.push([n, n]);
        } else {
            let top = res[res.length - 1];
            if (top[1] === n - 1) {
                top[1] = n;
            } else {
                res.push([n, n]);
            }
        }
    }
    return res.map(r => r[0] === r[1] ? "" + r[0] : r.join('->'));
}
