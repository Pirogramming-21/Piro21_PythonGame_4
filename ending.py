def print_game_over_screen(died_player_list):
    title_text = """
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______                                       
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \                                      
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |                                     
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /                                      
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.                                 
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|                                 
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

  __ _  __ _  _ __   ___   ___ __ __ ___  _ _ 
 / _` |/ _` || '  \ / -_) / _ \\ V // -_)| '_|
 \__, |\__,_||_|_|_|\___| \___/ \_/ \___||_|  
 |___/ 
 
  ________  ________  _____ ______   _______           ________  ___      ___ _______   ________     
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / \ \   __/|\ \  \|\  \   
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|
    
                                                                                                                                                              
    """
    if len(died_player_list) != 0:
      for player in died_player_list:
        print(f"{player}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzzz")

    print(title_text)

print_game_over_screen(died_player_list)