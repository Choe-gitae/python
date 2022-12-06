'''
[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 실행 ]
        print(count_vowel("pythonian"))
'''


def even_filter(num_list):
    return [n for n in num_list if n % 2 == 0]


def is_prime_number(num):
    return num % 2 != 0 and num % 3 != 0


def count_vowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in vowel:
        count += string.lower().count(i)
    return count


num_list = [n for n in range(20)]
print(even_filter(num_list))
print(is_prime_number(70))
print(count_vowel('AAA'))
