# 내가 푼 답안
n = int(input())
m = int(input())

array = list(map(int, input().split()))

result = 0
for i in range(n):
    result += array[i]

count = 0
while result >= m:
    result = 0

    for i in range(n):
        result += array[i] - count
    count += 1
print(count)

'''
# 책 답안
n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

start = 0 
end = max(array)

result = 0 
while(start <= end):
    total = 0 
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
        
    if total < m:
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1

print(result)
'''

'''
자꾸만 순차 탐색으로 문제를 푸려고 하는것 같다.
순차 탐색 방법이 뭔가 더 직관적으로 풀수 있는 것 같은 느낌이라서 그런것 같다...

이문제는 전형적인 이진 탐색 문제이다.
파라메트릭 서치 유형의 문제이다.
파라 메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 사용한다.

예를 들어 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.
코딩 테스트나 프로그래밍 대회에서는 보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결한다.

# 문제 해설에서 나온 절단기의 높이를 움직이는 방법을 생각한것은 나랑 같다 #
하지만 이 문제에서 절단기의 높이 범위가 한정적이었다면 순차탐색으로도 해결할 수 있지만, 현재 문제에서 절단기의 높이는 최대 10억까지의 정수 이므로 순차탐색은
분명 시간 초과를 받을 것이다.

반면에 높이를 이진 탐색으로 찾는다면, 대략 31번 만에 경우의 수를 모두 고려할 수 있다.
이때 떡의 개수 N이 최대 100만개 이므로 이진 탐색으로 절단기의 높이를 바꾸면서, 바꿀 때마다 모든 떡을 체크하는 경우 대력 최대 3,000만 번 정도의 연산으로
문제를 풀 수 있다.

문제의 시간 제한은 2초이므로 최악의 경우 3,000만 번 정도의 연산이 필요하다면 아슬아슬하게 시간 초과를 받지 않고 정답 판정을 받을 것이다.
'''

'''
순차 탐색의 경우 범위가 한정적일 경우(연산해야할 경우가 적은 경우)에 만 유용할 것 같고 큰 범위로 주어진다면 이진 탐색으로 풀어야 시간적 효율성에서 더 나은 코드를
짤수 있다. 이진 탐색이 아직 낯설지만 내일 앞의 두문제를 복습하면서 이진탐색의 내용을 좀더 명확히 가져가야 할 필요성이 느껴진다.
'''
