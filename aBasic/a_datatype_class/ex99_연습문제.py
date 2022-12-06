# 1. 사용자로부터 5개의숫자를읽어서리스트에저장하고숫자들의평균을계산하여출력한다.
# 또숫자중에서평균을출력하여보자.
'''total = 0
for i in range(5):
    total = total + int(input('정수를 입력하세요: '))
print(float(total/5))'''
from builtins import range

# 2. 사용자에게서받은문자들을 역순으로 출력한다.
'''input_str = input('문자열 입력: ')
print(input_str[::-1])'''

# 3. 사용자에게서받은정수들의평균과표준편차를계산하여출력한다.
# 평균과표준편차를프로그램을 작성하세요
'''
import numpy as np
input_float_list = [int(x) for x in input('정수를 입력하세요: ').split(' ')]
print('평균: %f' % np.mean(input_float_list))
print('표준편차: {}'.format(np.std(input_float_list)))
'''

# 4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
# 문자열을입력하시오: NUMBER
