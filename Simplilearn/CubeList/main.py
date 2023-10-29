def cube_printer():
    for i in range(len(lst)):
        lst[i] = lst[i] ** 3
    print(lst)


if __name__ == '__main__':
    lst = [2, 3, 4, 5, 6]
    cube_printer()
