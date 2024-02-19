def print_table(table):
    for line in table:
        print(" | ".join(line))
        print("-" * 9)

def verif_victory(table, player):
    # Verificar linhas e colunas
    for i in range(3):
        if all(table[i][j] == player for j in range(3)) or all(table[j][i] == player for j in range(3)):
            return True

    # Verificar diagonais
    if all(table[i][i] == player for i in range(3)) or all(table[i][2 - i] == player for i in range(3)):
        return True

    return False

def verif_draw(table):
    for line in table:
        if " " in line:
            return False
    return True

def get_valid_move(message):
    while True:
        try:
            jogada = int(input(message))
            if 0 <= jogada <= 2:
                return jogada
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Please, enter a valid character.")

def play_jogo_da_velha():
    table = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_table(table)

        line = get_valid_move("Choose a line (0, 1, 2): ")
        column = get_valid_move("Choose a column (0, 1, 2): ")

        if table[line][column] == " ":
            table[line][column] = current_player
        else:
            print("Position held. Try again.")
            continue

        if verif_victory(table, current_player):
            print_table(table)
            print(f"Congratulations, player {current_player}! You won!")
            break
        elif verif_draw(table):
            print_table(table)
            print("The game ended in a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_jogo_da_velha()
