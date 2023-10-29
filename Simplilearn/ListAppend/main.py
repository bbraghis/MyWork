def append_list():
    for i in list1:
        for j in list2:
            result.append(i+j)
    print(result)


if __name__ == '__main__':
    list1 = [36, 78, 22]
    list2 = [44, 66, 77]
    result = []
    append_list()
