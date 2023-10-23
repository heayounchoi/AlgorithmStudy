# 기하

# 세 막대[백준 14215]

# 삼각형의 가장 긴 변은 나머지 두 변의 합보다 클 수 없음.(a + b > c)
# 문제에서 각 막대의 길이를 마음대로 줄일 수 있음.
# 삼각형 둘레의 최대를 구하기 위해서 1만 빼주기
arr = list(map(int, input().split()))

arr.sort()
a, b, c = arr

if a + b <= c:
    c = a + b - 1

print(a + b + c)

# 터렛(1002)
# 두 원이 만나는 접점의 개수 구하기
from math import sqrt
T = int(input())

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    diff = abs(r1 - r2)

    ans = 0
    # 두 원이 일치    
    if dist == 0 and r1 == r2:
        ans = -1
    # 두 원이 외접하거나, 내접할 때
    elif dist == r1 + r2 or dist == diff:
        ans = 1
    # 두 원이 두  점에서 만날 때
    elif diff < dist < r1 + r2:
        ans = 2

    print(ans)

for _ in range(T):
    solve()