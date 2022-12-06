"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""


# (0) 인자로 리턴값도 없는 함수
def func():
    print('inside func')
    return 'OK'


func()
result = func()  # None
print(result)


# (1) 리턴값이 여러개 있는 함수
def func(arg):
    return arg + 5, arg - 5


result = func(10)
print(result)

a, b = func(10)
print(a, b)


# (2) 위치 인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!', name, '님')


func('하이', '홍길동')
func('박길동', '안녕')


# (3) 키워드 인자 (keyword argument)
func(name='홍길동', greeting='안녕')


# (4) 인자의 기본값
def func(greeting, name='길똥'):
    print(greeting, '!!!!', name, '님')


func('하이', '박길동')
func('안녕')


#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)
'''
첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?
'''


def func(a, b, c=0, *args):
    sum = a + b + c
    for i in args:
        sum += i
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다


# (6) 키워드 인자 모으기
def func(a, b, c=100, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    for K, V in kwargs.items():
        sum += V
    return sum


print(func(10, 20))
print(func(1, 2, 3))
print(func(1, 2, 3, 4, 5, 6))
print(func(1, 2, kor=10, eng=20))
print(func(1, 2, 3, 4, java=5, math=6, kor=7))
