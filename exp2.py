# 최댓값, 최솟값 구하기

# 함수 이용하기
# map 객체는 iterator로, 한 번 iteration을 거치면 그 내용이 소진되고 다시 사용할 수 없음
arr = list(map(int, input().split())) # 3 1 5 2 4

print(min(arr)) # 1
print(max(arr)) # 5

# 반복문 이용하기 (음수 고려X)
my_max = 0
for a in arr:
    if my_max < a:
        my_max = a

print(my_max) # 5

# 숫자 범위 고려하기
my_max = arr[0]
for a in arr[1:]:
    if my_max < a:
        my_max = a

print(my_max)