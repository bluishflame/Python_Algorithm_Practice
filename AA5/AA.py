import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
#����� ���ϱ� ���� round(�Ҽ� ù° �ڸ����� �ݿø�) �Լ� a ����Ʈ�� ��� �� ��
min = 2147000000
#������ ũ���� ���� ū ���� min�� ����
for idx, x in enumerate(a) :
    #�л���ȣ idx �л��� �� x enumerate�� a ����Ʈ�� �ε��� ���� ���� ���� ������ ����
    tmp = abs(x-ave) #�ӽú����� �л��� ���� ��� ������ �Ÿ� �� ���밪�� ����
    #�� ���밪�� ���� ���� �л��� ��տ� ������
    if tmp<min :
        min = tmp
        #tmp ���� min ������ ������ min�� tmp�� ����
        score = x
        #�信 ������ ����
        res = idx+1
        #0�� �ε������� ���������ϱ� +1
    elif tmp == min : #���� �Ÿ��� ���Դٸ� ���� �л��� �Ÿ��� ���� �л��� �Ÿ��� ���� ��
        if x>score : #������ �� ū �л��� ����
            score = x 
            res = idx+1 #������ ū �л����� ����
print(ave, res) #����̶� �л� ��ȣ ���

'''
��ǥ�� ���� ���� ����
round �� round_half_even ����� ���Ѵ�.

ex
a = 4.500
print(round(a))
--> 4 ���
��Ȯ�ϰ� 4.5 ������ ������ ¦���� �ٻ簪�� ������
4.5111�̸� ��Ȯ�ϰ� 5�� ������
a = 5.500
print(round(a))
--> 6
a = 66.5
a = a+0.5
a = int(a)
print(a)

'''
