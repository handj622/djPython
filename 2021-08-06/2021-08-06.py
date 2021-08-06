# n을 입력받고 h_time // m_time // s_time // result를 선언
n = int(input())

h_time = 0
m_time = 0
s_time = 0
result = 0

for i in range(n):
    if h_time != 3 or h_time != 13 or h_time != 23:
        for j in range(60):
            if m_time != 3 or m_time != 13 or m_time != 23 or m_time != 33 or m_time != 43 or m_time != 53 or m_time != 30 or m_time != 31 or m_time != 32 or m_time != 34 or m_time != 35 or m_time != 36 or m_time != 37 or m_time != 38 or m_time != 39:
                for k in range(60):
                    if s_time == 3 or s_time == 13 or s_time == 23 or s_time == 33 or s_time == 43 or s_time == 53 or s_time == 30 or s_time == 31 or s_time == 32 or s_time == 34 or s_time == 35 or s_time == 36 or s_time == 37 or s_time == 38 or s_time == 39:
                        result += 1
                    s_time += 1
                    if s_time == 60:
                        s_time = 0
            if m_time == 3 or m_time == 13 or m_time == 23 or m_time == 33 or m_time == 43 or m_time == 53 or m_time == 30 or m_time == 31 or m_time == 32  or m_time == 34 or m_time == 35 or m_time == 36 or m_time == 37 or m_time == 38 or m_time == 39:
                result += 60
            m_time += 1
            if m_time == 60:
                m_time = 0
    if h_time == 3 or h_time == 13 or h_time == 23:
        result += 3600
    h_time += 1
    if h_time == 25:
        h_time = 0

print(result)
'''
n = int(input())

h_time = 0
m_time = 0
s_time = 0
result = 0

for i in range(n):
    if h_time % 3 != 0 or h_time == 0:
        for i in range(60):
            # m_time이 0이거나 3으로 나눴을때 나머지가 0이 아니라면 s_time을 실행한다.
            if m_time % 3 != 0 or m_time == 0:
                for i in range(60):
                    if s_time % 3 == 0 and s_time != 0 and s_time != 60:
                        result += 1
                    s_time += 1
                    if s_time == 61:
                        s_time = 0
            # s_time과 비슷한 방법으로 m_time을 설정
            if m_time % 3 == 0 and m_time != 0 and m_time != 60:
                result += 60
            m_time += 1
            if m_time == 61:
                m_time = 0
    if h_time % 3 == 0 and h_time != 0 and h_time != 24:
        result += 3600
    h_time += 1
    if h_time == 25:
        h_time = 0

print(result)
'''






'''
1. 정수 N을 입력을 받는다.
2. h_time , m_time, s_time 변수를 선언.
3. s_time을 1씩 늘려가면서 60이 될때 m_time 숫자를 하나 늘리고 m_time이 60이 될때 h_time을 1씩 늘리게 한다.
4. 그 과정에서 s_time이나 m_time이나 h_time을 3으로 나눴을때 나머지가 0일 경우 result값을 1늘린다.
5. 입력받은 정수 N과 h_time이 같다면 반복문을 끝낸다  
6. print(result)로 값을 출력한다.
'''