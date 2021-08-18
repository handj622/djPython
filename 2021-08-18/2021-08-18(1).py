'''
array = [('바나나', 2),('사과', 5),('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
'''

# key를 기준으로 배열을 정렬하는 것이었다.
# 디폴트로는 제일 앞에있는 값으로 정렬이 되고 저렇게 키 값을 지정해주면 숫자를 기준으로 정렬해준다.


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

# left_side = [x for x in tail if x <= pivot] 이라는 처음보는 문법은 tail 배열 안에 들어있는 1부터의 값 중 기준이되는 pivot 보다 작거나 같은 숫자를
# 조건으로 하는 숫자들을 left_side 배열에 집어 넣는 것이고 right_side도 똑같은 원리로 pivot보다 큰 숫자를 조건으로 하는 숫자를 집어넣은 것이었다. 
# 어제한 공부의 내용에서 나온 질문들을 살펴보고 정확히 파악해서 너무 좋고 다행이다. 