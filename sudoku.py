import random
from time import perf_counter, sleep

def initialize_board_4x4():
    row0 = [1, 2, 3, 4]
    random.shuffle(row0)
    row1 = [row0[2], row0[3], row0[0], row0[1]]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = [row0[3], row0[2], row0[1], row0[0]]
    board = [row0, row1, row2, row3]
    return board

def initialize_board_6x6():
    row0 = [1, 2, 3, 4, 5, 6]
    random.shuffle(row0)
    row1 = [row0[3], row0[4], row0[5], row0[0], row0[1], row0[2]]
    row2 = [row0[2], row0[0], row0[1], row0[5], row0[3], row0[4]]
    row3 = [row0[5], row0[3], row0[4], row0[2], row0[0], row0[1]]
    row4 = [row0[1], row0[2], row0[0], row0[4], row0[5], row0[3]]
    row5 = [row0[4], row0[5], row0[3], row0[1], row0[2], row0[0]]
    board = [row0, row1, row2, row3, row4, row5]
    return board

def shuffle_ribbons(board):
    top = board[:2]
    mid = board[2:4]
    bottom = board[4:]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    return top + mid + bottom

def shuffle_ribbons2(board):
    top = board[:3]
    bottom = board[3:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    size = len(board)
    transposed = []
    for _ in range(size):
        transposed.append([])
    for row in board:
        for j in range(size):
            transposed[j].append(row[j])
    return transposed

def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def create_solution_board_6x6():
    board = initialize_board_6x6()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons2(board)
    board = transpose(board)
    return board

def copy_board(board):
    return [row[:] for row in board]

def get_level():
    level = input("난이도(초급(10점) : 1, 중급(20점) : 2, 고급(30점) : 3)를 숫자로 입력해주세요 : ")
    while level not in ("1", "2", "3"):
        level = input("난이도(초급(10점) : 1, 중급(20점) : 2, 고급(30점) : 3)를 숫자로 입력해주세요 : ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10
    
def make_holes(board, no_of_holes):
    size = len(board)
    while no_of_holes > 0:
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1            
    return board

def show_board(board):
    size = len(board)
    header = "S | " + " ".join(str(i + 1) for i in range(size))
    print(header)
    print("-" * len(header))
    row_number = 1
    for row in board:
        print(row_number, "|", end=' ')
        for entry in row:
            print('.' if entry == 0 else entry, end=' ')
        print()
        row_number += 1

def get_integer(message, i, j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

def play_sudoku_game(size, current_drinks, invited_players, user_name):
    start = perf_counter()
    solution_board = create_solution_board_4x4() if size == 1 else create_solution_board_6x6()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)

    score = 0
    while no_of_holes > 0:
        i = get_integer(f"가로줄번호(1~{len(puzzle_board)}): ", 1, len(puzzle_board)) - 1
        j = get_integer(f"세로줄번호(1~{len(puzzle_board)}): ", 1, len(puzzle_board)) - 1
        if puzzle_board[i][j] != 0:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer(f"숫자(1~{len(puzzle_board)}): ", 1, len(puzzle_board))
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
            score += 5
        else:
            print(n, "가(이) 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 당신의 점수가 5초 후에 공개됩니다.")
    score += 10
    finish = perf_counter()
    playing_time = round((finish - start) / 60, 1)
    sleep(5)
    
    if size == 1:
        if playing_time <= 2:
            print(playing_time, "분 걸렸습니다. 🍺나 빼고 모두 한 잔!🍺")
            target_name = "another_me"
            for player in invited_players:
                if player != user_name:
                    current_drinks[player] += 1
        elif 2 < playing_time <= 5:
            print(playing_time, "분 걸렸습니다. 🍺다 같이 한 잔!🍺")
            target_name = "all_target"
            for player in invited_players:
                current_drinks[player] += 1
        else:
            print(playing_time, "분 걸렸습니다. 🍺나만 한 잔!🍺")
            target_name = user_name
            current_drinks[user_name] += 1
    else:
        if playing_time <= 5:
            print(playing_time, "분 걸렸습니다. 🍺나 빼고 모두 한 잔!🍺")
            target_name = "another_me"
            for player in invited_players:
                if player != user_name:
                    current_drinks[player] += 1
        elif 5 < playing_time <= 10:
            print(playing_time, "분 걸렸습니다. 🍺다 같이 한 잔!🍺")
            target_name = "all_target"
            for player in invited_players:
                current_drinks[player] += 1
        else:
            print(playing_time, "분 걸렸습니다. 🍺나만 한 잔!🍺")
            target_name = user_name
            current_drinks[user_name] += 1

    return target_name, current_drinks  # 타겟 이름과 게임 결과 반환

def sudoku_game(current_drinks, invited_players, user_name):
    print("\n🍺 WELCOME TO SUDOKU WORLD! 🍺")
    if input("게임 설명이 필요하신가요? (0: 아니오, 1: 예): ").strip() == '1':
        print("\n게임 설명:")
        print("1. 보드 크기를 선택하세요 (4x4 또는 6x6).")
        print("2. 난이도를 선택하세요 (초급, 중급, 고급).")
        print("3. 빈칸에 올바른 숫자를 입력하여 보드를 완성하세요.")
        print("4. 올바른 숫자를 입력하면 점수를 얻습니다.")
        print("5. 잘못된 숫자를 입력하면 다시 시도해야 합니다.")
        print("\n벌칙 설명:")
        print("1. 초급 난이도에서 2분 이하로 완료하면 나 빼고 모두 한 잔!")
        print("2. 중급 난이도에서 5분 이하로 완료하면 나 빼고 모두 한 잔!")
        print("3. 모든 난이도에서 2~5분(초급), 5~10분(중급) 걸리면 다 같이 한 잔!")
        print("4. 모든 난이도에서 더 오래 걸리면 나만 한 잔!")
        sleep(5)

    board_size = int(input("스도쿠 보드 크기를 선택하세요 (1: 4x4, 2: 6x6): ").strip())
    target_name, current_drinks = play_sudoku_game(board_size, current_drinks, invited_players, user_name)
    print("게임을 종료합니다. 수고하셨습니다!")
    return target_name, current_drinks  # 타겟 이름과 게임 결과 반환