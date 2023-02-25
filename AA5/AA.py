import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
#평균을 구하기 위해 round(소수 첫째 자리에서 반올림) 함수 a 리스트의 모든 값 합
min = 2147000000
#정수형 크기의 가장 큰 값을 min에 대입
for idx, x in enumerate(a) :
    #학생번호 idx 학생의 값 x enumerate은 a 리스트의 인덱스 값과 실제 값을 쌍으로 대응
    tmp = abs(x-ave) #임시변수에 학생의 값과 평균 사이의 거리 값 절대값을 대입
    #이 절대값이 가장 작은 학생이 평균에 가깝다
    if tmp<min :
        min = tmp
        #tmp 값이 min 값보다 작으면 min을 tmp로 변경
        score = x
        #답에 점수도 저장
        res = idx+1
        #0번 인덱스부터 시작했으니까 +1
    elif tmp == min : #같은 거리가 나왔다면 지금 학생의 거리가 기존 학생의 거리와 같을 때
        if x>score : #점수가 더 큰 학생이 저장
            score = x 
            res = idx+1 #점수가 큰 학생으로 변경
print(ave, res) #평균이랑 학생 번호 출력

'''
대표값 문제 오류 수정
round 는 round_half_even 방식을 택한다.

ex
a = 4.500
print(round(a))
--> 4 출력
정확하게 4.5 지점에 있으면 짝수로 근사값을 보낸다
4.5111이면 정확하게 5로 보낸다
a = 5.500
print(round(a))
--> 6
a = 66.5
a = a+0.5
a = int(a)
print(a)

'''
