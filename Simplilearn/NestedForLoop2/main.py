def comp_printer():
    for i in comp:
        print("We will display each letter of "+i)
        for letter in i:
            print(letter)


if __name__ == '__main__':
    comp = ["Google", "Microsoft", "Nintendo", "Sega"]
    comp_printer()
