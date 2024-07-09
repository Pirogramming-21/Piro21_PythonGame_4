###### 이진 딸기 게임 ######

## 인트로: 이진딸~기 이진딸기 이진딸기이진딸기이진딸~기
"""
### 이진 딸기 게임 룰 ###
1. 1부터 15까지를 이진법으로 나타냄
   -> 0001, 0010, 0011, 0100, ..., 1111
2. 0에는 침묵하고 1에서 딸기라고 외치면 됨
3. 15까지 가면 역순으로 내려옴
"""
import random
import time

def explanation():
   print("~~~~~~~~~~~~~ 🍓 이진 딸기 게임 룰 🍓 ~~~~~~~~~~~~~")
   print("1. 1부터 15까지 이진법으로 나타낸다! (1 => 0001, 15 => 1111)")
   print("2. 0에서는 '-'를 입력하고 1에서는 '딸기'를 한 줄로 입력한다!")
   print("** 각 입력 사이에는 공백 필수!! **")
   print("** 7초 안에 입력은 필수!! **")
   print("3. 15까지 가면 역순으로 내려온다!")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
# current_num을 이진 딸기 버전으로 변환하는 함수
def to_bin_strawberry(current_num):
   # current_num을 2진수로 변환
   bin_current_num = bin(current_num)
   bin_current_num = bin_current_num[2:]
   bin_current_num = bin_current_num.zfill(4)

   bin_straw_ans = []
   for i in range(4):
      if bin_current_num[i] == '0':
         bin_straw_ans.append('-')
      else:
         bin_straw_ans.append('딸기')
   
   return bin_straw_ans

def bin_strawberry_game(invited_players, starter):
   print("❗️0에서는 '-'를 입력해주세요❗️")
   ex = input("게임 설명을 원하시면 'y'를 눌러주세요!(원하시지 않으면 아무키나 눌러주세요!): ")

   if ex == 'y':
      explanation()
      print("3초 뒤 게임이 시작됩니다")
      time.sleep(3)

   # 인트로
   print("~~~~~~~~~~~~~ 🍓 게임 START!! 🍓 ~~~~~~~~~~~~~")
   print("🍓이진딸~기 이진딸기 이진딸기이진딸기이진딸~기🍓")

   # 현재 숫자
   current_num = 1
   # 현재 player의 index
   current_player = invited_players.index(starter)
   # 15까지 도달했는지 확인하는 flag
   current_num_flag = 0
   # 게임이 몇 번 돌았는지 확인하는 cnt
   game_cnt = 1
   # 틀림을 확인하는 flag
   wrong_flag = 0

   while(1):
      if game_cnt == 16:
         time.sleep(2)
         print(f"이 게임~ 누가 했어~ {starter}가 했어~ 네가 마셔~~")
         return starter

      # 만약 현재 player가 사용자라면
      if invited_players[-1] == invited_players[current_player]:
         start_time = time.time()
         answer = input(f"{invited_players[current_player]}(7초 안에 입력해주세요): ").split()
         end_time = time.time()

         if end_time - start_time > 7:
            print("시간은 생명!! 생명!! 생명~ 생명~ 생명~")
            wrong_flag = 1
      # 만약 현재 player가 사용자가 아니라면
      # (current_num) ~ (current_num+1) 중 숫자 하나를 무작위로 선택
      else:
         random_ans = random.randint(current_num, current_num + 1)
         answer = to_bin_strawberry(random_ans)
         print(f"{invited_players[current_player]}: ", end="")
         time.sleep(2)
         print(*answer)
      
      if wrong_flag == 1:
         break
         
      # player가 말해야하는 정답을 담은 list
      bin_straw_ans = to_bin_strawberry(current_num)

      for i in range(4):
         # 정답을 틀리게 말했다면 while문 탈출
         if answer[i] != bin_straw_ans[i]:
            wrong_flag = 1
            time.sleep(1)
            print(f"{invited_players[current_player]}님이 틀리셨습니다!")
            break
      
      if wrong_flag == 1:
         break
      else:
         # 다음 player로 넘겨줌
         if len(invited_players) - 1 == current_player:
            current_player = 0
         else:
            current_player += 1
         
         # 만약 15에 도달하면 flag -> 1
         if current_num == 15:
            current_num_flag = 1
         
         # 15에 도달 -> flag:1 -> current_num--
         if current_num_flag == 1:
            current_num -= 1
         else:
            current_num += 1
         
         game_cnt += 1
   
   return invited_players[current_player]