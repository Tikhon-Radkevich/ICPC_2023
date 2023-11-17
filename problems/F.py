import math

n, h, w = map(int, input().split())
max_time = 0

for _ in range(n):
    t, a, b, x, y = map(int, input().split())
    max_time = max(max_time, t)
    vertical_growth = math.ceil(2 * a / h)
    horizontal_growth = math.ceil(2 * b / w)
    time_to_cover = max(vertical_growth, horizontal_growth)
    max_time = max(max_time, t + time_to_cover - 1)

print(max_time)
