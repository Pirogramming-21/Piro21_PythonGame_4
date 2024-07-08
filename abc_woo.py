import random
import string
import time
import nltk

nltk.download('words', quiet=True)

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
def abc_game(players, starter):
    current_player = players.index(starter)
    current_letter = random.choice(string.ascii_lowercase)
    turn_count = 0

    print("\n🍺 ABC 게임에 오신 것을 환영합니다! 🍺")
    if input("게임 설명이 필요하신가요? (0: 아니오, 1: 예): ").strip() == '1':
        print("\n게임 설명:")
        print("1. 각 플레이어는 순서대로 알파벳에 해당하는 단어를 입력하세요.")
        print("2. 올바른 단어를 입력하면 다음 알파벳으로 넘어갑니다.")
        print("3. 게임을 종료하려면 'exit'을 입력하세요.")
        print("4. 올바르지 않은 단어를 입력하거나 주어진 알파벳으로 시작하지 않는 단어를 입력하면 술을 마셔야 합니다.")
        print("5. 치사량에 도달한 플레이어는 게임에서 제외됩니다.")
        time.sleep(3)
        
    print(f"게임은 '{current_letter.upper()}'부터 시작합니다. 🍺")
    time.sleep(3)

    game_over = False
    target_name = None
    while not game_over and current_letter <= 'z':
        player = players[current_player]
        print(f"\n{player}의 차례입니다.")
        
        if player == players[-1]:
            word = input(f"{player}의 차례입니다. '{current_letter.upper()}'로 시작하는 단어를 입력하세요: ").strip()
        else:
            word = generate_computer_word(current_letter)
            print(f"{player}의 차례입니다. '{current_letter.upper()}'로 시작하는 단어를 입력하세요: {word}")

        if word.lower() == 'exit':
            print("게임이 종료되었습니다.")
            return current_player, target_name, turn_count

        if is_valid_word(word, current_letter):
            print(f"'{word}'는 올바른 단어입니다! 🍺")
            current_letter = chr(ord(current_letter) + 1) if current_letter != 'z' else 'a'
            current_player = (current_player + 1) % len(players)
            turn_count += 1

            if turn_count == 12:
                print("3턴 동안 틀리지 않았습니다. 모두 술을 마십니다! 🍺")
                return current_player, 'all', turn_count
        else:
            print(f"'{word}'는 올바른 단어가 아니거나 '{current_letter.upper()}'로 시작하지 않습니다. 🍺")
            print(f"이 게임 누가 했어? {player} (이)가 했어! {player} (이)가 마셔~~~")
            game_over = True
            target_name = player
            turn_count = 0

        time.sleep(3)

    print("게임이 종료되었습니다.")
    return current_player, target_name, turn_count