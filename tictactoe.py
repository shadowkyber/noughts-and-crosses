count = 1

col1 = [" ", " ", " "]
col2 = [" ", " ", " "]
col3 = [" ", " ", " "]
dub = []  # matches
d = [col1, col2, col3]


def grid():  # prints grid
    print("---------")
    print("|", d[0][0], d[0][1], d[0][2], "|")
    print("|", d[1][0], d[1][1], d[1][2], "|")
    print("|", d[2][0], d[2][1], d[2][2], "|")
    print("---------")


def cord(y, x):  # checks if cell already has X or O
    if d[y][x] != " ":
        print("This cell is occupied! Choose another one!")
        return "repeat"


def ver(y):  # checks if 3 match vertically (row)
    if col1[y] == col2[y] == col3[y] == marker:
        dub.append(col1[y])


def hor(letter):  # checks if 3 match horizontally (column)
    if col1.count(letter) == 3:
        dub.append(letter)
    if col2.count(letter) == 3:
        dub.append(letter)
    if col3.count(letter) == 3:
        dub.append(letter)


def dia():  # checks if 3 match diagonally
    if col1[0] == col2[1] == col3[2] == marker:
        dub.append(col1[0])
    if col1[2] == col2[1] == col3[0] == marker:
        dub.append(col1[2])


grid()

while True:
    if count % 2 == 0:
        marker = "O"
    else:
        marker = "X"

    while True:  # gets players move
        c = input("Enter the coordinates: ").split()
        if c[0].isdigit() and c[1].isdigit():
            c = [int(num) - 1 for num in c]
            if 1 < c[0] > 2 or 1 < c[1] > 2:
                print("Coordinates should be from 1 to 3!")
            elif cord(c[0], c[1]) != "repeat":
                break
        else:
            print("You should enter numbers!")

    # does players move
    if c[0] == 0:  # if player chooses 1 y
        col1.pop(c[1])
        col1.insert(c[1], marker)
    elif c[0] == 1:  # if player chooses 2 y
        col2.pop(c[1])
        col2.insert(c[1], marker)
    elif c[0] == 2:  # if player chooses 3 y
        col3.pop(c[1])
        col3.insert(c[1], marker)

    grid()

    ver(0)
    ver(1)
    ver(2)

    hor(marker)

    dia()

    count += 1

    if len(dub) != 0:
        print(dub[0], "wins")
        break
    elif " " not in col1 and " " not in col2 and " " not in col3:
        print("Draw")
        break
