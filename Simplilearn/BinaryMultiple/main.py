def multiple_finder():
    for index in range(len(lst)):
        if lst[index] % 5 == 0:
            print(lst[index])


if __name__ == '__main__':
    lst = [1000, 1010, 1001, 1100]
    multiple_finder()
