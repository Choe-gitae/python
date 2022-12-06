"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
from builtins import str

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이를 입력하세요->'))
# age += 1
# print('나이 : ', age)

# height = eval(input('키를 입력->'))
# print('키 : ', height)
# print(type(height))

# eval()
print('1+2')
print(eval('1+2'))


#----------------------------------
# 단을 입력받아 구구단을 구하기
'''dan = int(input('단을 입력하세요 -> '))
for i in range(1, 10):
    print(dan, "*", i, '=', i*dan)

i = 1
while i <= 9:
    print(i*dan)
    i += 1

for i in range(1, 10):
    print('{0} * {1} = {2}'.format(dan, i, dan*i))'''

#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕', '친구')
print('안녕' '친구')

for i in range(5):
    print(i)
for i in range(5):
    print(i, end='/')
print()
for i in range(5):
    print(i, end='/' if i<4 else '')

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
