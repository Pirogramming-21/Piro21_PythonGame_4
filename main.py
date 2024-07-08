import random
import time
from hee import lock_game
from abc_woo import abc_game
from sudoku import sudoku_game
from jy import bin_strawberry_game
from min import subway_game
from intro import start_game

# 플레이어 초대 함수
def invite_players(max_players=4):
    available_players = ["주희", "관우", "송민", "지요"]
    num_players = int(input(f"초대할 플레이어 수를 입력하세요 (최대 {max_players}명): "))
    
    if num_players > max_players:
        print(f"최대 {max_players}명만 초대할 수 있습니다.")
        return invite_players(max_players)
    
    invited_players = random.sample(available_players, num_players)
    print("초대된 플레이어:", *invited_players)
    
    return invited_players

# 음주 상태 출력 및 확인 함수
def drinking_status(invited_players, fatal_limits, current_drinks):
    time.sleep(2)
    # 치사량에 도달한 player의 이름을 담는 리스트
    died_player_list = []
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for player in invited_players:
        remaining = fatal_limits[player] - current_drinks[player]
        print(f"{player}는(은) 지금까지 {current_drinks[player]}잔! 치사량까지 {remaining}잔")
        if remaining <= 0:  # 치사량을 초과한 경우를 포함하도록 수정
            died_player_list.append(player)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return died_player_list

# 게임 리스트 출력 및 선택 함수
def print_game_list(starter, user_name):
    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~ 오늘의 Alcohol GAME 🍺 ~~~~~~~~~~~~~~~~~")
    print("         🍺 1. 자물쇠 비밀번호를 맞춰라~ 치사량 UP!!")
    print("         🍺 2. 나랑 ABC하러 갈래~~~~~?")
    print("         🍺 3. 피로그래머라면 이진 딸기🍓 먹으러 가자🫨")
    print("         🍺 4. 지하철 정복하러 가자!!")
    print("         🍺 5. WELCOME TO SUDOKU WORLD!")
    print("         🍺 6. 게임 종료")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(2)
    if starter == user_name:
        game_num = input(f"{starter}(이)가~ 좋아하는~ 랜덤~ 게임~ 무슨~ 게임~: ")
    else:
        game_num = str(random.randint(1, 6))  # 게임 선택을 문자열로 반환하도록 수정
        print(f"{starter}(이)가~ 좋아하는~ 랜덤~ 게임~ 무슨~ 게임~: {game_num}")
    
    time.sleep(2)
    return game_num

def limit_set(user_name):
    print("~~~~~~~~~~~~~ 🍺 소주 기준 당신의 주량은? 🍺 ~~~~~~~~~~~~~")
    print("            🍺 1. 소주 반병 (2잔)")
    print("            🍺 2. 소주 반병 ~ 한병 (4잔)")
    print("            🍺 3. 소주 한병 ~ 한병 반 (6잔)")
    print("            🍺 4. 소주 한병 반에서 두병 (8잔)")
    print("            🍺 5. 소주 두병 이상 (10잔)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while(True):
        limit_num = int(input(f"{user_name}님, 당신의 치사량을 입력하세요: "))
        if limit_num == 1:
            fatal_limit = 2
            break
        elif limit_num == 2:
            fatal_limit = 4
            break
        elif limit_num == 3:
            fatal_limit = 6
            break
        elif limit_num == 4:
            fatal_limit = 8
            break
        elif limit_num == 5:
            fatal_limit = 10
            break
        else:
            print("잘못된 번호를 입력하였습니다. 다시 입력해주세요.")

    print(f"{user_name}님, 당신의 치사량은 {fatal_limit}잔 입니다.")
    return fatal_limit

# 타겟 플레이어의 current_drinks 조절 함수
def adjust_drinks(target_name, current_drinks):
    current_drinks[target_name] += 1
    print(f"🍺누가 술을 마셔 {target_name}이(가) 술을 마셔🍺 원~~~샷!!!")

# 메인 함수
def main():
    user_name = input("당신의 이름을 입력하세요: ")
    # 유저의 치사량 설정
    user_fatal_limit = limit_set(user_name)
   
    # 초대할 친구들 설정
    invited_players = invite_players()
    # 모든 player가 들어있는 invited_players
    invited_players.append(user_name)
   
    # player들의 이름과 치사량이 들어있는 dictionary
    fatal_limits = {player: random.randint(1, 10) for player in invited_players}
    fatal_limits[user_name] = user_fatal_limit
   
    # player들의 이름과 현재까지 마신 잔 수가 들어있는 dictionary
    current_drinks = {player: 0 for player in invited_players}

    # 다음 게임 플레이어의 이름 (초기 player: 사용자)
    target_name = user_name
    
    while True:
        # 음주 상태 확인 및 출력
        died_player_list = drinking_status(invited_players, fatal_limits, current_drinks)
        # 전사한 사람이 있다면 while문 탈출
        if len(died_player_list) != 0:
            break
   
        # 게임 선택
        game_choice = print_game_list(target_name, user_name)
      
        # 게임 실행
        if game_choice == '1':
            target_name = lock_game(invited_players, target_name)
            fatal_limits[target_name] += 1
        elif game_choice == '2':
            current_player, target_name, turn_count = abc_game(invited_players, target_name)
            if target_name:
                if target_name == 'all':
                    for player in invited_players:
                        adjust_drinks(player, current_drinks)
                else:
                    adjust_drinks(target_name, current_drinks)
            target_name = invited_players[current_player]
        elif game_choice == '3':
            target_name = bin_strawberry_game(invited_players, target_name)
            adjust_drinks(target_name, current_drinks)
        elif game_choice == '4':
            target_name = subway_game(invited_players.index(user_name), invited_players, target_name)
            adjust_drinks(target_name, current_drinks)
        elif game_choice == '5':
            target_name = sudoku_game(current_drinks, invited_players, user_name)
            adjust_drinks(target_name, current_drinks)
        elif game_choice == '6':
            print(f"{target_name}이(가) 게임 종료를 선택했습니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

     # 게임 오버 창 띄우기
    import ending
    ending.end_game(invited_players, fatal_limits, current_drinks)
            
if __name__ == "__main__":
    start_game()
    main()