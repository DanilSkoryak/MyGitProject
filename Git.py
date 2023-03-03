print('Hello user')
try:
    num = int(input('Enter num: '))
    while True:
        try:
            data_num = int(input('1-Change num, 2-zero num, 3-exit: '))
        except ValueError:
            print('Use only numbers')
except ValueError:
    print('Use only numbers')