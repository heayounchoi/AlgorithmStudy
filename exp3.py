# 소수 구하기

# 소수 구하기 1
num = int(input())

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 

if is_prime(num):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
    
N = int(input())
result = 0
for i in range(2, N + 1):
    if is_prime(i):
        result += 1

print(f'2부터 {N} 까지 소수는 총 {result}개 있습니다.')

# 소수 구하기2
# 숫자 N이 소수가 아니라면, N=a*b 형태로 나타낼 수 있음. 여기서 a와 b는 1과 N을 제외한 약수들. 
# a가 N의 제곱근보다 작거나 같다면, b는 제곱근보다 큼. 반대로 a가 N의 제곱근보다 크다면, b는 제곱근보다 작음.
# 따라서 N이 소수인지 아닌지 판별하기 위해, N의 제곱근까지만 약수가 있는지 확인하면 됨.
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False 
    return True 

num = 1000000
result = 0
for i in range(2, num):
    if is_prime(i):
        result += 1

print(f'2부터 {num} 까지 소수는 총 {result}개 있습니다.')
