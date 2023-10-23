# 에라토스테네스의 체
num = 1000000
prime = [True] * (num + 1) # 처음엔 모두 소수로 초기화합니다.

prime[0], prime[1] = False, False # 2부터 시작하기 때문에 0, 1은 소수가 아닙니다.
for i in range(2, num + 1): # 2부터 백만까지 반복합니다.
    if prime[i]: # prime[i]가 True이면 소수입니다.
        for j in range(i * 2, num+1, i): # i * 2부터 i의 배수를 순회합니다.
            prime[j] = False # i의 배수는 모두 소수가 아닙니다.
            
result = 0
for i in range(num+1):
    if prime[i]:
        result += 1

print(f'2부터 {num} 까지 소수는 총 {result}개 있습니다.')