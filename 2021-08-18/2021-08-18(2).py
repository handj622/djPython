# CHAPTER 06. <2> "위에서 아래로"
# 수열 속해 있는 수의 개수 N을 입력받음.
n = int(input())

Array = []

for i in range(n):
    Array.append(int(input()))

result = sorted(Array)
result.reverse()

for i in range(n):
    print(result[i], end=' ')

'''
/usr/bin/python3 /Users/hyeon/PycharmProjects/djPython/2021-08-18/2021-08-18(2).py
(base) hyeon@Hyeonui-MacBookPro djPython % /usr/bin/python3 /Users/hyeon/PycharmProjects/djPython/2021-08-18/2021-08-18(2).py
zsh: no matches found: /Users/hyeon/PycharmProjects/djPython/2021-08-18/2021-08-18(2).py
(base) hyeon@Hyeonui-MacBookPro djPython % 

이상한 코드가 올라왔다. 실행하는데 no matches found 라는 말이 나오는것 같기도 하고
'''