import random
import string
import nltk

nltk.download('words')

from nltk.corpus import words

# 단어 목록 로드
word_list = set(words.words())

# 단어 유효성 검사 함수
def is_valid_word(word, letter):
    return len(word) > 1 and word[0].lower() == letter.lower() and word in word_list

# 컴퓨터가 단어를 생성하는 함수
def generate_computer_word(letter):
    possible_words = [word for word in word_list if word.startswith(letter) and len(word) > 1]
    return random.choice(possible_words) if possible_words else 'exit'

# ABC 게임 함수
def abc_game(players, current_drinks, fatal_limits, starter):
    current_player = players.index(starter)
    current_letter = random.choice(string.ascii_lowercase)

    print("\nABC 게임에 오신 것을 환영합니다!")
    print("각 플레이어는 순서대로 알파벳에 해당하는 단어를 입력하세요.")
    print("게임을 종료하려면 'exit'을 입력하세요.")
    print(f"게임은 '{current_letter.upper()}'부터 시작합니다.")

    game_over = False
    while not game_over and current_letter <= 'z':
        player = players[current_player]
        
        if player == players[-1]:  # 마지막 플레이어가 사용자가 됨
            word = input(f"{player}의 차례입니다. '{current_letter.upper()}'로 시작하는 단어를 입력하세요: ")
        else:
            word = generate_computer_word(current_letter)
            print(f"{player}의 차례입니다. '{current_letter.upper()}'로 시작하는 단어를 입력하세요: {word}")

        if word.lower() == 'exit':
            print("게임이 종료되었습니다.")
            return [player, current_drinks]

        if is_valid_word(word, current_letter):
            print(f"'{word}'는 올바른 단어입니다!")
            current_letter = chr(ord(current_letter) + 1) if current_letter != 'z' else 'a'  # 다음 알파벳으로 이동
            current_player = (current_player + 1) % len(players)  # 다음 플레이어로 이동
        else:
            print(f"'{word}'는 올바른 단어가 아니거나 '{current_letter.upper()}'로 시작하지 않습니다.")
            print(f"{player}가 게임에서 졌습니다.")
            current_drinks[player] += 1
            if current_drinks[player] >= fatal_limits[player]:
                print(f"{player}가 치사량에 도달했습니다. 게임을 종료합니다.")
            game_over = True
    
    return [players[current_player], current_drinks]