'''
코딩테스트에서 구현이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다.'
문제를 읽고 문제풀이 방법을 고민해서 정확한 풀이방법이 떠올라도 정답처리를 받을수 있는게 아니다.
생각해낸 풀이를 우리가 원하는 프로그래밍 언어로 정확히 구현해냈을 때 비로소 정답처리를 받을수 있다.
=> 프로그래밍 언어의 문법을 정확히 알고 있어야 하며 문제의 요구사항에 어긋나지 않는 답안 코드를 실수 없이 작성해야 한다.
'''
# 예제 4-1 상하좌우
n = int(input())

x, y = 1, 1
plans = input().split()

#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)


'''
아직 예제문제를 정확히 이해하지 못했다. 위의 코드는 책에 나와있는 코드이다.
코드를 보고 이해가 필요한 부분이 생겼다.
반복문의 in 앞에 어떤것이 들어가야 하는건지 정확히 문법을 찾아봐야함
range(len(move_types))가 말하는게 정확히 뭔지 문법을 찾아봐야함
continue가 무엇인지 찾아봐야함.

전체적으로 봤을때는 이해는 가는 코드이다.
dx와 dy를 배열을 통해 각 move_type에 맞춰서 표현했다는게 참신했다.
'''