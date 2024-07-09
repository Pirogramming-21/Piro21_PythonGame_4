def print_game_over_screen(died_player_list):
    title_text = """
    ____  ________  _____ ______   _______           ________  ___      ___ _______   ________     
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / \ \   __/|\ \  \|\  \   
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|
 __  .___________. __     _______.   .___________. __  .___  ___.  _______    .___________.  ______        _______   ______   
|  | |           |(_ )   /       |   |           ||  | |   \/   | |   ____|   |           | /  __  \      /  _____| /  __  \  
|  | `---|  |----` |/   |   (----`   `---|  |----`|  | |  \  /  | |  |__      `---|  |----`|  |  |  |    |  |  __  |  |  |  | 
|  |     |  |            \   \           |  |     |  | |  |\/|  | |   __|         |  |     |  |  |  |    |  | |_ | |  |  |  | 
|  |     |  |        .----)   |          |  |     |  | |  |  |  | |  |____        |  |     |  `--'  |    |  |__| | |  `--'  | 
|__|     |__|        |_______/           |__|     |__| |__|  |__| |_______|       |__|      \______/      \______|  \______/  
.______    __  .______        ______                   ______   ______    _______   __  .__   __.   _______                   
|   _  \  |  | |   _  \      /  __  \       ___       /      | /  __  \  |       \ |  | |  \ |  |  /  _____|                  
|  |_)  | |  | |  |_)  |    |  |  |  |     ( _ )     |  ,----'|  |  |  | |  .--.  ||  | |   \|  | |  |  __                    
|   ___/  |  | |      /     |  |  |  |     / _ \/\   |  |     |  |  |  | |  |  |  ||  | |  . `  | |  | |_ |                   
|  |      |  | |  |\  \----.|  `--'  |    | (_>  <   |  `----.|  `--'  | |  '--'  ||  | |  |\   | |  |__| |                   
| _|      |__| | _| `._____| \______/      \___/\/    \______| \______/  |_______/ |__| |__| \__|  \______|  
    """
    
    if len(died_player_list) == 0:
        print("\n다음 번에 만나요..ㅠㅠ")
    else:
        print("\n")
        for player in died_player_list:
            print(f"{player}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzzz")
        
    print(title_text)

def end_game(invited_players, fatal_limits, current_drinks):
    died_player_list = []
    for player, drinks in current_drinks.items():
        if drinks >= fatal_limits[player]:
            died_player_list.append(player)
    print_game_over_screen(died_player_list)