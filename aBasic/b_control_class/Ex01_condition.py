"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

a = -1
if a:
    print('True1')
else:
    print('False1')

a = 2
b = 0

if a and b:
    print('True2')

if a or b:
    print('True3')

# 결과값의 기준을 리턴
print(a and b)      # and 는 둘다 True라면 뒤가 기준   False 라면 False값 기준
print(a or b)       # or  는 앞이 기준

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6

print(c)    # 2


