# N명의 학생 N을 입력받는다.
n = int(input())

Array = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    Array.append((name,score))

def setting(data):
    return data[1]

result = sorted(Array, key=setting)

for i in range(n):
    print(result[i][0])

'''
이것도 2021-08-18(2)와 같은 이유에서 실행이 안된다.
그래도 파이참으로 실행했을때 두 문제 다 잘 실행 되었다.
오늘 몰랐던 개념적 부분을 잘 살펴보고 문제도 쉽긴 했지만 2문제나 풀어서 기분이 좋다. 
점점 속도를 붙이고 싶지만 구다형이 말한 자만하지 않는 선에서 계속해서 나아가자.
'''