import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
#input.txt�� ������ �и��ؼ� ������ str�ε� �װ��� int�� ��ȯ �������� ����
cnt = 0
#���� �ʱ�ȭ
for i in range(1, n+1) :
#����� 1���� �����ϴϱ� n���� ������ n+1����
        if n%i == 0 : #n�� i�� ���������� �������� 0 ==> n�� ����� i
            cnt +=1 #��� �߰ߵǸ� cnt 1 ����
        if cnt == k : #k��° ����� �߰ߵǸ� k��° ����� i
            print(i) #i ���
            break 
else : #���������� ������(��� �߰����� ���ϸ�) -1 ���
    print(-1)
