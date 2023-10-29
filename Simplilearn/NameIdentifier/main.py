def name_finder():
    while True:
        print("Please type your name.")
        name = input()
        if name == "Bob":
            break
    print("Thank you. You typed the correct name.")


if __name__ == '__main__':
    name_finder()
