# 재귀 함수
# 재귀의 제한 풀기
import sys 
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(10**6)

# 팩토리얼[백준 10872]
# 반복문으로 만들기
n = int(input())

def fac(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i 
    return factorial

print(fac(10))

# 재귀함수로 만들기
N = int(input())

def fac(n):
    # 종료조건 추가하기
    if n <= 1:
        return 1
    return n * fac(n-1)

print(fac(N))

# 재귀함수가 뭔가요?[백준 17478]
def recursion(n):
    line = '____' * n

    print(f'{line}"재귀함수가 뭔가요?"')
    if n == N:
        print(f'{line}"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:    
        print(f'{line}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{line}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{line}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recursion(n+1)

    print(f'{line}라고 답변하였지.')

N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(0)
