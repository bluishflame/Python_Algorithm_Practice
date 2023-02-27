import sys
sys.stdin = open("input.txt", "r")
n = int(input())
cnt = 0
for i in range(2, n+1) :
    if ch[i] == 0 : 
        cnt+=1
        for j in range(1, n+1, 1) :
            ch[j] = 1
print(cnt)
