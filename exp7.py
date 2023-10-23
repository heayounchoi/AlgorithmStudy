# 정렬

# 선택 정렬
arr = [3, 1, 4, 5, 2]

def selection_sort(arr):
    n = len(arr) # 리스트 길이 확인
    for i in range(n): # 리스트 만큼 반복
        min_idx = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: # 최솟값 구하기
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # i반째와 최솟값을 교환
        print(f'{i+1}번 째 정렬 후 = {arr}')
    return arr

print(selection_sort(arr))

# 거품 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print("i", i)
        for j in range(n - i - 1):
            print("j", j)
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f'변경 리스트 = {arr}')
    return arr
arr = [3, 1, 4, 5, 2]
print(bubble_sort(arr))

# 삽입 정렬
def insertion_sort(arr):
    new_arr = [arr[0]]
    print(f"1 번째 정렬된 리스트 = {new_arr}")
    for i in range(1, len(arr)):
        j = 0
        while j < i and new_arr[j] < arr[i]:
            j += 1
        new_arr.insert(j, arr[i])
        print(f"{i + 1} 번째 정렬된 리스트 = {new_arr}")
    return new_arr

arr = [3, 1, 4, 5, 2]
print("최종 정렬된 리스트 =", insertion_sort(arr))

def insertion_sort2(arr):
    for i in range(1, len(arr)):
        print(f"{i} 번째 새로운 리스트 = {arr[:i]} 기존 리스트 = {arr[i:]}")
        j = i        
        while 0 < j and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [3, 1, 4, 5, 2]
print("정렬이 끝난 리스트 =", insertion_sort2(arr))

# 수 정렬하기[백준 2750]
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))
    
arr.sort()
print(*arr)

for i in range(N - 1):
    for j in range(N - 1 - i):
        if arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(*arr)

# 국영수[백준 10825]
N = int(input())

arr = []
for _ in range(N):
    name, *scores = input().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : -x[1])

for st in arr:
    print(st)
    
arr.sort(key=lambda x : (-x[1], x[2]))

for st in arr:
    print(st)
    
arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for st in arr:
    print(st)