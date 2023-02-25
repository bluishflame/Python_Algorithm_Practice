import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() 
#set은 중복되는 값을 제거
for i in range(n) : #0부터 돈다
    for j in range(i+1, n) : #i는 이미 선택되었으니 i뒤에서부터 돈다
        for m in range(j+1, n) : #j는 이미 선택되었으니 j뒤에서부터 돈다
            # 중복을 방지하기 위해서
            res.add(a[i]+a[j]+a[m]) #중복을 제거하면서 res에 입력

res = list(res) #res를 리스트화해서
res.sort(reverse = True) #내림차순 정렬
print(res[k-1]) #0번부터니까 k번째는 k-1
