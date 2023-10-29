def while_print():
    i = 11
    while i > 0:
        j = 11
        while j > i:
            print("*", end='')
            j = j - 1
        i = i - 1
        print()


if __name__ == '__main__':
    while_print()
