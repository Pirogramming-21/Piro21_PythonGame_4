# 자물쇠 게임 함수
import random


def lock_game(players, user_name):
    secret_code = [random.randint(0, 9) for _ in range(4)]
    attempts = 0
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("🔐자물쇠 비밀번호 맞추기 게임입니다!!!!🔐")
    print("비밀번호는 0~9 사이의 숫자 4자리이며, 중복 가능합니다.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    while True:
        for player in players:
            if player == user_name:
                attempts += 1
                print(f"{player}님, 4자리 숫자를 입력하세요: ")
                guess = input()
                
                if len(guess) != 4 or not guess.isdigit():
                    print("잘못된 입력입니다. 4자리 숫자를 입력하세요.")
                    continue
                
                guess = list(map(int, guess))
                feedback = []
                
                for i in range(4):
                    if guess[i] < secret_code[i]:
                        feedback.append("UP")
                    elif guess[i] > secret_code[i]:
                        feedback.append("DOWN")
                    else:
                        feedback.append("CORRECT")
                
                print("피드백:", feedback)
                
                if guess == secret_code:
                    print(f"{player}님이 비밀번호를 맞췄습니다!")
                    return player
            else:
                random_num = [random.randint(0, 9) for _ in range(4)]
                print(f"{player}님, 4자리 숫자를 입력하세요: ") 
                print(''.join(map(str, random_num)))
                
                feedback = []
                
                for i in range(4):
                    if random_num[i] < secret_code[i]:
                        feedback.append("UP")
                    elif random_num[i] > secret_code[i]:
                        feedback.append("DOWN")
                    else:
                        feedback.append("CORRECT")

                print("피드백:", feedback)
                
                if random_num == secret_code:
                    print(f"{player}가 비밀번호를 맞췄습니다!")
                    return player

        print("비밀번호를 맞추지 못했습니다. 게임을 계속합니다.")