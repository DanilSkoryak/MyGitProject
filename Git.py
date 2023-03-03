print('Hello user')
try:
    num = int(input('Enter num: '))
    while True:
        try:
            data_num = int(input('1-Change num, 2-zero num, 3-exit: '))
            if data_num == 1:
                num = int(input('Enter num: '))
            elif data_num == 2:
                num = 0
            elif data_num == 3:
                break
        except ValueError:
            print('Use only numbers')
except ValueError:
    print('Use only numbers')