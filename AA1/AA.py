import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
#input.txt의 내용을 분리해서 읽으면 str인데 그것을 int로 변환 차례차례 매핑
cnt = 0
#개수 초기화
for i in range(1, n+1) :
#약수는 1부터 존재하니까 n까지 돌려면 n+1까지
        if n%i == 0 : #n을 i로 나누었더니 나머지가 0 ==> n의 약수가 i
            cnt +=1 #약수 발견되면 cnt 1 증가
        if cnt == k : #k번째 약수가 발견되면 k번째 약수는 i
            print(i) #i 출력
            break 
else : #정상적으로 끝나면(약수 발견하지 못하면) -1 출력
    print(-1)
