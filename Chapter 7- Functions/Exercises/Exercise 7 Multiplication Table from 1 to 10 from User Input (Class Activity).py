def num():
    number = int(input("Input number for its multiplication table: "))
    for i in range(1,11):
        print(number, 'x', i, '=', number*i)
num()