# 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. (오름차순 or 내림차순 등...)
# => 정렬 알고리즘은 프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중 하나이다.
#  => 이진 탐색이 가능해진다.

# 정렬 알고리즘) 
# => 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 (많이 사용하는 것들)
#  파이썬에서 제공하는 기본 정렬 라이브러리를 적용하여 좀 더 효과적인 정렬 수행 방법도 다룸 (이책에서)

#### 면접 단골문제 정렬 알고리즘 ####

# 선택 정렬)
# 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 
# 그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복하면 어떨까?
# 이 방법은 가장 원시적인 방법으로 매번 '가장 작은 것을 선택'한다는 의미에서 선택 정렬(selection Sort) 알고리즘이라고 한다.

# 예제 코드)
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range (len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑

print(array)
'''
# 삽입 정렬)
# 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입 정렬(Insertion Sort)이라고 부른다.
# 더불어 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
# 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에 그 위치에 삽입된다는 점이 특징이다.

# 예제 코드)
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            arrary[j], array[j-1] = array[j-1], array[i]
        else:
            break

print(array)
'''
# 퀵 정렬)
# 지금 까지 배운 알고리즘 중에 가장 많이 사용되는 알고리즘이다.
# 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이기도 하다.
# '기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은데이터의 위치를 바꾸면 어떨까?'
# => 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
# => 퀵 정렬에서는 피벗(Pivot)이 사용된다. : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'
# => 퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 한다.

# 호어 분할 방식에서의 규칙에 따른 피벗 설정
# => 리스트에서 첫 번째 데이터를 피벗으로 정한다.

# 이와 같이 피벗을 설정한 뒤에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 그다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다. 이러한 과정을 반복하면 '피벗'에 대하여 정렬이 수행된다.

# 널리 사용되고 있는 가장 직관적인 형태의 퀵 정렬 소스코드.
'''
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start + 1
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
'''
# 파이썬의 장점을 살려 더 직관적이고 기억하기 쉬운 방법
# 하지만 피벗과 데이터를 비교하는 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적인 코드 
'''
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
'''
# x for x in tail if x <= pivot 처음보는 문법이 등장했다.


# 계수 정렬)
# 계수 정렬(Count Sort)알고리즘은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
# 다만, 계수 정렬은 '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'만 사용할 수 있다.
# 예를 들어 데이터의 값이 무한한 범위를 가질 수 있는 실수형 데이터가 주어지는 경우 계수 정렬은 사용하기 어렵다.
# 계수 정렬은 앞서 다루었던 3가지 정렬 알고리즘 처럼 직접 데이터의 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식(비교 기반의 정렬알고리즘)이 아니다.

# 계수 정렬 소스코드
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
'''

# 파이썬의 정렬 라이브러리)
# 정렬 알고리즘 문제는 어느 정도 정해진 답이 있는, 즉 외워서 잘 풀어낼 수 있는 문제라고 할 수 있다.
# 정렬 알고리즘을 앞에서 봤던 예제처럼 직접 작성하게 되는 경우도 있지만 미리 만들어진 라이브러리를 이용 하는 것이 효과적인 경우가 더 많다.

# sorted() 함수 >
# 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
# 병합 정렬은 일반적으로 퀵 정렬 보다 느리지만 최악의 경우에도 시간 복잡도를 보장한다는 특징이 있다.
# 이러한 sorted() 함수는 리스트, 딕셔너리 자료형등을 입력받아서 정렬된 결과를 출력한다. 반환되는 결과는 리스트 자료형이다.

# sorted 소스코드
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
'''

# sort 소스코드
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)
'''

# 정렬 라이브러리에서 key를 활용한 소스코드
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def setting(data):
    return data[1]
result = sorted(array, key=setting)

result = sorted(array)
print(result)
'''
# 지금 위의 코드에서 key가 이해가 잘 가지 않는다.
# 내일 수강신청이 있어서 오늘은 여기까지 하고 자고 내일 다시 내용 앞에서부터 복습한뒤 위에서 아래로 라는 실전문제를 풀어보도록하자