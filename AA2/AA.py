import sys
sys.stdin = open("input.txt", "rt")
T = int(input()) 
#input은 str으로 읽으니 int로 형 변환
for t in range(T) : #0부터 돈다
    #각 case별로 읽어들임
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    #매핑한 것을 리스트화
    a = a[s-1:e]
    #s번째부터 e번째까지 추출
    a.sort()
    #오름차순 정렬
    print("#%d %d" %(t+1, a[k-1]))
    #정렬된 a 리스트의 k번째 숫자와 함께 번호 출력
