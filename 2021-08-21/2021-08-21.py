# n의 값을 받는다.
n = int(input())

array_A = list(map(int, input().split()))

m = int(input())
array_B = list(map(int, input().split()))

def find(n, m, array_A, array_B):
    status = "No"
    for i in range(m):
        for j in range(n):
            if array_B[i] == array_A[j]:
                print("yes")
                status = "Yes"
        
        if status == "No":
            print("no")
        else:
            status = "No"

find(n, m, array_A, array_B)

'''
와.... 정말 오랜 고민끝에 풀었다... 정말 야매로 푼 것 같긴 한데 일단 풀었다는 것에 만족한다.
나는 순차 탐색 방법을 응용하여 풀었는데 해설에서는 이진탐색트리로 풀었다.
아직 해설을 보지 않아서 어떻게 풀었는지는 잘 몰라서 
내일 이 문제에 대한 해설을 보고 이해한뒤 다음 문제로 넘어가야겠다.
'''