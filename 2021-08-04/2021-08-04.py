# n은 정한 숫자 k 는 나눌숫자 sum은 나눈횟수로 변수를 만들었다.
n,k = map(int, input().split())
sum = 0

# 정한숫자가 나눌숫자 보다 크거나 같다면
while n >= k:
    # 정한숫자에서 나눌숫자로 나눈 나머지가 0이 아니라면
    while n % k != 0:
        n -= 1
        sum += 1
    n // k
    sum += 1

# 정한숫자를 나누고 1보다 크다면
while n > 1:
    n -= 1
    sum += 1

# 나눈 횟수 출력
print(sum)

'''
주석을 달면서 해봤고 단순하게 푸는 답안 예시를 살짝만 참고 했고 거의다 비슷하게 코딩을 할수 있었다.
시간이 없어서 아직 파이썬 업데이트는 내일 하기로 했고 어제 했었던 코드 map을 이용해 숫자를 받는 함수를 이용해 문제를 풀어봤다.
'''
