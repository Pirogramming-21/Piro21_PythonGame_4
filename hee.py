import random
import time

def get_feedback(secret_code, guess):
    feedback = []
    for i in range(4):
        if guess[i] < secret_code[i]:
            feedback.append("UP")
        elif guess[i] > secret_code[i]:
            feedback.append("DOWN")
        else:
            feedback.append("CORRECT")
    return feedback

def make_guess(player, secret_code, is_user=False):
    if is_user:
        user_input = input(f"{player}님, 4자리 숫자를 입력하세요: ")
        random_num = [int(digit) for digit in user_input]
    else:
        random_num = [random.randint(0, 9) for _ in range(4)]
        time.sleep(2)
        print(f"{player}님, 4자리 숫자를 입력하세요: ")
        time.sleep(1)
        print(''.join(map(str, random_num)))

    feedback = get_feedback(secret_code, random_num)
    print("피드백:", feedback)
    
    if random_num == secret_code:
        print(f"🎊🎊🎊축하합니다, {player}님이 비밀번호를 맞췄습니다!!!!!🎊🎊🎊")
        print(f"              🎉 {player}님의 치사량 UP~!!!!! 🎉              ")
        return True
    return False

def lock_game(players, user_name):
    target_name = players[-1]
    secret_code = [random.randint(0, 9) for _ in range(4)]
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("         🔐자물쇠 비밀번호 맞추기 게임입니다!!!!🔐         ")
    print("    비밀번호는 0~9 사이의 숫자 4자리이며, 중복 가능합니다.   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    for player in players:
        if player == user_name:
            if make_guess(player, secret_code, is_user=True):
                return player

    while True:
        for player in players:
            if make_guess(player, secret_code, is_user=(player == user_name)):
                return player
        time.sleep(1)
        print("비밀번호를 맞추지 못했습니다. 게임을 계속합니다.")