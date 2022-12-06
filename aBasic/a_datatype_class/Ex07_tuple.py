"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = [1, 2, 3]      # list
t = {1, 2, 3}      # set
t = (1, 2, 3)      # tuple
print(t)
print(t[0])
print(t[-1])

# (2) 튜플은 요소를 변경하거나 삭제 안됨
print('------------------- 2 -----------------')
# t[1] = 0      error
# del t[1]      error
del t

# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
# 우선순위 ()로 취급함
t2 = (1,)
print(t2)
print(type(t2))

# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
t = (1, 2, 3)
t2 = (1,)
print(t[1])     # 2
print(t2[1:])   # ()
print(t + t2)   # (1, 2, 3, 1)
print(t * 2)    # (1, 2, 3, 1, 2, 3)
