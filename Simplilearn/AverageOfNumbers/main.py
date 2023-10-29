def average_pos():
    num = 0
    count = 0
    suma = 0
    while num >= 0:
        num = int(input("Enter any positive number"))
        if num >= 0:
            count = count + 1
            suma = suma + num
    avg = suma/count
    print('Total sum of numbers: ', suma, 'Average: ', avg)


if __name__ == '__main__':
    average_pos()
