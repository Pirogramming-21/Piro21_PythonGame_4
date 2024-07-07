###### 이진 딸기 게임 ######

## 인트로: 이진딸~기 이진딸기 이진딸기이진딸기이진딸~기
"""
### 이진 딸기 게임 룰 ###
1. 1부터 15까지를 이진법으로 나타냄
   -> 0001, 0010, 0011, 0100, ..., 1111
2. 0에는 침묵하고 1에서 딸기라고 외치면 됨
3. 15까지 가면 역순으로 내려옴
"""

def explanation():
   print("~~~~~~~~~~~~~ 🍓 이진 딸기 게임 룰 🍓 ~~~~~~~~~~~~~")
   print("1. 1부터 15까지 이진법으로 나타낸다! (1 => 0001, 15 => 1111)")
   print("2. 0에서는 '-'를 입력하고 1에서는 '딸기'를 한 줄로 입력한다!")
   print("** 각 입력 사이에는 공백 필수!! **")
   print("3. 15까지 가면 역순으로 내려온다!")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   

# current_num을 이진 딸기 버전으로 변환하는 함수
def to_bin_strawberry(current_num):
   # current_num을 2진수로 변환
   bin_current_num = bin(current_num)
   bin_current_num = bin_current_num[2:]
   bin_current_num = bin_current_num.zfill(4)

   for i in range(4):
      if bin_current_num[i] == '0':
         bin_straw_ans.append('-')
      else:
         bin_straw_ans.append('딸기')
   
   return bin_straw_ans

def bin_strawberry_game(invited_players, fatal_limits, current_drinks, starter):
   print("❗️0에서는 '-'를 입력해주세요❗️")
   ex = input("게임 설명을 보기 원하시나요? (y/n): ")

   if ex == 'y':
      explanation()
   else:
      # 인트로
      print("~~~~~~~~~~~~~ 🍓 게임 START!! 🍓 ~~~~~~~~~~~~~")
      print("🍓이진딸~기 이진딸기 이진딸기이진딸기이진딸~기🍓")

      # 현재 숫자
      current_num = 1
      # 현재 player의 index
      current_player = invited_players.find(starter)
      # 정답 판별을 위한 flag
      flag = 0

      while(1):
         answer = map(string, input(f"{invite_players[current_player]}: ").split())
         
         # player가 말해야하는 정답을 담은 list
         bin_straw_ans = bin_strawberry(current_num)

         for i in range(4):
            # 정답을 틀리게 말했다면
            if answer[i] != bin_straw_ans[i]:
               flag = 1
               break


         # 사용자의 순서라면
         if currentIndex == 0: