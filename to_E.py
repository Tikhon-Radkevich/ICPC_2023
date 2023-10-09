memo = {}


def find_hash(m, n):
    if m < 0:
        return 0
    elif n == 0:
        r = 0
        if m == 0:
            r += 1
        return r
    else:
        n -= 20
        m += 23
        s = memo.get((m, n), None)
        if s is None:
            s = find_hash(m, n)
            memo[(m, n)] = s
        m -= 46
        t = memo.get((m, n), None)
        if t is None:
            t = find_hash(m, n)
            memo[(m, n)] = t
        s += t
        m += 23
        n += 20
        if s >= 81023:
            s -= 81023
        return s


x = 125

print(find_hash(0, 40 * x + 40))
