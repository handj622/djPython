'''
순차탐색)
: 순차 탐색(Sequential Search)이란 리스트안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
  보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

<순차 탐색 소스코드>

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

이진 탐색)
: 이진 탐색(Binary Search)은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
  데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있다.
  탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.

=> 이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점이다.
   찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.

구현방법 : 재귀 함수를 이용하는 방법 // 단순하게 반복문을 이용하는 방법.

<재귀 함수로 구현한 이진 탐색 소스코드>
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


<반복문으로 구현한 이진 탐색 소스코드>
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

트리 자료구조)
: 이진 탐색은 전체 조건이 데이터 정렬이다. 예를 들어 동작하는 프로그램에서 데이터를 정렬해두는 경우가 많으므로
  이진 탐색을 효과적으로 사용할 수 있다. 데이터베이스는 내부저긍로 대용량 데이터 처리에 적합한 트리 (Tree)자료구조를 이용하여
  항상 데이터가 정렬되어있다.

: 트리 자료구조는 노드와 노드의 연결로 표현하며 여기에서 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체로 이해할 수 있다.
  트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를
  관리하기 위한 목적으로 사용한다. 트리 자료구조는 몇가지 주요한 특징이 있다.
   - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
   - 트리의 최상단 노드를 루트 노드라고 한다.
   - 트리의 최하단 노드를 단말 노드라고 한다.
   - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
   - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.
  정리하자면 큰 데이터를 처리하는 소프트 웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진 탐색과 같은 기법을 이용해
  빠르게 탐색이 가능하다.

이진 탐색 트리)
: 트리 자료구조 중에서 가장 간단한 형태가 이진 탐색 트리이다.
  이진 탐색 트리란 이진 탐색이 동작 할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.
   - 부모 노드보다 왼쪽 자식 노드가 작다.
   - 부모 노드보다 오른쪽 자식 노드가 크다.
   왼쪽 자식 노드 < 부모노드 < 오른쪽 자식 노드가 성립해야지 이진 탐색 트리라 할 수 있다.

빠르게 입력받기)
: 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
  데이터의 개수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 알고리즘을 의심해 보자.
  이처럼 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
  때로는 코딩 테스트 출제자가 아예 sys 라이브러리를 사용하기를 권고하는 문장을 문제에 적어 놓기도 한다.
  sys 라이브러리는 다음과 같은 방식으로 사용하며 한 줄씩 입력받는다.

<한 줄 입력받아 출력하는 소스코드>

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

  sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip()함수를 꼭 호출해야 한다.
  소스코드에 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데,
  이 공백 문제를 제거하려면 rstrip() 함수를 사용해야 한다.
'''