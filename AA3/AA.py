import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() 
#set�� �ߺ��Ǵ� ���� ����
for i in range(n) : #0���� ����
    for j in range(i+1, n) : #i�� �̹� ���õǾ����� i�ڿ������� ����
        for m in range(j+1, n) : #j�� �̹� ���õǾ����� j�ڿ������� ����
            # �ߺ��� �����ϱ� ���ؼ�
            res.add(a[i]+a[j]+a[m]) #�ߺ��� �����ϸ鼭 res�� �Է�

res = list(res) #res�� ����Ʈȭ�ؼ�
res.sort(reverse = True) #�������� ����
print(res[k-1]) #0�����ʹϱ� k��°�� k-1
