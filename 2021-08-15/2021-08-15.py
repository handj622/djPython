from collections import deque

# n과 m 크기를 입력받음
n, m = map(int, input().split())

# 필드 생성
MAP = []
for i in range(n):
    MAP.append(list(map(int, input())))

# 이동방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 미로 탈출 함수 생성.
def escape(x, y):
    queue = deque()
    queue.append((x, y))
    # result = 1
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
                # result += 1
                MAP[nx][ny] = MAP[x][y] + 1
                queue.append((nx, ny))
    
    # return result
    return MAP[n-1][m-1]


print(escape(0, 0))


# 처음에는 Line 20, 38, 42를 보면 움직이는 경우 값을 더해주려고 result라는 변수를 만들어 표현하려고 했었다.
# 깊은 고민끝에 이방법이 잘못됬다는 것을 알았다.
# 저렇게 result를 리턴해주게 되면 내가 만든 맵의 모든 1의 숫자의 개수를 더해주는것과 다름이 없었다.
# 이건 잘못된 표현이었다.
# 그래서 Line 39를 통해 지나간 곳의 숫자를 전에 움직인 곳의 숫자 보다 1씩 더해주는 방법으로 계산을 한뒤
# 맵의 각 특정 위치의 최소거리를 다 표현하게 만든것이다. 그래서 목적지인 위치가 MAP[n-1][m-1] 위치이기 때문에
# 그곳의 값을 출력하면 문제의 답이 나오게 된다.
