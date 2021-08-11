# N, M 의 값을 받는다.
n, m = map(int, input().split())

MAP = []
for i in range(n):
    MAP.append(list(map(int, input())))

def IceCream(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if MAP[x][y] == 0:
        MAP[x][y] =1
        IceCream(x - 1, y)
        IceCream(x, y - 1)
        IceCream(x + 1, y)
        IceCream(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if IceCream(i, j) == True:
            result += 1

print(result)
'''
MAP으로 필드(?)를 생성하는거 까지 하고 고민하다가 앞에서 배웠던것 중에 
만든 필드를 벗어나면 조건문을 이용하여 종료시키는 코드를 생각했는데 그다음 어떻게 해야할지 몰라 답안예시를 보았다.
아직 코드가 잘이해가 안되는 모양이다. DFS를 이용한 거라고 해설에서 얘기하고 있는데 솔직히 아직 뭔소린지 이해가 잘 되지 않는다.

하지만 계속해서 해나아갈 것이다. 계속 하다보면 이 부분이 이해가 되는 시점이 생길거라고 생각하고 있다.
문제는 크게 어렵지 않았던것 같다. 코드로 구현하는데 생각하는게 좀 시간이 걸리긴 하겠지만 
문제 자체를 이해하고 아 이렇게 짜면 되겠구나 하는 생각이 든다.

내일 이 문제 다시한번 복습하고 다음문제까지 풀어보자.
'''