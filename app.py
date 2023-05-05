
def validate_choice(question):
    n = int(input(question))
    v = True
    for i in range(len(table)):
        if n in table[i]:
            v = False
    if v:
        raise ValueError
    return n

def check_if_taken(n):
    return n in played

def print_table():
    print()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == len(table[i]) - 1:
                print("", table[i][j])
            else:
                print("",table[i][j], "|", end="")
        if i < len(table) - 1:
            print("-" * 11)
    print()

def change_player(number_of_players, player):
    player += 1
    x = player - 1
    k = number_of_players - 1 + 1
    if player > number_of_players or player < 1:
        return (x % (number_of_players - 1 + 1)) + 1
    else:
        return player

def check_if_winner():
    w = False
    cl, cc, cd1, cd2 = (0, 0, 0, 0,)
    for i in range(len(table)):
        cl, cc, cd1, cd2 = (1, 1, 1, 1,)
        for j in range(len(table[i]) - 1):
            if table[i][j] == table[i][j + 1]:
                cl += 1
            if table[j][i] == table[j + 1][i]:
                cc += 1
            if table[j][j] == table [j + 1][j + 1]:
                cd1 += 1
            if table[j][len(table[j]) - 1 - j] == table[j + 1][len(table[j]) - 1 - j - 1]:
                cd2 += 1
            if cl == 3 or cc == 3 or cd1 == 3 or cd2 == 3:
                w = True
    return w

def check_if_draw():
    d = False
    if len(played) == len(table) * len(table[0]):
        d = True
    return d


if __name__ == "__main__":
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    played = []
    player = 1
    s = "Let's play TicTacToe!"
    leng = len(s)
    print()
    print("=" * leng)
    print(s)
    print("=" * leng, "\n")
    print("""Instructions: Choose which square you want
to play and enter the number equivalent to
it so it will be filled out for you. Wait
for your turn to play again.""")
    print("=" * leng)
    print_table()
    while True:
        try:
            print(f"Player {player}'s turn")
            n = validate_choice("Pick a position to play: ")
            print(f"Chosen position: {n}")
            if check_if_taken(n):
                print("Position already taken, please choose an available one.")
                continue
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if n == table[i][j]:
                        played.append(table[i][j])
                        if player == 1:
                            table[i][j] = "X"
                        elif player == 2:
                            table[i][j] = "O"
            print_table()
            if check_if_winner():
                print(f"Congratulations Player {player}, you win!\n")
                break
            elif check_if_draw():
                print("Draw!\n")
                break
            player = change_player(2, player)

        except ValueError:
            print("Invalid choice. Check if your choice is a valid number and if it hasn't been taken")
