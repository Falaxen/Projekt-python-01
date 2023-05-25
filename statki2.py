import random
import os

#tworzenie tablic
player_board = [[0, 0, 0, 0, 0] for _ in range(5)]
bot_board = [[0, 0, 0, 0, 0] for _ in range(5)]

#funkcja do wyświetlania planszy
def display_boards(show_bot_ships=False):
    print("Plansza gracza:")
    print("   0 1 2 3 4")
    print("   _________")
    for i in range(5):
        print(f"{i}| {' '.join(str(cell) for cell in player_board[i])}")
    print("\nPlansza bota:")
    print("   0 1 2 3 4")
    print("   _________")
    for i in range(5):
        row = bot_board[i].copy()
        if not show_bot_ships:
            #żeby nie wyświetlało statków bota na planszy w trakcie gry
            row = [0 if cell == 1 else cell for cell in row]
        print(f"{i}| {' '.join(str(cell) for cell in row)}")

#funkcja do stawiania statków
def place_ships():
    ships_placed = 0
    while ships_placed < 3:
        print(f"Ustawianie statku {ships_placed + 1}")
        row = int(input("Podaj numer wiersza (0-4): "))
        col = int(input("Podaj numer kolumny (0-2): "))
        #sprawdzanie czy można tu postawić statek
        if row < 0 or row > 4 or col < 0 or col > 2:
            print("Niepoprawne współrzędne. Spróbuj ponownie.")
            continue
        if player_board[row][col] != 0 or player_board[row][col + 1] != 0 or player_board[row][col + 2] != 0:
            print("Statek nie może być ustawiony tutaj. Spróbuj ponownie.")
            continue

        #licznik statków i ich ustawienia
        player_board[row][col] = 1
        player_board[row][col + 1] = 1
        player_board[row][col + 2] = 1
        ships_placed += 1
        os.system("cls")
        display_boards()

#stawianie statków przez bota
def place_bot_ships():
    ships_placed = 0
    while ships_placed < 3:
        row = random.randint(0, 4)
        col = random.randint(0, 2)

        #sprawdzanie czy można tu postawić statek v2
        if bot_board[row][col] != 0 or bot_board[row][col + 1] != 0 or bot_board[row][col + 2] != 0:
            continue

        #licznik statków bota i ich ustawienia
        bot_board[row][col] = 1
        bot_board[row][col + 1] = 1
        bot_board[row][col + 2] = 1
        ships_placed += 1

#no strzelaj no strzelaj do polaka
def shoot(row, col, board):
    if board[row][col] == 1:
        board[row][col] = 'X'
        print("TRAFIONY!")
        input("Naciśnij enter")
        os.system("cls")
    elif board[row][col] == 'X' or board[row][col] == 'O':
        print("Już strzelałeś w to miejsce.")
        input()
        os.system("cls")
    else:
        board[row][col] = 'O'
        print("PUDŁO!")
        input("Naciśnij enter")
        os.system("cls")
#główna funkcja gierki
def play_game():
    print("Witaj w grze w statki!")
    display_boards()
    place_ships()
    place_bot_ships()
    game_over = False

    while not game_over:
        print("\nTwoja kolej:")
        row = int(input("Podaj numer wiersza (0-4): "))
        col = int(input("Podaj numer kolumny (0-4): "))
        while row < 0 or row > 4 or col < 0 or col > 4:
            print("\nPodałeś nieprawidłowe koordynaty!!!")
            row = int(input("Podaj numer wiersza (0-4): "))
            col = int(input("Podaj numer kolumny (0-4): "))
        shoot(row, col, bot_board)
        display_boards()

        #sprawdzanie czy gracz wygrał
        if all(all(cell != 1 for cell in row) for row in bot_board):
            print("Gratulacje! Wygrałeś!")
            input("super")
            break

        print("\nKolej bota:")
        bot_row = random.randint(0, 4)
        bot_col = random.randint(0, 4)
        while player_board[bot_row][bot_col] == 'X' or player_board[bot_row][bot_col] == 'O':
            bot_row = random.randint(0, 4)
            bot_col = random.randint(0, 4)
        shoot(bot_row, bot_col, player_board)
        os.system("cls")
        display_boards(show_bot_ships=False)

        #sprawdzanie czy bot wygrał
        if all(all(cell != 1 for cell in row) for row in player_board):
            print("Przegrałeś! Bot wygrał.")
            input("nie super")
            break

play_game()
