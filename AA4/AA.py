#�ּڰ� ���ϱ�

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') #���� ���� ���� �����ϱ� ���� ���� arrMin�� ���� ū ��(���Ѵ�)���� �ʱ�ȭ
for i in range (len(arr)) : #0���� 7���� 8�� �ݺ�
    if arr[i] < arrMin : #���ʷ� �� ���Ѵ뺸�� ������ ó���� ���� �׷��� arrMin�� ù ��° ���� �� �� �ڷκ��� �������� ���� ���ڶ� �񱳸� �ؼ� �� ���� ���̸� arrMin�� �� ���� ����
        #<��� <=��� �θ� ���� ���ڷ� �ٲ� 2�� 2�� �����ϱ�. ������ �׳� ù ��° 2
        arrMin = arr[i]
print(arrMin)

'''
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for x in arr :
    if x<arrMin :
        arrMIn=x
print(arrMin)

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for x in arr :
    if x<arrMin :
        arrMIn=x
print(arrMin)

������ ��� ���
'''
