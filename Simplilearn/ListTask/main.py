def list_task():
    for fruit in fruits:
        count = 0
        while count < 6:
            print(fruit, end=' ')
            count = count + 1
        print()


if __name__ == '__main__':
    fruits = ["apple", "orange", "kiwi"]
    list_task()
