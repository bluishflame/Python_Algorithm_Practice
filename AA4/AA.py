#최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') #가장 작은 값을 저장하기 위한 변수 arrMin을 가장 큰 값(무한대)으로 초기화
for i in range (len(arr)) : #0부터 7까지 8번 반복
    if arr[i] < arrMin : #차례로 비교 무한대보단 무조건 처음이 작음 그러면 arrMin에 첫 번째 값이 들어감 그 뒤로부터 착착착착 다음 숫자랑 비교를 해서 더 작은 값이면 arrMin에 그 값을 대입
        #<대신 <=라고 두면 뒤의 숫자로 바뀜 2랑 2가 있으니까. 지금은 그냥 첫 번째 2
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

동일한 결과 출력
'''
