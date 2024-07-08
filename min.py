import random
import time

# 지하철 노선 정보 
# 서울 지하철 1호선
line1 = [
    "소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사",
    "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문", "외대앞", "회기", "청량리", "제기동",
    "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청", "서울역", "남영", "용산", "노량진", "대방",
    "신길", "영등포", "신도림", "구로", "가산디지털단지", "독산", "금천구청", "석수", "관악", "안양", "명학", "금정",
    "군포", "당정", "의왕", "성균관대", "화서", "수원", "세류", "병점", "세마", "오산대", "오산", "진위", "송탄",
    "서정리", "지제", "평택", "성환", "직산", "두정", "천안", "봉명", "쌍용", "아산", "배방", "온양온천", "신창"
]

# 서울 지하철 2호선
line2 = [
    "시청", "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리", "한양대", "뚝섬",
    "성수", "건대입구", "구의", "강변", "잠실나루", "잠실", "잠실새내", "종합운동장", "삼성", "선릉", "역삼", "강남",
    "교대", "서초", "방배", "사당", "낙성대", "서울대입구", "봉천", "신림", "신대방", "구로디지털단지", "대림", "신도림",
    "문래", "영등포구청", "당산", "합정", "홍대입구", "신촌", "이대", "아현", "충정로"
]

# 서울 지하철 3호선
line3 = [
    "대화", "주엽", "정발산", "마두", "백석", "대곡", "화정", "원당", "원흥", "삼송", "지축", "구파발", "연신내", "불광",
    "녹번", "홍제", "무악재", "독립문", "경복궁", "안국", "종로3가", "을지로3가", "충무로", "동대입구", "약수", "금호",
    "옥수", "압구정", "신사", "잠원", "고속터미널", "교대", "남부터미널", "양재", "매봉", "도곡", "대치", "학여울",
    "대청", "일원", "수서", "가락시장", "경찰병원", "오금"
]

# 서울 지하철 4호선
line4 = [
    "당고개", "상계", "노원", "창동", "쌍문", "수유", "미아", "미아사거리", "길음", "성신여대입구", "한성대입구", "혜화",
    "동대문", "동대문역사문화공원", "충무로", "명동", "회현", "서울역", "숙대입구", "삼각지", "신용산", "이촌", "동작",
    "총신대입구", "사당", "남태령", "선바위", "경마공원", "대공원", "과천", "정부과천청사", "인덕원", "평촌", "범계",
    "금정", "산본", "수리산", "대야미", "반월", "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕",
    "오이도"
]

# 서울 지하철 5호선
line5 = [
    "방화", "개화산", "김포공항", "송정", "마곡", "발산", "우장산", "화곡", "까치산", "신정", "목동", "오목교", "양평",
    "영등포구청", "영등포시장", "신길", "여의도", "여의나루", "마포", "공덕", "애오개", "충정로", "서대문", "광화문",
    "종로3가", "을지로4가", "동대문역사문화공원", "청구", "신금호", "행당", "왕십리", "마장", "답십리", "장한평",
    "군자", "아차산", "광나루", "천호", "강동", "길동", "굽은다리", "명일", "고덕", "상일동"
]

# 서울 지하철 6호선
line6 = [
    "응암", "역촌", "불광", "독바위", "연신내", "구산", "응암", "새절", "증산", "디지털미디어시티", "월드컵경기장", "마포구청",
    "망원", "합정", "상수", "광흥창", "대흥", "공덕", "효창공원앞", "삼각지", "녹사평", "이태원", "한강진", "버티고개",
    "약수", "청구", "신당", "동묘앞", "창신", "보문", "안암", "고려대", "월곡", "상월곡", "돌곶이", "석계", "태릉입구",
    "화랑대", "봉화산", "신내"
]

# 서울 지하철 7호선
line7 = [
    "장암", "도봉산", "수락산", "마들", "노원", "중계", "하계", "공릉", "태릉입구", "먹골", "중화", "상봉", "면목", "사가정",
    "용마산", "중곡", "군자", "어린이대공원", "건대입구", "뚝섬유원지", "청담", "강남구청", "학동", "논현", "반포",
    "고속터미널", "내방", "이수", "남성", "숭실대입구", "상도", "장승배기", "신대방삼거리", "보라매", "신풍", "대림",
    "남구로", "가산디지털단지", "철산", "광명사거리", "천왕", "온수", "까치울", "부천종합운동장", "춘의", "신중동",
    "부천시청", "상동", "삼산체육관", "굴포천", "부평구청"
]

# 서울 지하철 8호선
line8 = [
    "암사", "천호", "강동구청", "몽촌토성", "잠실", "석촌", "송파", "가락시장", "문정", "장지", "복정", "산성", "남한산성입구",
    "단대오거리", "신흥", "수진", "모란"
]

# 서울 지하철 9호선
line9 = [
    "개화", "김포공항", "공항시장", "신방화", "마곡나루", "양천향교", "가양", "증미", "등촌", "염창", "신목동", "선유도",
    "당산", "국회의사당", "여의도", "샛강", "노량진", "노들", "흑석", "동작", "구반포", "신반포", "고속터미널", "사평",
    "신논현", "언주", "선정릉", "삼성중앙", "봉은사", "종합운동장", "삼전", "석촌고분", "석촌", "송파나루", "한성백제",
    "올림픽공원", "둔촌오륜", "중앙보훈병원"
]

subway_lines = {
    1: line1, 2: line2, 3: line3, 4: line4, 5: line5,
    6: line6, 7: line7, 8: line8, 9: line9
}

def select_line():
    while True:
        line = input("몇 호선으로 게임을 시작할까요? (1-9): ")
        if line.isdigit() and 1 <= int(line) <= 9:
            return int(line)
        else:
            print("1에서 9 사이의 숫자를 입력해주세요.")

def invited_players_turn(line_number, used_stations):
    main_line = subway_lines[line_number]
    adjacent_line = subway_lines[min(line_number + 1, 9)]
    
    available_stations = set(main_line + adjacent_line) - used_stations
    if not available_stations:
        return None
    invited_players_line = random.choice(list(available_stations))
    return invited_players_line

def subway_game(user, players, starter):
    used_stations = set()
    # 현재 player의 index
    current_player = players.index(starter)

    print("지하철 게임에 오신 것을 환영합니다!")
    if(current_player == user) : # user랑 같다면  
        line_number = select_line()
    else: 
        line_number = random.randint(1, 9)
    
    print("지~하철 지하철! 지~하철 지하철! 몇호선~ 몇호선! 몇호선~ 몇호선!")
    print(f"{line_number}호선~~ {line_number}호선~~")

    game_over = False
    while not game_over:
        player = players[current_player]
        print(f"\n{player}의 차례입니다.")
        
        if current_player == user:  #사용자일 때
            start_time = time.time()
            station = input("5초 안에 역 이름을 입력하세요 (게임 종료: '종료' 입력): ").strip()
            end_time = time.time()

            # 종료 입력하면
            if station.lower() == '종료':
                break

            if end_time - start_time > 5:
                print("시간은 생명!! 생명!! 생명~ 생명~ 생명~")
                game_over = True
            
            elif station in used_stations:
                print("이미 사용된 역이잖아~")
                game_over = True

            elif station not in subway_lines[line_number]:
                print(f"이 역은 {line_number}호선에 없습니다!!!")
                game_over = True
                
            else:
                print("정답입니다!")
                used_stations.add(station)
                current_player = (current_player + 1) % len(players)
            
        else: # invited_player일 때
            station = invited_players_turn(line_number, used_stations)
            time.sleep(2)
            print(f"{station}!!")
            if station is None:
                print("남은 역이 없습니다~")
                game_over = True

            elif station in used_stations:
                print("이미 사용된 역이잖아~")
                game_over = True

            elif station not in subway_lines[line_number]:
                print(f"이 역은 {line_number}호선에 없습니다!!!")
                game_over = True

            else:
                print("정답입니다!")
                used_stations.add(station)
                current_player = (current_player + 1) % len(players)

    return players[current_player]