def drawBoard(ht, wt):
    for i in range(ht):
        if ht == wt:
            drawHoriz(ht)
            drawVertical(ht)
        else:
            pass
    drawHoriz(ht)


def drawHoriz(s):
    print(" --- " * s)


def drawVertical(s):
    print("|    " * (s + 1))


def main():
    print("BOARDS")
    ht = int(input("Enter the height of the board: "))
    wt = int(input("Enter the width of the board: "))
    drawBoard(ht, wt)


if __name__ == "__main__":
    main()
