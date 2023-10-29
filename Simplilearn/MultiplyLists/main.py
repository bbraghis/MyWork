def multiply_lists():
    for i in list1:
        for j in list2:
            if i == j:
                continue
            print(i, '*', j, '=', i*j)


if __name__ == '__main__':
    list1 = [2, 5, 6]
    list2 = [2, 5, 6]
    multiply_lists()
