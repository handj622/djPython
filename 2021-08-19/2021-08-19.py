# N(배열의 원소 갯수), K(바꿔치기 횟수)를 입력받는다.
n, k = map(int, input().split())

#배열 A 와 B 를 생성
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 배열 A를 오름차순으로 정렬하고 배열 B를 내림차순으로 정렬한다.
array_A = sorted(A)
array_B = sorted(B, reverse = True)

# 입력받은 바꿔치기의 횟수를 입력 받는다.
for i in range(k):
    # 숫자가 작은 array_A의 숫자와 숫자가 큰 B의 숫자를 변경한다.
    array_A[i], array_B[i] = array_B[i], array_A[i]

# 변경된 배열 array_A의 합을 구하고 출력한다.
print(sum(array_A))

'''
CHAPTER 06 정렬의 마지막 문제를 다 풀었다.
이번 CHAPTER 06 정렬 파트의 모든 문제를 혼자 풀었다.
물론 쉬웠던것 같았지만 앞의 내용의 이해와 베이스를 바탕으로 나올수 있었던 모습이었던것 같다.
내일 부터는 이진 탐색에 대한 내용이 나온다.
자료구조를 하면서 이진탐색에 대한 내용이 가장 어려웠는데 걱정이 되긴 하지만
다양한 유형을 배워 볼수 있을것 같아 도전의식은 올라온다.
CHAPTER 06는 이렇게 끝나고 다름 챕터로 넘어가면 될것 같다.
'''