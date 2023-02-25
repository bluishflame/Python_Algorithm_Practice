import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
#cnt는 0으로 초기화하고 n+m보다 크진 않겠지만 넉넉하게 선언
#리스트 크기가 0으로 초기화되면서 n+m+3 개수만큼 크기가 생긴다
max = -2147000000
#max는 가장 작은 값으로 초기화
for i in range(1, n+1) : #1부터 n까지 돌아야 하니까 n+1
     for j in range(1, m+1) : #1부터 m까지 돌아야 하니까 m+1
         cnt[i+j]+=1 #i+j가 눈의 합이니까 1씩 증가
for i in range(n+m+1) : #나타나는 빈도 최대값 찾기 n+m까지 돌아야 하니까 n+m+1 
    if cnt[i] > max : #cnt의 i가 max보다 크면
        max = cnt[i] #max를 cnt의 i로 변경
for i in range(n+m+1) :
    if cnt[i] == max : #가장 큰 빈도수 값 찾기
        print(i, end=' ') #옆으로 출력
