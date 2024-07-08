def print_intro():
    intro = '''
-------------------------------------------------------------------------------------------------------------------------------
       ___       __        ______   ______    __    __    ______    __           _______      ___      .___  ___.  _______ 
      /   \     |  |      /      | /  __  \  |  |  |  |  /  __  \  |  |         /  _____|    /   \     |   \/   | |   ____|
     /  ^  \    |  |     |  ,----'|  |  |  | |  |__|  | |  |  |  | |  |        |  |  __     /  ^  \    |  \  /  | |  |__   
    /  /_\  \   |  |     |  |     |  |  |  | |   __   | |  |  |  | |  |        |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
   /  _____  \  |  `----.|  `----.|  `--'  | |  |  |  | |  `--'  | |  `----.   |  |__| |  /  _____  \  |  |  |  | |  |____ 
  /__/     \__\ |_______| \______| \______/  |__|  |__|  \______/  |_______|    \______| /__/     \__\ |__|  |__| |_______|
                                              
                                     ღ(¯`◕‿◕´¯) ♫ ♪ ♫  by K-장s  ♫ ♪ ♫ (¯`◕‿◕´¯)ღ
--------------------------------------------------------------------------------------------------------------------------------
'''
    print(intro)

def start_game():
    print_intro()
    while True:
        choice = input("게임을 진행할까요? (y/n): ")
        if choice.lower() == 'y':
            print("게임을 시작합니다!")
            # 여기에 main
            break
        elif choice.lower() == 'n':
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. y 또는 n을 입력해주세요.")

if __name__ == "__main__":
    start_game()