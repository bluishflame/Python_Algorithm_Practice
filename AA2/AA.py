import sys
sys.stdin = open("input.txt", "rt")
T = int(input()) 
#input�� str���� ������ int�� �� ��ȯ
for t in range(T) : #0���� ����
    #�� case���� �о����
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    #������ ���� ����Ʈȭ
    a = a[s-1:e]
    #s��°���� e��°���� ����
    a.sort()
    #�������� ����
    print("#%d %d" %(t+1, a[k-1]))
    #���ĵ� a ����Ʈ�� k��° ���ڿ� �Բ� ��ȣ ���
