def generate_pilobor_array(n, k):
    if k > (n - 1) * (n - 2) // 2:
        return [-1]  # No solution exists

    array = [0] * n
    for i in range(n):
        array[i] = i + 1

    if k == 0:
        return array

    diff = k
    idx = n - 1

    while diff > 0:
        if diff >= idx:
            array[idx], array[idx - 1] = array[idx - 1], array[idx]
            diff -= idx
        else:
            break
        idx -= 1

    return array

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = generate_pilobor_array(n, k)
    if result[0] == -1:
        print(-1)
    else:
        print(*result)
