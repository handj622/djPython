# 문제 이해가 너무 안되어서 3-3.py main()함수를 이용하는 답안 예시를 이용한 코드이다.
# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한줄씩 입력받는 반복문
for i in range(n):
    data = list(map(int, input().split()))
    # 현재줄에서 가장 작은수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)