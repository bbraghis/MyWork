def list_pop():
    while a:
        print(a.pop())
    else:
        print("There are no elements left in the list")


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    list_pop()
