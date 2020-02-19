def main():
    # f = open("texto.txt", "w+")
    # f1 = open("texto.txt", "a")
    f2 = open("texto.txt", "r")
    # for i in range(10):
    #     f.write(f"This is line {i}\n")
    #     f1.write(f"Escrita nao destrutiva #{i+10}\n")

    if f2.mode == "r":
        # contents = f2.read()
        # print(contents)

        fl = f2.readlines()
        for x in fl:
            print(x)


    # f.close()
    # f1.close()
    f2.close()


if __name__ == '__main__':
    main()
