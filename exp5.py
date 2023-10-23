# 유클리드 호제법

# 최대 공약수 구하기
# map을 통해 여러 숫자 입력 받기. 
a, b = map(int, input().split())
# a와 b 중 작은 숫자로 시작하기
n = a if a < b else b

# n부터 1까지 반복
for i in range(n, 0, -1):
    # a와 b가 동시에 나누어떨어지는 첫 번째 수가 최대 공약수
    if a % i == 0 and b % i == 0:
        print(i)
        # 최대 공약수를 구했기 때문에 빠져나옴
        break
    
# 유클리드 호제법
# 두 정수 a와 b(a>b)의 최대공약수는 b와 a mod b의 최대공약수와 같음.
a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

print(gcd(a, b))