def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b


if __name__ == '__main__':
    print('\n첫번째 숫자를 입력하세요 제발.')
    input1 = int(input('입력: '))

    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
    act = input('기호: ')

    print('\n두번째 숫자를 입력하세요.')
    input2 = int(input('입력: '))

    if act == '+':
        result = plus(input1, input2)

    if act == '-':
        result = minus(input1, input2)

    if act == '*':
        result = mul(input1, input2)

    if act == '/':
        result = divide(input1, input2)

    print(f'\n사칙연산 결과는 {result} 입니다.')