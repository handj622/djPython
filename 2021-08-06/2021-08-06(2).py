# n을 입력 받고 n의 알파벳 부분은 x1(가로) 숫자부분은 y1(세로)으로 선언을 하고 sum을 선언했다.
n = input()
x1 = ord(n[0])-ord('`')
y1 = int(n[1])
sum = 0
# 움직일수 있는 방향을 배열 way로 표현을 해보았다.
way = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

# range를 이용해 0부터 7까지 i의 값을 넣어 반복문을 표현하였다.
for i in range(0, 8):
    # 배열을 표현할때 way[i] 이런거뿐만 아니라 way안에 있는 숫자 하나하나를 이용하기 위해서 문법을 찾아 보았더니 way[?][?]이런식으로 표현하면 몇번째 배열의
    # 몇번째꺼 라는 걸 표현할수 있는걸 배웠다. 그리고 사용했다.
    x2 = x1 + way[i][0]
    y2 = y1 + way[i][1]
    # if 문을 이용해서 1부터 8까지의 범위 안에만 들어갔을 경우 움직일수 있는 경우의 수로 더했다.
    if 1 <= x2 <= 8 and 1 <= y2 < 8:
        sum += 1

print(sum)
'''
문제 해설과 비교해 보았을때 비슷하지만 다르게 풀었다. 
처음으로 내힘으로 풀어본 문제여서 기분이 좋았다.
답안 예시에서 또 문법에 대한 앎이 필요해졌다.
1. ord를 나도 사용하긴 했지만 column = int(ord.....  나는 ord 앞에 int 를 붙이지 않았는데 잘 돌아갔는데 왜 int 를 붙였는지 알아봐야겠다. ord
    를 썼을때 자료형이 어떻게 주어지는지(?) 알아봐야겠다. 내생각에는 int 로 생각해서 int를 안 붙인 것이었다. 
2. next_row = row + step[0] 에서 step[0]이 (-2,-1)에서 -2 를 나타낸다는 것 더 깊게 알아봐야할 필요성이 생겼다.


'''
# 답안 예시
'''
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))- int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''