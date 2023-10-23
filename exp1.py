# 1부터 n까지의 합계 구하기

# for 문으로 합계 구하기
n = int(input())

result = 0
for i in range(1, n + 1):
    result += i

print(result)

# while 문 사용하기
N = int(input())

cnt = 1
my_sum = 0
while cnt <= N:
    my_sum += cnt
    cnt += 1

print(my_sum)

# 내장 함수 사용하기
N = int(input())

my_sum = sum(range(1, N+1))

print(my_sum)

# 수열의 합 구하는 공식으로 구하기
# 앞에서의 반복문에서는 모든 숫자를 하나하나 계산하기 때문에 10만 개의 데이터라면 10만 개의 덧셈이 필요하지만, 
# 수열의 합을 구하는 공식을 사용하면 더하기 한 번, 곱하기 한 번, 나누기 한 번으로 값을 구할 수 있음
n = int(input())

result = (1 + n) * n / 2
print(result)