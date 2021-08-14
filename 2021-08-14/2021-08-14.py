from collections import deque

# n과 m 크기를 입력받음
n, m = map(int, input().split())

# 필드 생성
MAP = []
for i in range(n):
    MAP.append(list(map(int, input())))

# 이동방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 미로 탈출 함수 생성.
def Escape(x, y):
    queue = deque([x,y])
    result = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만들어진 맵을 벗어날때 컨티뉴를 통해 나오게 한다.
            # 밑에거 하면서 생각난건데 여기도 움직인값을 넣어줘야한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽에 가는 경우의 수도 제거 해야한다.
            # 변경된 위치를 표현하는게 있어야 겠다고 생각됨.
            if MAP[nx][ny] == 0:
                continue

            # 이제 움직이는 경우 값을 더해야한다.
            if MAP[nx][ny] == 1:
                result += 1
                queue.append((nx, ny))
    
    return result

print(Escape(0,0))