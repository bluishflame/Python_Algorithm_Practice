import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
#cnt�� 0���� �ʱ�ȭ�ϰ� n+m���� ũ�� �ʰ����� �˳��ϰ� ����
#����Ʈ ũ�Ⱑ 0���� �ʱ�ȭ�Ǹ鼭 n+m+3 ������ŭ ũ�Ⱑ �����
max = -2147000000
#max�� ���� ���� ������ �ʱ�ȭ
for i in range(1, n+1) : #1���� n���� ���ƾ� �ϴϱ� n+1
     for j in range(1, m+1) : #1���� m���� ���ƾ� �ϴϱ� m+1
         cnt[i+j]+=1 #i+j�� ���� ���̴ϱ� 1�� ����
for i in range(n+m+1) : #��Ÿ���� �� �ִ밪 ã�� n+m���� ���ƾ� �ϴϱ� n+m+1 
    if cnt[i] > max : #cnt�� i�� max���� ũ��
        max = cnt[i] #max�� cnt�� i�� ����
for i in range(n+m+1) :
    if cnt[i] == max : #���� ū �󵵼� �� ã��
        print(i, end=' ') #������ ���
