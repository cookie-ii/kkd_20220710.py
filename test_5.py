from pydoc import locate
from unicodedata import decimal
import win32ui
import keyboard
from PIL import ImageGrab
from PIL import Image
import image
import pyautogui as pag
import cv2

import win32api
import win32gui
import win32con
import time
import random
import ctypes
import pywinauto
from ctypes import windll
from pywinauto import application
import numpy as np
macro_start = time.time()     # 전체 사이클 타임확인을 위한 시작시간 체크

# 시작 계정임다
account=0
if account == 0:
    title_t = "국왕만두만"
elif account == 1:
    title_t = "국왕꾸안꾸"
else:
    title_t = "국왕만두만"
    print('계정 뭐얏')
hWnd = win32gui.FindWindow(None, title_t)
hwakjangja = '.png'

# //// 여기부턴 조건 확인용
bWood_Quick = False         # 나무 쾌속생산!
bJelbean_Quick = False      # 젤리빈 쾌속생산!
bSugar_Quick = False        # 각설탕 쾌속생산!
bSmith_Quick = False        # 대장간 쾌속생산!
bJelbean_Quick = False      # 잼가게 쾌속생산!
bRollc_Quick = False        # 공작소 쾌속생산!
bTropicalAction_A = True    # 트로피칼 A 계정 돌릴거냐
bTropicalAction_B = True    # 트로피칼 B 계정 돌릴거냐
bResearch_auto_A = False     # 연구소 자동돌림(명확히 지정해줘야만 함..)
bResearch_auto_B = False     # 연구소 자동돌림(명확히 지정해줘야만 함..)
jjokji_limit_A = False       # 쪽지 제한 걸기(오늘 보상 다 받으면 끝냄)
jjokji_limit_B = False       # 쪽지 제한 걸기(오늘 보상 다 받으면 끝냄)
check_mark_action_A = False # 체크 마크 클릭여부(생산 건물 업글 시에는 False 해놔야 열차 녹스는 거 방지..)
check_mark_action_B = False # 체크 마크 클릭여부(생산 건물 업글 시에는 False 해놔야 열차 녹스는 거 방지..)
bAccount_A_Completed = False    # 롱텀 A 완료
bAccount_B_Completed = False    # 롱텀 B 완료
bShort_Term_ing = False     # 숏텀 모드?
tShort_Term_Start = time.time() # 초기화를 여기서 시켜줘야 하나....

bInitDoneA = False          # A 실행완료
bInitDoneB = False          # B 실행완료
bAccountA = False           # A계정(윗계정) 작업중
bAccountB = False           # B계정(아랫계정) 작업중
bZeroPointed = False        # 영점조정(맨 왼쪽 아래 화면)
bInPositionA = False        # 어디든 건물 안
bInPositionB = False        # 어디든 건물 안
bThisRoomEnd = False        # 이 생산건물 리스트 다 채움(다음 건물 넘어가며 해지)
bProducting = False         # 생산중
bCheckFound = False         # 체크표시 뜸
bHoldingTime = True         # 대기 상태
zero_adjust_A = False       # 섬 얼굴로 원점조정
zero_adjust_B = False       # 섬 얼굴로 원점조정
bProd_ready_A = False       # 간판 하나라도 보이니?
bProd_ready_B = False       # 간판 하나라도 보이니?
bUrgentA = False            # 빠른생산(기본 재료나 도끼, 젤리빈잼 등)
bUrgentB = False            # 빠른생산(기본 재료나 도끼, 젤리빈잼 등)
bStarHarvest = False        # 별사탕 수확
bTrain = False              # 곰젤리 열차
bBalloonA = False           # 곰젤리 열기구
bBalloonB = False           # 곰젤리 열기구
bResearch = False           # 연구소
bTropical = False           # 트로피칼
bAdventure = False          # 모험
bArena = False              # 아레나
bMailReceive = False        # 메일 받기
bWishTree = False           # 소원 나무
bFruitskan = False          # 후르츠칸 납품
bSmith_in_doneA = False     # A 대장간 들어옴(생산 시작 지점)
bSmith_in_doneB = False     # B 대장간 들어옴(생산 시작 지점)
bMacroTime = True           # 매크로 도는 중?
bProdHigh = False           # 동일 건물 2개인 경우 2번째 건물에서 높은 생산품 우선 생산
bSecond = False             # 두 번째 건물 작업이냐?
bAcc_A_First = False        # 계정 먼저 시작 순서(True일 때 A부터, 아니면 B부터)
bFirstCookhouA = False      # 첫 쿠하(클릭)
bFirstCookhouB = False      # 첫 쿠하(클릭)
bFirstFountainA = False     # 첫 분수(시간 확인만?)
bFirstFountainB = False     # 첫 분수(시간 확인만?)
bBbopkkiA = False           # 일일뽑기보상 받았나?
bBbopkkiB = False           # 일일뽑기보상 받았나?
bQuickUse = True            # 시계태엽(빨리감기) 쓸래?
bTropical_Confirmed_A = False # 트로피칼 확인
bTropical_Confirmed_B = False # 트로피칼 확인
# 생산 목표 수량의 80% 밑이면 아낌모드로, 소원나무에서 배제함
jjokji_biscuit_A = False            # 비스킷 아낌모드
jjokji_biscuit_B = False            # 비스킷 아낌모드
jjokji_berry_A = False              # 젤리베리 아낌모드
jjokji_berry_B = False              # 젤리베리 아낌모드
jjokji_milk_A = False               # 우유 아낌모드
jjokji_milk_B = False               # 우유 아낌모드
jjokji_cotton_A = False             # 솜사탕 아낌모드
jjokji_cotton_B = False             # 솜사탕 아낌모드
trade_legend_A = False     # 오색 조개 갤러리 전설 영혼석 살까?
trade_legend_B = False     # 오색 조개 갤러리 전설 영혼석 살까?
trade_legend_C = False     # 오색 조개 갤러리 전설 영혼석 살까?
trade_hero_A = False       # 오색 조개 갤러리 영웅 영혼석 살까?
trade_hero_B = False       # 오색 조개 갤러리 영웅 영혼석 살까?
trade_hero_C = False       # 오색 조개 갤러리 영웅 영혼석 살까?

set_max_power_A = 1300000    # 아레나 상대 전투력 Max
set_max_power_B = 1300000    # 아레나 상대 전투력 Max
fountain_set_time_A = 1800  # 분수 클릭 주기
cookie_set_time_A = 1800    # 쿠키하우스 클릭 주기
fountain_set_time_B = 1800  # 분수 클릭 주기
cookie_set_time_B = 1800    # 쿠키하우스 클릭 주기
how_many_cycle = 1          # 롱텀 생산 사이클. 대충 2면 음..
delay_to_next_account = 1   # 다음 계정 동작 전 대기시간
heart_set_num = 150          # 하트가 이 숫자보다 많으면.. 모험 실행
man_mac_time = 6000         # 수동 매크로 돌리고 파이썬 실행한 경우, 이 시간 후에 수동 매크로 끄고 자동 돌림
prod_pix_confirm = 2        # 픽셀 못읽는거 n번(스크롤업 n*2 번) 해도 안되면 좌로 넘김
jjokji_numb = 10            # 소원나무 쪽지 보내는 횟수(4개 다 짤려도 그냥 나옴)
Producting_Time = 600       # 생산 최대 시간
tShort_Term_Set = 1800      # 쑛텀 생산 시간

# 글로벌 조건 입력하는 곳(어느 곳이든 동일)
# ----------- 전체 조건 -------------
random_int = 5
easy_prod = 0.7                 # 1시간 이내 제품
normal_prod = 0.9               # 1~2시간 제품
hard_prod = 0.95                # 2시간 초과
# 킹덤패스
bReward = (121, 207, 16)        # 모두 받기 활성화
pix_pass_reward_exist = (255, 0, 0)

# 건물 내부 색상
pix_wood = (117, 57, 38)        # 나무
pix_jelbean = (1, 239, 237)     # 젤리빈
pix_white = (255, 255, 255)     # 설탕
pix_biscuit = (206, 137, 54)    # 비스킷
pix_berry = (187, 41, 46)       # 젤리베리
pix_milk = (232, 242, 242)      # 우유
pix_cotton = (255, 247, 255)    # 솜
pix_smith = (164, 116, 84)      # 도끼 스미스
pix_jelly = (13, 172, 201)      # 젤리빈 잼 젤리
pix_rollc = (215, 148, 105)     # 솔새 롤케
pix_bread = (142, 66, 10)        # 호밀빵 브레드
pix_jampy = (166, 29, 45)       # 젤리스튜 잼파이
pix_doye = (158, 84, 42)        # 비스킷 화분 - 도예
pix_flower = (254, 31, 132)     # 캔디꽃 - flower
pix_milky = (214, 229, 228)     # 크림 - milky
pix_latte = (255, 251, 239)     # 젤리빈 라떼 - latte
pix_dolls = (109, 236, 250)     # 쿠션 - dolls
pix_beer = (152, 103, 67)       # 크림루트비어 - beer
pix_muffin = (192, 91, 58)      # 머핀 - muffin
pix_jewel = (143, 99, 63)       # 글레이즈드링 - jewel
pix_magic = (92, 55, 48)        # 마법공방 - magic
pix_icecream = (254, 253, 229)  # 디즈니 아이스크림 트럭
pix_status_in = (227, 163, 2)   # 생산건물 내 07.31. 수정
pix_status_in_dark = (113, 81, 1)   # 건물 안이긴 한데 창이 떠있음
pix_status_in_magic_dark = (109, 81, 9)     # 마법공방이고 생산품 보상이 떠있음


pix_rollc_d = (237, 197, 122)   # 솔새 롤케 내린 상태
pix_bread_d = (242, 223, 195)   # 빵집 내린 상태
pix_jampy_d = (171, 183, 59)    # 젤리스튜 내린 상태
pix_doye_d = (183, 177, 249)    # 도예 내린 상태
pix_flower_d = (211, 136, 227)  # 꽃가게 내린 상태
pix_icecream_d = (225, 161, 92) # 아이스크림 내린 상태

# 왕국(건물 밖)
pix_status_out = (12, 193, 252)  # 바탕화면(왕국), 트로피컬도 동일
pix_status_out_window = (6, 97, 124)  # 창이 떠서 어두워짐
pix_status_out_esc = (6, 97, 126)  # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
pix_status_bal_lobby = (175, 131, 0) # 열기구 로비
pix_status_bal_window = (127, 95, 4)  #열기구 창 떠서 어두워짐
pix_status_kdpass = (42, 27, 19) # 킹덤패스
pix_status_warehouse = (55, 64, 105) # 창고 뜸
pix_status_mail = (60, 70, 105)  # 우편함
pix_lackof1 = (243, 233, 223)  # 베이지색
pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
pix_status_cookiehouse = (9, 138, 180) # 엥 이게 다 달라?
pix_status_lotto = (255, 208, 3)  # 뽑기, 해변교역소
pix_status_mycookie = (95, 240, 241) #내 쿠키...으... 움직이면 틀어질텐데
pix_status_fountain = (84, 93, 134) # 분수..
pix_stats_kkd_start = (11, 10, 42) # 바탕화면 나갔네
pix_status_trade = (255, 209, 2)  # 해상무역센터 로비
pix_status_wanted = (29, 10, 12)  # 오늘의 현상수배 선택하는 곳
pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
pix_status_fight_comp1 = (121, 98, 74)  # 모험 전투 후1
pix_status1_tropical = (255, 98, 170)  # 트로피칼이다
pix_status1_tropical_windowopen = (127, 49, 85)  # 트로피칼에 메뉴창 떠있다

# 곰젤리열기구
pix_status_bal_what = (85, 63, 0)
pix_status_bal_arrive = (170, 169, 168) # 열기구 보상수령(바닥 글씨 마침표)
pix_status_bal_lobby = (174, 130, 2) # 열기구 로비
pix_status_ballon = (29, 36, 46) # 열기구 날아다니는 중
pix_status_bal_window = (127, 95, 4)  #열기구 창 떠서 어두워짐

# 스샷모드
pix_clicked = (28, 39, 51)      # 클릭해서 어두워짐

# 앵무 엔터 Angmu_Enter
pix_green = (121,207,12)

# 연구소 research_action
pix_research_selected = (58, 73, 109)
pix_green = (121, 207, 12)   # 녹색(가능)
pix_grey = (160, 160, 160)   # 회색(불가능)

# 아레나 Arena_action
pix_medal_normal = (249, 206, 22) # 이건 왜지
pix_medal_normal1 = (249, 205, 21) # 이건 왜지
pix_daejun_selected = (65, 58, 56)
pix_daejun_not_selected = (69, 78, 121)

# 하트 소진 Heart_sojin
pix_adv_dark = (74, 44, 34)  # 스토리모드 어둠모드 확인

# 소원나무 sowon_jjokji_action
pix_upper_void = (46, 30, 50) # 이미지 확인공간 대기상태(아무 생산품도 클릭 안함)
pix_wait = (115, 224, 0) # 갱신하기 후 기다림 오른쪽 연두색>>체크인듯
pix_wait1 = (0, 167, 255) # 갱신하기 후 기다림 왼쪽 파란색막대기둥
pix_wait2 = (112, 222, 0) # 대기중이야..
pix_no_reward = (33, 44, 64) # 일일보상 대기상태
pix_yes_reward = (255, 255, 250)    # 일일보상 받아!

# 그 외, 기타, 차이점, 미사용
pix_stats_kkd_start = (11, 10, 42) # 바탕화면 나갔네
pix_status_arena_lobby = (197, 196, 194) # 아레나 로비화면!
pix_status_boldline_yes = (13, 16, 48)
pix_status_temple = (177, 123, 153) # 찬란한 영웅들의 신전 대기화면, 석상화면 같음
pix_status_temple_dark = (88, 61, 76) # 찬란한 영웅들의 신전 화면 어두워졌을 때(슬롯 확장 잘못누름)
pix_tier_up1 = (20, 19, 18)  # 다이아 2티어
pix_tier_up2 = (5, 4, 2)  # 마스터 5티어
# ----------------------------------

# 건물 종류
prod_build_num_list = ('몰라요', '나무', '젤리빈', '각설탕', '비스킷', '젤리베리', '우유', '솜', '대장간', '잼가게', '공작소', '빵집', '잼파이', '도예', '꽃가게', '우유 가공소', '라떼', '인형공방', '오크통 쉼터', '퐁 드 파티세리', '살롱 드 주얼리', '마법공방', '아이스크림')
# 건물 이름
building_name = ['Wood', 'Jelbean', 'Sugar', 'Biscuit', 'Berry', 'Milk', 'Cotton',
                 'Smith', 'Jelly', 'Rollc', 'Bread', 'Jampy', 'Doye', 'Flower',
                 'Milky', 'Latte', 'Doll', 'Beer', 'Muffin', 'Jewel', 'Magic', 'IceCream']
# 재고 수량 파악하는 숫자..
production_number = ('prod_1', 'prod_1_1', 'prod_2', 'prod_3',
                     'prod_3_1', 'prod_4', 'prod_4_1', 'prod_4_2',
                     'prod_5', 'prod_5_1', 'prod_6', 'prod_7',
                     'prod_8', 'prod_8_1', 'prod_9', 'prod_9_1', 'prod_0')
# 생산 렙
prod_build_prod_max = (0,3,3,3,3,3,3,3,7,5,4,6,6,4,6,3,3,3,3,3,3,14,5)
# 건물 개수
prod_build_number = (0,2,2,3,3,3,3,11,7,5,6,6,4,6,3,3,3,3,3,3,14,5)
prod_build_now = 0  # 초기값 : 몰라요
# ----------------------------------

wood_min_A = 1900
wood_max_A = 2000
wood_prod_A = 2

jelbean_min_A = 2900
jelbean_max_A = 3000
jelbean_prod_A = 2

sugar_min_A = 2900
sugar_max_A = 3000
sugar_prod_A = 2

biscuit_min_A = -1
biscuit_max_A = 2000
biscuit_prod_A = 2

berry_min_A = -1
berry_max_A = 2000
berry_prod_A = 2

milk_min_A = -1
milk_max_A = 2000
milk_prod_A = 1

cotton_min_A = -1
cotton_max_A = 2000
cotton_prod_A = 3

smith_num_A = 2           # 대장간 건물 수
smith_lev1_A = 600        # 도끼
smith_lev2_A = 300        # 곡괭이
smith_lev3_A = 300        # 톱
smith_lev4_A = 300        # 삽
smith_lev5_A = 100        # 말뚝
smith_lev6_A = 140        # 집게
smith_lev7_A = 140        # 망치

jelly_num_A = 2           # 젤리쨈 건물 수
jelly_lev1_A = 200      # 젤리빈
jelly_lev2_A = 200      # 스윗젤리 잼
jelly_lev3_A = 200      # 달고나 잼
jelly_lev4_A = 100      # 석류 잼
jelly_lev5_A = 100      # 톡톡베리 잼

rollc_num_A = 2           #롤케이크 건물 수
rollc_lev1_A = 200       # 솔방울새 인형
rollc_lev2_A = 160       # 도토리 램프
rollc_lev3_A = 80       # 뻐꾹뻐꾹 시계
rollc_lev4_A = 80       # 백조깃털 드림캐처

bread_num_A = 2           # 빵집 건물 수
bread_lev1_A = 140      # 든든한 호밀빵
bread_lev2_A = 140      # 달콤쫀득 잼파이
bread_lev3_A = 140      # 은행 포카치아
bread_lev4_A = 80      # 슈가코팅 도넛
bread_lev5_A = 80      # 폭신 카스테라
bread_lev6_A = 40      # 골드리치 크로와상

jampy_num_A = 2           # 잼파이 건물 수
jampy_lev1_A = 140       # 따끈따끈 젤리스튜
jampy_lev2_A = 140       # 곰젤리 버거
jampy_lev3_A = 100       # 캔디크림 파스타
jampy_lev4_A = 80       # 폭신폭신 오므라이스
jampy_lev5_A = 80       # 콤비네이션 피자젤리
jampy_lev6_A = 40        # 고급스러운 젤리빈 정식

doye_num_A = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_A = 200        # 비스킷 화분
doye_lev2_A = 140        # 반짝반짝 유리판
doye_lev3_A = 100        # 반짝이는 색동구슬
doye_lev4_A = 80        # 무지갯빛 디저트 보울

flower_num_A = 2          # 꽃가게 건물 수
flower_lev1_A = 160      # 캔디꽃
flower_lev2_A = 140      # 행복한 꽃화분
flower_lev3_A = 60      # 캔디꽃다발
flower_lev4_A = 40      # 롤리팝 꽃바구니
flower_lev5_A = 40      # 유리꽃 부케
flower_lev6_A = 40      # 찬란한 요거트 화환

milky_num_A = 2           # 우유 가공소 건물 수
milky_lev1_A = 100        # 크림
milky_lev2_A = 100       # 버터
milky_lev3_A = 100       # 수제 치즈

latte_num_A = 2         # 라떼 건물 수
latte_lev1_A = 100       # 젤리빈 라떼
latte_lev2_A = 100       # 몽글몽글 버블티
latte_lev3_A = 100        # 스윗베리 에이드

dolls_num_A = 2         # 러블리 인형공방 건물 수
dolls_lev1_A = 100      # 구름사탕 쿠션
dolls_lev2_A = 60      # 곰젤리 솜인형
dolls_lev3_A = 100      # 용과 드래곤 솜인형

beer_num_A = 2          # 오크통 쉼터 건물 수
beer_lev1_A = 100        # 크림 루트비어
beer_lev2_A = 100        # 레드베리 주스
beer_lev3_A = 100        # 빈티지 와일드 보틀

muffin_num_A = 2        # 퐁 드 파티세리 건물 수
muffin_lev1_A = 100      # 으스스 머핀
muffin_lev2_A = 100      # 생딸기 케이크
muffin_lev3_A = 100      # 파티파티 쉬폰케이크

jewel_num_A = 2          # 살롱 드 쥬얼리 건물 수
jewel_lev1_A = 100      # 글레이즈드 링
jewel_lev2_A = 200      # 루비베리 브로치
jewel_lev3_A = 40      # 로얄 곰젤리 크라운

magic_num_A = 1    # 마법공방
magic_lev1_A = 1    # 고농축 에스프레소
magic_lev2_A = 1    # 울퉁불퉁 뿔고구마
magic_lev3_A = 40    # 향기로운 포도주스
magic_lev4_A = 2    # 칼슘 튼튼 우유 
magic_lev5_A = 80    # 까끌까끌 생호밀 
magic_lev6_A = 0    # 빨리감기 태엽장치
magic_lev7_A = 0    # 수수께끼의 파우더 주머니
magic_lev8_A = 0    # 수수께끼의 빛나는 파우더 주머니
magic_lev9_A = 0    # 수수께끼의 신비한 파우더 주머니
magic_lev10_A = 0   # 힘의 설탕결정
magic_lev11_A = 0   # 신속의 설탕결정
magic_lev12_A = 0   #  마력의 설탕결정
magic_lev13_A = 0   # 토핑 조각
magic_lev14_A = 0   # 찬란한 빛조각

wood_min_B = 2000
wood_max_B = 2000
wood_prod_B = 2

jelbean_min_B = 2000
jelbean_max_B = 2000
jelbean_prod_B = 2

sugar_min_B = 2000
sugar_max_B = 2000
sugar_prod_B = 2

biscuit_min_B = -1
biscuit_max_B = 2000
biscuit_prod_B = 2

berry_min_B = -1
berry_max_B = 2000
berry_prod_B = 2

milk_min_B = -1
milk_max_B = 2000
milk_prod_B = 1

cotton_min_B = -1
cotton_max_B = 2000
cotton_prod_B = 3

smith_num_B = 2           # 대장간 건물 수
smith_lev1_B = 600        # 도끼
smith_lev2_B = 300        # 곡괭이
smith_lev3_B = 300        # 톱
smith_lev4_B = 300        # 삽
smith_lev5_B = 100        # 말뚝
smith_lev6_B = 100        # 집게
smith_lev7_B = 140        # 망치

jelly_num_B = 2           # 젤리쨈 건물 수
jelly_lev1_B = 300      # 젤리빈 잼
jelly_lev2_B = 300      # 스윗젤리 잼
jelly_lev3_B = 300      # 달고나 잼
jelly_lev4_B = 80      # 석류 잼
jelly_lev5_B = 0      # 톡톡베리 잼

rollc_num_B = 2           #롤케이크 건물 수
rollc_lev1_B = 200       # 솔방울새 인형
rollc_lev2_B = 200       # 도토리 램프
rollc_lev3_B = 100       # 뻐꾹뻐꾹 시계
rollc_lev4_B = 100       # 백조깃털 드림캐처

bread_num_B = 2           # 빵집 건물 수
bread_lev1_B = 140      # 든든한 호밀빵
bread_lev2_B = 120      # 달콤쫀득 잼파이
bread_lev3_B = 120      # 은행 포카치아
bread_lev4_B = 100      # 슈가코팅 도넛
bread_lev5_B = 100      # 폭신 카스테라
bread_lev6_B = 0      # 골드리치 크로와상

jampy_num_B = 2           # 잼파이 건물 수
jampy_lev1_B = 160      # 따끈따끈 젤리스튜
jampy_lev2_B = 140      # 곰젤리 버거
jampy_lev3_B = 100      # 캔디크림 파스타
jampy_lev4_B = 100      # 폭신폭신 오므라이스
jampy_lev5_B = 100      # 콤비네이션 피자젤리
jampy_lev6_B = 0      # 고급스러운 젤리빈 정식

doye_num_B = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_B = 200       # 비스킷 화분
doye_lev2_B = 200       # 반짝반짝 유리판
doye_lev3_B = 200       # 반짝이는 색동구슬
doye_lev4_B = 80       # 무지갯빛 디저트 보울

flower_num_B = 2          # 꽃가게 건물 수
flower_lev1_B = 200      # 캔디꽃
flower_lev2_B = 220      # 행복한 꽃화분
flower_lev3_B = 200      # 캔디꽃다발
flower_lev4_B = 60      # 롤리팝 꽃바구니
flower_lev5_B = 40      # 유리꽃 부케
flower_lev6_B = 0      # 찬란한 요거트 화환

milky_num_B = 2           # 우유 가공소 건물 수
milky_lev1_B = 200      # 크림
milky_lev2_B = 100      # 버터
milky_lev3_B = 60      # 수제 치즈

latte_num_B = 2         # 라떼 건물 수
latte_lev1_B = 200      # 젤리빈 라떼
latte_lev2_B = 100      # 몽글몽글 버블티
latte_lev3_B = 0      # 스윗베리 에이드

dolls_num_B = 2         # 러블리 인형공방 건물 수
dolls_lev1_B = 100      # 구름사탕 쿠션
dolls_lev2_B = 80      # 곰젤리 솜인형
dolls_lev3_B = 0      # 용과 드래곤 솜인형

beer_num_B = 2          # 오크통 쉼터 건물 수
beer_lev1_B = 80      # 크림 루트비어
beer_lev2_B = 80      # 레드베리 주스
beer_lev3_B = 80      # 빈티지 와일드 보틀

muffin_num_B = 2        # 퐁 드 파티세리 건물 수
muffin_lev1_B = 100      # 으스스 머핀
muffin_lev2_B = 100      # 생딸기 케이크
muffin_lev3_B = 60      # 파티파티 쉬폰케이크

jewel_num_B = 1          # 살롱 드 쥬얼리 건물 수
jewel_lev1_B = 40      # 글레이즈드 링
jewel_lev2_B = 40      # 루비베리 브로치
jewel_lev3_B = 10      # 로얄 곰젤리 크라운

magic_num_B = 1    # 마법공방
magic_lev1_B = 20    # 고농축 에스프레소
magic_lev2_B = 20    # 울퉁불퉁 뿔고구마
magic_lev3_B = 20    # 향기로운 포도주스
magic_lev4_B = 10    # 칼슘 튼튼 우유 
magic_lev5_B = 80    # 까끌까끌 생호밀
magic_lev6_B = 0    # 빨리감기 태엽장치
magic_lev7_B = 0    # 수수께끼의 파우더 주머니
magic_lev8_B = 0    # 수수께끼의 빛나는 파우더 주머니
magic_lev9_B = 0    # 수수께끼의 신비한 파우더 주머니
magic_lev10_B = 0   # 힘의 설탕결정
magic_lev11_B = 0   # 신속의 설탕결정
magic_lev12_B = 0   #  마력의 설탕결정
magic_lev13_B = 0   # 토핑 조각
magic_lev14_B = 0   # 찬란한 빛조각


'''
# 왜 win32api에서 MAKELONG을 쓰지? https://lemon7z.tistory.com/72
# MAKELONG이 문제가 아니라 SendMessage가 문젠가 https://gall.dcinside.com/mgallery/board/view/?id=umamusu&no=59245
def clickR(x, y, random_int):
    lParam = win32api.MAKELONG(x+random.randint(-random_int,random_int), y+random.randint(-random_int,random_int))
    # 자식 없음(아마도) https://airfox1.tistory.com/3
    # hWnd1 = win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)
'''

# 숫자 찾기 시리즈(prod_check에 쓰임)
def find_num(image, yPosition, list_output):
    num_list = LocateAll_Center(image, 620,yPosition+20,33,18, 0.8)
    print('num_list_find_num',image, num_list)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(나무-솜 생산에 쓰임)
def find_upper_num(image, list_output):
    num_list = LocateAll_Center(image, 515,46,48,19, 0.8)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(하트 확인 쓰임)
def find_heart_num(image, list_output):
    num_list = LocateAll_Center(image, 376,48,26,15, 0.83)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(기차에 쓰임)
def find_train_num(image, list_output, line):
    num_list = LocateAll_Center(image, 375,150+(line-1)*149,135,24, 0.83)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(소원나무에 쓰임)
def find_sowon_num(image, list_output, x1, x2):
    num_list = LocateAll_Center(image, x1,186,x2-x1,18, 0.83)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(앵무 교역소에 쓰임)
def find_num_x(image, x1, x2, list_output):
    num_list = LocateAll_Center(image, x1,440,x2-x1,26, 0.85)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    # print(image,list_output)
    return

# 숫자 찾기 시리즈(모험하기-하트확인에 쓰임)
def find_num_new_heart(image, x1, x2, list_output):
    num_list = LocateAll_Center(image, x1,444,x2-x1,15, 0.85)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(아레나에 쓰임)
def find_num_arena(image, x1, x2, list_output):
    num_list = LocateAll_Center(image, x1,x2,65,16, 0.85)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return

# 숫자 찾기 시리즈(앵무 교역소에 쓰임)
def find_num_trade_in(image, trade_howmuch, trade_region_restrict, list_output):
    # 보유량: 이미지 바로 오른쪽 픽셀부터... 최대 56?x18 범위
    num_list = Find_in_Area(image, trade_howmuch[0]+22,trade_howmuch[1]-9,trade_region_restrict,18, 0.92)
    if len(num_list) != 0:
        for p in num_list:
            list_output.append(p)
    return


# 이미지 찾기 시리즈(대충 연구소에 쓰임)
def find_image_in(where_to):
    its_image = LocateCenterOnScreenshot(where_to, 0.95)
    if (its_image):
        return True
    else:
        return False

# 이미지 찾기 시리즈(대충 연구소에 쓰임)
def find_and_check(where_to):
    its_image = LocateCenterOnScreenshot(where_to, 0.85)
    if (its_image):
        click(its_image[0], its_image[1])
        time.sleep(0.3)
        if find_image_in(where_to):
            return True
        else:
            print('비슷한 이미지였나봄')
            # 뭔가 창이 떠있는 경우 닫기(X)
            research_window = Find_in_Area('research_window', 600,35,245,130, 0.9)
            if (research_window):
                click(research_window[0], research_window[1])
                time.sleep(0.3)
            return False
    else:
        print('비슷한 이미지도 없음')
        return False


def del_duplication(dif, list_origin):
    list_origin.sort()
    list_origin = list(set(list_origin))
    del_list = list()
    if len(list_origin) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
        print('list_origin del_duple', list_origin)
        for i in range(len(list_origin)-1):
            for j in range(len(list_origin)-1-i):
                if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif:
                    del_list.append(list_origin[i])
                if list_origin[i][0] == list_origin[i+1+j][0]:
                    del_list.append(list_origin[i])
    list_origin = [x for x in list_origin if x not in del_list]
    list_origin.sort()
    return list_origin

# 생산 시리즈(이미지 찾아서 숫자 읽는 것)
def prod_check(image):
    error_count = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 10):
            break
        its_location = Find_in_Area(image, 590,83,30,455, 0.9)
        if not (its_location):
            error_count = error_count + 1
            prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
            if (prod_clock):
                x_start, y_start = prod_clock[0], prod_clock[1]
            else:
                x_start, y_start = 610, 150
            Drag(x_start, y_start, x_start, y_start-40, 1)  # 이미지 못 읽으면 위로 조금씩 올려봄
            if error_count > 2:
                print('두 번 읽었지만 읽지 못했습니다. 999로 가정합니다.')
                return 9999
        else:
            break
    if (its_location):  # 해당 이미지를 찾은 경우
        its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
        list_real_num = list()  # 실제값 계산을 위한 리스트 생성
        list_num_0 = list()
        list_num_1 = list()
        list_num_2 = list()
        list_num_3 = list()
        list_num_4 = list()
        list_num_5 = list()
        list_num_6 = list()
        list_num_7 = list()
        list_num_8 = list()
        list_num_9 = list()
        # 으아아아아 숫자 가져와아아아아
        find_num('prod_0', its_location[1], list_num_0)
        find_num('prod_1', its_location[1], list_num_1)
        find_num('prod_1_1', its_location[1], list_num_1)
        find_num('prod_2', its_location[1], list_num_2)
        find_num('prod_3', its_location[1], list_num_3)
        find_num('prod_3_1', its_location[1], list_num_3)
        find_num('prod_4', its_location[1], list_num_4)
        find_num('prod_4_1', its_location[1], list_num_4)
        find_num('prod_4_2', its_location[1], list_num_4)
        find_num('prod_5', its_location[1], list_num_5)
        find_num('prod_6', its_location[1], list_num_6)
        find_num('prod_7', its_location[1], list_num_7)
        find_num('prod_8', its_location[1], list_num_8)
        find_num('prod_8_1', its_location[1], list_num_8)
        find_num('prod_9', its_location[1], list_num_9)
        find_num('prod_9_1', its_location[1], list_num_9)
        list_num_0 = del_duplication(3, list_num_0)
        list_num_1 = del_duplication(3, list_num_1)
        list_num_2 = del_duplication(3, list_num_2)
        list_num_3 = del_duplication(3, list_num_3)
        list_num_4 = del_duplication(3, list_num_4)
        list_num_5 = del_duplication(3, list_num_5)
        list_num_6 = del_duplication(3, list_num_6)
        list_num_7 = del_duplication(3, list_num_7)
        list_num_8 = del_duplication(3, list_num_8)
        list_num_9 = del_duplication(3, list_num_9)
        if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
            for p in list_num_0:
                list_real_num.append((p[0],0))

        if (list_num_1):
            for p in list_num_1:
                list_real_num.append((p[0],1))

        if (list_num_2):
            for p in list_num_2:
                list_real_num.append((p[0],2))

        if (list_num_3):
            for p in list_num_3:
                list_real_num.append((p[0],3))

        if (list_num_4):
            for p in list_num_4:
                list_real_num.append((p[0],4))

        if (list_num_5):
            for p in list_num_5:
                list_real_num.append((p[0],5))

        if (list_num_6):
            for p in list_num_6:
                list_real_num.append((p[0],6))

        if (list_num_7):
            for p in list_num_7:
                list_real_num.append((p[0],7))

        if (list_num_8):
            for p in list_num_8:
                list_real_num.append((p[0],8))

        if (list_num_9):
            for p in list_num_9:
                list_real_num.append((p[0],9))

        # 지겨운 실제값 리스트를 받았으니
        list_real_num.sort()    # 추려서

        for i in range(len(list_real_num)): # 실제 int값으로 변환
            its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)

        return its_number

# 나무-솜 숫자 확인 - 확인 완료
def Upper_numb():
    its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
    list_real_num = list()  # 실제값 계산을 위한 리스트 생성
    list_num_0 = list()
    list_num_1 = list()
    list_num_2 = list()
    list_num_3 = list()
    list_num_4 = list()
    list_num_5 = list()
    list_num_6 = list()
    list_num_7 = list()
    list_num_8 = list()
    list_num_9 = list()
    # 으아아아아 숫자 가져와아아아아
    find_upper_num('up_0', list_num_0)
    find_upper_num('up_1', list_num_1)
    find_upper_num('up_2', list_num_2)
    find_upper_num('up_3', list_num_3)
    find_upper_num('up_4', list_num_4)
    find_upper_num('up_5', list_num_5)
    find_upper_num('up_6', list_num_6)
    find_upper_num('up_7', list_num_7)
    find_upper_num('up_8', list_num_8)
    find_upper_num('up_9', list_num_9)
    list_num_0 = del_duplication(3, list_num_0)
    list_num_1 = del_duplication(3, list_num_1)
    list_num_2 = del_duplication(3, list_num_2)
    list_num_3 = del_duplication(3, list_num_3)
    list_num_4 = del_duplication(3, list_num_4)
    list_num_5 = del_duplication(3, list_num_5)
    list_num_6 = del_duplication(3, list_num_6)
    list_num_7 = del_duplication(3, list_num_7)
    list_num_8 = del_duplication(3, list_num_8)
    list_num_9 = del_duplication(3, list_num_9)
    
    if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0],0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0],1))

    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0],2))

    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0],3))

    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0],4))

    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0],5))

    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0],6))

    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0],7))

    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0],8))

    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0],9))

    # 지겨운 실제값 리스트를 받았으니
    list_real_num.sort()    # 추려서

    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)
    
    print('이 제품의 수량은 =', its_number)
    return its_number

def Heart_new_numb():
    # ++
    heart_new_heart = Find_in_Area('heart_new_heart', 30,430,40,42, 0.85)
    if (heart_new_heart):
        print('heart_new_heart',heart_new_heart)
        x1 = heart_new_heart[0]+22
    else:
        print('하트를 못찾아요!')
        return 0
    heart_new_slash = Find_in_Area('heart_new_slash', 83,443,22,19, 0.9)
    if (heart_new_slash):
        print('heart_new_slash',heart_new_slash)
        x2 = heart_new_slash[0]-3
    else:
        print('슬래시를 못찾아요!')
        return 0

    its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
    list_real_num = list()  # 실제값 계산을 위한 리스트 생성
    list_num_0 = list()
    list_num_1 = list()
    list_num_2 = list()
    list_num_3 = list()
    list_num_4 = list()
    list_num_5 = list()
    list_num_6 = list()
    list_num_7 = list()
    list_num_8 = list()
    list_num_9 = list()
    # 으아아아아 숫자 가져와아아아아
    find_num_new_heart('up_hn_0', x1, x2, list_num_0)
    find_num_new_heart('up_hn_0_1', x1, x2, list_num_0)
    find_num_new_heart('up_hn_1', x1, x2, list_num_1)
    find_num_new_heart('up_hn_1_1', x1, x2, list_num_1)
    find_num_new_heart('up_hn_2', x1, x2, list_num_2)
    find_num_new_heart('up_hn_3', x1, x2, list_num_3)
    find_num_new_heart('up_hn_4', x1, x2, list_num_4)
    find_num_new_heart('up_hn_5', x1, x2, list_num_5)
    find_num_new_heart('up_hn_6', x1, x2, list_num_6)
    find_num_new_heart('up_hn_7', x1, x2, list_num_7)
    find_num_new_heart('up_hn_8', x1, x2, list_num_8)
    find_num_new_heart('up_hn_9', x1, x2, list_num_9)
    find_num_new_heart('up_hn_9_1', x1, x2, list_num_9)
    list_num_0 = del_duplication(2, list_num_0)
    list_num_1 = del_duplication(2, list_num_1)
    list_num_2 = del_duplication(2, list_num_2)
    list_num_3 = del_duplication(2, list_num_3)
    list_num_4 = del_duplication(2, list_num_4)
    list_num_5 = del_duplication(2, list_num_5)
    list_num_6 = del_duplication(2, list_num_6)
    list_num_7 = del_duplication(2, list_num_7)
    list_num_8 = del_duplication(2, list_num_8)
    list_num_9 = del_duplication(2, list_num_9)
    if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0],0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0],1))
        print('append 후 list_1', list_num_1)
    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0],2))

    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0],3))

    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0],4))

    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0],5))

    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0],6))

    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0],7))

    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0],8))

    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0],9))

    # 지겨운 실제값 리스트를 받았으니
    list_real_num.sort()    # 추려서
    print('set 이전',list_real_num)
    
    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)

    print('현재 재고는 =', its_number)
    return its_number

def Heart_sojin(WhatToDo):
    error_count = 0
    bNormalMode = True          # 일반모드 해야할 때 True
    bZoomOutComp = False        # 줌아웃 했늬
    bSpeedCheck = False         # 1.5배 속도 체크
    bAutoCheck = False          # 자동 전투 체크
    
    bStep1_play = False         # 플레이 버튼을 눌렀는가?
    bStep2_Adv = False          # 모험하기에서 월드 탐험을 클릭했는가?
    bStep3_Epi = False          # 에피소드(1~12)중 하나 들어와 있는 경우
    bStep4_Epi_Confirm = False  # 원하는 에피소드에 들어왔니?
    bStep5_Epi_Select = False   # 에피소드 선택 화면이니?
    bEntered = False            # 스테이지 골라서 전투 시작을 눌렀는가?
    bNormalSelected = False     # 에피소드 들어와서 일반모드 확인한 경우
    start_time = time.time()
    
    while True:
        if not While_True_Condition(start_time,900):
            # End_kkd()                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
            # Kingdom_ready('kkd_out')            # 재부팅
            return False
        pix_status = Get_pixel_tuple(605,55) # 상단골드
        pix_status2 = Get_pixel_tuple(540,510) # 마침표

        cond_adv_mode_select = Find_in_Area('cond_adv_mode_select', 12,38,37,36, 0.85)  # Play버튼 누른 후 모험하기 창
        adv_normal = Find_in_Area('adv_normal', 232,53,35,19, 0.85)       # 에피소드에서 좌상단 일반/어둠 선택 확인하기
        cond_adv_out_1 = LocateCenterOnScreenshot('cond_adv_out_1', 0.85)   # 1렙 맵
        cond_adv_out_2 = LocateCenterOnScreenshot('cond_adv_out_2', 0.85)   # 2렙 맵
        cond_adv_out_3 = LocateCenterOnScreenshot('cond_adv_out_3', 0.85)   # 3렙 맵
        cond_adv_out_4 = LocateCenterOnScreenshot('cond_adv_out_4', 0.85)   # 4렙 맵
        cond_adv_out_5 = LocateCenterOnScreenshot('cond_adv_out_5', 0.85)   # 5렙 맵
        cond_adv_out_6 = LocateCenterOnScreenshot('cond_adv_out_6', 0.85)   # 6렙 맵
        cond_adv_out_7 = LocateCenterOnScreenshot('cond_adv_out_7', 0.85)   # 7렙 맵
        cond_adv_out_8 = LocateCenterOnScreenshot('cond_adv_out_8', 0.85)   # 8렙 맵
        cond_adv_out_9 = LocateCenterOnScreenshot('cond_adv_out_9', 0.85)   # 9렙 맵
        cond_adv_out_10 = LocateCenterOnScreenshot('cond_adv_out_10', 0.85)   # 10렙 맵
        cond_adv_out_11 = LocateCenterOnScreenshot('cond_adv_out_11', 0.85)   # 11렙 맵
        cond_adv_out_12 = LocateCenterOnScreenshot('cond_adv_out_12', 0.85)   # 12렙 맵
        adv_worldmap = Find_in_Area('adv_worldmap', 33,467,52,43, 0.85)   # 좌하단 월드맵 아이콘
        adv_goto_wangkook = Find_in_Area('adv_goto_wangkook', 845,470,40,40, 0.85)   # 우하단 왕국가기 아이콘
        adv_8_epi = Find_in_Area('adv_8_epi', 75,52,18,14, 0.85)      # 에피소드 8 입니까?
        # adv_8_25 = LocateCenterOnScreenshot('adv_8_25', 0.83)   # 8-25
        # adv_8_26 = LocateCenterOnScreenshot('adv_8_26', 0.83)   # 8-26
        adv_8_28 = LocateCenterOnScreenshot('adv_8_28', 0.83)   # 8-28
        adv_8_29 = LocateCenterOnScreenshot('adv_8_29', 0.83)   # 8-29
        cond_adv_stage_select = Find_in_Area('cond_adv_stage_select', 408,39,100,50, 0.83)   # 스테이지 고르는 화면
        cond_kkd_out = Find_in_Area('cond_kkd_out', 825,490,45,40, 0.85)    # 쿠키왕국
        
        # 자동 전투 체크        
        if bEntered and not bAutoCheck:
            cond_adv_automode = Find_in_Area('cond_adv_automode', 39,433,12,14, 0.85)   # 황금 "동" 글씨
            cond_adv_not_automode = Find_in_Area('cond_adv_not_automode', 39,433,12,14, 0.85)   # 회색 "동" 글씨
            if (cond_adv_not_automode):
                click(cond_adv_not_automode[0], cond_adv_not_automode[1])
            if (cond_adv_automode):
                print('자동 전투 확인!')
                bAutoCheck = True

        # 속도 체크
        adv_speed1 = Find_in_Area('adv_speed1', 35,497,20,15, 0.85)   # 12렙 맵
        adv_speed2 = Find_in_Area('adv_speed2', 35,497,20,15, 0.85)   # 12렙 맵
        adv_speed3 = Find_in_Area('adv_speed3', 35,497,20,15, 0.85)   # 12렙 맵
        
        if bEntered and (adv_speed1):
            click(adv_speed1[0], adv_speed1[1])
            time.sleep(0.5)
            bSpeedCheck = False
        if bEntered and (adv_speed2):
            click(adv_speed2[0], adv_speed2[1])
            time.sleep(0.5)
            bSpeedCheck = False
        if bEntered and not bSpeedCheck and (adv_speed3):
            print('1.5배 ok')
            bSpeedCheck = True

        # 오 이 버튼들은 동일한가 본데..
        cond_end_fight1 = LocateCenterOnScreenshot('Cond_wanted_go_kingdom', 0.9)   # 왕국가기 버튼
        cond_end_fight2 = LocateCenterOnScreenshot('Cond_wanted_refignt', 0.9)   # 다시하기 버튼
        cond_end_fight3 = LocateCenterOnScreenshot('Cond_wanted_go_out', 0.9)   # 나가기 버튼
        
        if (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            click(540,510)
            # bWanted_fight_ing = False
            bStep2_Adv = True
            bEntered = True
        
        if (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            click(540,510)
            # bWanted_fight_ing = False
            bStep2_Adv = True
            bEntered = True
        
        # 좌하단 우하단 아이콘으로 현재 에피소드 중 하나에 들어와 있는지를 확인.. 스테이지 넘나들려면 리셋해야나
        if (adv_worldmap) and (adv_goto_wangkook):
            bEntered = False            # 스테이지 골라서 전투 시작을 눌렀는가?
            bStep1_play = True          # 플레이 버튼을 눌렀는가?
            bStep2_Adv = True           # 모험하기에서 월드 탐험을 클릭했는가?
            bStep3_Epi = True           # 에피소드(1~12)중 하나 들어와 있는 경우
            
        # 모험하기 화면
        if not bEntered and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if not bEntered and ((pix_status == pix_status_out) or (cond_kkd_out)) and not bStep1_play:
            print('Play 버튼 클릭~!')
            click(760,500)
            time.sleep(10)
            bStep1_play = False             # 플레이 버튼을 눌렀는가?(조건은 모험하기 화면에서 다시 살리겠지)
            bStep2_Adv = False              # 모험하기에서 월드 탐험을 클릭했는가?
            bStep3_Epi = False              # 에피소드(1~12)중 하나 들어와 있는 경우
            bStep4_Epi_Confirm = False      # 원하는 에피소드에 들어왔니?
            bStep5_Epi_Select = False       # 에피소드 선택 화면이니?

        if not bEntered and bStep1_play and not bStep2_Adv and not bStep3_Epi and not bStep4_Epi_Confirm and not bStep5_Epi_Select:
            cond_wanted = LocateCenterOnScreenshot('cond_world_adventure', 0.85)    # 월드 탐험의 팀?
            if (cond_wanted):
                print('모험하기 - 월드탐험 있으니 들어가자!')
                click(cond_wanted[0], cond_wanted[1])
                time.sleep(5)
                
            if not (cond_wanted):
                print('드래그드래그')
                Drag(200,500,800,501, 2)
                error_count = error_count+1
                if error_count > 3:
                    print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                    return
        
        # 원하는 에피소드인가?
        if not bEntered and bStep3_Epi and not bStep4_Epi_Confirm:
            # 나중에 다른 에피 추가할 때 여기다 하면 될듯..
            if ((WhatToDo == '8-29') or (WhatToDo == '8-25')):
                adv_8_epi = Find_in_Area('adv_8_epi', 75,52,18,14, 0.8)
                if (adv_8_epi):
                    print('에피소드 8에 잘 오셨습니다.')
                    bStep4_Epi_Confirm = True
                else:
                    print('8 에피 가야는데 여긴 아닌거 같습니다.')
                    if (adv_worldmap):
                        print('일반모드 선택하고 월드맵 나갑니다.')
                        click(250,70)
                        time.sleep(0.5)
                        click(250,70)
                        time.sleep(1.5)
                        click(adv_worldmap[0], adv_worldmap[1])
                        time.sleep(2)
                        bStep3_Epi = False
                    else:
                        print('여긴 어디 나는 누구.. 우선 왕국으로?')
                        click(892,54)
                        time.sleep(1)
                        click(892,54)
                        time.sleep(1)
                        click(892,54)
                        time.sleep(1)
                        click(892,54)
                        time.sleep(4)
                        Kingdom_ready('kkd_out')

        # 에피소드 선택 화면 
        if not bEntered and (cond_adv_stage_select):
            bStep1_play = True          # 플레이 버튼을 눌렀는가?(조건은 모험하기 화면에서 다시 살리겠지)
            bStep2_Adv = True           # 모험하기에서 월드 탐험을 클릭했는가?
            bStep3_Epi = False          # 에피소드(1~12)중 하나 들어와 있는 경우
            bStep4_Epi_Confirm = False  # 원하는 에피소드에 들어왔니?
            bStep5_Epi_Select = True    # 에피소드 선택 화면이니?

        if not bEntered and bStep5_Epi_Select:
            # 나중에 다른 에피 추가할 때 여기다 하면 될듯..
            # 에피소드 8 가고 싶다
            pix_status = Get_pixel_tuple(605, 55)  # 상단골드
            if (pix_status == pix_adv_dark):      # 어둠모드야?
                click(78,61)    # 일반모드 클릭해요
                time.sleep(1)
            print('도니')
            if ((WhatToDo == '8-29') or (WhatToDo == '8-25')):
                if (cond_adv_out_8):
                    click(cond_adv_out_8[0], cond_adv_out_8[1])
                    time.sleep(3)
                    cond_adv_stage_select = Find_in_Area('adv_8_29', 408,39,100,50, 0.83)   # 스테이지 고르는 화면
                    if not (cond_adv_stage_select):
                        bStep5_Epi_Select = False
                    else:
                        click(cond_adv_out_8[0], cond_adv_out_8[1])
                        time.sleep(3)
                else:
                    if (cond_adv_out_9):
                        if cond_adv_out_9[0] > 365+3:
                            click(cond_adv_out_9[0]-365,cond_adv_out_9[1]+73)
                        else:
                            print('왼쪽으로 드래그드래그')
                            x, y = 480+random.randint(-100,100), 500+random.randint(-20,20)
                            Drag(x, y, x+300, y, 2)
                            time.sleep(2)
                            
                    else:
                        if (cond_adv_out_1) or (cond_adv_out_2) or (cond_adv_out_3) or (cond_adv_out_4) or (cond_adv_out_5) or (cond_adv_out_6) or (cond_adv_out_7):
                            print('오른쪽으로 드래그드래그')
                            x, y = 480+random.randint(-100,100), 500+random.randint(-20,20)
                            Drag(x, y, x-300, y, 2)
                            time.sleep(2)
                            
                        if (cond_adv_out_9) or (cond_adv_out_10) or (cond_adv_out_11) or (cond_adv_out_12):
                            print('왼쪽으로 드래그드래그')
                            x, y = 480+random.randint(-100,100), 500+random.randint(-20,20)
                            Drag(x, y, x+300, y, 2)
                            time.sleep(2)
            
        # 일반모드 해야하고, 에피소드 들어와 있으며, 노멀모드 선택을 아직 안한
        if bNormalMode and bStep3_Epi and not bNormalSelected and not bEntered and bStep4_Epi_Confirm:
            if (adv_normal):
                print('일반모드 확인')
                bNormalSelected = True
            else:
                print('일반모드 선택합니다.')
                click(250,70)
                time.sleep(0.5)
                click(250,70)
                time.sleep(1.5)

        # 에피소드 안에 들어와 있고, 아직 8-29에 들어가지 않았으면
        if (WhatToDo == '8-29') and bStep3_Epi and not bEntered and not bZoomOutComp and bNormalSelected: # 8-29 스테이지, 시작 안한 경우
            # 에피스드 8인지 확인
            adv_8_epi = Find_in_Area('adv_8_epi', 75,52,18,14, 0.8)
            if (adv_8_epi):
                print('에피소드 8이네요!')
                # 줌아웃 하고
                Wheel_Down(800,370)
                time.sleep(1)
                Wheel_Down(810,375)
                time.sleep(1)
                Wheel_Down(790,365)
                time.sleep(1)
                print('줌아웃, 진입 준비 완료!')
                bZoomOutComp = True

        # 28 있으면 29 위치 클릭
        if (adv_8_28) and (WhatToDo == '8-29'):
            click(adv_8_28[0]+94,adv_8_28[1]-50)
            time.sleep(1)
            adv_8_29_in = LocateCenterOnScreenshot('adv_8_29_in', 0.95)   # 8-29 클릭완료
            if (adv_8_29_in):
                print('8-29 클릭했네요')
                click(715,490)          # 전투 준비 클릭(현상수배랑 글씨 사이즈가 다르네 씁..)
                time.sleep(1.5)
                click(820,495)          # 전투 시작 클릭
                time.sleep(1)
                cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.9)
                if (cond_balloon_lack_heart):
                    print('젤리고기 부족..')
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(4)
                    return False
                else:
                    bEntered = True
        
        # 29 있으면 클릭
        if (adv_8_29) and (WhatToDo == '8-29'):
            click(adv_8_29[0], adv_8_29[1])
            time.sleep(1)
            adv_8_29_in = LocateCenterOnScreenshot('adv_8_29_in', 0.95)   # 8-29 클릭완료
            if (adv_8_29_in):
                print('8-29 클릭했네요')
                click(715,490)          # 전투 준비 클릭(현상수배랑 글씨 사이즈가 다르네 씁..)
                time.sleep(1.5)
                click(820,495)          # 전투 시작 클릭
                time.sleep(1)
                cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.9)
                if (cond_balloon_lack_heart):
                    print('젤리고기 부족..')
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(1)
                    click(892,54)
                    time.sleep(4)
                    return False
                bEntered = True
            
        if(cond_end_fight3):   # 나가기 버튼이 있는데
            if (cond_end_fight2):   # 다시하기 버튼이 있으면
                print('다시하기 버튼!')
                click(cond_end_fight2[0], cond_end_fight2[1]) # 눌러~
                time.sleep(0.5)
                click(cond_end_fight2[0], cond_end_fight2[1]) # 눌러~
                time.sleep(1)
                # bWanted_fight_ing = True
            else:
                click(cond_end_fight1[0], cond_end_fight1[1])  # 왕국가기버튼 클릭. 나가기 버튼과 항상 함께 있어서 오류날 일 없겠지
                time.sleep(0.5)
                click(cond_end_fight1[0], cond_end_fight1[1])  # 왕국가기버튼 클릭. 나가기 버튼과 항상 함께 있어서 오류날 일 없겠지
                time.sleep(15)
                if Kingdom_ready('kkd_out'):    # 어후 왕국에 잘 들어왔어
                    print('월드탐험 잘 마치고 종료합니다!')
                    return True

def Account_Change():
    global hWnd
    global title_t
    global account
    global bTropical
    global bResearch_auto
    global jjokji_limit
    global check_mark_action
    global jjokji_biscuit
    global jjokji_berry
    global jjokji_milk
    global jjokji_cotton
    global trade_legend
    global trade_hero
    global bTropical_Confirmed

    global wood_min
    global wood_max
    global wood_prod
    global jelbean_min
    global jelbean_max
    global jelbean_prod
    global sugar_min
    global sugar_max
    global sugar_prod
    global biscuit_min
    global biscuit_max
    global biscuit_prod
    global berry_min
    global berry_max
    global berry_prod
    global milk_min
    global milk_max
    global milk_prod
    global cotton_min
    global cotton_max
    global cotton_prod

    global smith_lev1
    global smith_lev2
    global smith_lev3
    global smith_lev4
    global smith_lev5
    global smith_lev6
    global smith_lev7
    global jelly_lev1
    global jelly_lev2
    global jelly_lev3
    global jelly_lev4
    global jelly_lev5
    global rollc_lev1
    global rollc_lev2
    global rollc_lev3
    global rollc_lev4
    global bread_lev1
    global bread_lev2
    global bread_lev3
    global bread_lev4
    global bread_lev5
    global bread_lev6
    global jampy_lev1
    global jampy_lev2
    global jampy_lev3
    global jampy_lev4
    global jampy_lev5
    global jampy_lev6
    global doye_lev1
    global doye_lev2
    global doye_lev3
    global doye_lev4
    global flower_lev1
    global flower_lev2
    global flower_lev3
    global flower_lev4
    global flower_lev5
    global flower_lev6
    global milky_lev1
    global milky_lev2
    global milky_lev3
    global latte_lev1
    global latte_lev2
    global latte_lev3
    global dolls_lev1
    global dolls_lev2
    global dolls_lev3
    global beer_lev1
    global beer_lev2
    global beer_lev3
    global muffin_lev1
    global muffin_lev2
    global muffin_lev3
    global jewel_lev1
    global jewel_lev2
    global jewel_lev3
    global magic_lev1
    global magic_lev2
    global magic_lev3
    global magic_lev4
    global magic_lev5
    global magic_lev6
    global magic_lev7

    global smith_num
    global jelly_num
    global rollc_num
    global bread_num
    global jampy_num
    global doye_num
    global flower_num
    global milky_num
    global latte_num
    global dolls_num
    global beer_num
    global muffin_num
    global jewel_num
    global magic_num
    global fountain_set_time
    global cookie_set_time
    global set_max_power

    if account == 0:
        account = 1
    elif account == 1:
        # 3계정 돌릴 경우 account=2 주고
        account = 0
    elif account == 2:
        account = 0
    else:
        print('계정 전환 오류! A계정부터 다시..')
        account = 0
    
    if account == 0:
        print('A계정 돕니다')
        bTropical = bTropicalAction_A           # 트로피칼 돌릴래
        bResearch_auto = bResearch_auto_A       # 연구소 자동 돌릴래
        jjokji_limit = jjokji_limit_A           # 쪽지 보상까지만 돌릴래
        check_mark_action = check_mark_action_A # 건물 업글중 체크마크 클릭 안함
        jjokji_biscuit = jjokji_biscuit_A       # 비스킷 아낌모드
        jjokji_berry = jjokji_berry_A           # 젤리베리 아낌모드
        jjokji_milk = jjokji_milk_A             # 우유 아낌모드
        jjokji_cotton = jjokji_cotton_A         # 솜사탕 아낌모드
        trade_legend = trade_legend_A           # 오색조개 전설 조각
        trade_hero = trade_hero_A               # 오색조개 영웅 조각
        bTropical_Confirmed = bTropical_Confirmed_A # 트로피칼 실행했나
        
        # 기본 생산품        
        wood_min = wood_min_A
        wood_max = wood_max_A
        wood_prod = wood_prod_A
        jelbean_min = jelbean_min_A
        jelbean_max = jelbean_max_A
        jelbean_prod = jelbean_prod_A
        sugar_min = sugar_min_A
        sugar_max = sugar_max_A
        sugar_prod = sugar_prod_A
        biscuit_min = biscuit_min_A
        biscuit_max = biscuit_max_A
        biscuit_prod = biscuit_prod_A
        berry_min = berry_min_A
        berry_max = berry_max_A
        berry_prod = berry_prod_A
        milk_min = milk_min_A
        milk_max = milk_max_A
        milk_prod = milk_prod_A
        cotton_min = cotton_min_A
        cotton_max = cotton_max_A
        cotton_prod = cotton_prod_A
        
        smith_lev1 = smith_lev1_A   # 도끼
        smith_lev2 = smith_lev2_A   # 곡괭이
        smith_lev3 = smith_lev3_A   # 톱
        smith_lev4 = smith_lev4_A   # 삽
        smith_lev5 = smith_lev5_A   # 말뚝
        smith_lev6 = smith_lev6_A   # 집게
        smith_lev7 = smith_lev7_A   # 망치
        jelly_lev1 = jelly_lev1_A   # 젤리빈
        jelly_lev2 = jelly_lev2_A   # 스윗젤리 잼
        jelly_lev3 = jelly_lev3_A   # 달고나 잼
        jelly_lev4 = jelly_lev4_A   # 석류 잼
        jelly_lev5 = jelly_lev5_A   # 톡톡베리 잼
        rollc_lev1 = rollc_lev1_A   # 솔방울새 인형
        rollc_lev2 = rollc_lev2_A   # 도토리 램프
        rollc_lev3 = rollc_lev3_A   # 뻐꾹뻐꾹 시계
        rollc_lev4 = rollc_lev4_A   # 백조깃털 드림캐처
        bread_lev1 = bread_lev1_A   # 든든한 호밀빵
        bread_lev2 = bread_lev2_A   # 달콤쫀득 잼파이
        bread_lev3 = bread_lev3_A   # 은행 포카치아
        bread_lev4 = bread_lev4_A   # 슈가코팅 도넛
        bread_lev5 = bread_lev5_A   # 폭신 카스테라
        bread_lev6 = bread_lev6_A   # 골드리치 크로와상
        jampy_lev1 = jampy_lev1_A   # 따끈따끈 젤리스튜
        jampy_lev2 = jampy_lev2_A   # 곰젤리 버거
        jampy_lev3 = jampy_lev3_A   # 캔디크림 파스타
        jampy_lev4 = jampy_lev4_A   # 폭신폭신 오므라이스
        jampy_lev5 = jampy_lev5_A   # 콤비네이션 피자젤리
        jampy_lev6 = jampy_lev6_A   # 고급스러운 젤리빈 정식
        doye_lev1 = doye_lev1_A     # 비스킷 화분
        doye_lev2 = doye_lev2_A     # 반짝반짝 유리판
        doye_lev3 = doye_lev3_A     # 반짝이는 색동구슬
        doye_lev4 = doye_lev4_A     # 무지갯빛 디저트 보울
        flower_lev1 = flower_lev1_A # 캔디꽃
        flower_lev2 = flower_lev2_A # 행복한 꽃화분
        flower_lev3 = flower_lev3_A # 캔디꽃다발
        flower_lev4 = flower_lev4_A # 롤리팝 꽃바구니
        flower_lev5 = flower_lev5_A # 유리꽃 부케
        flower_lev6 = flower_lev6_A # 찬란한 요거트 화환
        milky_lev1 = milky_lev1_A   # 크림
        milky_lev2 = milky_lev2_A   # 버터
        milky_lev3 = milky_lev3_A   # 수제 치즈
        latte_lev1 = latte_lev1_A   # 젤리빈 라떼
        latte_lev2 = latte_lev2_A   # 몽글몽글 버블티
        latte_lev3 = latte_lev3_A   # 스윗베리 에이드
        dolls_lev1 = dolls_lev1_A   # 구름사탕 쿠션
        dolls_lev2 = dolls_lev2_A   # 곰젤리 솜인형
        dolls_lev3 = dolls_lev3_A   # 용과 드래곤 솜인형
        beer_lev1 = beer_lev1_A     # 크림 루트비어
        beer_lev2 = beer_lev2_A     # 레드베리 주스
        beer_lev3 = beer_lev3_A     # 빈티지 와일드 보틀
        muffin_lev1 = muffin_lev1_A # 으스스 머핀
        muffin_lev2 = muffin_lev2_A # 생딸기 케이크
        muffin_lev3 = muffin_lev3_A # 파티파티 쉬폰케이크
        jewel_lev1 = jewel_lev1_A   # 글레이즈드 링
        jewel_lev2 = jewel_lev2_A   # 루비베리 브로치
        jewel_lev3 = jewel_lev3_A   # 로얄 곰젤리 크라운
        magic_lev1 = magic_lev1_A  # 고농축 에스프레소
        magic_lev2 = magic_lev2_A  # 울퉁불퉁 뿔고구마
        magic_lev3 = magic_lev3_A  # 향기로운 포도주스
        magic_lev4 = magic_lev4_A  # 빨리감기 태엽장치
        magic_lev5 = magic_lev5_A  # 수수께끼의 파우더 주머니
        magic_lev6 = magic_lev6_A  # 수수께끼의 빛나는 파우더 주머니
        magic_lev7 = magic_lev7_A  # 수수께끼의 신비한 파우더 주머니

        smith_num = smith_num_A     # 대장간 건물 수
        jelly_num = jelly_num_A     # 젤리쨈 건물 수
        rollc_num = rollc_num_A     # 롤케이크 건물 수
        bread_num = bread_num_A     # 빵집 건물 수
        jampy_num = jampy_num_A     # 잼파이 건물 수
        doye_num = doye_num_A       # 토닥토닥 도예공방 건물 수
        flower_num = flower_num_A   # 꽃가게 건물 수
        milky_num = milky_num_A     # 우유 가공소 건물 수
        latte_num = latte_num_A     # 라떼 건물 수
        dolls_num = dolls_num_A     # 러블리 인형공방 건물 수
        beer_num = beer_num_A       # 오크통 쉼터 건물 수
        muffin_num = muffin_num_A   # 퐁 드 파티세리 건물 수
        jewel_num = jewel_num_A     # 살롱 드 쥬얼리 건물 수
        magic_num = magic_num_A     # 마법공방
        fountain_set_time = fountain_set_time_A # 분수 클릭 주기
        cookie_set_time = cookie_set_time_A     # 쿠하 클릭 주기
        set_max_power = set_max_power_A         # 아레나 상대 전투력 커트라인
    elif account == 1:
        print('B계정 돕니다')
        bTropical = bTropicalAction_B           # 트로피칼 돌릴래
        bResearch_auto = bResearch_auto_B       # 연구소 자동 돌릴래
        jjokji_limit = jjokji_limit_B           # 쪽지 보상까지만 돌릴래
        check_mark_action = check_mark_action_B # 건물 업글중 체크마크 클릭 안함
        jjokji_biscuit = jjokji_biscuit_B       # 비스킷 아낌모드
        jjokji_berry = jjokji_berry_B           # 젤리베리 아낌모드
        jjokji_milk = jjokji_milk_B             # 우유 아낌모드
        jjokji_cotton = jjokji_cotton_B         # 솜사탕 아낌모드
        trade_legend = trade_legend_B           # 오색조개 전설 조각
        trade_hero = trade_hero_B               # 오색조개 영웅 조각
        bTropical_Confirmed = bTropical_Confirmed_B # 트로피칼 실행했나

        # 기본 생산품
        wood_min = wood_min_B
        wood_max = wood_max_B
        wood_prod = wood_prod_B
        jelbean_min = jelbean_min_B
        jelbean_max = jelbean_max_B
        jelbean_prod = jelbean_prod_B
        sugar_min = sugar_min_B
        sugar_max = sugar_max_B
        sugar_prod = sugar_prod_B
        biscuit_min = biscuit_min_B
        biscuit_max = biscuit_max_B
        biscuit_prod = biscuit_prod_B
        berry_min = berry_min_B
        berry_max = berry_max_B
        berry_prod = berry_prod_B
        milk_min = milk_min_B
        milk_max = milk_max_B
        milk_prod = milk_prod_B
        cotton_min = cotton_min_B
        cotton_max = cotton_max_B
        cotton_prod = cotton_prod_B

        smith_lev1 = smith_lev1_B   # 도끼
        smith_lev2 = smith_lev2_B   # 곡괭이
        smith_lev3 = smith_lev3_B   # 톱
        smith_lev4 = smith_lev4_B   # 삽
        smith_lev5 = smith_lev5_B   # 말뚝
        smith_lev6 = smith_lev6_B   # 집게
        smith_lev7 = smith_lev7_B   # 망치
        jelly_lev1 = jelly_lev1_B   # 젤리빈
        jelly_lev2 = jelly_lev2_B   # 스윗젤리 잼
        jelly_lev3 = jelly_lev3_B   # 달고나 잼
        jelly_lev4 = jelly_lev4_B   # 석류 잼
        jelly_lev5 = jelly_lev5_B   # 톡톡베리 잼
        rollc_lev1 = rollc_lev1_B   # 솔방울새 인형
        rollc_lev2 = rollc_lev2_B   # 도토리 램프
        rollc_lev3 = rollc_lev3_B   # 뻐꾹뻐꾹 시계
        rollc_lev4 = rollc_lev4_B   # 백조깃털 드림캐처
        bread_lev1 = bread_lev1_B   # 든든한 호밀빵
        bread_lev2 = bread_lev2_B   # 달콤쫀득 잼파이
        bread_lev3 = bread_lev3_B   # 은행 포카치아
        bread_lev4 = bread_lev4_B   # 슈가코팅 도넛
        bread_lev5 = bread_lev5_B   # 폭신 카스테라
        bread_lev6 = bread_lev6_B   # 골드리치 크로와상
        jampy_lev1 = jampy_lev1_B   # 따끈따끈 젤리스튜
        jampy_lev2 = jampy_lev2_B   # 곰젤리 버거
        jampy_lev3 = jampy_lev3_B   # 캔디크림 파스타
        jampy_lev4 = jampy_lev4_B   # 폭신폭신 오므라이스
        jampy_lev5 = jampy_lev5_B   # 콤비네이션 피자젤리
        jampy_lev6 = jampy_lev6_B   # 고급스러운 젤리빈 정식
        doye_lev1 = doye_lev1_B     # 비스킷 화분
        doye_lev2 = doye_lev2_B     # 반짝반짝 유리판
        doye_lev3 = doye_lev3_B     # 반짝이는 색동구슬
        doye_lev4 = doye_lev4_B     # 무지갯빛 디저트 보울
        flower_lev1 = flower_lev1_B # 캔디꽃
        flower_lev2 = flower_lev2_B # 행복한 꽃화분
        flower_lev3 = flower_lev3_B # 캔디꽃다발
        flower_lev4 = flower_lev4_B # 롤리팝 꽃바구니
        flower_lev5 = flower_lev5_B # 유리꽃 부케
        flower_lev6 = flower_lev6_B # 찬란한 요거트 화환
        milky_lev1 = milky_lev1_B   # 크림
        milky_lev2 = milky_lev2_B   # 버터
        milky_lev3 = milky_lev3_B   # 수제 치즈
        latte_lev1 = latte_lev1_B   # 젤리빈 라떼
        latte_lev2 = latte_lev2_B   # 몽글몽글 버블티
        latte_lev3 = latte_lev3_B   # 스윗베리 에이드
        dolls_lev1 = dolls_lev1_B   # 구름사탕 쿠션
        dolls_lev2 = dolls_lev2_B   # 곰젤리 솜인형
        dolls_lev3 = dolls_lev3_B   # 용과 드래곤 솜인형
        beer_lev1 = beer_lev1_B     # 크림 루트비어
        beer_lev2 = beer_lev2_B     # 레드베리 주스
        beer_lev3 = beer_lev3_B     # 빈티지 와일드 보틀
        muffin_lev1 = muffin_lev1_B # 으스스 머핀
        muffin_lev2 = muffin_lev2_B # 생딸기 케이크
        muffin_lev3 = muffin_lev3_B # 파티파티 쉬폰케이크
        jewel_lev1 = jewel_lev1_B   # 글레이즈드 링
        jewel_lev2 = jewel_lev2_B   # 루비베리 브로치
        jewel_lev3 = jewel_lev3_B   # 로얄 곰젤리 크라운
        magic_lev1 = magic_lev1_B  # 고농축 에스프레소
        magic_lev2 = magic_lev2_B  # 울퉁불퉁 뿔고구마
        magic_lev3 = magic_lev3_B  # 향기로운 포도주스
        magic_lev4 = magic_lev4_B  # 빨리감기 태엽장치
        magic_lev5 = magic_lev5_B  # 수수께끼의 파우더 주머니
        magic_lev6 = magic_lev6_B  # 수수께끼의 빛나는 파우더 주머니
        magic_lev7 = magic_lev7_B  # 수수께끼의 신비한 파우더 주머니
        smith_num = smith_num_B     # 대장간 건물 수
        jelly_num = jelly_num_B     # 젤리쨈 건물 수
        rollc_num = rollc_num_B     # 롤케이크 건물 수
        bread_num = bread_num_B     # 빵집 건물 수
        jampy_num = jampy_num_B     # 잼파이 건물 수
        doye_num = doye_num_B       # 토닥토닥 도예공방 건물 수
        flower_num = flower_num_B   # 꽃가게 건물 수
        milky_num = milky_num_B     # 우유 가공소 건물 수
        latte_num = latte_num_B     # 라떼 건물 수
        dolls_num = dolls_num_B     # 러블리 인형공방 건물 수
        beer_num = beer_num_B       # 오크통 쉼터 건물 수
        muffin_num = muffin_num_B   # 퐁 드 파티세리 건물 수
        jewel_num = jewel_num_B     # 살롱 드 쥬얼리 건물 수
        magic_num = magic_num_B     # 마법공방
        fountain_set_time = fountain_set_time_B # 분수 클릭 주기
        cookie_set_time = cookie_set_time_B     # 쿠하 클릭 주기
        set_max_power = set_max_power_B         # 아레나 상대 전투력 커트라인
    else:
        print('C계정은 이곳에 추가')
        account == 2
    
    # 계정에 맞게 핸들 넘김
    if account == 0:    # 1번 계정
        title_t = "국왕만두만"
    elif account == 1:  # 2번 계정
        title_t = "국왕꾸안꾸"
    # elif account == 2:  # 3번 계정
        # title_t = ""
    else:
        title_t = "국왕만두만"
        print('계정 뭐얏')
    hWnd = win32gui.FindWindow(None, title_t)
    return

# 했음
def Angmu_Enter(whereto):
    bStep1_Trade = False        # 후르츠칸 해상무역센터 들어왔니?
    bStep2_Angmu = False        # 앵무 해변교역소 들어왔니?
    
    bTradeEvent = False         # 무역센터 진행
    bResearchEvent = False      # 연구소 진행
    bBalloonEvent = False       # 열기구 진행
    bTrainEvent = False         # 열차 진행
    bSowonEvent = False         # 소원나무 진행
    bFountain = False           # 분수 찾아 들어가기
    # 길드 보상
    bShop = False               # 상점 보상

    # 왕국 화면임니까
    Kingdom_ready('kkd_out')
    start_time = time.time()
    # 먼저, 이벤트 있는지 확인
    while True:
        if not While_True_Condition(start_time,60):
            return
        act_popup_mark_x = Find_in_Area('act_popup_mark_x', 155-20,511-20,40,40, 0.9)
        cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.95)
        if (cond_balloon_lack_heart):
            click(cond_balloon_lack_heart[0], cond_balloon_lack_heart[1])
            time.sleep(0.5)
        
        if whereto == 'fountain':
            print('[왕국활동-분수] 좌상 드래그 한 상태라 가정')
            Kingdom_ready('kkd_out')
            act_fountain1 = LocateCenterOnScreenshot('act_fountain1', 0.88)
            act_fountain2 = LocateCenterOnScreenshot('act_fountain2', 0.88)
            act_fountain3 = LocateCenterOnScreenshot('act_fountain3', 0.88)
            # 2번이 젤 잘 인식되나..
            if (act_fountain2):
                print('act_fountain2',act_fountain2)
                click(act_fountain2[0]-130,act_fountain2[1]+24)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            elif (act_fountain1):
                print('act_fountain1',act_fountain1)
                click(act_fountain1[0]-130,act_fountain1[1]+24+35)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            elif (act_fountain3):
                print('act_fountain3',act_fountain3)
                click(act_fountain3[0]-130,act_fountain3[1]+24-21)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            else:
                print('화면에 없는뎁쇼...?')
                Enter_Screenshot_mode('left_up')
        elif whereto == 'guild':
            cond_guild = Find_in_Area('cond_guild', 470,465,18,19, 0.9)
            if (cond_guild):
                print('cond_guild',cond_guild)
                click(cond_guild[0], cond_guild[1])
                start_guild_t = time.time()
                while True:
                    if not While_True_Condition(start_guild_t, 50):
                        return
                    cond_guild_in = Find_in_Area('cond_guild_in', 626,477,19,19, 0.9)
                    if (cond_guild_in):
                        time.sleep(2)
                        print('cond_guild_in',cond_guild_in)
                        click(450,380)
                        time.sleep(1)
                        click(450,380)
                        time.sleep(2)
                        click(865,500)
                        time.sleep(5)
                        Kingdom_ready('kkd_out')
            else:
                print('길드 보상 수령 완료!')
                return
        elif whereto == 'shop':
            cond_shop = Find_in_Area('cond_shop', 45,111,23,21, 0.9)
            cond_shop1 = Find_in_Area('cond_shop1', 45,111,23,21, 0.9)
            if (cond_shop):
                click(cond_shop[0], cond_shop[1])
                time.sleep(2)
                if Kingdom_ready('sangjum_in'):
                    bShop = True
                    break
                else:
                    print('상점 진입 실패!')
                    return False
            elif (cond_shop1):
                click(cond_shop1[0], cond_shop1[1])
                time.sleep(2)
                if Kingdom_ready('sangjum_in'):
                    bShop = True
                    break
                else:
                    print('상점 진입 실패!')
                    return False
            else:
                print('[상점] 이벤트 없음')
                Kingdom_ready('kkd_out')
                return False
        
        else:
            # 왕국활동 창이 켜져 있으면
            if (act_popup_mark_x):
                if whereto == 'trade':
                    # 이미지 확인(무역센터 느낌표)
                    activity_trade1 = Find_in_Area('activity_trade1', 155-40,95+13-40,80,80, 0.95)
                    if (activity_trade1):
                        print('[왕국활동] 무역센터 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 무역센터로 들어갑니다.')
                        click(155,135)
                        time.sleep(2)
                        bTradeEvent = True
                        break
                if whereto == 'research':
                    # 이미지 확인(연구소 느낌표)
                    if Kingdom_ready('research_in'):
                        bResearchEvent = True
                        break
                    else:
                        activity_research = Find_in_Area('activity_research', 155-40,95+76*1-40,80,80, 0.95)
                        if (activity_research):
                            print('[왕국활동] 연구소 이벤트가 없습니다.')
                            return False
                        else:
                            print('[왕국활동] 연구소 들어갑니다.')
                            click(155,135+76+32)
                            time.sleep(2)
                            bResearchEvent = True
                            break
                        
                if whereto == 'balloon':
                    # 이미지 확인(열기구 느낌표)
                    activity_balloon = Find_in_Area('activity_balloon', 155-40,95+76*2+40,80,80, 0.95)
                    if (activity_balloon):
                        print('[왕국활동] 열기구 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 열기구 들어갑니다.')
                        click(155,135+76*2+32)
                        time.sleep(2)
                        bBalloonEvent = True
                        break
                if whereto == 'train':
                    # 이미지 확인(열차 느낌표)
                    activity_train = Find_in_Area('activity_train', 115,95+76*3+27,80,80, 0.95)
                    if (activity_train):
                        print('[왕국활동] 곰젤리 열차 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 곰젤리 열차 들어갑니다.')
                        click(155,135+76*3+32)
                        time.sleep(2)
                        bTrainEvent = True
                        break
                if whereto == 'sowon':
                    print('[왕국활동] 소원나무는 그냥 들어가 드립니다.')
                    click(155,135+76*4)
                    time.sleep(2)
                    bSowonEvent = False
                    return print('[앵무엔터] 소원나무 진입!')
                    
            else:
                if whereto == 'trade' and Kingdom_ready('trade_in'):
                    bTradeEvent = True
                    break
                elif whereto == 'research' and Kingdom_ready('research_in'):
                    bResearchEvent = True
                    break
                elif whereto == 'balloon' and Kingdom_ready('balloon_in'):
                    bBalloonEvent = True
                    break
                elif whereto == 'train' and Kingdom_ready('train_in'):
                    bTrainEvent = True
                    break
                else:
                    Kingdom_ready('kkd_out')

                # 왕국활동 창 꺼져있는 상태에선
                act_check_mark = Find_in_Area('act_check_mark', 174,458,13,11, 0.9)         # 체크 마크
                act_nukimpyo_mark = Find_in_Area('act_nukimpyo_mark', 174,458,13,11, 0.9)   # 느낌표 마크
            
                if (act_check_mark) or (act_nukimpyo_mark): # 뭐라도 있으면
                    click(155,490)          # 클릭해!
                    time.sleep(1)
                else:
                    print('[왕국활동]아무 이벤트도 없습니다.')
                    return False

    activity_monitor_time = time.time()
    # 분수 입장
    while bFountain:
        if not While_True_Condition(activity_monitor_time, 60):
            return
        Cond_fountain = Find_in_Area('Cond_fountain', 512,63,44,30, 0.9)
        pix_prod = Get_pixel_tuple(630,470)       # 보상 수령 가능여부
        if (Cond_fountain):
            if (pix_prod == pix_green):
                click(655, 465)
            else:
                click(892,54)
                time.sleep(1)
                return print('분수 보상 수령할 게 없네요!')
        # 있었는데요. 없습니다.
        Cond_fountain_result = LocateCenterOnScreenshot('Cond_fountain_result', 0.9)
        if (Cond_fountain_result):
            click(295,60)
            time.sleep(0.3)
            Cond_fountain_result = LocateCenterOnScreenshot('Cond_fountain_result', 0.9)
            if not (Cond_fountain_result):
                Kingdom_ready('kkd_out')
                return print('분수 보상 수령 완료!')
        time.sleep(1)
    
    # 상점 입장
    while bShop:
        if not While_True_Condition(activity_monitor_time, 120):
            return
        cond_shop_red_dot = Find_in_Area('cond_shop_red_dot', 160,32,19,505, 0.9)
        cond_shop_red_check = Find_in_Area('cond_shop_red_check', 160,32,19,505, 0.9)
        cond_shop_jaehwa = Find_in_Area('cond_shop_jaehwa', 53,505,75,33, 0.9)
        if (cond_shop_red_check) and not (cond_shop_red_dot):
            print('cond_shop_red_check',cond_shop_red_check)
            clickExact(cond_shop_red_check[0], cond_shop_red_check[1])
            time.sleep(1)
            cond_shop_dobby_is = Find_in_Area('cond_shop_dobby_is', 180,485,740,27, 0.9)
            if (cond_shop_dobby_is):
                click(cond_shop_dobby_is[0], cond_shop_dobby_is[1])
                time.sleep(2)
        if (cond_shop_red_dot):
            print('cond_shop_red_dot',cond_shop_red_dot)
            clickExact(cond_shop_red_dot[0], cond_shop_red_dot[1])
            time.sleep(1)
        if not (cond_shop_red_check) and not (cond_shop_red_dot):
            if not (cond_shop_jaehwa):
                click(35,55)
                time.sleep(1)
                Drag(25,505,25,100,1)
                time.sleep(1)
            else:
                print('상점보상 끝!')
                click(892,54)
                time.sleep(2)
                Kingdom_ready('kkd_out')
                return True
        time.sleep(1)    
    # 무역센터 진입
    trade_error_count = 0
    while bTradeEvent:
        if not While_True_Condition(activity_monitor_time, 120):
            return
        cond_trade_event = Find_in_Area('cond_trade_event', 170,102,9,14, 0.85)             # 해상무역센터 이벤트 발생
        cond_trade_perl = LocateCenterOnScreenshot('cond_trade_perl', 0.85)               # 해상무역센터 위치 확인
        cond_trade_angmu = Find_in_Area('cond_trade_angmu', 150,320,29,25, 0.85)            # 해상무역센터 앵무 교역소 이벤트
        cond_trade_refresh = Find_in_Area('cond_trade_refresh', 733,500,34,18, 0.85)        # 해상무역센터 앵무 교역소 새로고침
        cond_trade_angmu_confirm = Find_in_Area('cond_trade_angmu_confirm', 420,80,58,33, 0.85)   # 해상무역센터 앵무 교역소 위치 확인
        cond_trade_angmu_yoomul = Find_in_Area('cond_trade_angmu', 70,325,20,20, 0.85)  # 오색 조개 갤러리 이벤트 있음!
        
        if not bStep2_Angmu and (cond_trade_event):
            print('cond_trade_event',cond_trade_event)
            # 엥 이건 왜 있는거지...+??
        if not bStep2_Angmu and (cond_trade_perl):
            print('cond_trade_perl',cond_trade_perl)
            # 앵무 교역소!
            if (cond_trade_angmu):
                print('cond_trade_angmu',cond_trade_angmu)
                click(cond_trade_angmu[0]-26,cond_trade_angmu[1]+24)
                time.sleep(2)
            # 오색 조개 갤러리!
            elif (cond_trade_angmu_yoomul):
                # 갤러리 들어가는 게 우선이지...
                while True:
                    if not While_True_Condition(activity_monitor_time, 120):
                        return
                    
                    cond_trade_gallary = Find_in_Area('cond_trade_gallary', 60,40,50,30, 0.85)  # 오색 조개 갤러리 들어옴!
                    if (cond_trade_gallary):    # 갤러리 들어와 있는 상태에서
                        print('갤러리 잘 들어옴!')
                        break
                    else:
                        print('갤러리 들어가자!')
                        click(57, 356)   # 오색 조개 갤러리 들어가!
                    time.sleep(1)
                    
                trade_error_count = 0
                while True:
                    if not While_True_Condition(activity_monitor_time, 120):
                        return
                    mark_x = Find_in_Area('mark_x', 619,144,30,30, 0.85)  # 뭔가 창이 떠있으?
                    if mark_x:
                        # 뭔지 모르지만 떠있으니 사고 본다
                        click(460, 382)  # 구입하기 클릭클릭!!
                        time.sleep(1)
                        # 만약 조개가 부족하면 ㅠ.ㅠ
                        cond_trade_not_enough = Find_in_Area('cond_trade_not_enough', 378,213,173,35, 0.85)
                        if (cond_trade_not_enough):
                            click(460, 382)   # 확인 클릭!
                            time.sleep(1)
                            click(635, 159)  # x 클릭!
                            time.sleep(1)
                            
                    cond_trade_pearl1 = Find_in_Area('cond_trade_pearl', 103,454,50,50, 0.85)  # 펄 마크! (전설 영혼석 자리 - 바요,서리)
                    if (cond_trade_pearl1):
                        click(172, 281)   # 전설 영혼석 클릭!
                        time.sleep(1)
                        click(460, 382)  # 구입하기 클릭클릭!!
                        time.sleep(2)
                        # 만약 조개가 부족하면 ㅠ.ㅠ
                        cond_trade_not_enough = Find_in_Area('cond_trade_not_enough', 378,213,173,35, 0.85)
                        if (cond_trade_not_enough):
                            click(460, 382)   # 확인 클릭!
                            time.sleep(1)
                            click(635, 159)  # x 클릭!
                            time.sleep(1)
                            cond_trade_pearl1 = False

                    if trade_legend:
                        cond_trade_pearl2 = Find_in_Area('cond_trade_pearl', 320,281,50,50, 0.85)  # 펄 마크! (전설 영혼 조각 자리)
                        if (cond_trade_pearl2):
                            click(386, 222)   # 전설 영혼 조각 클릭!
                            time.sleep(1)
                            click(460, 382)  # 구입하기 클릭클릭!!
                            time.sleep(2)
                            # 만약 조개가 부족하면 ㅠ.ㅠ
                            cond_trade_not_enough = Find_in_Area('cond_trade_not_enough', 378,213,173,35, 0.85)
                            if (cond_trade_not_enough):
                                click(460, 382)   # 확인 클릭!
                                time.sleep(1)
                                click(635, 159)  # x 클릭!
                                time.sleep(1)
                                cond_trade_pearl2 = False
                    else:
                        cond_trade_pearl2 = False
                    
                    if trade_hero:
                        cond_trade_pearl3 = Find_in_Area('cond_trade_pearl', 320,455,50,50, 0.85)  # 펄 마크! (에픽 영혼 조각 자리)
                        if (cond_trade_pearl3):
                            click(388, 400)   # 에픽 영혼 조각 클릭!
                            time.sleep(1)
                            click(460, 382)  # 구입하기 클릭클릭!!
                            time.sleep(2)
                    else:
                        cond_trade_pearl3 = False
                    
                    cond_trade_pearl4 = Find_in_Area('cond_trade_pearl', 496,455,50,50, 0.85)  # 펄 마크! (길드 유물 자리)
                    if (cond_trade_pearl4):
                        click(561, 403)  # 유물 자리 클릭!
                        time.sleep(1)
                        click(460, 382)  # 구입하기 클릭클릭!!
                        time.sleep(4)
                        click(289, 54)  # 허공 한 번 클릭
                        time.sleep(2)
                        # 만약 조개가 부족하면 ㅠ.ㅠ
                        cond_trade_not_enough = Find_in_Area('cond_trade_not_enough', 378,213,173,35, 0.85)
                        if (cond_trade_not_enough):
                            click(460, 382)   # 확인 클릭!
                            time.sleep(1)
                            click(635, 159)  # x 클릭!
                            time.sleep(1)
                            cond_trade_pearl4 = False
                    
                    if not ((cond_trade_pearl1) or (cond_trade_pearl2) or (cond_trade_pearl3) or (cond_trade_pearl4)):
                        print('모든 구매를 마칩니다.')
                        click(892, 54)
                        time.sleep(2)
                        click(892, 54)
                        time.sleep(4)
                        Kingdom_ready('kkd_out')
                        return False

                    time.sleep(0.5)
            else:
                print('이벤트가 없는데 그냥 들어올리 없서!')
                click(289, 54)  # 허공 한 번 클릭
                trade_error_count = trade_error_count + 1
                time.sleep(1)
                if trade_error_count > 10:
                    print('무엇때문에 들어왔을까')
                    click(892, 54)
                    time.sleep(6)
                    Kingdom_ready('kkd_out')
                    return False
                    
        if bStep2_Angmu and (cond_trade_refresh):       # 앵무 교역소, 무료 새로고침인 경우
            print('cond_trade_refresh',cond_trade_refresh)
            click(cond_trade_refresh[0], cond_trade_refresh[1])
        
        if bStep2_Angmu and not (cond_trade_refresh):   # 앵무 교역소, 새로고침 클릭 완료
            print('[앵무엔터] 교역소 들어와 새로고침도 완료 했습니다!')
            return True
        
        if not bStep2_Angmu and (cond_trade_angmu_confirm):
            print('[교역소 in] 앵무 교역소 in!',cond_trade_angmu_confirm)
            bStep2_Angmu = True
        time.sleep(1)

    # 연구소 입장 확인까지만
    while bResearchEvent:
        if not While_True_Condition(activity_monitor_time, 120):
            return
        cond_research = Find_in_Area('cond_research', 12,36,36,36, 0.9)  # 연구소 노움 얼굴
        if (cond_research):
            return True
        Cond_research_comp = LocateCenterOnScreenshot('Cond_research_comp', 0.945)
        if (Cond_research_comp):
            print('Cond_research_comp',Cond_research_comp)
            click(460, 295)
        time.sleep(1)
    
    # 열기구 입장 확인 및 보내기.
    while bBalloonEvent:
        complete_confirm = 0
        error_count = 0
        while True:
            if not While_True_Condition(activity_monitor_time, 120):
                return

            cond_kkd_balloon = Find_in_Area('cond_kkd_balloon', 9,36,25,35, 0.85)               # 열기구 로비
            cond_kkd_balloon_ing = Find_in_Area('cond_kkd_balloon_ing', 364,85,28,37, 0.85)     # 열기구 날아다니는 중
            cond_balloon_arrive = LocateCenterOnScreenshot('cond_balloon_arrive', 0.95)   # 열기구 도착 화면
            if (cond_balloon_arrive):
                error_count = 0
                complete_confirm = 0
                click(cond_balloon_arrive[0], cond_balloon_arrive[1])
                time.sleep(0.3)
            elif (cond_kkd_balloon_ing):
                print('열기구 날아다니는 중인데 왜 들어왔지?')
                complete_confirm = 0
                click(892,54)
                time.sleep(2)
                return False
            elif (cond_kkd_balloon):
                print('로비.. 보상 수령 이전 화면일 수 있으니 기다려 봅시다..!',complete_confirm)
                error_count = 0
                if complete_confirm > 5:
                    print('오케이 확인 완료! balloon send로 넘깁니다!')
                    return True
                time.sleep(1)
                complete_confirm = complete_confirm + 1
            else:
                print('error_count',error_count)
                error_count = error_count + 1
                time.sleep(1)
                if error_count > 10:
                    return False

    # 기차 입장 확인까지만
    while bTrainEvent:
        if not While_True_Condition(activity_monitor_time, 30):
            return
        cond_kkd_train = Find_in_Area('cond_kkd_train', 30,42,25,33, 0.85)  # 곰젤리열차
        if (cond_kkd_train):
            return True
        time.sleep(1)

# 변수 x, y.... 중 y는 안쓰긴 하는데
def Angmu_Action_condition(x):
    bBuy_Must = False   # 꼭 사(별의 조각, 각종 수정, 1렙 스킬 파우더, 솜)
    bBuy_Mid = False    # 재고 봐서 사(기존 동일 : 2렙 스킬 파우더 - 325 이상만)
    bBuy_Mid_1 = False  # 재고 봐서 사(재고 비교해서 적은놈이면 삼 : 베리,비스킷,우유)
    bBuy_No = False     # 안 살거
    # 살지말지 고민좀 해보고(다 캡처 못한 영혼석, 사탕, 3렙 스킬 파우더)
    # 3. 3렙 파우더, 시계의 경우 줄 것의 재고 비율이...... 몇 프로로 해야 하나
    # 1. 1렙 파우더, 조각들, 솜은 무조건 구매함(못사면 말고)
    trade_must_buy = ('crystal_pure', 'crystal_magic', 'crystal_power', 'crystal_quick', 'trade_star', 'trade_black',
                      'trade_assist_lv1', 'trade_bomb_lv1', 'trade_fist_lv1', 'trade_recovery_lv1', 'trade_shield_lv1',
                      'trade_shooting_lv1', 'trade_staff_lv1', 'trade_sword_lv1',
                      'trade_cotton')
    for t in trade_must_buy:
        item_check = Find_in_Area(t, x+35,345,60,50, 0.82)
        if (item_check):
            print('꼭 살것!')
            new_ctr = item_check    # 살거 위치 확인(현재 ctr은 상자 왼쪽 상단 baseline)
            bBuy_Must = True    # 꼭 사야해!
            break
    if bBuy_Must:
        click(new_ctr[0], new_ctr[1])
        time.sleep(1)
        click(460, 385)
        time.sleep(2)
        trade_not_enough = Find_in_Area('trade_not_enough', 472,221,25,17, 0.85)
        if (trade_not_enough):
            print('앗 부족..')
            click(635, 160)
            time.sleep(0.3)
            click(635, 160)
            time.sleep(1)
        return True
    
    # 2. 2렙 파우더의 경우 줄 것 재고 325개 이상은 구매함(나무,젤빈,각설,1렙 스킬파우더 상관없음)
    trade_mid_buy = ('trade_assist_lv2', 'trade_bomb_lv2', 'trade_fist_lv2', 'trade_recovery_lv2', 'trade_shield_lv2',
                     'trade_shooting_lv2', 'trade_staff_lv2', 'trade_sword_lv2')
    for t in trade_mid_buy:
        item_check = Find_in_Area(t, x+35,345,60,50, 0.82)
        if (item_check):
            print('Mid 조건!')
            new_ctr = item_check    # 살거 위치 확인(현재 ctr은 상자 왼쪽 상단 baseline)
            bBuy_Mid = True     # 재고 봐서 사야해!
            break
    if bBuy_Mid:
        if Angmu_check(x+9) > 324:
            print('어머 이건 사야해!')
            click(new_ctr[0], new_ctr[1])
            time.sleep(1)
            click(480, 385)
            time.sleep(2)
            trade_not_enough = Find_in_Area('trade_not_enough', 472,221,25,17, 0.85)
            if (trade_not_enough):
                print('앗 부족..')
                click(635, 160)
                time.sleep(0.3)
                click(635, 160)
                time.sleep(0.3)
            return True
        else:
            print('325개 안되어 취소!')
            return True
    # 3. 물물교환 할거(베리, 비스킷, 우유)
    trade_mid_buy_1 = ('trade_berry', 'trade_biscuit', 'trade_milk')
    for t in trade_mid_buy_1:
        item_check = Find_in_Area(t, x+35,345,60,50, 0.82)
        if (item_check):
            print('Mid_1 조건!')
            new_ctr = item_check    # 살거 위치 확인(현재 ctr은 상자 왼쪽 상단 baseline)
            bBuy_Mid_1 = True     # 재고 봐서 사야해!
            break
    if bBuy_Mid_1:
        print('어머 이건 봐야 해!')
        # 줄게 뭐니?
        bJeryo = False
        trade_jeryo = ('trade_small_wood', 'trade_small_jelbean', 'trade_small_sugar')  # 이거 아니면 동급 재료(베리 비스킷 우유)
        for t in trade_jeryo:
            whatisthis = Find_in_Area(t, x,430,40,46, 0.85)
            if (whatisthis):
                print(t)
                bJeryo = True
                break
        if bJeryo:  # 기본재료면 걍 넘겨보리기
            print('오 기본재료로 중간재료 개이득!')
            click(new_ctr)
            time.sleep(1)
            click(random.randint(420,500),random.randint(370,400))
            time.sleep(2)
            trade_not_enough = Find_in_Area('trade_not_enough', confidence=0.85, region=(472,221,25,17))
            if (trade_not_enough):
                print('앗 부족..')
                click(635, 160)
                time.sleep(0.3)
                click(635, 160)
                time.sleep(0.3)
            return True
        else:
            # 동급재료면 줄거 재고 파악
            iTrade_to_give = Angmu_check(x+9)
            # 읽었으면 들어가서
            if iTrade_to_give > 0:
                click(new_ctr[0], new_ctr[1])
                time.sleep(1)
                # 받을 거 수량 파악
                iTrade_to_receive = Trade_how_much()
                # 줄 것 재고가 받을 것 재고보다 많으면
                if iTrade_to_give > iTrade_to_receive:
                    print('오 이거 바꾸자!')
                    click(random.randint(420,500),random.randint(370,400))
                    time.sleep(2)
                    trade_not_enough = Find_in_Area('trade_not_enough', 472,221,25,17, 0.85)
                    if (trade_not_enough):
                        print('앗 부족..')
                        click(635, 160)
                        time.sleep(0.3)
                        click(635, 160)
                        time.sleep(0.3)
                    return True
                else:
                    # 받을 게 줄 것보다 재고 많은 경우 걍 빠져나옴
                    print('안바꿈!')
                    click(635, 160)
                    time.sleep(0.3)
                    click(635, 160)
                    time.sleep(0.3)
                    return True
            else:
                print('왜 못읽지?')
                return True
    
    # 4. 안 살거(나무 젤리빈 각설)
    trade_not_buy = ('trade_wood', 'trade_jelbean', 'trade_sugar')
    for t in trade_not_buy:
        item_check = Find_in_Area(t, x+35,345,60,50, 0.82)
        if (item_check):
            print('기본재룐 안사요!')
            return True
    
    print('조건 네 개 아니면.. 3렙 파우더, 영혼석, 사탕 또는 시계 중 하나겠네')

def Angmu_check(x1):
    trade_slash = Find_in_Area('trade_slash', x1,439,100,28, 0.85)
    trade_slash_mini = Find_in_Area('trade_slash_mini', x1,439,100,28, 0.85)
    trade_slash_real_mini = Find_in_Area('trade_slash_real_mini', x1,439,100,28, 0.85)
    if (trade_slash):
        x2 = trade_slash[0]
    if (trade_slash_mini):
        x2 = trade_slash_mini[0]
    if (trade_slash_real_mini):
        x2 = trade_slash_real_mini[0]
    if (not (trade_slash)) and (not (trade_slash_mini)) and (not (trade_slash_real_mini)):
        print('/없음')
        return 0

    its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
    list_real_num = list()  # 실제값 계산을 위한 리스트 생성
    list_num_0 = list()
    list_num_1 = list()
    list_num_2 = list()
    list_num_3 = list()
    list_num_4 = list()
    list_num_5 = list()
    list_num_6 = list()
    list_num_7 = list()
    list_num_8 = list()
    list_num_9 = list()
    # 으아아아아 숫자 가져와아아아아
    find_num_x('up_th0', x1, x2, list_num_0)
    find_num_x('up_th0_1', x1, x2, list_num_0)
    find_num_x('up_th0_2', x1, x2, list_num_0)
    find_num_x('up_th1', x1, x2, list_num_1)
    find_num_x('up_th1_1', x1, x2, list_num_1)
    find_num_x('up_th2', x1, x2, list_num_2)
    find_num_x('up_th3', x1, x2, list_num_3)
    find_num_x('up_th3_1', x1, x2, list_num_3)
    find_num_x('up_th4', x1, x2, list_num_4)
    find_num_x('up_th4_1', x1, x2, list_num_4)
    find_num_x('up_th5', x1, x2, list_num_5)
    find_num_x('up_th5_1', x1, x2, list_num_5)
    find_num_x('up_th6', x1, x2, list_num_6)
    find_num_x('up_th6_1', x1, x2, list_num_6)
    find_num_x('up_th7', x1, x2, list_num_7)
    find_num_x('up_th8', x1, x2, list_num_8)
    find_num_x('up_th9', x1, x2, list_num_9)
    find_num_x('up_ths_0', x1, x2, list_num_0)
    find_num_x('up_thm_0', x1, x2, list_num_0)
    find_num_x('up_ths_0_1', x1, x2, list_num_0)
    find_num_x('up_ths_0_2', x1, x2, list_num_0)
    find_num_x('up_ths_1', x1, x2, list_num_1)
    find_num_x('up_thm_1', x1, x2, list_num_1)
    find_num_x('up_ths_2', x1, x2, list_num_2)
    find_num_x('up_ths_2_1', x1, x2, list_num_2)
    find_num_x('up_ths_3', x1, x2, list_num_3)
    find_num_x('up_thm_3', x1, x2, list_num_3)
    find_num_x('up_ths_4', x1, x2, list_num_4)
    find_num_x('up_thm_4', x1, x2, list_num_4)
    find_num_x('up_ths_5', x1, x2, list_num_5)
    find_num_x('up_ths_5_1', x1, x2, list_num_5)
    find_num_x('up_ths_6', x1, x2, list_num_6)
    find_num_x('up_ths_6_1', x1, x2, list_num_6)
    find_num_x('up_ths_7', x1, x2, list_num_7)
    find_num_x('up_ths_7_1', x1, x2, list_num_7)
    find_num_x('up_ths_8', x1, x2, list_num_8)
    find_num_x('up_ths_8_1', x1, x2, list_num_8)
    find_num_x('up_ths_8_2', x1, x2, list_num_8)
    find_num_x('up_ths_9', x1, x2, list_num_9)
    find_num_x('up_thm_9', x1, x2, list_num_9)
    find_num_x('up_ths_9_1', x1, x2, list_num_9)
    list_num_0 = del_duplication(3, list_num_0)
    list_num_1 = del_duplication(3, list_num_1)
    list_num_2 = del_duplication(3, list_num_2)
    list_num_3 = del_duplication(3, list_num_3)
    list_num_4 = del_duplication(3, list_num_4)
    list_num_5 = del_duplication(3, list_num_5)
    list_num_6 = del_duplication(3, list_num_6)
    list_num_7 = del_duplication(3, list_num_7)
    list_num_8 = del_duplication(3, list_num_8)
    list_num_9 = del_duplication(3, list_num_9)
    if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0],0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0],1))
        print('append 후 list_1', list_num_1)
    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0],2))

    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0],3))

    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0],4))

    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0],5))

    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0],6))

    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0],7))

    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0],8))

    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0],9))

    # 지겨운 실제값 리스트를 받았으니
    list_real_num.sort()    # 추려서
    print('set 이전',list_real_num)
    
    # list_real_num1 = set(list_real_num)
    
    # print('set 이후',list_real_num1)
    
    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)

    print('현재 재고는 =', its_number)
    return its_number


def Angmu_Aft_Refresh():
    Scroll_count = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 300):
            return

        if Scroll_count == 0:
            trade_kidung = Find_in_Area('trade_kidung', 2,350,917,45, 0.85)
            trade_block = Find_in_Area('trade_block', 2,350,917,45, 0.85)
            trade_nachimban = Find_in_Area('trade_nachimban', 2,350,917,45, 0.85)
            if (trade_kidung):
                kidung_numb = Angmu_check(trade_kidung[0] - 26)
            else:
                kidung_numb = 0
            if (trade_block):
                block_numb = Angmu_check(trade_block[0] - 26)
            else:
                block_numb = 0
            if (trade_nachimban):
                nachimban_numb = Angmu_check(trade_nachimban[0] - 26)
            else:
                nachimban_numb = 0
            
            max_numb = max(kidung_numb, block_numb, nachimban_numb)
            
            if kidung_numb > 0 and kidung_numb == max_numb:
                click(trade_kidung[0], trade_kidung[1])
                time.sleep(0.2)
                click(460, 385)
                time.sleep(2)
            if block_numb > 0 and block_numb == max_numb:
                click(trade_block[0], trade_block[1])
                time.sleep(0.2)
                click(460, 385)
                time.sleep(2)
            if nachimban_numb > 0 and nachimban_numb == max_numb:
                click(trade_nachimban[0], trade_nachimban[1])
                time.sleep(0.2)
                click(460, 385)
                time.sleep(2)
            # Angmu_Action('trade_tro_1', trade_tro_1)
            # Angmu_Action('trade_tro_2', trade_tro_2)
            
            Angmu_Action_condition(543)
            Angmu_Action_condition(700)
        
        # 드래그는 음 조건 봐서
        if Scroll_count >= 5:
            print('완료')
            click(892,54)
            time.sleep(2)
            click(892,54)
            time.sleep(6)
            return
        else:
            # 드래그드래그
            Drag(804, 485, 804-157*4, 485, 4)
            time.sleep(0.2)
        
        start_lineup = time.time()
        while True:
            if not While_True_Condition(start_lineup, 30):
                # 세부 정렬하기
                return

            cond_trade_angmu_confirm = Find_in_Area('cond_trade_angmu_confirm', 420,80,58,33, 0.85)   # 해상무역센터 앵무 교역소 위치 확인
            if not (cond_trade_angmu_confirm):
                print('튕기거나 빠져나갔나봐요...')
                Kingdom_ready('kkd_out')
                return
            
            trade_baseline_gray = LocateCenterOnScreenshot('trade_baseline_gray', 0.85)
            if (trade_baseline_gray):
                if (92 >= trade_baseline_gray[0] > 70) or (92+157 >= trade_baseline_gray[0] > 70+157):
                    print('오우예')
                    Scroll_count = Scroll_count + 1
                    break
                else:
                    Drag_MouseDown(790, 485, 790+50, 485, 2)
                    trade_baseline_gray_new = LocateCenterOnScreenshot('trade_baseline_gray', 0.85)
                    if (trade_baseline_gray_new):
                        Drag(790+50-trade_baseline_gray_new[0]+73,485,3)   # 153인데 20 더 여유줌
                    time.sleep(0.2)
            
            trade_baseline = LocateCenterOnScreenshot('trade_baseline', 0.85)
            if (trade_baseline):
                if (92 >= trade_baseline[0] > 70) or (92+157 >= trade_baseline[0] > 70+157):
                    print('오우예')
                    Scroll_count = Scroll_count + 1
                    break
                else:
                    Drag_MouseDown(790, 485, 790+50, 485, 2)
                    time.sleep(0.5)
                    trade_baseline_new = LocateCenterOnScreenshot('trade_baseline', 0.85)
                    if (trade_baseline_new):
                        Drag(790+50-trade_baseline_new[0]+73, 485, 3)
                    time.sleep(0.2)

        # 맞나 후. 이상. 후..
        if 5 >= Scroll_count >= 1:
            trade_baseline_list = LocateAll_Center('trade_baseline', 0.943)
            if len(trade_baseline_list) != 0:
                for p in trade_baseline_list:
                    Angmu_Action_condition(p[0])

    return print('Angmu_Aft_Refresh 완료!')

# 킹덤패스 일일/시즌미션, 시즌 보상 수령
def Kpass_reward():
    pix_pass_reward = Get_pixel_tuple(901,138) # 패스 보상
    if pix_pass_reward == pix_pass_reward_exist:
        click(870,155)
        time.sleep(1)
    else:
        print('킹덤패스 보상 없음!')
        return
    
    bPass1 = False
    bPass2 = False
    bPass3 = False
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 80):
            return

        bClicked = False
        pix_kpass1 = Get_pixel_tuple(16,101)          # 데일리 미션
        pix_kpass2 = Get_pixel_tuple(16+143,101)      # 시즌 미션
        pix_kpass3 = Get_pixel_tuple(16-1+143*2,101)  # 시즌 보상
        pix_reward = Get_pixel_tuple(770,520)         # 모두 받기
        if pix_kpass1 == pix_white: # 데일리 미션
            if pix_reward == bReward:
                click(826, 529)
                time.sleep(0.5)
            else:
                bPass1 = True
            
        if pix_kpass2 == pix_white: # 시즌 미션
            if pix_reward == bReward:
                click(826, 529)
                time.sleep(0.5)
            else:
                bPass2 = True
        if pix_kpass3 == pix_white: # 시즌 보상
            if pix_reward == bReward:
                click(826, 529)
                time.sleep(0.5)
            else:
                bPass3 = True
        if not bPass1:
            click(80, 113)
            time.sleep(0.5)
        elif not bPass2:
            click(80+143*1, 113)
            time.sleep(0.5)
        elif not bPass3:
            click(80+143*2, 113)
            time.sleep(0.5)
        else:
            print('다 수령했네요')
            click(892, 55)
            time.sleep(1.5)
            return
        time.sleep(1)

def Skip_Next(prod_direction_left):
    if prod_direction_left:
        click(164, 280)
        time.sleep(0.3)
    else:
        click(485, 280)
        time.sleep(0.3)
    start_time = time.time()
    if not While_True_Condition(start_time, 20):
        return
    # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
    # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
    dotdotdot_1 = Find_in_Area('dotdotdot_1', 223,190,205,132, 0.9)   # 화살표 피한 센터 위치
    dotdotdot_1_1 = Find_in_Area('dotdotdot_1', 150,323,370,110, 0.9)   # 화살표 아래 넓은 위치
    dotdotdot_2 = Find_in_Area('dotdotdot_2', 223,190,205,132, 0.9)   # 화살표 피한 센터 위치
    dotdotdot_2_1 = Find_in_Area('dotdotdot_2', 150,323,370,110, 0.9)   # 화살표 아래 넓은 위치
    dotdotdot_3 = Find_in_Area('dotdotdot_3', 223,190,205,132, 0.9)   # 화살표 피한 센터 위치
    dotdotdot_3_1 = Find_in_Area('dotdotdot_3', 150,323,370,110, 0.9)   # 화살표 아래 넓은 위치
    
    if (dotdotdot_1):
        print('dotdotdot_1 = ', dotdotdot_1)
        click(dotdotdot_1[0], dotdotdot_1[1])
        time.sleep(0.3)
    if (dotdotdot_1_1):
        print('dotdotdot_1_1 = ', dotdotdot_1_1)
        click(dotdotdot_1_1[0], dotdotdot_1_1[1])
        time.sleep(0.3)
    if (dotdotdot_2):
        print('dotdotdot_2 = ', dotdotdot_2)
        click(dotdotdot_2[0], dotdotdot_2[1])
        time.sleep(0.3)
    if (dotdotdot_2_1):
        print('dotdotdot_2_1 = ', dotdotdot_2_1)
        click(dotdotdot_2_1[0], dotdotdot_2_1[1])
        time.sleep(0.3)
    if (dotdotdot_3):
        print('dotdotdot_3 = ', dotdotdot_3)
        click(dotdotdot_3[0], dotdotdot_3[1])
        time.sleep(0.3)
    if (dotdotdot_3_1):
        print('dotdotdot_3_1 = ', dotdotdot_3_1)
        click(dotdotdot_3_1[0], dotdotdot_3_1[1])
        time.sleep(0.3)
    return

def Trade_how_much():
    trade_howmuch = LocateCenterOnScreenshot('trade_howmuch', 0.89)
    if (trade_howmuch):
        # '개'가 있으면 그 부분까지만 읽음..
        trade_howmuch_end = Find_in_Area('trade_howmuch_end', trade_howmuch[0]+22,trade_howmuch[1]-9,62,18, 0.8)
        if (trade_howmuch_end):
            print('trade_howmuch_end',trade_howmuch_end)
            trade_region_restrict = (trade_howmuch_end[0] - 6) - (trade_howmuch[0] + 22)
        else:
            print('trade_howmuch_end 없음')
            trade_region_restrict = 52
        print('trade_region_restrict',trade_region_restrict)
        
        its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
        list_real_num = list()  # 실제값 계산을 위한 리스트 생성
        list_num_0 = list()
        list_num_1 = list()
        list_num_2 = list()
        list_num_3 = list()
        list_num_4 = list()
        list_num_5 = list()
        list_num_6 = list()
        list_num_7 = list()
        list_num_8 = list()
        list_num_9 = list()
        # 으아아아아 숫자 가져와아아아아
        find_num_trade_in('up_tr_0', trade_howmuch, trade_region_restrict, list_num_0)
        find_num_trade_in('up_tr_0_1', trade_howmuch, trade_region_restrict, list_num_0)
        find_num_trade_in('up_tr_1', trade_howmuch, trade_region_restrict, list_num_1)
        find_num_trade_in('up_tr_2', trade_howmuch, trade_region_restrict, list_num_2)
        find_num_trade_in('up_tr_2_1', trade_howmuch, trade_region_restrict, list_num_2)
        find_num_trade_in('up_tr_3', trade_howmuch, trade_region_restrict, list_num_3)
        find_num_trade_in('up_tr_4', trade_howmuch, trade_region_restrict, list_num_4)
        find_num_trade_in('up_tr_4_1', trade_howmuch, trade_region_restrict, list_num_4)
        find_num_trade_in('up_tr_5', trade_howmuch, trade_region_restrict, list_num_5)
        find_num_trade_in('up_tr_6', trade_howmuch, trade_region_restrict, list_num_6)
        find_num_trade_in('up_tr_6_1', trade_howmuch, trade_region_restrict, list_num_6)
        find_num_trade_in('up_tr_7', trade_howmuch, trade_region_restrict, list_num_7)
        find_num_trade_in('up_tr_7_1', trade_howmuch, trade_region_restrict, list_num_7)
        find_num_trade_in('up_tr_8', trade_howmuch, trade_region_restrict, list_num_8)
        find_num_trade_in('up_tr_8_1', trade_howmuch, trade_region_restrict, list_num_8)
        find_num_trade_in('up_tr_9', trade_howmuch, trade_region_restrict, list_num_9)
        find_num_trade_in('up_tr_9_1', trade_howmuch, trade_region_restrict, list_num_9)

        list_num_0 = del_duplication(2, list_num_0)
        list_num_1 = del_duplication(2, list_num_1)
        list_num_2 = del_duplication(2, list_num_2)
        list_num_3 = del_duplication(2, list_num_3)
        list_num_4 = del_duplication(2, list_num_4)
        list_num_5 = del_duplication(2, list_num_5)
        list_num_6 = del_duplication(2, list_num_6)
        list_num_7 = del_duplication(2, list_num_7)
        list_num_8 = del_duplication(2, list_num_8)
        list_num_9 = del_duplication(2, list_num_9)
        if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
            for p in list_num_0:
                list_real_num.append((p[0],0))
        if (list_num_1):
            for p in list_num_1:
                list_real_num.append((p[0],1))
            print('append 후 list_1', list_num_1)
        if (list_num_2):
            for p in list_num_2:
                list_real_num.append((p[0],2))
        if (list_num_3):
            for p in list_num_3:
                list_real_num.append((p[0],3))
        if (list_num_4):
            for p in list_num_4:
                list_real_num.append((p[0],4))
        if (list_num_5):
            for p in list_num_5:
                list_real_num.append((p[0],5))
        if (list_num_6):
            for p in list_num_6:
                list_real_num.append((p[0],6))
        if (list_num_7):
            for p in list_num_7:
                list_real_num.append((p[0],7))
        if (list_num_8):
            for p in list_num_8:
                list_real_num.append((p[0],8))
        if (list_num_9):
            for p in list_num_9:
                list_real_num.append((p[0],9))
        list_real_num.sort()    # 추려서
        print('set 이전',list_real_num)
        for i in range(len(list_real_num)): # 실제 int값으로 변환
            its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)

        print('현재 재고는 =', its_number)
        return its_number
    else:
        print('보유량: 글씨를 찾지 못했어요!')
        # 걍 사고봐 : 0, 그럼 안사 : 9999
        return 9999

def Train_time(line):
    train_arrive_time = Find_in_Area('train_arrive_time', 280,150+(line-1)*149,75,28, 0.9)
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 30):
            return
        if not (train_arrive_time):
            print('if not 조건')
            train_arrived = Find_in_Area('Cond_train_arrived', 492,118+(line-1)*149,333,111, 0.95)
            
            if (train_arrived):
                click(train_arrived[0], train_arrived[1])
                time.sleep(3)
            
            send_train = Find_in_Area('Cond_train_send', 500,110+(line-1)*149,290,120, 0.8)
            # 색상 구분 못하네....
            send_train_error = Find_in_Area('Cond_train_send_error', 500,110+(line-1)*149,290,120, 0.97)
            
            if (send_train):
                print('기차 보내자')
                click(send_train[0], send_train[1])
                time.sleep(1)
                click(send_train[0], send_train[1])
                time.sleep(1)
                break
            elif (send_train_error):
                print('납품 불가한 제품이 있습니다.')
                time.sleep(1)
                return False
        train_arrive_time_re = Find_in_Area('train_arrive_time', 280,150+(line-1)*149,75,28, 0.9)
        if (train_arrive_time_re):
            train_arrive_time = train_arrive_time_re
            break

    print('%s계정의 %s 라인 조건.'%(title_t,line))
    if (train_arrive_time):
        list_real_num = list()  # 실제값 계산을 위한 리스트 생성
        list_num_0 = list()
        list_num_1 = list()
        list_num_2 = list()
        list_num_3 = list()
        list_num_4 = list()
        list_num_5 = list()
        list_num_6 = list()
        list_num_7 = list()
        list_num_8 = list()
        list_num_9 = list()
        # 으아아아아 숫자 가져와아아아아
        find_train_num('train_0', list_num_0, line)
        find_train_num('train_1', list_num_1, line)
        find_train_num('train_2', list_num_2, line)
        find_train_num('train_3', list_num_3, line)
        find_train_num('train_4', list_num_4, line)
        find_train_num('train_5', list_num_5, line)
        find_train_num('train_6', list_num_6, line)
        find_train_num('train_7', list_num_7, line)
        find_train_num('train_8', list_num_8, line)
        find_train_num('train_9', list_num_9, line)
        list_num_0 = del_duplication(3, list_num_0)
        list_num_1 = del_duplication(3, list_num_1)
        list_num_2 = del_duplication(3, list_num_2)
        list_num_3 = del_duplication(3, list_num_3)
        list_num_4 = del_duplication(3, list_num_4)
        list_num_5 = del_duplication(3, list_num_5)
        list_num_6 = del_duplication(3, list_num_6)
        list_num_7 = del_duplication(3, list_num_7)
        list_num_8 = del_duplication(3, list_num_8)
        list_num_9 = del_duplication(3, list_num_9)
        
        if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
            for p in list_num_0:
                list_real_num.append((p[0],0))

        if (list_num_1):
            for p in list_num_1:
                list_real_num.append((p[0],1))

        if (list_num_2):
            for p in list_num_2:
                list_real_num.append((p[0],2))

        if (list_num_3):
            for p in list_num_3:
                list_real_num.append((p[0],3))

        if (list_num_4):
            for p in list_num_4:
                list_real_num.append((p[0],4))

        if (list_num_5):
            for p in list_num_5:
                list_real_num.append((p[0],5))

        if (list_num_6):
            for p in list_num_6:
                list_real_num.append((p[0],6))

        if (list_num_7):
            for p in list_num_7:
                list_real_num.append((p[0],7))

        if (list_num_8):
            for p in list_num_8:
                list_real_num.append((p[0],8))

        if (list_num_9):
            for p in list_num_9:
                list_real_num.append((p[0],9))

        # 지겨운 실제값 리스트를 받았으니
        list_real_num.sort()    # 추려서

        if len(list_real_num) == 4:
            print('잘읽었네')
            time_h = list_real_num[0][1]*10 + list_real_num[1][1]
            time_m = list_real_num[2][1]*10 + list_real_num[3][1]
            remain_time = time_h*3600+(time_m+1)*60
            print('남은 시간(초) =', remain_time)
            return remain_time
        else:
            print('숫자 넘어가는 순간 캐치한듯')
            return False

def Wood_to_Cotton_Quick(Max_number, Making_Level, prod_direction_left):   # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
    prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        click(random.randint(223+5,428-5),random.randint(190+5,410-5))
        time.sleep(0.5)
    # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
    prod_full_list2 = Find_in_Area('prod_full_list2', 45,60,55,22, 0.95)
    prod_full_list3 = Find_in_Area('prod_full_list3', 45,60,55,22, 0.95)
    prod_full_list4 = Find_in_Area('prod_full_list4', 45,60,55,22, 0.95)
    prod_full_list5 = Find_in_Area('prod_full_list5', 45,60,55,22, 0.95)
    prod_full_list6 = Find_in_Area('prod_full_list6', 45,60,55,22, 0.95)
    prod_full_list7 = Find_in_Area('prod_full_list7', 45,60,55,22, 0.95)
    # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    if (prod_full_list2) or (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!')
        Skip_Next(prod_direction_left)
        return True
    else:
        up_1 = Find_in_Area('up_1', 515,47,14,15, 0.8)
        if (up_1):
            print('1천대!')
            its_number = 1000
        else:
            up_2 = Find_in_Area('up_2', 515,47,14,15, 0.8)
            if (up_2):
                print('2천대!')
                its_number = 2000
            else:
                up_3 = Find_in_Area('up_3', 515,47,14,15, 0.8)
                if (up_3):
                    print('3천대!')
                    its_number = 3000
                else:
                    up_4 = Find_in_Area('up_4', 515,47,14,15, 0.8)
                    if (up_4):
                        print('4천대!')
                        its_number = 4000
                    else:
                        up_5 = Find_in_Area('up_5', 515,47,14,15, 0.8)
                        if (up_5):
                            print('5천대!')
                            its_number = 5000
                        else:
                            up_6 = Find_in_Area('up_6', 515,47,14,15, 0.8)
                            if (up_6):
                                print('6천대!')
                                its_number = 6000
                            else:
                                print('1000 미만...')
                                its_number = 999

        # 설정 수량보다 많아지면 걍 넘어가고
        if its_number >= Max_number:
            Skip_Next(prod_direction_left)
            return False
        # 설정 수량보다 적으면 생산 렙으로 생산
        else:
            wood_list_lv2 = Find_in_Area('wood_list_lv2',58,185,33,106, 0.9)
            jelbean_list_lv2 = Find_in_Area('jelbean_list_lv2',58,185,33,106, 0.9)
            sugar_list_lv2 = Find_in_Area('sugar_list_lv2',58,185,33,106, 0.9)
            if (wood_list_lv2):
                wood_clear = True
            else:
                wood_clear = False
            if(jelbean_list_lv2):
                jelbean_clear = True
            else:
                jelbean_clear = False
            if (sugar_list_lv2):
                sugar_clear = True
            else:
                sugar_clear = False
            start_del_time = time.time()
            while True:
                now_del_time = time.time()
                if now_del_time - start_del_time > 30:
                    Skip_Next(prod_direction_left)
                    return True
                if not wood_clear and not jelbean_clear and not sugar_clear:
                    break
                if wood_clear:
                    wood_list_lv2 = Find_in_Area('wood_list_lv2',58,185,33,106, 0.9)
                    if (wood_list_lv2):
                        click(wood_list_lv2[0], wood_list_lv2[1])
                        time.sleep(0.3)
                    else:
                        prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
                        if (prod_refresh):
                            click(prod_refresh[0], prod_refresh[1]) # >> 클릭(즉시생산)
                            # remain_time_dia = Find_in_Area('remain_time_dia', 90,145,24,20, 0.945)
                            time.sleep(0.5)
                            remain_time_less_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            remain_time_about_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                click(75, 200-73) # 첫째 칸 클릭
                                time.sleep(0.2)
                                click(462, 378)  # 확인
                                time.sleep(0.2)
                                break
                if jelbean_clear:
                    jelbean_list_lv2 = Find_in_Area('jelbean_list_lv2',58,185,33,106, 0.9)
                    if (jelbean_list_lv2):
                        click(jelbean_list_lv2[0], jelbean_list_lv2[1])
                        time.sleep(0.3)
                    else:
                        prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
                        if (prod_refresh):
                            click(prod_refresh[0], prod_refresh[1]) # >> 클릭(즉시생산)
                            # remain_time_dia = Find_in_Area('remain_time_dia', 90,145,24,20, 0.945)
                            time.sleep(0.5)
                            remain_time_less_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            remain_time_about_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                click(75, 200-73) # 첫째 칸 클릭
                                time.sleep(0.2)
                                click(462, 378)  # 확인
                                time.sleep(0.2)
                                break
                if sugar_clear:
                    sugar_list_lv2 = Find_in_Area('sugar_list_lv2',58,185,33,106, 0.9)
                    if (sugar_list_lv2):
                        click(sugar_list_lv2[0], sugar_list_lv2[1])
                        time.sleep(0.3)
                    else:
                        prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
                        if (prod_refresh):
                            click(prod_refresh[0], prod_refresh[1]) # >> 클릭(즉시생산)
                            # remain_time_dia = Find_in_Area('remain_time_dia', 90,145,24,20, 0.945)
                            time.sleep(0.5)
                            remain_time_less_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            remain_time_about_minute = Find_in_Area('remain_time_less_minute', confidence = 0.945, region = (570,239,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                click(651, 85)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                click(75, 200-73) # 첫째 칸 클릭
                                time.sleep(0.2)
                                click(462, 378)  # 확인
                                time.sleep(0.2)
                                break
            click(855, 200+(Making_Level-1)*153)
            time.sleep(0.3)
            click(855, 200+(Making_Level-1)*153)
            time.sleep(0.3)
            Skip_Next(prod_direction_left)
            return True

# 실제 생산하는 녀석.. 이렇게 보니 앞에 생산품도 함수로 만들수 있지 않을까
def prod_action(image, list_image, check_num):
    print('Prod_action함수!',image, list_image, check_num)
    error_count = 0
    prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        click(random.randint(223+5,428-5),random.randint(190+5,410-5))
        time.sleep(0.5)
    
    cond_2nd_clear = Find_in_Area('cond_2nd_clear', 75-10,200-10,20,20, 0.96)
    if (cond_2nd_clear):
        ShowTime = True
    else:
        return True
    
    # 생산품 하나 확인하고, 동작하는 시간은
    start_time = time.time()
    while ShowTime:
        if not While_True_Condition(start_time, 40):
            return
        prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
        if not (prod_refresh):
            # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
            click(random.randint(223+5,428-5),random.randint(190+5,410-5))
            time.sleep(0.5)
        # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
        prod_full_list2 = Find_in_Area('prod_full_list2', 45,60,55,22, 0.95)
        prod_full_list3 = Find_in_Area('prod_full_list3', 45,60,55,22, 0.95)
        prod_full_list4 = Find_in_Area('prod_full_list4', 45,60,55,22, 0.95)
        prod_full_list5 = Find_in_Area('prod_full_list5', 45,60,55,22, 0.95)
        prod_full_list6 = Find_in_Area('prod_full_list6', 45,60,55,22, 0.95)
        prod_full_list7 = Find_in_Area('prod_full_list7', 45,60,55,22, 0.95)
        # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        if (prod_full_list2) or (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!')
            return True

        ctr = Find_in_Area(image, 560,75,105,460, 0.85)
        prd_done = LocateCenterOnScreenshot('prod_done', 0.85)
        list_full = LocateCenterOnScreenshot('Cond_makinglist_full', 0.97)
        list_full1 = LocateCenterOnScreenshot('Cond_makinglist_full1', 0.97)
        lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
        not_opened = LocateCenterOnScreenshot('Cond_not_opened', 0.95)
        ctr_list = Find_in_Area(list_image, 40,168,71,321, 0.9)

        if (ctr):   # 이미지 찾음
            print('이미지 검색!',image)
            while True:
                if ctr[1] < 465:   # 최대 밑으로 스크롤 한 경우 464 이하여야 함. 넘어가면 불안쓰
                    print('이미지 범위 내에요!')
                    break
                else:
                    print('이미지가 너무 밑에 있어 올립니다.')
                    Drag_MouseDown(ctr[0],ctr[1],ctr[0],ctr[1]-20,1)
                    time.sleep(0.3)
                    Drag_MouseDown(ctr[0],ctr[1]-20,ctr[0],ctr[1],1)
                    time.sleep(1)
                    ctr_new = Find_in_Area(image, 560,75,105,460, 0.85)
                    if (ctr_new):    # 새 위치 찾아서
                        print('ctr_new',ctr_new)
                        if ctr_new[1] < 465:
                            print('오우예')
                            Drag(ctr[0],ctr[1],ctr[0]+1,ctr[1],1)
                            break
                        else:
                            Drag(ctr[0],ctr[1],ctr[0],ctr[1] + (460 - ctr_new[1]),2)   # 현재 마우스 위치에서 목표(y:208까지의 차이값 만큼 빼줌)
                            time.sleep(1)
                    else:
                        Drag(ctr[0],ctr[1],ctr[0]+1,ctr[1],1)
                        print('왜 못찾냐 시계를...')
                        break
                    ctr = LocateCenterOnScreenshot(image, 0.85)
            target_numb = check_num - prod_check(image)
            # 목표 수량 미만
            if target_numb > 0:
                print('목표 수량 미달!',target_numb)
                if (list_full) or (list_full1) or (prd_done):       # 생산 완료
                    print('목표 생산물 클릭 완료!!')
                    return True
                elif (lack_of_material):                            # 재료 부족
                    print('재료가 부족해요')
                    click(892,54)
                    time.sleep(0.5)
                    return False
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    click(892,54)
                    time.sleep(0.5)
                    return False
                else:                                               # 그거 아니면 생산 클릭
                    print('생산품 클릭!')
                    click(ctr[0]+235,ctr[1]+48)
                    time.sleep(0.3)
                    click(ctr[0]+235,ctr[1]+48)
                    time.sleep(0.5)

                    lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
                    if (lack_of_material):
                        print('재료가 부족해요')
                        click(892,54)
                        time.sleep(0.5)
                        return False

            # 목표 수량 초과
            if target_numb <= 0:
                print('목표 수량 초과!')
                if (ctr_list):
                    if 111 >= ctr_list[0] >=40:
                        print('이 제품은 충분히 생산했으니 삭제하겠써요!')
                        click(ctr_list[0], ctr_list[1])
                        time.sleep(0.7)
                else:
                    return False
        else:       # 이미지 못찾음
            print('이미지를 찾지 못했습니다.')
            if error_count > 2:                         # 그래도 못찾으면 에러
                return False
            if error_count == 1:
                prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
                if (prod_clock):
                    x_start, y_start = prod_clock[0], prod_clock[1]
                else:
                    x_start, y_start = 610, 150
                Drag(x_start, y_start, x_start, y_start-20, 1)
                time.sleep(1)
                error_count = error_count+1
            if 2 >= error_count >= 0:
                prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
                if (prod_clock):
                    x_start, y_start = prod_clock[0], prod_clock[1]
                else:
                    x_start, y_start = 610, 150
                Drag(x_start, y_start, x_start, y_start-20, 1)
                time.sleep(1)
                error_count = 1

# 소원나무 아이템 눌렀을 때 수량 확인
def Sowon_numb():
    slash_found = False
    sowon_num_start_pos = Find_in_Area('sowon_num_start_pos', 439-12-11, 188, 24+11*2+5+3, 14+2, 0.8)
    if (sowon_num_start_pos):
        print('sowon_num_start_pos',sowon_num_start_pos)
        x1 = sowon_num_start_pos[0] + 11
    else:
        print('량 : 을 못찾아 437+11로 고정합니다.')
        x1 = 437+11
    sowon_num_slash_1 = Find_in_Area('sowon_num_slash_1', 480,185,30,20, 0.85)
    if (sowon_num_slash_1):
        print('sowon_num_slash_1',sowon_num_slash_1)
        x2 = sowon_num_slash_1[0]
        slash_found = True
    sowon_num_slash_2 = Find_in_Area('sowon_num_slash_2', 480, 185, 30, 20, 0.85)
    if not slash_found and (sowon_num_slash_2):
        print('sowon_num_slash_2',sowon_num_slash_2)
        x2 = sowon_num_slash_2[0]
        slash_found = True
    
    if not slash_found:
        print('슬래시를 못읽어 499로 가정합니다.')
        x2 = 499
    its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
    list_real_num = list()  # 실제값 계산을 위한 리스트 생성
    list_num_0 = list()
    list_num_1 = list()
    list_num_2 = list()
    list_num_3 = list()
    list_num_4 = list()
    list_num_5 = list()
    list_num_6 = list()
    list_num_7 = list()
    list_num_8 = list()
    list_num_9 = list()
    # 으아아아아 숫자 가져와아아아아
    find_sowon_num('up_s0', list_num_0, x1, x2)
    find_sowon_num('up_s0_1', list_num_0, x1, x2)
    find_sowon_num('up_s1', list_num_1, x1, x2)
    find_sowon_num('up_s1_1', list_num_1, x1, x2)
    find_sowon_num('up_s2', list_num_2, x1, x2)
    find_sowon_num('up_s3', list_num_3, x1, x2)
    find_sowon_num('up_s4', list_num_4, x1, x2)
    find_sowon_num('up_s5', list_num_5, x1, x2)
    find_sowon_num('up_s5_1', list_num_5, x1, x2)
    find_sowon_num('up_s6', list_num_6, x1, x2)
    find_sowon_num('up_s7', list_num_7, x1, x2)
    find_sowon_num('up_s8', list_num_8, x1, x2)
    find_sowon_num('up_s9', list_num_9, x1, x2)
    find_sowon_num('up_s0', list_num_0, x1, x2)
    
    list_num_0 = del_duplication(3, list_num_0)
    list_num_1 = del_duplication(3, list_num_1)
    list_num_2 = del_duplication(3, list_num_2)
    list_num_3 = del_duplication(3, list_num_3)
    list_num_4 = del_duplication(3, list_num_4)
    list_num_5 = del_duplication(3, list_num_5)
    list_num_6 = del_duplication(3, list_num_6)
    list_num_7 = del_duplication(3, list_num_7)
    list_num_8 = del_duplication(3, list_num_8)
    list_num_9 = del_duplication(3, list_num_9)
    
    if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0],0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0],1))

    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0],2))

    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0],3))

    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0],4))

    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0],5))

    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0],6))

    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0],7))

    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0],8))

    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0],9))

    # 지겨운 실제값 리스트를 받았으니
    list_real_num.sort()    # 추려서

    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)
    
    print('현재 제품의 수량은 =', its_number)
    return its_number


def Sowon_Prod_New(jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
    for i in range(1,64):
        mid_text = str(i)
        start_text = 'sowon_item_check'
        now_image = Find_in_Area(start_text+mid_text+hwakjangja, 460-20,95-20,40,40, 0.9)
        if (now_image):
            if i == 1:
                print('나무')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 2: 
                print('젤리빈')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 3: 
                print('각설탕')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 4: 
                print('비스킷')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 5: 
                print('젤리베리')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 6: 
                print('우유')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 7: 
                print('솜')
                if Sowon_numb() > 1000:
                    return True
                else:
                    return False
            elif i == 8: 
                print('단단 도끼',smith_lev1)
                if Sowon_numb() > smith_lev1*easy_prod:
                    return True
                else:
                    return False
            elif i == 9: 
                print('튼튼 곡괭이',smith_lev2)
                if Sowon_numb() > smith_lev2*easy_prod:
                    return True
                else:
                    return False
            elif i == 10: 
                print('슥삭슥삭 톱',smith_lev3)
                if Sowon_numb() > smith_lev3*easy_prod:
                    return True
                else:
                    return False
            elif i == 11: 
                print('푹푹 삽',smith_lev4)
                if Sowon_numb() > smith_lev4*easy_prod:
                    return True
                else:
                    return False
            elif i == 12: 
                print('신비한 프레첼 말뚝',smith_lev5)
                if Sowon_numb() > smith_lev5*normal_prod:
                    return True
                else:
                    return False
            elif i == 13: 
                print('영롱한 푸른사탕 집게',smith_lev6)
                if Sowon_numb() > smith_lev6*normal_prod:
                    return True
                else:
                    return False
            elif i == 14: 
                print('불변의 슈가 코팅 망치',smith_lev7)
                if Sowon_numb() > smith_lev7*hard_prod:
                    return True
                else:
                    return False
            
            elif i == 15: 
                print('젤리빈 잼',jelly_lev1)
                if Sowon_numb() > jelly_lev1*easy_prod:
                    return True
                else:
                    return False
            elif i == 16: 
                print('스윗젤리 잼',jelly_lev2)
                if Sowon_numb() > jelly_lev2*easy_prod:
                    return True
                else:
                    return False
            elif i == 17: 
                print('달고나 잼',jelly_lev3)
                if jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > jelly_lev3*easy_prod:
                        return True
                    else:
                        return False
            elif i == 18: 
                print('석류 잼',jelly_lev4)
                if jjokji_milk or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > jelly_lev4*normal_prod:
                        return True
                    else:
                        return False
            elif i == 19: 
                print('톡톡베리 잼',jelly_lev5)
                if Sowon_numb() > jelly_lev5*hard_prod:
                    return True
                else:
                    return False
            elif i == 20: 
                print('솔방울새 인형',rollc_lev1)
                if Sowon_numb() > rollc_lev1*easy_prod:
                    return True
                else:
                    return False
            elif i == 21: 
                print('도토리 램프',rollc_lev2)
                if jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > rollc_lev2*easy_prod:
                        return True
                    else:
                        return False
            elif i == 22:
                print('뻐꾹뻐꾹 시계',rollc_lev3)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > rollc_lev3*normal_prod:
                        return True
                    else:
                        return False
            elif i == 23: 
                print('백조깃털 드림캐쳐',rollc_lev4)
                if jjokji_biscuit or jjokji_berry or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > rollc_lev4*hard_prod:
                        return True
                    else:
                        return False
            elif i == 24: 
                print('든든한 호밀빵',bread_lev1)
                if jjokji_biscuit:
                    return False
                else:
                    if Sowon_numb() > bread_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 25: 
                print('달콤쫀득 잼파이',bread_lev2)
                if jjokji_biscuit:
                    return False
                else:
                    if Sowon_numb() > bread_lev2*easy_prod:
                        return True
                    else:
                        return False
            elif i == 26: 
                print('은행 포카치아',bread_lev3)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > bread_lev3*easy_prod:
                        return True
                    else:
                        return False
            elif i == 27: 
                print('슈가코팅 도넛',bread_lev4)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > bread_lev4*easy_prod:
                        return True
                    else:
                        return False
            elif i == 28: 
                print('폭신 카스테라',bread_lev5)
                if jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > bread_lev5*normal_prod:
                        return True
                    else:
                        return False
            elif i == 29: 
                print('골드리치 크로와상',bread_lev6)
                if Sowon_numb() > bread_lev6*hard_prod:
                    return True
                else:
                    return False
            elif i == 30: 
                print('따끈따끈 젤리스튜',jampy_lev1)
                if jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > jampy_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 31: 
                print('곰젤리 버거',jampy_lev2)
                if jjokji_biscuit:
                    return False
                else:
                    if Sowon_numb() > jampy_lev2*easy_prod:
                        return True
                    else:
                        return False
            elif i == 32: 
                print('캔디크림 파스타',jampy_lev3)
                if jjokji_biscuit or jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > jampy_lev3*easy_prod:
                        return True
                    else:
                        return False
            elif i == 33: 
                print('폭신폭신 오므라이스',jampy_lev4)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > jampy_lev4*normal_prod:
                        return True
                    else:
                        return False
            elif i == 34: 
                print('콤비네이션 피자젤리',jampy_lev5)
                if Sowon_numb() > jampy_lev5*hard_prod:
                    return True
                else:
                    return False
            elif i == 35: 
                print('고급스러운 젤리빈 정식',jampy_lev6) 
                if Sowon_numb() > jampy_lev6*hard_prod:
                    return True
                else:
                    return False
            elif i == 36: 
                print('비스킷 화분',doye_lev1)
                if jjokji_biscuit:
                    return False
                else:
                    if Sowon_numb() > doye_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 37: 
                print('반짝반짝 유리판',doye_lev2)
                if jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > doye_lev2*easy_prod:
                        return True
                    else:
                        return False
            elif i == 38: 
                print('반짝이는 색동구슬',doye_lev3)
                if jjokji_biscuit or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > doye_lev3*normal_prod:
                        return True
                    else:
                        return False
            elif i == 39: 
                print('무지갯빛 디저트 보울',doye_lev4)
                if jjokji_milk or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > doye_lev4*hard_prod:
                        return True
                    else:
                        return False
            elif i == 40: 
                print('캔디꽃',flower_lev1)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > flower_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 41: 
                print('행복한 꽃화분',flower_lev2)
                if jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > flower_lev2*easy_prod:
                        return True
                    else:
                        return False
            elif i == 42: 
                print('캔디꽃다발',flower_lev3)
                if jjokji_biscuit or jjokji_berry or jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > flower_lev3*easy_prod:
                        return True
                    else:
                        return False
            elif i == 43: 
                print('롤리팝 꽃바구니',flower_lev4)
                if jjokji_biscuit:
                    return False
                else:
                    if Sowon_numb() > flower_lev4*normal_prod:
                        return True
                    else:
                        return False
            elif i == 44: 
                print('유리꽃 부케',flower_lev5)
                if Sowon_numb() > flower_lev5*hard_prod:
                    return True
                else:
                    return False
            elif i == 45: 
                print('찬란한 요거트 화환',flower_lev6)
                if Sowon_numb() > flower_lev6*hard_prod:
                    return True
                else:
                    return False
            elif i == 46: 
                print('크림',milky_lev1)
                if jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > milky_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 47: 
                print('버터',milky_lev2)
                if Sowon_numb() > milky_lev2*normal_prod:
                    return True
                else:
                    return False
            elif i == 48: 
                print('수제 치즈',milky_lev3)
                if Sowon_numb() > milky_lev3*hard_prod:
                    return True
                else:
                    return False
            elif i == 49: 
                print('젤리빈 라떼',latte_lev1)
                if jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > latte_lev1*easy_prod:
                        return True
                    else:
                        return False
            elif i == 50: 
                print('몽글몽글 버블티',latte_lev2)
                if jjokji_biscuit or jjokji_berry or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > latte_lev2*hard_prod:
                        return True
                    else:
                        return False
            elif i == 51: 
                print('스윗베리 에이드',latte_lev3) 
                if Sowon_numb() > latte_lev3*hard_prod:
                    return True
                else:
                    return False
            elif i == 52: 
                print('구름사탕 쿠션',dolls_lev1)
                if jjokji_biscuit or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > dolls_lev1*normal_prod:
                        return True
                    else:
                        return False
            elif i == 53: 
                print('곰젤리 솜인형',dolls_lev2)
                if jjokji_biscuit or jjokji_berry or jjokji_milk or jjokji_cotton:
                    return False
                else:
                    if Sowon_numb() > dolls_lev2*hard_prod:
                        return True
                    else:
                        return False
            elif i == 54: 
                print('용과 드래곤 솜인형',dolls_lev3) 
                if Sowon_numb() > dolls_lev3*hard_prod:
                    return True
                else:
                    return False
            elif i == 55: 
                print('크림 루트비어',beer_lev1)
                if jjokji_biscuit or jjokji_berry:
                    return False
                else:
                    if Sowon_numb() > beer_lev1*normal_prod:
                        return True
                    else:
                        return False
            elif i == 56: 
                print('레드베리 주스',beer_lev2)
                if Sowon_numb() > beer_lev2*hard_prod:
                    return True
                else:
                    return False
            elif i == 57: 
                print('빈티지 와일드 보틀',beer_lev3)
                if Sowon_numb() > beer_lev3*hard_prod:
                    return True
                else:
                    return False
            elif i == 58: 
                print('으스스 머핀',muffin_lev1)
                if jjokji_biscuit or jjokji_milk:
                    return False
                else:
                    if Sowon_numb() > muffin_lev1*normal_prod:
                        return True
                    else:
                        return False
            elif i == 59: 
                print('생딸기 케이크',muffin_lev2)
                if Sowon_numb() > muffin_lev2*easy_prod:
                    return True
                else:
                    return False
            elif i == 60: 
                print('파티파티 쉬폰케이크',muffin_lev3) 
                if Sowon_numb() > muffin_lev3*hard_prod:
                    return True
                else:
                    return False
            elif i == 61: 
                print('글레이즈드 링',jewel_lev1)
                if Sowon_numb() > jewel_lev1*normal_prod:
                    return True
                else:
                    return False
            elif i == 62: 
                print('루비베리 브로치',jewel_lev2)
                if Sowon_numb() > jewel_lev2*hard_prod:
                    return True
                else:
                    return False
            elif i == 63: 
                print('로얄 곰젤리 크라운',jewel_lev3)
                if Sowon_numb() > jewel_lev3*hard_prod:
                    return True
                else:
                    return False
            else:
                print('못찾거나 안팔거!')
                return False


def jjokji_check(x):
    start_time = time.time()
    if not While_True_Condition(start_time, 20):
        return

    jokji1_ok = True
    # 우하 확인
    click(236+54+(x-1)*165,317+54)
    time.sleep(1)
    pix_status = Get_pixel_tuple(460,90) # 소원나무 확인 뽀인트
    if pix_status == pix_upper_void:
        print('우하 없고')
    else:
        # if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
        if Sowon_Prod_New(jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
            click(687, 83)
            time.sleep(0.5)
        else:
            jokji1_ok = False
            click(687, 83)
            time.sleep(0.5)

    if jokji1_ok:
        # 좌하 확인
        click(236+(x-1)*165,317+54)
        time.sleep(1)
        pix_status = Get_pixel_tuple(460,90) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('좌하 없고')
        else:
            # if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
            if Sowon_Prod_New(jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                click(687, 83)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                click(687, 83)
                time.sleep(0.5)
    if jokji1_ok:
        # 우상 확인
        click(236+54+(x-1)*165,317)
        time.sleep(1)
        pix_status = Get_pixel_tuple(460,90) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('우상 없고')
        else:
            # if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
            if Sowon_Prod_New(jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                click(687, 83)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                click(687, 83)
                time.sleep(0.5)
    if jokji1_ok:
        # 좌상 확인
        click(236+(x-1)*165,317)
        time.sleep(1)
        pix_status = Get_pixel_tuple(460,90) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('좌상 없고')
        else:
            # if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
            if Sowon_Prod_New(jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                click(687, 83)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                click(687, 83)
                time.sleep(0.5)
    
    if jokji1_ok:
        print('쪽지 보냅니다!')
        click(262+(x-1)*165, 437)
        time.sleep(1)
        return True
    
    if not jokji1_ok:
        print('쪽지 짤라!!')
        click(262+(x-1)*165, 145)
        time.sleep(1)
        return False


# 소원나무 내부 픽셀, 이미지 조건 확인
def Sowon_jjokji_action(jjokji_numb, jjokji_limit):
    how_many_jjokji = jjokji_numb
    jjokji_sended = 0
    bEvent_checked = False
    start_time = time.time()
    # 소원나무 들어가기
    while True:
        if not While_True_Condition(start_time,30):
            return
        act_popup_mark_x = Find_in_Area('act_popup_mark_x', 155-20,511-20,40,40, 0.9) # 왕국활동 팝업?
        if (act_popup_mark_x):
            print('팝업!!')
            act_sowon = LocateCenterOnScreenshot('act_sowon', 0.9) # 왕국활동 팝업?
            if (act_sowon):
                print('소원나무 들어간닷!')
                click(act_sowon[0], act_sowon[1])
                time.sleep(2)
            else:
                print('왕국 활동 - 소원나무 아이콘 어딨대요?')
            
            
        else:
            cond_kkd_sowon = Find_in_Area('cond_kkd_sowon', 430,45,31,35, 0.85)    # 소원나무
            if (cond_kkd_sowon):
                print('소원나무 들어왔슴돠!')
                break
            else:
                print('왕국활동 눌러!')
                click(155, 502)
    
    wait_jjokji1 = True
    wait_jjokji2 = True
    wait_jjokji3 = True
    wait_jjokji4 = True
    if jjokji_limit:  # 쪽지 보상까지만 진행?
        jjokji_today_complete = Find_in_Area('jjokji_today_complete', 53,428,68,25, 0.85)
        if (jjokji_today_complete): # 오늘 보상 다 받았으면 나감
            click(892, 54)
            time.sleep(3)
            Kingdom_ready('kkd_out')
            return True
    wait_count = 0
    start_time = time.time()
    # 소원나무 쪽지 작업 시작
    while True:
        if not While_True_Condition(start_time, 300):
            return
        if not bEvent_checked:
            cond_sowon_event = Find_in_Area('cond_sowon_event', 104,317,30,14, 0.85)    # 소원나무 x5 이벤트
            if (cond_sowon_event):
                bSowonEvent = True
                bEvent_checked = True

        pix_status = Get_pixel_tuple(460,90) # 소원나무 확인 뽀인트
        pix_reward = Get_pixel_tuple(36,339) # 소원나무 일일보상 칸 좌상단
        pix_jokji1 = Get_pixel_tuple(265,450) # 쪽지1
        pix_jokji2 = Get_pixel_tuple(427,450) # 쪽지2
        pix_jokji3 = Get_pixel_tuple(589,450) # 쪽지3
        pix_jokji4 = Get_pixel_tuple(751,450) # 쪽지4
        pix_jokji1_wait = Get_pixel_tuple(705+85-165*3,224) # 쪽지1
        pix_jokji2_wait = Get_pixel_tuple(705+85-165*2,225) # 쪽지2
        pix_jokji3_wait = Get_pixel_tuple(705+85-165*1,225) # 쪽지3
        pix_jokji4_wait = Get_pixel_tuple(705+85,225) # 쪽지4
        
        # 일일보상 확인
        if pix_reward == pix_no_reward:
            print('일일보상 No')
        elif pix_reward == pix_yes_reward:
            print('일일보상 받으세요~')
            click(85,385)
            time.sleep(3)
            click(85,385)
        else:
            print('뭐지!!!!!!!!!!!!!')
        
        # 실질적으로 쪽지 보내기
        if pix_status == pix_upper_void:
            print('아이템 확인 대기 상태')
            if pix_jokji1 == pix_green:
                print('쪽지 1 열려있다')
                if jjokji_check(1):
                    wait_jjokji1 = True
                    jjokji_sended = jjokji_sended + 1
            else:
                if pix_jokji1_wait == pix_wait:
                    print('쪽지 1 대기상태')
                    wait_jjokji1 = False
                else:
                    diff = 0
                    for i in range(3):
                        diff = diff + abs(pix_jokji1_wait[i] - pix_wait[i])
                    if diff < 5:
                        print('쪽지 1 대기상태')
                        wait_jjokji1 = False
                    else:
                        click(190+75, 260)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji1_wait)
            if pix_jokji2 == pix_green:
                print('쪽지 2 열려있다')
                if jjokji_check(2):
                    wait_jjokji2 = True
                    jjokji_sended = jjokji_sended + 1
            else:
                if pix_jokji2_wait == pix_wait:
                    print('쪽지 2 대기상태')
                    wait_jjokji2 = False
                else:
                    diff = 0
                    for i in range(3):
                        diff = diff + abs(pix_jokji2_wait[i] - pix_wait[i])
                    if diff < 5:
                        print('쪽지 2 대기상태')
                        wait_jjokji2 = False
                    else:
                        click(190+75+165*1, 260)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji2_wait)
            if pix_jokji3 == pix_green:
                print('쪽지 3 열려있다')
                if jjokji_check(3):
                    wait_jjokji3 = True
                    jjokji_sended = jjokji_sended + 1
            else:
                if pix_jokji3_wait == pix_wait:
                    print('쪽지 3 대기상태')
                    wait_jjokji3 = False
                else:
                    diff = 0
                    for i in range(3):
                        diff = diff + abs(pix_jokji3_wait[i] - pix_wait[i])
                    if diff < 5:
                        print('쪽지 3 대기상태')
                        wait_jjokji3 = False
                    else:
                        click(190+75+165*2, 260)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji3_wait)
            if pix_jokji4 == pix_green:
                print('쪽지 4 열려있다')
                if jjokji_check(4):
                    wait_jjokji4 = True
                    jjokji_sended = jjokji_sended + 1
            else:
                if pix_jokji4_wait == pix_wait:
                    print('쪽지 4 대기상태')
                    wait_jjokji4 = False
                else:
                    diff = 0
                    for i in range(3):
                        diff = diff + abs(pix_jokji4_wait[i] - pix_wait[i])
                    if diff < 5:
                        print('쪽지 4 대기상태')
                        wait_jjokji4 = False
                    else:
                        click(190+75+165*3, 260)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji4_wait)
        
        if (wait_jjokji1 or wait_jjokji2 or wait_jjokji3 or wait_jjokji4):
            wait_count = 0
        else:
            print('웨잇카운트 쁠쁠')
            wait_count = wait_count + 1
            if wait_count > 5:
                print('쪽지를 %s개 보냈지만 다 대기중이라 나가요!'%(jjokji_sended))
                click(892, 54)
                time.sleep(4)
                Kingdom_ready('kkd_out')
                return
        
        if jjokji_sended >= how_many_jjokji:
            print('쪽지를 %s개나 보냈어요!'%(jjokji_sended))
            click(892, 54)
            time.sleep(4)
            Kingdom_ready('kkd_out')
            return
        print('--------절취선--------')    

        time.sleep(1)

def Arena_Event():
    bStep1_play = False        # 플레이 버튼을 눌렀는가?
    error_count = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time,900):
            return
        
        pix_status = Get_pixel_tuple(605,55) # 상단골드
        pix_status2 = Get_pixel_tuple(540,510) # 마침표
        cond_adv_mode_select = Find_in_Area('cond_adv_mode_select', confidence=0.85, region=(12,38,37,36))  # Play버튼 누른 후 모험하기 창
        cond_kkd_out = Find_in_Area('cond_kkd_out', confidence=0.85, region=(825,490,45,40))    # 쿠키왕국
        cond_adv_tro_mode = LocateCenterOnScreenshot('cond_adv_tro_mode', confidence=0.85, region=(2,32,917,505))   # 트로피컬 소다제도의 '도'
        cond_adv_arena = LocateCenterOnScreenshot('cond_adv_arena', 0.8)
        cond_adv_arena_no_ticket = LocateCenterOnScreenshot('cond_adv_arena_no_ticket', confidence=0.9, region = (2, 32, 917, 505))
        
        # 바탕화면도 모험하기도 아니면 우선 바탕화면으로
        if not (cond_kkd_out) and not (cond_adv_mode_select):
            print('왕국도 모험하기 화면도 아니네요!')
            Kingdom_ready('kkd_out')
            
        # 모험하기 화면
        if not bStep1_play and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if (pix_status == pix_status_out or (cond_kkd_out)) and not bStep1_play:
            print('Play 버튼 클릭~!')
            click(random.randint(730,785),random.randint(470,525))
            time.sleep(3)

        if bStep1_play:
            if (cond_adv_arena):
                print('킹덤 아레나 입장모드 보임',cond_adv_arena)
                if (cond_adv_arena_no_ticket):
                    print('근데 티켓이 없네?',cond_adv_arena_no_ticket)
                    click(892,54)
                    time.sleep(6)
                    return False
                else:
                    print('아레나 입장합니다!')
                    click(cond_adv_arena[0], cond_adv_arena[1])
                    time.sleep(6)
                    return True
                    
            if not (cond_adv_arena):
                print('드래그드래그')
                Drag(random.randint(730,785),random.randint(470,525),random.randint(730,785)-300,random.randint(470,525),2)
                error_count = error_count+1
                if error_count > 5:
                    print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                    click(892,54)
                    time.sleep(8)
                    return False
        time.sleep(0.3)

def find_num_arena(image, x1, x2, list_output):
    num_list = LocateAll_Center(image, x1,x2,65,16, 0.85)
    if len(num_list) != 0:
        for ctr in num_list:
            list_output.append(ctr)
    # print(image,list_output)
    return

def Power_check(x1, x2):
    its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
    list_real_num = list()  # 실제값 계산을 위한 리스트 생성
    list_num_0 = list()
    list_num_1 = list()
    list_num_2 = list()
    list_num_3 = list()
    list_num_4 = list()
    list_num_5 = list()
    list_num_6 = list()
    list_num_7 = list()
    list_num_8 = list()
    list_num_9 = list()
    # 으아아아아 숫자 가져와아아아아
    find_num_arena('up_a_0', x1, x2, list_num_0)
    find_num_arena('up_as_0', x1, x2, list_num_0)
    find_num_arena('up_as_0_1', x1, x2, list_num_0)
    find_num_arena('up_a_1', x1, x2, list_num_1)
    find_num_arena('up_a_2', x1, x2, list_num_2)
    find_num_arena('up_as_2', x1, x2, list_num_2)
    find_num_arena('up_a_3', x1, x2, list_num_3)
    find_num_arena('up_as_3', x1, x2, list_num_3)
    find_num_arena('up_a_4', x1, x2, list_num_4)
    find_num_arena('up_as_4', x1, x2, list_num_4)
    find_num_arena('up_a_5', x1, x2, list_num_5)
    find_num_arena('up_as_5', x1, x2, list_num_5)
    find_num_arena('up_a_6', x1, x2, list_num_6)
    find_num_arena('up_as_6', x1, x2, list_num_6)
    find_num_arena('up_a_7', x1, x2, list_num_7)
    find_num_arena('up_as_7', x1, x2, list_num_7)
    find_num_arena('up_a_8', x1, x2, list_num_8)
    find_num_arena('up_as_8', x1, x2, list_num_8)
    find_num_arena('up_as_8_1', x1, x2, list_num_8)
    find_num_arena('up_a_8_1', x1, x2, list_num_8)
    find_num_arena('up_a_8_2', x1, x2, list_num_8)
    find_num_arena('up_a_9', x1, x2, list_num_9)
    find_num_arena('up_as_9', x1, x2, list_num_9)
    list_num_0 = del_duplication(2, list_num_0)
    list_num_1 = del_duplication(2, list_num_1)
    list_num_2 = del_duplication(2, list_num_2)
    list_num_3 = del_duplication(2, list_num_3)
    list_num_4 = del_duplication(2, list_num_4)
    list_num_5 = del_duplication(2, list_num_5)
    list_num_6 = del_duplication(2, list_num_6)
    list_num_7 = del_duplication(2, list_num_7)
    list_num_8 = del_duplication(2, list_num_8)
    list_num_9 = del_duplication(2, list_num_9)
    if (list_num_0): # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0],0))
    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0],1))
        print('append 후 list_1', list_num_1)
    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0],2))
    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0],3))
    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0],4))
    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0],5))
    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0],6))
    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0],7))
    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0],8))
    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0],9))
    list_real_num.sort()    # 추려서
    print('set 이전',list_real_num)
    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)
    print('요놈 전투력은 =', its_number)
    return its_number

def Arena_action( set_max_power):
    bFight_started = False
    bMedalShop_Checked = False
    while True:
        cond_adv_arena_robby = LocateCenterOnScreenshot('cond_adv_arena_robby', 0.95)    # 아레나 티켓 0
        if not (cond_adv_arena_robby):
            print('cond_adv_arena_robby',cond_adv_arena_robby)
        if keyboard.is_pressed('end'):
            return
        start_time = time.time()
        while True: # 로비, 티어 변경 시 다시 이미지 확인하기 위함
            if not While_True_Condition(start_time, 60):
                return
            
            pix_status = Get_pixel_tuple(510, 55) # 상단 메달
            pix_status2 = Get_pixel_tuple(415, 115) # 대전하기 칸 색깔
            if pix_status != pix_medal_normal:
                print('pix_status',pix_status)
            if cond_adv_arena_robby:    # 로비!
                # 정상 색상인가!
                if ((pix_status2 == pix_daejun_selected) or (pix_status2 == pix_daejun_not_selected)):
                    print('로비 확인!')
                    break
                else:
                    # 티어 변경?
                    print('뭐여!')
                    click(415, 115)
                    time.sleep(0.5)
        
        # 로비 확인하고, 메달 상점 확인하기
        while not bMedalShop_Checked:
            cond_arena_medal = LocateCenterOnScreenshot('cond_arena_medal', confidence=0.9, region = (2, 32, 917, 505))
            click(cond_arena_medal[0], cond_arena_medal[1])
            time.sleep(1)
            start_arena_medal_t = time.time()
            while True:
                now_arena_medal_t = time.time()
                if now_arena_medal_t - start_arena_medal_t > 30:
                    print('모지!')
                    break
                if keyboard.is_pressed('end'):
                    print('end 누름')
                    break
                cond_arena_soldout1 = Find_in_Area('cond_arena_soldout1', confidence=0.932, region = (70, 179, 40, 40))
                cond_arena_soldout2 = Find_in_Area('cond_arena_soldout1', confidence=0.932, region = (190, 179, 40, 40))
                # cond_arena_soldout3 = Find_in_Area('cond_arena_soldout1', confidence=0.932, region = (70, 330, 40, 40))
                # cond_arena_soldout4 = Find_in_Area('cond_arena_soldout1', confidence=0.932, region = (190, 330, 40, 40))
                
                if (cond_arena_soldout1):
                    print('전설 샀음!')
                else:
                    click(90,200)
                    time.sleep(1)
                    click(460, 385)
                    time.sleep(2)
                
                if (cond_arena_soldout2):
                    print('슈퍼 에픽 샀음!')
                else:
                    click(210,200)
                    time.sleep(1)
                    click(460, 385)
                    time.sleep(2)
                
                if (cond_arena_soldout1) and (cond_arena_soldout2):
                    print('다 사뜸!')
                    bMedalShop_Checked = True
                    click(872,122)
                    time.sleep(1)
                    break
                time.sleep(0.5)
        # 로비이니 확인!
        while True:
            # 전투 아이콘 별로 1~4 상대 탐색
            cond_adv_arena_fight_icon = LocateAll_Center('cond_adv_arena_fight_icon', 0.95)
            for ctr in cond_adv_arena_fight_icon:
                cond_adv_arena_robby_ticket0 = Find_in_Area('cond_adv_arena_robby_ticket0', 660,45,45,20, 0.9)    # 아레나 티켓 0
                if (cond_adv_arena_robby_ticket0):
                    print('티켓 떨어짐!')
                    click(892, 54)
                    time.sleep(1.5)
                    click(892, 54)
                    time.sleep(10)
                    Kingdom_ready('kkd_out')
                    return
                else:
                    if (ctr):
                        print(ctr)
                        checked_num = Power_check(ctr[0]-223, ctr[1]-31)
                        if checked_num > set_max_power:
                            print('넌 봐준다..')
                        else:
                            start_time = time.time()
                            print('뽜이트!')
                            while True:
                                if not While_True_Condition(start_time, 180):
                                    return

                                # 전투시작 아이콘 없으면 전투(로비에서) 클릭
                                if not bFight_started:  # 전투 시작 안했으면 전투 시작 클릭
                                    cond_start_fight = LocateCenterOnScreenshot('Cond_wanted_start_fignt', 0.9)
                                    if not (cond_start_fight):
                                        click(ctr[0], ctr[1])
                                    else:   # 전투시작 아이콘 있으면
                                        click(cond_start_fight[0], cond_start_fight[1])
                                    time.sleep(1)

                                    # 로딩 창 떴다? 그럼 들어간거.
                                    cond_adv_arena_fight_entered = LocateCenterOnScreenshot('cond_adv_arena_fight_entered', 0.85)            # 로딩창 VS
                                    cond_adv_arena_fight_entered1 = LocateCenterOnScreenshot('cond_adv_arena_fight_entered1', 0.85)          # 킹덤 아레나 글씨
                                    cond_adv_arena_fight_entered2 = Find_in_Area('cond_adv_arena_fight_entered2', 40-25,447-25,50,50, 0.85)    # 아레나 진입 후 DMG ON 버튼
                                    if (cond_adv_arena_fight_entered) or (cond_adv_arena_fight_entered1) or (cond_adv_arena_fight_entered2):
                                        print('전투 진입해뜸!')
                                        bFight_started = True

                                    # 가끔(?) VS 인식 못하고 넘어가나? 트로피 보이면 전투 시작이라 판단(쩝..)
                                    cond_adv_arena_end_fight = LocateCenterOnScreenshot('cond_adv_arena_end_fight', 0.8)
                                    if (cond_adv_arena_end_fight):
                                        bFight_started = True

                                else:   # 전투에 들어갔다면 트로피 모양 보일 때까지 대기
                                    cond_adv_arena_end_fight = LocateCenterOnScreenshot('cond_adv_arena_end_fight', 0.8)
                                    if (cond_adv_arena_end_fight):
                                        click(cond_adv_arena_end_fight[0], cond_adv_arena_end_fight[1])
                                        time.sleep(0.5)
                                        cond_end_fight3 = LocateCenterOnScreenshot('Cond_wanted_go_out', 0.95)   # 나가기 버튼
                                        if (cond_end_fight3):
                                            click(cond_end_fight3[0], cond_end_fight3[1])
                                            time.sleep(0.5)
                                    
                                    cond_adv_arena_robby = LocateCenterOnScreenshot('cond_adv_arena_robby', 0.95)    # 아레나 로비
                                    # 로비로 잘 돌아옴
                                    if (cond_adv_arena_robby):
                                        print('로비로 잘 돌아옴')
                                        bFight_started = False
                                        break
                                    # 전투 중 1초 주기
                                    time.sleep(1)
            cond_adv_arena_robby_ticket0 = Find_in_Area('cond_adv_arena_robby_ticket0', 660,45,45,20, 0.9)    # 아레나 티켓 0
            if (cond_adv_arena_robby_ticket0):
                print('티켓 떨어짐!')
                click(892, 54)
                time.sleep(0.5)
                click(892, 54)
                time.sleep(10)
                Kingdom_ready('kkd_out')
                return
            else:
                # 1~4번 상대 탐색 완료했으면 내려서
                Drag(490,315, 490, 100, 2)
                time.sleep(2)
                # 마지막 놈만 확인
                cond_adv_arena_fight_icon = Find_in_Area('cond_adv_arena_fight_icon', 793,399,98,73, 0.8)   # 맨 아랫줄만
                if (cond_adv_arena_fight_icon):
                    checked_num = Power_check(cond_adv_arena_fight_icon[0]-223, cond_adv_arena_fight_icon[1]-31)
                    if checked_num > set_max_power:
                        print('마지막놈 너도 봐준다..')
                        cond_adv_arena_refresh = LocateCenterOnScreenshot('cond_adv_arena_refresh', 0.95)
                        if (cond_adv_arena_refresh):
                            print('새로고침!')  # 이후 다시 처음부터
                            click(cond_adv_arena_refresh[0], cond_adv_arena_refresh[1])
                            time.sleep(1)
                            break
                        else:
                            print('새로고침 했는데 다 훑었음!')
                            click(892, 54)
                            time.sleep(1.5)
                            click(892, 54)
                            time.sleep(10)
                            Kingdom_ready('kkd_out')
                            return
                    else:
                        print('뽜이트!')
                        start_time = time.time()
                        while True:
                            if not While_True_Condition(start_time, 180):
                                return
                            if not bFight_started:  # 전투 시작 안했으면 전투 시작 클릭
                                cond_start_fight = LocateCenterOnScreenshot('Cond_wanted_start_fignt', confidence=0.9, region=(2,32,917,505))
                                if not (cond_start_fight):
                                    click(cond_adv_arena_fight_icon[0], cond_adv_arena_fight_icon[1])
                                else:   # 전투시작 아이콘 있으면
                                    click(cond_start_fight[0], cond_start_fight[1])
                                time.sleep(1)

                                # 로딩 창 떴다? 그럼 들어간거.
                                cond_adv_arena_fight_entered = LocateCenterOnScreenshot('cond_adv_arena_fight_entered', confidence=0.85, region=(2,32,917,505))            # 로딩창 VS
                                cond_adv_arena_fight_entered1 = LocateCenterOnScreenshot('cond_adv_arena_fight_entered1', confidence=0.85, region=(2,32,917,505))          # 킹덤 아레나 글씨
                                cond_adv_arena_fight_entered2 = Find_in_Area('cond_adv_arena_fight_entered2', confidence=0.85, region=(40-25,447-25,50,50))    # 아레나 진입 후 DMG ON 버튼
                                if (cond_adv_arena_fight_entered) or (cond_adv_arena_fight_entered1) or (cond_adv_arena_fight_entered2):
                                    print('전투 진입해뜸!')
                                    # click(827 + (account // 2) * 960, 491 + (account % 2) * 540)
                                    bFight_started = True

                            else:   # 전투에 들어갔다면 트로피 모양 보일 때까지 대기
                                cond_adv_arena_end_fight = LocateCenterOnScreenshot('cond_adv_arena_end_fight', 0.8)
                                if (cond_adv_arena_end_fight):
                                    click(cond_adv_arena_end_fight[0], cond_adv_arena_end_fight[1])
                                    time.sleep(0.5)
                                    cond_end_fight3 = LocateCenterOnScreenshot('Cond_wanted_go_out', 0.95)   # 나가기 버튼
                                    if (cond_end_fight3):
                                        click(cond_end_fight3[0], cond_end_fight3[1])
                                        time.sleep(0.5)
                                
                                cond_adv_arena_robby = LocateCenterOnScreenshot('cond_adv_arena_robby', 0.95)    # 아레나 로비
                                # 로비로 잘 돌아옴
                                if (cond_adv_arena_robby):
                                    print('로비로 잘 돌아옴')
                                    bFight_started = False
                                    break
                                # 전투 중 1초 주기
                                time.sleep(1)
                else:
                    print('이미 한번 돌았던 건가..')
                    cond_adv_arena_refresh = LocateCenterOnScreenshot('cond_adv_arena_refresh', 0.95)
                    if (cond_adv_arena_refresh):
                        print('새로고침!')
                        click(cond_adv_arena_refresh[0], cond_adv_arena_refresh[1])
                        time.sleep(1)
                        break
                    else:
                        print('새로고침 했는데 다 훑었음!')
                        click(892, 54)
                        time.sleep(1.5)
                        click(892, 54)
                        time.sleep(10)
                        Kingdom_ready('kkd_out')
                        return

def Wood_to_Cotton(Min_number, Max_number, Making_Level, prod_direction_left):   # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
    start_time = time.time()
    if not While_True_Condition(start_time,10):
        return

    prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20,  0.945)
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        click(random.randint(223+5,428-5),random.randint(190+5,410-5))
        time.sleep(0.5)
    # 클릭했는데도 리스트가 가득 차있다? 얘들은 좋지
    prod_full_list2 = Find_in_Area('prod_full_list2', 45,60,55,22, 0.95)
    prod_full_list3 = Find_in_Area('prod_full_list3', 45,60,55,22, 0.95)
    prod_full_list4 = Find_in_Area('prod_full_list4', 45,60,55,22, 0.95)
    prod_full_list5 = Find_in_Area('prod_full_list5', 45,60,55,22, 0.95)
    prod_full_list6 = Find_in_Area('prod_full_list6', 45,60,55,22, 0.95)
    prod_full_list7 = Find_in_Area('prod_full_list7', 45,60,55,22, 0.95)
    # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    if (prod_full_list2) or (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!')
        Skip_Next(prod_direction_left)
        return False

    its_number = Upper_numb()
    print('확인한 상단 숫자 =', its_number)
    if Max_number*0.8 > its_number:     # 최대 수량의 80% 이하이면
        bujockhaeyo = True
    else:
        bujockhaeyo = False
    

    if Min_number < its_number < Max_number:
        print('중간수량 : 설정 레벨로 진행합니다.')
        click(855, 200 + (Making_Level-1)*153)  # 1렙이면 200. 2~3렙은 153씩 올라감
        time.sleep(0.5)
        Skip_Next(prod_direction_left)
        return bujockhaeyo
    
    if  Min_number >= its_number:  # 최소수량 이하이면 1렙 고정.
        print('위험수량 : 1레벨로 생산합니다.')
        start_time = time.time()
        while True:
            if not While_True_Condition(start_time, 30):
                return
            
            prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
            if (prod_refresh):
                click(prod_refresh[0], prod_refresh[1]) # >> 클릭(즉시생산)
                # remain_time_dia = Find_in_Area('remain_time_dia', 90,145,24,20, 0.945)
                time.sleep(0.5)
                remain_time_less_minute = Find_in_Area('remain_time_less_minute', 570,239,49,25, 0.94) # 다이아 10 확인
                remain_time_about_minute = Find_in_Area('remain_time_less_minute', 570,239,49,25, 0.94) # 다이아 10 확인
                if (remain_time_less_minute) or (remain_time_about_minute):
                    click(651, 85)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    break
                else:
                    print('1분 넘게 남아 삭제함돠')
                    click(651, 85)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    click(75, 200-73) # 첫째 칸 클릭
                    time.sleep(0.2)
                    click(462, 378)  # 확인
                    time.sleep(0.2)
            else:
                break
        click(855, 200)
        time.sleep(0.3)
        click(855, 200)
        time.sleep(0.3)
        Skip_Next(prod_direction_left)
        return bujockhaeyo

    if its_number >= Max_number:
        print('최대수량 : 생산하지 않고 넘어갑니다.')
        pix_lackof = Get_pixel_tuple(545,745-540) # 재료부족창?
        if pix_lackof != pix_lackof1:
            click(164,280)
            time.sleep(0.5)
        return bujockhaeyo

def three_prod_action(check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left):
    start_time = time.time()
    if not While_True_Condition(start_time,20):
        return

    prod_refresh = Find_in_Area('prod_refresh', 90,145,24,20, 0.945)
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        click(random.randint(223+5,428-5),random.randint(190+5,410-5))
        time.sleep(0.5)
    
    cond_2nd_clear = Find_in_Area('cond_2nd_clear', 75-10,200-10,20,20, 0.9)
    if not (cond_2nd_clear):
        Skip_Next(prod_direction_left)
        return True
    
    # 풀리스트인 경우 넘어감
    prod_full_list2 = Find_in_Area('prod_full_list2', 45,60,55,22, 0.95)
    prod_full_list3 = Find_in_Area('prod_full_list3', 45,60,55,22, 0.95)
    prod_full_list4 = Find_in_Area('prod_full_list4', 45,60,55,22, 0.95)
    prod_full_list5 = Find_in_Area('prod_full_list5', 45,60,55,22, 0.95)
    prod_full_list6 = Find_in_Area('prod_full_list6', 45,60,55,22, 0.95)
    prod_full_list7 = Find_in_Area('prod_full_list7', 45,60,55,22, 0.95)
    if (prod_full_list2) or (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!')
        Skip_Next(prod_direction_left)
        return True

    # 3렙건물이니 고정
    prod_pin = (612, 95)

    target_numb1 = check_num1 - numb_new_recog(prod_pin, 1)
    target_numb2 = check_num2 - numb_new_recog(prod_pin, 2)
    target_numb3 = check_num3 - numb_new_recog(prod_pin, 3)
    # 기타 조건 초기화
    line1_clicked = 0
    line2_clicked = 0
    line3_clicked = 0
    prod_line1_completed =False
    prod_line2_completed =False
    prod_line3_completed =False
    list_numbb1 = 0
    list_numbb2 = 0
    list_numbb3 = 0

    # 리스트를 한번만 읽자!
    if check_num1 != 0:          # 목표값이 있고(열었고)
        if target_numb1 > 0:    # 목표 수량보다 부족한 경우
            list_numb1 = LocateAll_Center(check_list_img1, 42,169,66,318, 0.95)
            if len(list_numb1)>0:
                list_numbb1 = len(list_numb1)        # 현재 리스트에 몇 개 있냐
            else:
                list_numbb1 = 0
    else:
        prod_line1_completed = True
        compare_numb1 = -1
        list_numbb1 = 0

    if check_num2 != 0:          # 목표값이 있고(열었고)
        if target_numb2 > 0:    # 목표 수량보다 부족한 경우
            list_numb2 = LocateAll_Center(check_list_img2, 42,169,66,318, 0.95)
            if len(list_numb2)>0:
                list_numbb2 = len(list_numb2)        # 현재 리스트에 몇 개 있냐
            else:
                list_numbb2 = 0
    else:
        prod_line2_completed = True
        compare_numb2 = -1
        list_numbb2 = 0
    
    if check_num3 != 0:          # 목표값이 있고(열었고)
        if target_numb3 > 0:    # 목표 수량보다 부족한 경우
            list_numb3 = LocateAll_Center(check_list_img3, 42,169,66,318, 0.95)
            if len(list_numb3)>0:
                list_numbb3 = len(list_numb3)        # 현재 리스트에 몇 개 있냐
            else:
                list_numbb3 = 0
    else:
        prod_line3_completed = True
        compare_numb3 = -1
        list_numbb3 = 0

    print('현재 리스트에는 = 1:%s, 2:%s, 3:%s개 있습니다.'%(list_numbb1,list_numbb2,list_numbb3))
    while True:
        if not While_True_Condition(start_time, 30):
            return
        
        # 풀리스트인 경우 넘어감
        prod_full_list2 = Find_in_Area('prod_full_list2', 45,60,55,22, 0.95)
        prod_full_list3 = Find_in_Area('prod_full_list3', 45,60,55,22, 0.95)
        prod_full_list4 = Find_in_Area('prod_full_list4', 45,60,55,22, 0.95)
        prod_full_list5 = Find_in_Area('prod_full_list5', 45,60,55,22, 0.95)
        prod_full_list6 = Find_in_Area('prod_full_list6', 45,60,55,22, 0.95)
        prod_full_list7 = Find_in_Area('prod_full_list7', 45,60,55,22, 0.95)
        if (prod_full_list2) or (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!')
            Skip_Next(prod_direction_left)
            return True

        # 리스트 수량 파악
        if (target_numb1 - list_numbb1 - line1_clicked) > 0:   # 부족분-리스트 > 0 이면 더 만들어야지
            compare_numb1 = (target_numb1 - list_numbb1 - line1_clicked)/check_num1  # 비율(1을 안넘음)
        else:
            compare_numb1 = -1
            prod_line1_completed =True
            
        if (target_numb2 - list_numbb2 - line2_clicked) > 0:   # 부족분-리스트 > 0 이면 더 만들어야지
            compare_numb2 = (target_numb2 - list_numbb2 - line2_clicked)/check_num2  # 비율(1을 안넘음)
        else:
            compare_numb2 = -1
            prod_line2_completed =True
                    
        if (target_numb3 - list_numbb3 - line3_clicked) > 0:   # 부족분-리스트 > 0 이면 더 만들어야지
            compare_numb3 = (target_numb3 - list_numbb3 - line3_clicked)/check_num3  # 비율(1을 안넘음)
        else:
            compare_numb3 = -1
            prod_line3_completed =True

        if (prod_line1_completed and prod_line2_completed and prod_line3_completed):
            Skip_Next(prod_direction_left)
            return False
        else:
            max_numb = max(compare_numb1, compare_numb2, compare_numb3)
            if max_numb == compare_numb1 and not prod_line1_completed:
                click(755, 197)
                lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
                not_opened = LocateCenterOnScreenshot('Cond_not_opened', 0.95)
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    click(892,54)
                    time.sleep(0.5)
                    line1_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    click(892,54)
                    time.sleep(0.5)
                    line1_clicked = 999             # 나락으로 보내버력!
                else:
                    line1_clicked = line1_clicked + 1
            if max_numb == compare_numb2 and not prod_line2_completed:
                click(755, 197+153)
                lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
                not_opened = LocateCenterOnScreenshot('Cond_not_opened', 0.95)
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    click(892,54)
                    time.sleep(0.5)
                    line2_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    click(892,54)
                    time.sleep(0.5)
                    line2_clicked = 999             # 나락으로 보내버력!
                else:
                    line2_clicked = line2_clicked + 1
            if max_numb == compare_numb3 and not prod_line3_completed:
                click(755, 197+153*2)
                lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
                not_opened = LocateCenterOnScreenshot('Cond_not_opened', 0.95)
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    click(892,54)
                    time.sleep(0.5)
                    line3_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    click(892,54)
                    time.sleep(0.5)
                    line3_clicked = 999             # 나락으로 보내버력!
                else:
                    line3_clicked = line3_clicked + 1

def numb_new_recog(prod_pin, line):
    its_number = 0
    how_many_nums = 0
    pos_numb = 0        # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
    num_list = list()
    print('라인 %s번 진행합니다!'%(line))
    # 3렙 건물인 경우 무조건 prod_pin = (612,95)
    pix_jaritsu1_1 = Get_pixel_tuple(prod_pin[0]+19,prod_pin[1]+81+153*(line-1)) # 상
    pix_jaritsu1_2 = Get_pixel_tuple(prod_pin[0]+19,prod_pin[1]+87+153*(line-1)) # 하
    if ((pix_jaritsu1_1) == pix_white) and ((pix_jaritsu1_2) == pix_white):
        pix_zero_1 = Get_pixel_tuple(prod_pin[0]+24,prod_pin[1]+82+153*(line-1)) # 상
        pix_zero_2 = Get_pixel_tuple(prod_pin[0]+24,prod_pin[1]+85+153*(line-1)) # 하
        for p in pix_zero_1:
            if p < 252:
                pos_numb = 1
        for p in pix_zero_2:
            if p < 252:
                pos_numb = 1
        if pos_numb == 0:
            # print('이 숫자는 0 입니다!')
            its_number = 0
            return 0
        # if pos_numb == 1:
            # print('이 숫자는 한 자릿 수 입니다!')
    else:
        pix_jaritsu2_1 = Get_pixel_tuple(prod_pin[0]+14,prod_pin[1]+81+153*(line-1)) # 상
        pix_jaritsu2_2 = Get_pixel_tuple(prod_pin[0]+14,prod_pin[1]+81+153*(line-1)) # 하
        if ((pix_jaritsu2_1) == pix_white) and ((pix_jaritsu2_2) == pix_white):
            # print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            # print('이 숫자는 세 자릿 수 입니다!')
            pos_numb = 3
    # print('자릿수 다시 확인', pos_numb)
    if pos_numb == 1:
        # print('한 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        for t in production_number:
            num_check = Find_in_Area(t, prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14, 0.84)
            if (num_check):
                its_number = its_number + int(t[5])
                break
        return its_number

    if pos_numb == 2:
        # print('두 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),10,14)
        for i in range(2):
            for t in production_number:
                num_check = Find_in_Area(t, prod_pin[0]+34-pos_numb*5-10*i,prod_pin[1]+85-7+153*(line-1),10,14, 0.84)
                if (num_check):
                    its_number = its_number + int(t[5])*10**i
                    break
        return its_number

    if pos_numb == 3:
        # print('세 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        for i in range(3):
            for t in production_number:
                num_check = Find_in_Area(t, 640-i*9,prod_pin[1]+85-7+153*(line-1),10,14, 0.84)
                if (num_check):
                    its_number = its_number + int(t[5])*10**i
                    break
        return its_number


# -----------새-----------함-----------수-----------추-----------가-----------+dd

# 랜덤 변수 없는 클릭
def clickExact(x, y):
    lParam = win32api.MAKELONG(x, y)
    # 자식 없음(아마도) https://airfox1.tistory.com/3
    # hWnd1 = win32gui.FindWindowEx(hWnd, None, None, None)
    # win32gui.PostMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

# 랜덤값(디폴트 5) 있는 클릭
def click(x, y):
    lParam = win32api.MAKELONG(x+random.randint(-random_int,random_int), y+random.randint(-random_int,random_int))
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

# 휠다운...만 할랬더니 왜 줌아웃되지.. mousemove 안하면 다른 계정이 안먹네?
def Wheel_Down(x, y):
    lParam = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam)
    time.sleep(0.1)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEWHEEL, win32con.WHEEL_DELTA * 3, lParam)
    time.sleep(0.1)

def Keyboard_Press(key):
    # http://lab.cliel.com/entry/%EA%B0%80%EC%83%81-Key-Code%ED%91%9C
    # 키맵...핑 짜잉나네에! 우선 ctrl:17, alt:18, esc:27, 좌:37, 상:38, 우:39, 하:40
    # c: 67, x:88, z:90
    hWnd = win32gui.FindWindowEx(0, 0, 0, title_t)
    # hWnd = win32gui.FindWindowEx(0, 0, 0, title_t)
    # win32gui.SetFocus(hWnd)
    # PBYTE256 = ctypes.c_ubyte * 256
    # _user32 = ctypes.WinDLL("user32")
    # GetKeyboardState = _user32.GetKeyboardState
    # SetKeyboardState = _user32.SetKeyboardState
    # MapVirtualKeyA = _user32.MapVirtualKeyA
    # AttachThreadInput = _user32.AttachThreadInput
    # oldKeyboardState = PBYTE256()
    # keyboardStateBuffer = PBYTE256()
    # GetKeyboardState(ctypes.byref(oldKeyboardState))
    # current = win32api.GetCurrentThreadId()
    # lparam = win32api.MAKELONG(0,MapVirtualKeyA(key, 0))
    # lparam_ctrl = win32api.MAKELONG(0,MapVirtualKeyA(win32con.VK_CONTROL, 0))
    # win32gui.SendMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    # AttachThreadInput(current, hWnd, True)
    # GetKeyboardState( ctypes.byref(oldKeyboardState) )
    # keyboardStateBuffer[win32con.VK_CONTROL] |= 128
    # SetKeyboardState( ctypes.byref(keyboardStateBuffer) )
    
    # print('hWnd1',hWnd1)
    # lParam = win32api.MAKELONG(30, 30)
    # win32gui.PostMessage(hwnd, win32con.WM_MOUSEMOVE, None, lParam)
    # win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    # win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
    # # 이거 하면 되긴 하는데... 창이 튀어나오냐...!
    # # 심지어 SetForegroundWindow 하기 전에 shell.SendKeys('%') 뭔가 키 입력을 보내야 한다고...?
    # win32gui.SetForegroundWindow(hWnd)
    # win32gui.PostMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    # 얜 안먹네
    # win32gui.PostMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    # print('이건아니겠지',win32gui.IsWindowEnabled(hWnd))
    if key == 'setup':
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(18, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(38, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(18, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(38, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        return
    elif key == 'esc':
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        return
    else:
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        return

def mouseDown(x, y, random_int):
    lParam = win32api.MAKELONG(x+random.randint(-random_int,random_int), y+random.randint(-random_int,random_int))
    win32gui.PostMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)

def mouseUp(x, y, random_int):
    lParam = win32api.MAKELONG(x+random.randint(-random_int,random_int), y+random.randint(-random_int,random_int))
    win32gui.PostMessage(hWnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

def mouseMove(x, y):
    lParam = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam)

# x, y 에서 x1, y1까지, 총 이동 시간
def Drag(x, y, to_X, to_Y, duration):
    lParam = win32api.MAKELONG(x,y)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam)
    time.sleep(0.1)
    # X, Y 이동거리
    x_mov, y_mov = abs(to_X - x), abs(to_Y - y)
    # 총 이동 틱 거리
    tot_mov = x_mov + y_mov
    if tot_mov > 0: # 쨌든 이동
        if x_mov == 0:  # y로만 이동
            for i in range(tot_mov):
                if to_Y - y > 0:    # Y 목표값이 더 클 때(아래로 이동)
                    j = i
                else:
                    j = -i
                lParam1 = win32api.MAKELONG(x,y+j)
                # win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam1)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        elif y_mov == 0:    # x로만 이동
            for i in range(tot_mov):
                if to_X - x > 0:    # X목표값이 더 클 때(오른쪽 이동)
                    k = i
                else:
                    k = -i
                lParam1 = win32api.MAKELONG(x+k,y)
                # win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam1)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        else:   # x, y 이동
            j = 0
            for i in range(tot_mov):
                if i == 0:  # 첫 이동은 x로 하자.. 걍.. 그러자...
                    if to_X - x > 0:    # X목표값이 더 클 때(오른쪽 이동)
                        k = 1
                        tic_x = 1
                        tic_y = 0
                    else:
                        k = -1
                        tic_x = 1
                        tic_y = 1
                elif i == 1:    # 두 번째 이동은 Y
                    if to_Y - y > 0:    # Y 목표값이 더 클 때(아래로 이동)
                        j = 1
                        tic_x = 1
                        tic_y = 1
                    else:
                        j = -1
                        tic_x = 1
                        tic_y = 1
                else:   # 이후에는 비율로 왔다리갔다리
                    if (x_mov - tic_x)/x_mov < (y_mov - tic_y)/y_mov:   # X 이동 %가 Y이동 %보다 작을 때(x가 더 많이 감. y로 이동할 차례)
                        if j > 0:   # 관성에 따라 가던 대로 쭉 가
                            j = j + 1
                            tic_y = tic_y + 1
                        else:
                            j = j - 1
                            tic_y = tic_y + 1
                    else:   # X 이동할 차례
                        if k > 0:   # 관성에 따라 가던 대로 쭉 가
                            k = k + 1
                            tic_x = tic_x + 1
                        else:
                            k = k - 1
                            tic_x = tic_x + 1
                # 이렇게 j와 k값에 의해 대각선 이동
                lParam1 = win32api.MAKELONG(x+k,y+j)
                # win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam1)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        # time.sleep(0.3)
        # lParam = win32api.MAKELONG(x,y)
        time.sleep(1)
        win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam1)
        time.sleep(1)
        return
        # win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam1)
    else:
        print('현재 위치와 목표 위치가 같은데 왜 이동?')
        # lParam = win32api.MAKELONG(x,y)
        # win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)
        return

# 클릭한 채로 이동(완전 동일하나 마우스 up이 없...)
def Drag_MouseDown(x, y, to_X, to_Y, duration):
    lParam = win32api.MAKELONG(x,y)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam)
    time.sleep(0.1)
    # X, Y 이동거리
    x_mov, y_mov = abs(to_X - x), abs(to_Y - y)
    # 총 이동 틱 거리
    tot_mov = x_mov + y_mov
    if tot_mov > 0: # 쨌든 이동
        if x_mov == 0:  # y로만 이동
            for i in range(tot_mov):
                if to_Y - y > 0:    # Y 목표값이 더 클 때(아래로 이동)
                    j = i
                else:
                    j = -i
                lParam1 = win32api.MAKELONG(x,y+j)
                # win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam1)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        elif y_mov == 0:    # x로만 이동
            for i in range(tot_mov):
                if to_X - x > 0:    # X목표값이 더 클 때(오른쪽 이동)
                    k = i
                else:
                    k = -i
                lParam1 = win32api.MAKELONG(x+k,y)
                # win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, None, lParam1)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        else:   # x, y 이동
            j = 0
            for i in range(tot_mov):
                if i == 0:  # 첫 이동은 x로 하자.. 걍.. 그러자...
                    if to_X - x > 0:    # X목표값이 더 클 때(오른쪽 이동)
                        k = 1
                        tic_x = 1
                        tic_y = 0
                    else:
                        k = -1
                        tic_x = 1
                        tic_y = 1
                elif i == 1:    # 두 번째 이동은 Y
                    if to_Y - y > 0:    # Y 목표값이 더 클 때(아래로 이동)
                        j = 1
                        tic_x = 1
                        tic_y = 1
                    else:
                        j = -1
                        tic_x = 1
                        tic_y = 1
                else:   # 이후에는 비율로 왔다리갔다리
                    if (x_mov - tic_x)/x_mov < (y_mov - tic_y)/y_mov:   # X 이동 %가 Y이동 %보다 작을 때(x가 더 많이 감. y로 이동할 차례)
                        if j > 0:   # 관성에 따라 가던 대로 쭉 가
                            j = j + 1
                            tic_y = tic_y + 1
                        else:
                            j = j - 1
                            tic_y = tic_y + 1
                    else:   # X 이동할 차례
                        if k > 0:   # 관성에 따라 가던 대로 쭉 가
                            k = k + 1
                            tic_x = tic_x + 1
                        else:
                            k = k - 1
                            tic_x = tic_x + 1
                # 이렇게 j와 k값에 의해 대각선 이동
                lParam1 = win32api.MAKELONG(x+k,y+j)
                win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam1)
                time.sleep(duration/abs(tot_mov))
        # win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam1)
        return
    else:
        print('현재 위치와 목표 위치가 같은데 왜 이동?')
        return
    
def rgbint2rgbtuple(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return (blue, green, red)

def Get_pixel_tuple(x, y):
    get_current_image(title_t)
    im = Image.open('test'+hwakjangja)
    pos = x, y
    pix_rgb = im.getpixel(pos)
    # pix_status = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    # pix_rgb = rgbint2rgbtuple(pix_status)
    return pix_rgb

def While_True_Condition(start_time, max_act_time):  # Ture:정상상태(다음 동작 가능), False:이상상태(다음 동작 안함-최대시간 초과 등)
    get_current_image(title_t)
    now_time = time.time()
    # 범위 = 440, 363, 43, 29
    cond_network = Find_in_Area('cond_network', 440,363,43,29, 0.95)
    cond_halted = LocateCenterOnScreenshot('cond_halted', 0.9)
    cond_g_play = LocateCenterOnScreenshot('cond_g_play', 0.9)
    if start_time - now_time > max_act_time:
        End_kkd()                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
        Kingdom_ready('kkd_out')            # 재부팅
        return False
    elif keyboard.is_pressed('end'):
        return False
    elif (cond_network):
        click(462,377)
        time.sleep(0.3)
    elif (cond_g_play):
        click(cond_g_play[0], cond_g_play[1])
    elif (cond_halted):
        click(740,310)
        End_kkd()
        Kingdom_ready('kkd_out')            # 재부팅
    else:
        return True

def Tropical_Event():
    bStep1_play = False        # 플레이 버튼을 눌렀는가?
    error_count = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 120):
            return False
        pix_status = Get_pixel_tuple(605,55) # 상단골드
        cond_adv_mode_select = Find_in_Area('cond_adv_mode_select', 12,38,37,36, 0.9)  # Play버튼 누른 후 모험하기 창
        cond_kkd_out = Find_in_Area('cond_kkd_out', 825,490,45,40, 0.85)    # 쿠키왕국
        cond_adv_tro_mode = LocateCenterOnScreenshot('cond_adv_tro_mode', 0.9)   # 트로피컬 소다제도의 '도'
        cond_adv_tro = LocateCenterOnScreenshot('cond_adv_tro', 0.9)             # '도' 위에 이벤트 있는 경우 빨간 말풍선
        
        # 바탕화면도 모험하기도 아니면 우선 바탕화면으로
        if not (cond_kkd_out) and not (cond_adv_mode_select):
            print('왕국도 모험하기 화면도 아니네요!')
            Kingdom_ready('kkd_out')
            
        # 모험하기 화면
        if not bStep1_play and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if (pix_status == pix_status_out or (cond_kkd_out)) and not bStep1_play:
            print('Play 버튼 클릭~!')
            click(750, 500)
            time.sleep(10)
        
        if bStep1_play:
            if (cond_adv_tro_mode):
                print('트로피컬 소다제도 글씨 확인!')
                if (cond_adv_tro):
                    print('재점령 당한 곳이 있어 트로피칼 들어갑니다!')
                    click(cond_adv_tro[0], cond_adv_tro[1])
                    return True
                else:
                    print('이벤트 없어서 복귀합니다!')
                    click(892,54)
                    time.sleep(8)
                    return False
                    
            if not (cond_adv_tro_mode):
                print('드래그드래그')
                Drag(750+random.randint(-20,20), 500+random.randint(-20,20), 200+random.randint(-20,20), 500+random.randint(-20,20), 1)
                time.sleep(2)
                error_count = error_count+1
                if error_count > 5:
                    print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                    click(892,54)
                    time.sleep(8)
                    return False

def Tropical_Fight():
    bFighting = False
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 240):
            return
        
        pix_status = Get_pixel_tuple(605,55) # 상단골드
        # pix_status_scr = Get_pixel_tuple(910,55) # = 미세 오른쪽
        pix_status2 = Get_pixel_tuple(540,510) # 마침표
        cond_kkd_tro = Find_in_Area('cond_kkd_tro', 18,448,45,40, 0.85)    # 트로피칼(좌하단 파라솔 꽃)
        Cond_tropical_knife = LocateCenterOnScreenshot('Cond_tropical_knife', 0.8)    # 트로피칼 재점령당한 칼모양
        Cond_tropical_fight = LocateCenterOnScreenshot('Cond_tropical_fight', 0.8)    # 트로피칼 전투 준비, 시작도 동일한가?
        cond_quick = LocateCenterOnScreenshot('cond_quick', 0.8)             # 빨리감기
        cond_quick_button = LocateCenterOnScreenshot('cond_quick_button', 0.8)             # 빨리감기 시작 버튼
        cond_end_fight3 = LocateCenterOnScreenshot('Cond_wanted_go_out', 0.95)        # 나가기 버튼
        cond_tropical_exclamation = LocateCenterOnScreenshot('cond_tropical_exclamation', 0.95)        # 느낌표

        if bFighting and (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            time.sleep(1)
            click(540,510)
            bFighting = False
            time.sleep(2)
        
        if bFighting and (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            time.sleep(1)
            click(540,510)
            bFighting = False
            time.sleep(2)

        # 빨리감기와 전투 버튼이 같이 있으면
        if not bFighting and (cond_quick) and (Cond_tropical_fight):
            # 빨리감기 쓸 경우
            if bQuickUse:
                print('빨리감기 버튼 클릭')
                time.sleep(0.5)
                click(cond_quick[0], cond_quick[1])
                time.sleep(1)
            # 빨리감기 안쓸 경우
            else:
                print('빨리감기 아닌 전투 시작')
                click(807,493)
                bFighting = True

        # 새로 열린 영토 느낌표
        if not bFighting and (cond_tropical_exclamation):
            click(cond_tropical_exclamation[0], cond_tropical_exclamation[1])
            time.sleep(2)
            Kingdom_ready('tropical_in')
                
        
        # 칼모양 있고 전투 버튼 없으면 칼을 클릭
        if not bFighting and (Cond_tropical_knife) and not (Cond_tropical_fight):
            print('재점령 당한 곳 클릭!')
            click(Cond_tropical_knife[0], Cond_tropical_knife[1])
            time.sleep(2)
        
        # if not bFighting and (Cond_tropical_knife_new) and not (Cond_tropical_fight):
        #     print('새로 연 곳 클릭!')
        #     click(Cond_tropical_knife_new)
        #     time.sleep(2)
        
        # 칼모양 있고 전투 버튼 있으면 전투 클릭
        if not bFighting and (Cond_tropical_knife) and (Cond_tropical_fight):
            print('전투 로비 들어가기!1')
            click(Cond_tropical_fight[0], Cond_tropical_fight[1])
            time.sleep(2)

        # 칼모양 없고 전투 버튼 있고 빨리감기 없으면 전투 클릭
        if not bFighting and not (Cond_tropical_knife) and (Cond_tropical_fight) and not (cond_quick):
            print('전투 로비 들어가기!2')
            click(Cond_tropical_fight[0], Cond_tropical_fight[1])
            time.sleep(2)
        
        if not bFighting and (cond_quick_button):
            print('빨리감기 시작')
            click(cond_quick_button[0], cond_quick_button[1])
            time.sleep(6)
            click(460,415)
            time.sleep(2)
        
        if (cond_end_fight3):   # 나가기 버튼이 있으면
            click(cond_end_fight3[0], cond_end_fight3[1]) # 눌러~
            time.sleep(3)

        if not bFighting and (cond_kkd_tro) and not (Cond_tropical_knife):
            print('더 돌 곳이 없네요!')
            click(865,492)
            time.sleep(1)
            click(892,55)
            time.sleep(1)
            Kingdom_ready('kkd_out')
            return True
        
        print('[트로피칼] 실행중...')

def Enter_Screenshot_mode(left_where):
    error_count = 0
    reboot = 0
    drag_times = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time,60):
            return
        pix_status_scr = Get_pixel_tuple(910, 55)    # 스샷모드 : = 미세 오른쪽
        screen_mode_clicked = LocateCenterOnScreenshot('screen_mode_clicked', 0.95)
        screen_mode_not_clicked = LocateCenterOnScreenshot('screen_mode_not_clicked', 0.95)
        screenshot_mode = Find_in_Area('screenshot_mode', 703,270,112,130, 0.95)
        if (screen_mode_clicked) or (pix_status_scr == pix_clicked):
            # print('클릭했다!')
            if (screenshot_mode):
                print('screenshot_mode',screenshot_mode)
                clickExact(screenshot_mode[0], screenshot_mode[1])
                time.sleep(0.5)
                bScreenshotClicked = True
        elif (screen_mode_not_clicked):
            # print('클릭 안했다!',screen_mode_not_clicked)
            click(889,45)
        else:
            if bScreenshotClicked:
                print('스샷모드 들어왔나 봅니다')
                error_count = 0
                break
            else:
                print('클릭도 안했는데, 어.. 없다면')
                # esc 한번 해보고..
                if error_count == 0:
                    # click(284, 15)  # 창 선택...은 필요 없겠구나
                    # time.sleep(0.1)
                    click(892, 54)  # X표시 클릭
                    time.sleep(0.5)
        time.sleep(1)
    
    if bScreenshotClicked:
        print('줌아웃1')
        Wheel_Down(300, 300)
        time.sleep(2)
        print('줌아웃2')
        Wheel_Down(350, 300)
        time.sleep(2)
        print('줌아웃3')
        Wheel_Down(300, 350)
        time.sleep(2)
    
    while (left_where == 'left_up') and (drag_times < 4):
        Drag(264+random.randint(-100,100),255+random.randint(-100,100),600,500,0.5)
        drag_times = drag_times + 1

    while (left_where == 'left_down') and (drag_times < 4):
        Drag(215+random.randint(-100,100),375+random.randint(-100,100),600,100,0.5)
        drag_times = drag_times + 1
    
    Kingdom_ready('kkd_out')
    return print('위치 이동 완료!')
        

def Building_Num_Check():
    start_time = time.time()
    max_act_time = 180
    pix_error_count = 0
    while True:
        if not While_True_Condition(start_time, max_act_time):
            return 0
        pix_status = Get_pixel_tuple(605, 55)       # 상단 골드
        pix_prod = Get_pixel_tuple(610, 140)        # 생산품 픽셀
        
        bInPosition = LocateCenterOnScreenshot('bInPosition', 0.8)  # 건물 안(쿠키 다시 선택)
        
        if pix_status == pix_status_in or (bInPosition):   # 건물 안 ok
            if pix_prod == pix_wood:
                print('나무!')
                pix_error_count = 0
                return 1
            elif pix_prod == pix_jelbean:
                print('젤리빈!')
                pix_error_count = 0
                return 2
            elif pix_prod == pix_white:
                print('각설탕!')
                pix_error_count = 0
                return 3
            elif pix_prod == pix_biscuit:
                print('비스킷!')
                pix_error_count = 0
                return 4
            elif pix_prod == pix_berry:
                print('젤리베리!')
                pix_error_count = 0
                return 5
            elif pix_prod == pix_milk:
                print('우유!')
                pix_error_count = 0
                return 6
            elif pix_prod == pix_cotton:
                print('솜!')
                pix_error_count = 0
                return 7
            elif pix_prod == pix_smith:
                print('smith!')
                pix_error_count = 0
                return 8
            elif pix_prod == pix_jelly:
                print('jelly!')
                pix_error_count = 0
                return 9
            elif pix_prod == pix_rollc:
                print('rollc!')
                pix_error_count = 0
                return 10
            # elif pix_prod == pix_rollc_d:
            #     print('rollc!')
            #     pix_error_count = 0
            #     return 10
            elif pix_prod == pix_bread:
                print('bread!')
                pix_error_count = 0
                return 11
            # elif pix_prod == pix_bread_d:
            #     print('bread!')
            #     pix_error_count = 0
            #     return 11
            elif pix_prod == pix_jampy:
                print('jampy!')
                pix_error_count = 0
                return 12
            # elif pix_prod == pix_jampy_d:
            #     print('jampy!')
            #     pix_error_count = 0
            #     return 12
            elif pix_prod == pix_doye:
                print('doye!')
                pix_error_count = 0
                return 13
            # elif pix_prod == pix_doye_d:
            #     print('doye!')
            #     pix_error_count = 0
            #     return 13
            elif pix_prod == pix_flower:
                print('flower!')
                pix_error_count = 0
                return 14
            # elif pix_prod == pix_flower_d:
            #     print('flower!')
            #     pix_error_count = 0
            #     return 14
            elif pix_prod == pix_milky:
                print('milky!')
                pix_error_count = 0
                return 15
            elif pix_prod == pix_latte:
                print('latte!')
                pix_error_count = 0
                return 16
            elif pix_prod == pix_dolls:
                print('dolls!')
                pix_error_count = 0
                return 17
            elif pix_prod == pix_beer:
                print('beer!')
                pix_error_count = 0
                return 18
            elif pix_prod == pix_muffin:
                print('muffin!')
                pix_error_count = 0
                return 19
            elif pix_prod == pix_jewel:
                print('jewel!')
                pix_error_count = 0
                return 20
            elif pix_prod == pix_magic:
                print('Magic!')
                pix_error_count = 0
                return 21
            elif pix_prod == pix_icecream:
                print('icecream!')
                pix_error_count = 0
                return 22
            else:
                print(pix_prod)
                print('건물 안에서... 픽셀값 찾게 위로 올림')
                for i in range(2):
                    prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
                    if (prod_clock):
                        x_start, y_start = prod_clock[0], prod_clock[1]
                    else:
                        x_start, y_start = 610, 150
                    Drag(x_start, y_start, x_start, 540, 1)
                    time.sleep(1)
                pix_error_count = pix_error_count + 1
                if pix_error_count == 2:
                    return 0
        else:
            print('건물 안이 아니다!')
            Enter_Building()

def End_kkd():
    time.sleep(0.3)
    click(940,520)
    time.sleep(3)
    click(677,137)
    time.sleep(5)
    return

def Balloon_send():
    error_count = 0
    start_time = time.time()
    while True:
        if not While_True_Condition(start_time, 180):
            return
        pix_status = Get_pixel_tuple(605,55) # 상단골드
        cond_kkd_balloon = Find_in_Area('cond_kkd_balloon', 9,36,25,35, 0.85)               # 열기구 로비
        cond_kkd_balloon_ing = Find_in_Area('cond_kkd_balloon_ing', 364,85,28,37, 0.85)     # 열기구 날아다니는 중
        cond_balloon_arrive = LocateCenterOnScreenshot('cond_balloon_arrive', 0.9)   # 열기구 도착 화면
        cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.9)    # 부족!
        
        if (pix_status == pix_status_bal_window) or (cond_balloon_lack_heart) or (pix_status == pix_status_bal_what):
            print('젤리고기 부족..')
            click(892,54)
            # click(396,386)
            time.sleep(0.5)
            click(892,54)
            time.sleep(0.3)
            Kingdom_ready('kkd_out')
            break
        
        elif (cond_balloon_arrive):
            print('열기구 도착!')
            error_count = 0
            click(cond_balloon_arrive[0], cond_balloon_arrive[1])
            time.sleep(1)
            
        # 로비..
        elif pix_status == pix_status_bal_lobby or (cond_kkd_balloon):
            error_count = 0
            click(345,505)      # 이건 자동선택이고
            time.sleep(1)
            click(760,505)      # 이건 보내기고
            time.sleep(3)
        
        # 잘 날아감
        elif pix_status == pix_status_ballon or (cond_kkd_balloon_ing):
            print('열기구 나는중!')
            Kingdom_ready('kkd_out')
            return True
        
        else:
            print('열기구 - 남은 조건이 뭐가 있을까..')
            if error_count > 5:
                Kingdom_ready('kkd_out')
                return False
            else:
                error_count = error_count + 1
                time.sleep(1)


def Updown(updown):
    if updown == 'up':
        prod_clock = Find_in_Area('prod_clock', 554,350,20,153, 0.8)
        # y좌표 208이 원래 제일 위. 맨 아랫칸으로 가면 215. 225쯤 되면 맨 아래 짤림
        if (prod_clock):
            Drag_MouseDown(prod_clock[0],prod_clock[1],prod_clock[0],prod_clock[1]-20,1)    # 한 번 움직여보고
            Drag_MouseDown(prod_clock[0],prod_clock[1]-20,prod_clock[0],prod_clock[1],1)    # 두 번 움직여보고
            prod_clock_new = Find_in_Area('prod_clock', 554,350,20,153, 0.8)
            if (prod_clock_new):    # 새 위치 찾아서
                Drag(prod_clock[0],prod_clock[1],prod_clock[0],prod_clock[1] + (208 - prod_clock_new[1]), 2)
            time.sleep(1)
    if updown == 'down':
        print('dd')

# 올리고 내리고... 우선 내리는('up') 것만 되어있음
def Updown_Confidence(updown):
    if updown == 'up':
        Drag(610, 530, 610, 530-153*3, 2)
    if updown == 'down':
        Drag(610, 100, 610, 81+153*3, 2)

    start_time = time.time()
    while True:
        print('정교 위치 체크중...')
        if not While_True_Condition(start_time, 20):
            print('동작 최대시간 초과 or End버튼 누름')
            return
        # 두 번째 시계
        time.sleep(0.5)
        prod_clock = Find_in_Area('prod_clock', 554,198,20,153, 0.76)
        # y좌표 208이 원래 제일 위. 맨 아랫칸으로 가면 215. 225쯤 되면 맨 아래 짤림
        if (prod_clock):
            print('prod_clock',prod_clock)
            if 216 > prod_clock[1] > 200:
                print('오우예')
                return
            else:
                # 2, 3번 시계 보면 안되니....
                if prod_clock[1] > 200+153*2:
                    Drag_MouseDown(prod_clock[0], prod_clock[1] - 153*2, prod_clock[0], prod_clock[1] - 153*2 - 20, 1)
                    Drag_MouseDown(prod_clock[0], prod_clock[1] - 153*2 - 20, prod_clock[0], prod_clock[1] - 153*2, 1)
                    current_x, current_y = prod_clock[0], prod_clock[1]-153*2
                elif prod_clock[1] > 200+153:
                    Drag_MouseDown(prod_clock[0], prod_clock[1] - 153, prod_clock[0], prod_clock[1] - 153 - 20, 1)
                    Drag_MouseDown(prod_clock[0], prod_clock[1] - 153 - 20, prod_clock[0], prod_clock[1] - 153, 1)
                    current_x, current_y = prod_clock[0], prod_clock[1]-153
                else:
                    Drag_MouseDown(prod_clock[0], prod_clock[1], prod_clock[0], prod_clock[1]-20, 1)
                    Drag_MouseDown(prod_clock[0], prod_clock[1]-20, prod_clock[0], prod_clock[1], 1)
                    current_x, current_y = prod_clock[0], prod_clock[1]
                time.sleep(1)
                prod_clock_new = Find_in_Area('prod_clock', 554,198,20,153, 0.76)
                if (prod_clock_new):    # 새 위치 찾아서
                    if 212 > prod_clock_new[1] > 204:
                        print('오우예')
                        Drag(current_x, current_y, current_x+1, current_y, 0.1) # 마우스 눌린거 풀어줌(x로 한 칸 이동)
                        return
                    else:
                        Drag(current_x, current_y, current_x, current_y + 208 - prod_clock_new[1], 3)   # 현재 마우스 위치에서 목표(y:208까지의 차이값 만큼 빼줌)
                time.sleep(1)
        else:
            print('왜 못찾냐 시계를...')
            return


def Kingdom_ready(whereto):    # 특정 위치 확인
    error_position = 0
    start_time = time.time()
    err_crit_count = False
    while True:
        if not While_True_Condition(start_time, 120):
            print('[Kingdom_ready] 시간 초과!')
            return

        pix_status = Get_pixel_tuple(605,55)    # 상단골드
        pix_status2 = Get_pixel_tuple(540,510)  # 마침표
        pix_status_scr1 = Get_pixel_tuple(65, 505) # = 왼쪽아래 건설하기 아이콘쪽
        
        # 220203 추가 - 이미지 확인방식 추가(업뎃 후 픽셀값 변경...)
        cond_kkd_out = Find_in_Area('cond_kkd_out', 825,490,45,40, 0.9)    # 쿠키왕국
        cond_kkd_train = Find_in_Area('cond_kkd_train', 30,42,25,33, 0.9)  # 곰젤리열차
        cond_kkd_tro = Find_in_Area('cond_kkd_tro', 18,448,45,40, 0.85)    # 트로피칼(좌하단 파라솔 꽃)
        cond_kkd_sowon = Find_in_Area('cond_kkd_sowon', 430,45,31,35, 0.85)    # 소원나무
        cond_kkd_sangjum = Find_in_Area('cond_kkd_sangjum', 14,40,46,29, 0.85)   # 상점
        cond_kkd_balloon = Find_in_Area('cond_kkd_balloon', 9,36,25,35, 0.85)   # 열기구(대기)
        cond_kkd_balloon_ing = Find_in_Area('cond_kkd_balloon_ing', 364,85,28,37, 0.85)   # 열기구(대기)
        cond_gold = Find_in_Area('cond_gold', 310,35,555,50, 0.8)           # 골드 위치
        cond_gnome = Find_in_Area('cond_gnome', 310,35,555,50, 0.8)         # 노움 위치
        bInPosition = LocateCenterOnScreenshot('bInPosition', 0.8)             # 건물 안
        cond_adv_mode_select = Find_in_Area('cond_adv_mode_select', 12,38,37,36, 0.85)  # Play버튼 누른 후 모험하기 창
        cond_kkd_arena = LocateCenterOnScreenshot('cond_kkd_arena', 0.8)      # 킹덤아레나
        cond_reward = LocateCenterOnScreenshot('cond_reward', 0.8)      # 미션 보상받기
        mark_x_mission = Find_in_Area('mark_x_mission', 778,124,50,50, 0.8)      # 미션 취소
        cond_error_page = LocateCenterOnScreenshot('cond_error_page', 0.8)      # 검은 바탕... 렉 등에 의한 오류?
        cond_alarm = LocateCenterOnScreenshot('cond_alarm', 0.8)      # 검은 바탕... 렉 등에 의한 오류?
        cond_trade_perl = LocateCenterOnScreenshot('cond_trade_perl', 0.85)               # 해상무역센터 위치 확인
        
        if (cond_gold):
            # 혹시 또 1픽셀씩 오갈 수 있..으니?
            if 593 >= cond_gold[0] >= 591:
                # 소원,열차,상점,쿠키성 중 하나!
                if not (cond_kkd_sowon) and not (cond_kkd_train) and not (cond_kkd_sangjum):
                    print('쿠키성이네요!')
                    click(892,54)
                    time.sleep(1)
        
        if (cond_reward):
            click(cond_reward[0], cond_reward[1])
            time.sleep(2)
        
        if (mark_x_mission):
            click(mark_x_mission[0], mark_x_mission[1])
            time.sleep(1)
        
        # 상하단 픽셀 위치 모두 (0, 0, 0)이고 esc 누른 경우
        if pix_status == (0, 0, 0) and pix_status == (0, 0, 0) and (cond_error_page):
            End_kkd()                            # 쿠킹덤 종료

        if pix_status == pix_status_in or (bInPosition):   # 건물 안 ok
            error_position = 0
            print('건물 안이네요!')
            if (pix_status == whereto) or (whereto == 'prod_in'):   # 건물 안이냐고 물었으면 ok
                return True
            else:
                if whereto == 'prod_in':    # 건물 안이냐고 물은 게 아니면 No
                    return False
                click(892,54)
                time.sleep(0.3)
            
        elif pix_status == (pix_status_in_dark or pix_status_in_magic_dark) :    # 건물 안에서 창이 떠있으면 esc
            error_position = 0
            print('건물 내부 : 창은 닫자.')
            clickExact(940,438)
            time.sleep(0.3)
            
        elif (cond_trade_perl):    # 무역센터
            error_position = 0
            print('무역센터 내부!')
            if (pix_status == whereto) or (whereto == 'trade_in'):
                print('무역센터야!')
                return True
            else:
                if whereto == 'trade_in':
                    return False
                print('무역센터 아니야!')
                click(892,54)
                time.sleep(0.3)
        
        elif (cond_gnome):
            error_position = 0
            if whereto == 'research_in':
                print('연구소 옥희')
                return True
            else:
                print('연구소 안희야')
                click(628,117)  # 창 떠있을 수 있으니..
                time.sleep(1)
                click(892,54)
                time.sleep(3)
                
        elif pix_status == pix_status_fountain:    # 분수 내부
            error_position = 0
            print('분수 내부!')
            if (pix_status == whereto) or (whereto == 'fountain_in'):
                print('분수?')
                return True
            else:
                if whereto == 'fountain_in':
                    return False
                print('분수 아니야!')
                clickExact(940,438)
                time.sleep(0.3)
        
        elif (cond_adv_mode_select):    # 모험하기
            error_position = 0
            if (pix_status == whereto) or (whereto == 'mohum'):
                print('모험하기?')
                return True
            else:
                if whereto == 'mohum':
                    return False
                print('모험은 아...직?')
                clickExact(940,438)
                time.sleep(0.3)

        elif pix_status == pix_status_wanted:    # 현상수배 하기
            error_position = 0
            if (pix_status == whereto) or (whereto == 'wanted'):
                print('현상수배하기?')
                return True
            else:
                if whereto == 'wanted':
                    return False
                print('현상수배 선택 창이네?')
                clickExact(940,438)
                time.sleep(0.3)

        elif pix_status2 == pix_status_wanted:    # 현상수배 전투 종료
            error_position = 0
            if (pix_status == whereto) or (whereto == 'wanted_end'):
                print('현상수배 전투 완료!!')
                click(540,510)
                time.sleep(2)
                return True
            else:
                if whereto == 'wanted_end':
                    print('현상수배 전투중!')    
                    return False
                print('현상수배 전투중!')
                
                time.sleep(0.1)
                clickExact(940,438)
                time.sleep(0.3)

        elif pix_status == pix_status_kdpass:    # 킹덤패스
            error_position = 0
            print('킹덤패스! 아냐!')
            clickExact(940,438)
            time.sleep(0.3)

        elif pix_status == pix_status_warehouse:    # 창고
            error_position = 0
            print('창고! 아냐!')
            clickExact(940,438)
            time.sleep(0.3)
    
        elif pix_status == pix_status_lotto:    # 뽑기
            error_position = 0
            print('뽑기 아냐!')
            clickExact(940,438)
            time.sleep(0.3)

        elif pix_status == pix_status_mycookie:    # 내 쿠키..
            error_position = 0
            print('내쿠키 아냐!')
            
            time.sleep(0.1)
            clickExact(940,438)
            time.sleep(0.3)            
        
        elif pix_status == pix_status_not_prod:     # 건물 클릭했지만 쿠하나 일반건물
            error_position = 0
            print('이상한 건물!')
            
            time.sleep(0.1)
            clickExact(940,438)
            time.sleep(1)

        elif pix_status == pix_status_arena_lobby:
            print('아레나 로비 들어왔습니다!')
            click(284, 15)
            time.sleep(0.3)
            clickExact(940,438)
            time.sleep(1)

        elif (cond_kkd_train):
            error_position = 0
            if (whereto == 'train_in'):
                print('곰젤리 열차입니다!')
                return True
            else:
                
                time.sleep(0.1)
                clickExact(940,438)
                time.sleep(1)
                
        elif (cond_kkd_sowon):
            error_position = 0
            if (whereto == 'sowon_in'):
                print('소원나무 입니다!')
                return True
            else:
                print('소원나무 가려던 게 아니니 나갑니다.')
                click(892,54)
                time.sleep(1)
                screenshot_mode = Find_in_Area('screenshot_mode', 703,325-55,112,20+110, 0.95)
                if not (screenshot_mode):
                    click(892,54)
                time.sleep(2)
             
        elif (cond_kkd_sangjum):
            error_position = 0
            if (whereto == 'sangjum_in'):
                print('상점 입니다!')
                return True
            else:
                print('상점으로 가려던 게 아니니 나갑니다.')
                click(892,54)
                time.sleep(1)
                screenshot_mode = Find_in_Area('screenshot_mode', 703,325-55,112,20+110, 0.95)
                if not (screenshot_mode):
                    click(892,54)
                time.sleep(2)

        elif pix_status == pix_status_cookiehouse:
            error_position = 0
            print('쿠키하우스 안이에요')
            clickExact(940,438)
            time.sleep(1)

        elif pix_status == pix_status_out_window:
            error_position = 0
            print('창을 닫아요~')
            click(390,390)
            time.sleep(1)
        
        elif pix_status == pix_status_out_esc or (cond_alarm):
            error_position = 0
            if (pix_status_scr1 == pix_status1_tropical) or (cond_kkd_tro):   # 트로피컬 메인화면
                click(869, 494) # 왕국가기 버튼 클릭
                time.sleep(1)
                click(892,54)
                time.sleep(1)
            
            if(pix_status_scr1 == pix_status1_tropical_windowopen): # 트로피컬 메뉴화면
                clickExact(940,438)
                click(869, 494) # 왕국가기 버튼 클릭
                time.sleep(0.2)
                click(892,54)
                time.sleep(1)
            
            else:
                print('esc 취소')
                cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.95)
                if (cond_balloon_lack_heart):
                    click(cond_balloon_lack_heart[0], cond_balloon_lack_heart[1])
        
        elif (cond_kkd_out):
            error_position = 0
            if (cond_gold):
                if (cond_kkd_arena):
                    print('킹덤아레나 동상인가요?')
                    click(605,55)
                    time.sleep(1)
                else:
                    print('왕국이네요!')
                    if (whereto == 'kkd_out'):
                        cond_balloon_lack_heart = LocateCenterOnScreenshot('cond_balloon_lack_heart', 0.96)
                        if (cond_balloon_lack_heart):
                            click(cond_balloon_lack_heart[0], cond_balloon_lack_heart[1])
                        return True
                    elif (whereto == 'tropical_in'):
                        print('왕국인데 트로피칼 볼래요')
                        if Tropical_Event():     # 트로피칼에 이벤트 없으면
                            print('트로피칼 입장!')
                            return True
                        else:
                            print('트로피칼 이벤트 없어서 들어가지 않습니다.')
                            return False
                    else:
                        return False
                        
            else:
                print('왕국이긴 한데 이상한 건물인가 봅니다.')
                clickExact(940,438)
                time.sleep(0.7)
        
        elif pix_status == pix_stats_kkd_start:
            error_position = 0
            print('꺼졌네요... 재실행')
            Check_Initiating()

        elif pix_status == pix_status_ballon or (cond_kkd_balloon_ing):    # 열기구
            error_position = 0
            print('열기구 날아다니는 중!')
            if (pix_status == whereto) or (whereto == 'balloon_in'):
                return True
            else:
                if whereto == 'balloon_in':
                    return False
                click(892,54)
                time.sleep(2)
        
        elif pix_status == pix_status_bal_lobby or (cond_kkd_balloon):
            error_position = 0
            if (pix_status == whereto) or (whereto == 'balloon_in'):
                print('열기구 놀고 있네요')
                return True
            else:
                print('열기구 보내고 나갈께요!')
                Balloon_send()
                return False
        
        elif (cond_kkd_tro):
            error_position = 0
            if (whereto == 'tropical_in'):
                print('트로피칼 들어왔습니다!')
                return True
            else:
                # print('트로피칼 들어와서 돌리고 나갑니다.')
                # Tropical_Fight()
                print('트로피칼이 목적지가 아님니닷')
                clickExact(940,438)
                time.sleep(2)
                clickExact(940,438)
                time.sleep(2)
        
        else:
            if not (pix_status2 == 'wanted_end'):
                print('그 모든 게 아니라면....')
                mark_x = LocateCenterOnScreenshot('mark_x', 0.95)
                if (mark_x):
                    click(mark_x[0], mark_x[1])
                    time.sleep(5)
                if error_position == 0:
                    clickExact(940,438)
                    time.sleep(1)
                    Keyboard_Press('setup')
                    time.sleep(0.3)
                if error_position > 3:
                    click(605,55)
                    time.sleep(5)
                if error_position == 6:
                    Keyboard_Press('setup')
                if error_position == 7:
                    get_current_image_region(title_t, 2+100, 32+100, 917-200, 505-200, 'nox_halted_monitoring')
                    time.sleep(10)
                    halted_check = LocateCenterOnScreenshot('nox_halted_monitoring', 0.99)
                    if (halted_check):
                        click(904,16)
                        time.sleep(1)
                        click(660,325)
                        time.sleep(20)
                        Keyboard_Press('setup')
                    else:
                        End_kkd()
                        Check_Initiating()
                if error_position >= 8:
                    error_position = 0
                    if err_crit_count:
                        print('계속 반복하지 마렴..')
                        return False
                    else:
                        err_crit_count = True
                print('Error count =', error_position)
                error_position = error_position +1
            else:
                print('여긴 안도니')
                time.sleep(5)
                return False

def Check_Initiating():
    print('부팅여부 확인합니다.')
    bStart_Lv1 = False
    bStart_Lv2 = False
    start_time = time.time()
    kkd_start = LocateCenterOnScreenshot('init_kkm', 0.9)      # 녹스 바탕화면(쿠킹덤 실행 아이콘)
    kkd_touch = LocateCenterOnScreenshot('init_touch', 0.8)    # Touch To Start 화면
    kkd_down = LocateCenterOnScreenshot('init_Touch1', 0.95)   # 다운로드
    if (kkd_start) or (kkd_touch) or (kkd_down):
        start_time = time.time()
        while True:
            if not While_True_Condition(start_time, 300):
                return
            kkd_start = LocateCenterOnScreenshot('init_kkm', 0.9)      # 녹스 바탕화면(쿠킹덤 실행 아이콘)
            if (kkd_start):
                print('[부팅중] 계정 튕김! 쿠킹덤 아이콘 클릭!')
                click(kkd_start[0], kkd_start[1])
                bStart = True
                time.sleep(1)
            
            if bStart and not (kkd_start):
                print('[부팅중] 계정 튕김! 쿠킹덤 아이콘 클릭 완료!')
                time.sleep(3)
                break

        # 쿠킹덤 아이콘 실행 후 Touch to start쪽. 조건 없이 없어질 때까지 클릭
        while True:
            if not While_True_Condition(start_time, 300):
                return
            kkd_touch = LocateCenterOnScreenshot('init_touch', 0.8)    # Touch To Start 화면
            kkd_down = LocateCenterOnScreenshot('init_Touch1', 0.95)   # 다운로드

            if (kkd_touch):
                time.sleep(3)
                print('[부팅중] Touch to Start 터치!')
                click(410,380)
                bStart_Lv2 = True
                
            if (kkd_down):
                time.sleep(3)
                print('[부팅중] 다운로드 터치!')
                click(kkd_down[0], kkd_down[1])
                bStart_Lv2 = True
            
            if (not (kkd_touch) and not (kkd_down)) and bStart_Lv2:
                print('[부팅중] Touch to Start 터치 완료!')
                break
        
        if bStart_Lv2:
            print('부팅 실행 했습니다.')
            time.sleep(17)
            return
    else:
        print('튕긴건 아니네요')
        return

def Enter_Building():
    error_position = 0
    st_t = time.time()
    while True:
        # 최대 동작시간 5분?
        if not While_True_Condition(st_t, 300):
            print('[Enter_Building] 종료..')
            return False
        bWod_r = False
        bWod_l = False
        print('건물 들어가기 전 왕국 위치 확인')
        if not Kingdom_ready('prod_in'):
            Check_Initiating()
        else:
            print('이미 건물 안이네요!')
            return True

        while True:
            if not While_True_Condition(st_t, 300):
                print('[Enter_Building] 종료..')
                return False
            # 범위 = 271, 79, 545, 377
            wood_sign_r = Find_in_Area('wood_sign_r', 271, 79, 545, 377, 0.85)
            wood_sign_l = Find_in_Area('wood_sign_l', 271, 79, 545, 377, 0.85)

            # 못찾은 조건
            if (not (wood_sign_r) and not (wood_sign_l)):    # 왕국, 간판 없음
                print('간판이 없으니 스샷모드로 찾아볼까요')
                Enter_Screenshot_mode('left_down')
                # 중간에 풀렸다면?... 아몰랑

            # 우간판 조건
            if (wood_sign_r):
                if not bWod_r:
                    print('우간판 먼저 들어가 보고')
                    clickExact(wood_sign_r[0]-10, wood_sign_r[1]+10)
                    time.sleep(2)

                if Kingdom_ready('prod_in'):
                    print('우간판으로 건물 진입!')
                    return
                else:
                    print('우간판 클릭했지만 성공은 못했군..')
                    bWod_r = True

                if bWod_r:
                    print('한 번으로 못들어갔다면 다시 정조준')
                    time.sleep(2)
                    
                    wood_sign_r = Find_in_Area('wood_sign_r', 271, 79, 545, 377, 0.85)
                    if (wood_sign_r):
                        clickExact(wood_sign_r[0]-10, wood_sign_r[1]+10)
                        time.sleep(2)
                        if Kingdom_ready('prod_in'):
                            print('우간판으로 건물 진입!')
                            return
                    else:
                        print('어... 뭐야 왜 간판 사라짐...')
                        Kingdom_ready('kkd_out')

            # 좌간판 조건
            if (wood_sign_l):
                print('우간판이 없으니 좌간판이라도')
                clickExact(wood_sign_l[0]+10, wood_sign_l[1]-10)
                time.sleep(2)
                
                if Kingdom_ready('prod_in'):
                    print('좌간판으로 건물 진입!')
                    return
                else:
                    print('우간판 클릭했지만 성공은 못했군..')
                    bWod_l = True

                if (wood_sign_l) and bWod_l:
                    print('한 번으로 못들어갔다면 다시 정조준')
                    time.sleep(2)
                
                    wood_sign_l = Find_in_Area('wood_sign_l', 271, 79, 545, 377, 0.85)
                    if (wood_sign_l):
                        clickExact(wood_sign_l[0]+10, wood_sign_l[1]-10)
                        time.sleep(2)
                        if Kingdom_ready('prod_in'):
                            print('우간판으로 건물 진입!')
                            return
                    else:
                        print('어... 뭐야 왜 간판 사라짐...')
                        Kingdom_ready('kkd_out')

# locateCenterOnScreen 쓰고 싶을 때
def LocateCenterOnScreenshot(File_Name, confidence):
    """ Match all template occurrences which have a higher likelihood than the threshold """
    get_current_image(title_t)
    im = cv2.imread('test'+hwakjangja)
    template = cv2.imread(File_Name + hwakjangja)
    try:
        width, height = template.shape[:2]
        # shape쓰면 회전하나?
        # print('width, height',width, height)
        match_probability = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)
        # 여러 이미지 찾을 때(threshold 이상값)
        match_locations = np.where(match_probability >= confidence)
        # 제일 잘 맞는애 찾을 때
        # match_locations = np.unravel_index(match_probability.argmax(), match_probability.shape)

        # Add the match rectangle to the screen
        locations = []
        # 아니 띠바 왜죠? 직사각형 찾으면 height, width값이 또 바껴?
        for x, y in zip(*match_locations[::-1]):
            locations.append((int((x*2 + height)*0.5), int((y*2 + width)*0.5)))
        if len(locations) >= 1:
            # 순차오름 먹여주고(x,y 작은값부터 정열의 정렬)
            locations.sort()
            # print('sort후 locations',locations)
            return locations[0]
        else:
            return locations
    except:
        print(f'[LocateCenterOnScreenshot] {File_Name} 읽기 실패..')

# LocateAllOn 쓰고 싶을 때(범위 지정, 결과 다수..)
def LocateAll_Center(File_Name, x, y, x_range, y_range, confidence):
    im = cv2.imread('test'+hwakjangja, cv2.IMREAD_COLOR)
    im_range = im[y:y+y_range, x:x+x_range]
    template = cv2.imread(File_Name + hwakjangja, cv2.IMREAD_COLOR)
    try:
        width, height = template.shape[:2]
        match_probability = cv2.matchTemplate(im_range, template, cv2.TM_CCOEFF_NORMED)
        match_locations = np.where(match_probability >= confidence)
        locations = []
        for x1, y1 in zip(*match_locations[::-1]):
            locations.append((int((x1*2 + height)*0.5+x), int((y1*2 + width)*0.5+y)))
        return locations
    except:
        print(f'[LocateAll_Center] {File_Name} 읽기 실패')
        return []

# 지정된 범위 안, File_Name 유무 확인
def Find_in_Area(File_Name, x, y, x_range, y_range, confidence):
    get_current_image(title_t)
    # 우선 현재 화면 저장한 거 읽어와서
    im = cv2.imread('test'+hwakjangja, cv2.IMREAD_COLOR)
    # 범위로 자르기
    im_range = im[y:y+y_range, x:x+x_range]
    # 잘 잘렸는지 확인
    # cv2.imshow('why',im_range)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # 찾으려는 이미지도 읽어와서
    template = cv2.imread(File_Name + hwakjangja, cv2.IMREAD_COLOR)
    try:
        width, height = template.shape[:2]
        match_probability = cv2.matchTemplate(im_range, template, cv2.TM_CCOEFF_NORMED)
        match_locations = np.where(match_probability >= confidence)
        # match_location = np.unravel_index(match_probability.argmax(), match_probability.shape)
        locations = []
        for x1, y1 in zip(*match_locations[::-1]):
            locations.append((int((x1*2 + height)*0.5+x), int((y1*2 + width)*0.5+y)))
        if (locations):
            locations = locations[0]
        return locations
    except:
        print(f'[Find_in_Area] {File_Name} 읽기 실패')
        return []

# 설정 창 제목의 현재 화면을 받아서 test에 저장함
def get_current_image(title_t):
    # get window handle and dimensions
    hwnd = win32gui.FindWindow(None, title_t)
    dimensions = win32gui.GetWindowRect(hwnd)   # 창 정렬했으면 0계정 (0, 0, 960, 540), 1계정 (0, 540, 960, 1080)
    dimensions_w = 960
    dimensions_h = 540
    # 뭔가 막 받아오고 비트맵타입으로 변경하고 막.. 왠만한건 이 여섯 줄이 세트인듯
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, dimensions_w, dimensions_h)
    saveDC.SelectObject(saveBitMap)
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hWnd, saveDC.GetSafeHdc(), 0)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    # Image는 PIL안에 있음..? (https://www.geeksforgeeks.org/python-pil-image-frombuffer-method/)
    # Image.frombuffer(mode, size, data, decoder_name=’raw’, *args)
    # 이미지를 생성하는데, 컬러로('RGB'), 원래 사이즈(960X540), 받아온 이미지(bmpstr),
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    # 종료 전에 핸들 돌려주기인가.. 이 4줄도 고정
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    # im2 = im[300:500, 300:500]
    if result == 1:
    #PrintWindow Succeeded
        im.save('test'+hwakjangja)
        # im.show()
        # im2.show()
    return im

def get_current_image_region(title_t, x, y, x_range, y_range, file_name):
    get_current_image(title_t)
    im = cv2.imread('test'+hwakjangja, cv2.IMREAD_COLOR)
    # 범위로 자르기
    im_range = im[y:y+y_range, x:x+x_range]
    cv2.imwrite(file_name+hwakjangja, im_range)
    return im_range

# Canny 처리된 이미지 비교하기. 우선은 건물 내에서 건물 이름 읽기용
def Image_Compare_Canny(im1):
    img_saved = cv2.imread(im1+hwakjangja)
    # print('img_saved',img_saved)
    im = cv2.imread('test'+hwakjangja, cv2.IMREAD_COLOR)
    # 주의: 왜인지는 모르겠지만 [y:y+y_range, x:x_range]네...
    img_read = im[55:75, 295:355]
    img_read_gry = cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(img_read_gry, (3,3), 0)
    canny = cv2.Canny(blurred_img, 100, 200)
    cv2.imwrite('test_canny'+hwakjangja,canny)
    img_to_compare = cv2.imread('test_canny'+hwakjangja)
    
    err = np.sum((img_saved.astype("float") - img_to_compare.astype("float")) ** 2)
    err /= float(img_saved.shape[0] * img_to_compare.shape[1])
    return err

def Building_Num_Check():
    while True:
        if keyboard.is_pressed('end'):
            break
        bConfirmed = False
        for txt in building_name:
            err = Image_Compare_Canny(txt+'_canny')
            if err < 20000:
                print(txt)
                bConfirmed = True
                building_number = building_name.index(txt) + 1
                print(building_number)
                return building_number
            # else:
            #     print('not_matched err = ',err)
        if not bConfirmed:
            # click(325, 300)
            # time.sleep(0.5)
            print('맞는 이미지가 없음', err)
            return False
        time.sleep(0.5)

# DPI 셋팅(https://stackoverflow.com/questions/51786794/using-imagegrab-with-bbox-from-pywin32s-getwindowrect)
ctypes.windll.user32.SetProcessDPIAware()

# --------------------------절취선--------------------------
while True: # 여기서부턴 실제 생산
    err_crit_count = False
    start_timeA = time.time()
    if keyboard.is_pressed('END'):
        break

    print('start time = ', start_timeA)
    
    # 첫 account 다음 것부터 시작(0 -> 1, 1->2, 2->3?)
    Account_Change()

    # 초기화
    cycle_check = 0
    bwoodcompleted = False
    bjelbeancompleted = False
    bsugarcompleted = False
    bbiscuitcompleted = False
    bberrycompleted = False
    bmilkcompleted = False
    bcottoncompleted = False
    bsmithcompleted = False
    bjellycompleted = False
    bbreadcompleted = False
    bjampycompleted = False
    brollccompleted = False
    bdoyecompleted = False
    bflowercompleted = False
    bmilkycompleted = False
    blattecompleted = False
    bdollcompleted = False
    bbeercompleted = False
    bmuffincompleted = False
    bjewelcompleted = False
    bmagiccompleted = False
    if not bFirstCookhouA:
        cookie_time_A = time.time()
    if not bFirstFountainA:
        fountain_time_A = time.time()
    if not bFirstCookhouB:
        cookie_time_B = time.time()
    if not bFirstFountainB:
        fountain_time_B = time.time()

    if bAccount_A_Completed and bAccount_B_Completed:
        print('숏텀 모드 진입!')
        # 숏텀 모드 첫 진입 시 한 번 체크 해주고
        if not bShort_Term_ing:
            bShort_Term_ing = True
            tShort_Term_Start = time.time()
        else:
            tShort_Term_Now = time.time()
            if tShort_Term_Now - tShort_Term_Start > tShort_Term_Set:
                print('숏텀 모드 종료, 롱덤 모드 1차례씩 돌립니다.')
                bAccount_A_Completed = False
                bAccount_B_Completed = False
                bShort_Term_ing = False

        # 앵무 교역소 확인
        if Angmu_Enter('trade'):
            Angmu_Aft_Refresh()
        
        # 연구소 돌리기... 잠정 중단
        # if bResearch_auto:
        #     if account == 0:
        #         if Angmu_Enter('research'):
        #             research_action('C',research_A)   # 케이크 충전 가속
        #         if Angmu_Enter('research'):
        #             research_action('C',research_AA)   # 케이크 충전 가속
        #     if account == 1:
        #         if Angmu_Enter('research'):
        #             research_action('C',research_B)   # 케이크 충전 가속
        #         if Angmu_Enter('research'):
        #             research_action('C',research_BB)   # 케이크 충전 가속

        # 열차
        if Angmu_Enter('train'):     # 느낌표 떠있으면 들어감, 아니면 패스
            train_1 = Train_time(1)   # 왔으면 보내고;;
            train_2 = Train_time(2)
            train_3 = Train_time(3)
            if account == 0:
                train_A_1 = train_1
                train_A_2 = train_2
                train_A_3 = train_3
            if account == 1:
                train_B_1 = train_1
                train_B_2 = train_2
                train_B_3 = train_3
            print('열차 남은 시간 : ', train_1)
            print('열차 남은 시간 : ', train_2)
            print('열차 남은 시간 : ', train_3)
            Kingdom_ready('kkd_out')
            # 시간 체크를 정확히 하려면 Train_time함수를 while True: 안에 넣어서 return 값이 True가 되는 조건으로...

        # 열기구 보내기
        if Angmu_Enter('balloon'):
            Balloon_send()

        # 21.12.04 추가 - 체크 마크 클릭하기
        check_mark_time = time.time()   # 혹시 모르니 시간 제한도 넣고..
        while True:
            if not While_True_Condition(check_mark_time, 120):
                break
            check_check = LocateCenterOnScreenshot('check', 0.9)
            if (check_check):   # 있으면 클릭하긴 하는데..
                click(check_check)
                time.sleep(2)   # 2초쯤 기다리면 되려나..
                # ++ 여기다 열차, 열기구, 연구소, 트로피칼, 건물 완료, 왕국 미션 완료 다 때려박아야할듯..
                Kingdom_ready('kkd_out')   # 이쯤 되니 헷갈리네....그냥 빠져나오는 거였나..
            if not (check_check):
                print('체크 마크 없네요!')
                break
            time.sleep(2)

        # 실행 체크
        # Check_Initiating()
        Kingdom_ready('kkd_out')
        #건물에 들어가기..
        Enter_Building()
        # 건물 안에 들어왔으니 생산 시작
        # 초기화
        cycle_check = 0
        prod_direction_left = True
        # 쑛텀 생산 시작
        while True:
            if not While_True_Condition():
                break

            # urgent_now_t = time.time()
            # 설정 시간 지나면 나가기... 우선 1시간으로? 아님 시간 설정?
            # if urgent_now_t - urgent_start_t > 3600:
            #     click(891,54)
            #     break
            if (cycle_check > 30):
                print('쑛텀 : %s계정 마치고 다음 계정 들어갑니다.'%(title_t))
                Kingdom_ready('kkd_out')
                break
                
            kkd_start = LocateCenterOnScreenshot('init_kkm', 0.9)
            lack_of_material = LocateCenterOnScreenshot('lack_material', 0.95)
            pix_lackof = Get_pixel_tuple(545,745-540) # 재료부족창?

            pix_prod = Get_pixel_tuple(610,140)
            
            if pix_lackof == pix_lackof1:
                print('꺼져!(off!)')
                click(545,205)
                time.sleep(0.3)
                click(892, 54)
                time.sleep(0.3)
                Skip_Next(prod_direction_left)
            
            if pix_prod == pix_wood:
                pix_error_count = 0
                print('wood!')
                Wood_to_Cotton_Quick(wood_max, 1, prod_direction_left)
                if prod_direction_left:
                    cycle_check = cycle_check + 1
            
            elif pix_prod == pix_magic:
                print('Magic!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)
            
            elif pix_prod == pix_icecream:      # 마법 건물이면 prod_direction_left 오른쪽으로 돌려욧!
                pix_error_count = 0
                print('icecream!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)
            
            elif pix_prod == pix_jelbean:
                pix_error_count = 0
                print('jelbean!')
                Wood_to_Cotton_Quick(jelbean_max, 1, prod_direction_left)
            
            elif pix_prod == pix_white:
                pix_error_count = 0
                print('sugar!')
                Wood_to_Cotton_Quick(sugar_max, 1, prod_direction_left)

            elif pix_prod == pix_biscuit:
                pix_error_count = 0
                print('biscuit!')
                Wood_to_Cotton_Quick(biscuit_max, 2, prod_direction_left)
                
            elif pix_prod == pix_berry:
                pix_error_count = 0
                print('berry!')
                Wood_to_Cotton_Quick(berry_max, 2, prod_direction_left)
                
            elif pix_prod == pix_milk:
                pix_error_count = 0
                print('milk!')
                Wood_to_Cotton_Quick(milk_max, 1, prod_direction_left)
            
            elif pix_prod == pix_cotton:
                pix_error_count = 0
                print('cotton!')
                Wood_to_Cotton_Quick(cotton_max, cotton_prod, prod_direction_left)

            elif pix_prod == pix_smith:
                pix_error_count = 0
                print('smith!')
                # 작업 순방향 시작
                if not (smith_lev1==0) and not bsmithcompleted:
                    if not prod_action('smith_lev1', 'smith_stby_lv1', smith_lev1):
                        if (smith_lev2==0):
                            bsmithcompleted =  True
                        if not (smith_lev2==0) and not bsmithcompleted:
                            if not prod_action('smith_lev2', 'smith_stby_lv2', smith_lev2):
                                if (smith_lev3==0):
                                    bsmithcompleted =  True
                                if not (smith_lev3==0) and not bsmithcompleted:
                                    if not prod_action('smith_lev3', 'smith_stby_lv3', smith_lev3):
                                        if (smith_lev4==0):
                                            bsmithcompleted =  True
                                        if not (smith_lev4==0) and not bsmithcompleted:
                                            Updown('up')
                                            if not prod_action('smith_lev4', 'smith_stby_lv4', smith_lev4):
                                                if (smith_lev5==0):
                                                    bsmithcompleted =  True
                                                if not (smith_lev5==0) and not bsmithcompleted:
                                                    Updown('up')
                                                    if not prod_action('smith_lev5', 'smith_stby_lv5', smith_lev5):
                                                        if (smith_lev6==0):
                                                            bsmithcompleted =  True
                                                        if not (smith_lev6==0) and not bsmithcompleted:
                                                            Updown('up')
                                                            if not prod_action('smith_lev6', 'smith_stby_lv6', smith_lev6):
                                                                if (smith_lev7==0):
                                                                    bsmithcompleted =  True
                                                                if not (smith_lev7==0) and not bsmithcompleted:
                                                                    Updown('up')
                                                                    if not prod_action('smith_lev7', 'smith_stby_lv7', smith_lev7):
                                                                        bsmithcompleted =  True
                                                                    Skip_Next(prod_direction_left)
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                else:
                    Skip_Next(prod_direction_left)
                # 작업 순방향 끝
            
            elif pix_prod == pix_jelly:
                pix_error_count = 0
                print('jelly!')
                # 작업 순방향 시작
                if not (jelly_lev1==0) and not bjellycompleted:
                    if not prod_action('jelly_lev1', 'jelly_stby_lv1', jelly_lev1):
                        if (jelly_lev2==0):
                            bjellycompleted = True
                        if not (jelly_lev2==0) and not bjellycompleted:
                            if not prod_action('jelly_lev2', 'jelly_stby_lv2', jelly_lev2):
                                if (jelly_lev3==0):
                                    bjellycompleted = True
                                if not (jelly_lev3==0) and not bjellycompleted:
                                    if not prod_action('jelly_lev3', 'jelly_stby_lv3', jelly_lev3):
                                        if (jelly_lev4==0):
                                            bjellycompleted = True
                                        if not (jelly_lev4==0) and not bjellycompleted:
                                            Updown('up')
                                            if not prod_action('jelly_lev4', 'jelly_stby_lv4', jelly_lev4):
                                                if (jelly_lev5==0):
                                                    bjellycompleted = True
                                                if not (jelly_lev5==0) and not bjellycompleted:
                                                    Updown('up')
                                                    if not prod_action('jelly_lev5', 'jelly_stby_lv5', jelly_lev5):
                                                        bjellycompleted = True
                                                    Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                else:
                    Skip_Next(prod_direction_left)
                # 작업 순방향 끝
            
            elif pix_prod == pix_rollc:
                pix_error_count = 0
                print('rollc!')
                # 작업 순방향 시작
                if not (rollc_lev1==0) and not brollccompleted:
                    if not prod_action('rollc_lev1', 'rollc_stby_lv1', rollc_lev1):
                        if (rollc_lev2==0):
                            brollccompleted = True
                        if not (rollc_lev2==0) and not brollccompleted:
                            if not prod_action('rollc_lev2', 'rollc_stby_lv2', rollc_lev2):
                                if (rollc_lev3==0):
                                    brollccompleted = True
                                if not (rollc_lev3==0) and not brollccompleted:
                                    if not prod_action('rollc_lev3', 'rollc_stby_lv3', rollc_lev3):
                                        if (rollc_lev4==0):
                                            brollccompleted = True
                                        if not (rollc_lev4==0) and not brollccompleted:
                                            Updown('up')
                                            if not prod_action('rollc_lev4', 'rollc_stby_lv4', rollc_lev4):
                                                brollccompleted = True
                                            Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                else:
                    Skip_Next(prod_direction_left)
                # 작업 순방향 끝

            elif pix_prod == pix_bread:
                pix_error_count = 0
                print('bread!')
                prod_direction_left = True
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_jampy:
                pix_error_count = 0
                print('jampy!')
                prod_direction_left = True
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_doye:
                pix_error_count = 0
                print('doye!')
                prod_direction_left = True
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_flower:
                pix_error_count = 0
                print('flower!')
                prod_direction_left = True
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_milky:
                pix_error_count = 0
                print('milky!')
                prod_direction_left = True
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_latte:
                pix_error_count = 0
                print('latte!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)


            elif pix_prod == pix_dolls:
                pix_error_count = 0
                print('dolls!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)
                
            
            elif pix_prod == pix_beer:
                pix_error_count = 0
                print('beer!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)

            elif pix_prod == pix_muffin:
                pix_error_count = 0
                print('muffin!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)
            
            elif pix_prod == pix_jewel:
                pix_error_count = 0
                print('jewel!')
                prod_direction_left = False
                Skip_Next(prod_direction_left)

            elif (kkd_start):
                print('[생산중] 계정 튕김! 쿠킹덤을 실행합니다!')
                # 실행 체크
                Check_Initiating()
                # 줌아웃, 좌하단으로 화면이동. 간판 하나라도 찾으면 True.. 없을조건..도 만들어야겠네
                # Check_Prod_Ready()
                #건물에 들어가기..
                Enter_Building()
            
            elif (lack_of_material):
                print('아이템이 부족하대요~ 다음으로 넘어갑니다아~')
                click(629,169)
                time.sleep(0.5)
                Skip_Next(prod_direction_left)
            
            elif not Kingdom_ready('prod_in'):
                print('설마 여기 도나')
                Enter_Building()
            
            else:
                pix_error_count = pix_error_count + 1
                if prod_pix_confirm >= pix_error_count:
                    print('건물 안에서... 픽셀값 찾게 위로 올림')
                    for i in range(2):
                        prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
                        if (prod_clock):
                            x_start, y_start = prod_clock[0], prod_clock[1]
                        else:
                            x_start, y_start = 610, 150
                        Drag(x_start, y_start, x_start, 540, 1)
                        time.sleep(1)
                else:
                    print('건물 안에서... 이게 아니라면... 우선 좌클릭')
                    Skip_Next(prod_direction_left)
        print('다음 계정을 실행합니다.')

    elif bAccount_A_Completed and account == 0:
        print('A 계정 끝났으니 B계정 돌릴 차례입니다.')
        break
    elif bAccount_B_Completed and account == 1:
        print('B 계정 끝났으니 A계정 돌릴 차례입니다.')
        break
    else:   # bAccount_A_Completed a나 b 살아있는 경우
        prod_direction_left = True
        # 실행 체크
        # Check_Initiating()
        Kingdom_ready('kkd_out')
        #건물에 들어가기..
        Enter_Building()
        # 건물 안에 들어왔으니 생산 시작
        Product_Start_Time = time.time()
        while True: # 건물 내 작업만 주구장창..?
            if keyboard.is_pressed('END'):
                break
            print('생산을 집도한다! 계정 = %s, 싸이클 = %s'%(title_t, cycle_check))
            Product_Now_Time = time.time()

            # 싸이클 완료 조건
            if (cycle_check > how_many_cycle*2) or ((Product_Now_Time - Product_Start_Time) > Producting_Time):
                print('싸이클 완료. 왕국 활동 진행 후 말미를 드립니다.')
                Kingdom_ready('kkd_out')
                
                # 개별 계정 돌려야 하는 경우 : 쿠하만?
                now_time = time.time()  # 현재 시각은?
                if account == 0:
                    bAccount_A_Completed = True
                    # 분수 클릭(자연스레 좌상으로 화면 이동)
                    if not bFirstFountainA:
                        Angmu_Enter('fountain')
                        fountain_time_A = time.time()  # 클릭한 시간을 다시 저장
                        bFirstFountainA = True
                    else:
                        if (now_time - fountain_time_A) > fountain_set_time_A:
                            Angmu_Enter('fountain')
                            fountain_time_A = time.time()  # 클릭한 시간을 다시 저장

                    # 쿠하 클릭
                    if not bFirstCookhouA:
                        print('[쿠하] 계정 A 첫 클릭')
                        Cond_cookiehouse = Find_in_Area('Cond_cookiehouse', 249,78,576,382, 0.9)
                        if (Cond_cookiehouse):
                            click(Cond_cookiehouse[0], Cond_cookiehouse[1])
                            cookie_time_A = time.time()  # 클릭한 시간을 다시 저장
                            bFirstCookhouA = True
                    else:
                        if (now_time - cookie_time_A) > cookie_set_time:
                            print('[쿠하] 설정 시간이 지나서 클릭합니다.', now_time - cookie_time_A)
                            time.sleep(1)
                            Cond_cookiehouse = Find_in_Area('Cond_cookiehouse', 249,78,576,382, 0.9)
                            if (Cond_cookiehouse):
                                click(Cond_cookiehouse[0], Cond_cookiehouse[1])
                            cookie_time_A = time.time()  # 클릭한 시간을 다시 저장
        
                        
                if account == 1:
                    bAccount_B_Completed = True
                    # 분수 클릭(자연스레 좌상으로 화면 이동)
                    if not bFirstFountainB:
                        Angmu_Enter('fountain')
                        fountain_time_B = time.time()  # 클릭한 시간을 다시 저장
                        bFirstFountainB = True
                    else:
                        if (now_time - fountain_time_B) > fountain_set_time_B:
                            Angmu_Enter('fountain')
                            fountain_time_B = time.time()  # 클릭한 시간을 다시 저장

                    # 쿠하 클릭
                    if not bFirstCookhouB:
                        print('[쿠하] 계정 B 첫 클릭')
                        Cond_cookiehouse = Find_in_Area('Cond_cookiehouse', 249,78,576,382, 0.9)
                        if (Cond_cookiehouse):
                            click(Cond_cookiehouse[0], Cond_cookiehouse[1])
                            cookie_time_B = time.time()  # 클릭한 시간을 다시 저장
                        bFirstCookhouB = True
                    else:
                        if (now_time - cookie_time_B) > cookie_set_time:
                            print('[쿠하] 설정 시간이 지나서 클릭합니다.', now_time - cookie_time_B)
                            time.sleep(1)
                            Cond_cookiehouse = Find_in_Area('Cond_cookiehouse', 249,78,576,382, 0.9)
                            if (Cond_cookiehouse):
                                click(Cond_cookiehouse[0], Cond_cookiehouse[1])
                                cookie_time_B = time.time()  # 클릭한 시간을 다시 저장
                
                # 여기서부턴 계정 자동 구분 되는 넘들
                # 211206 추가 - 하트 남은 수량 확인해서... 마지막으로 돈 곳을 다시 돌기.(위치 클릭)
                # 220203 추가 - 하트 클릭했을 때 밑에 시간 뜨면 조건확인, 안뜨면 바로 소진
                Kingdom_ready('kkd_out')
                get_current_image_region(title_t, 380, 65, 51, 14, 'heart_full_check')
                click(357,55)
                time.sleep(1)
                diff_check = Find_in_Area('heart_full_check', confidence=0.95, grayscale=True, region=(380, 65, 51, 14))
                if (diff_check):
                    print('하트 수량 Full입니다!')
                    click(396,386)
                    print('하트 소진모드 들어감다')     # 마지막 들어간 곳이 센터정렬 되어서 그곳을 계속 돈다... 즉, 어둠모드는 아직 안됨 ㅠㅠ
                    Heart_sojin('8-29')         # 8-29라 쓰지만 의미 읍따는 ㅠㅠ
                else:
                    print('하트 수량 Full이 아닙니다.')
                    click(396,386)
                    time.sleep(1)
                    while True:
                        cond_kkd_out = Find_in_Area('cond_kkd_out', confidence=0.85, region=(825,490,45,40))    # 쿠키왕국
                        cond_adv_mode_select = Find_in_Area('cond_adv_mode_select', confidence=0.85, region=(12,38,37,36))  # Play버튼 누른 후 모험하기 창
                        if (cond_adv_mode_select):      # 플레이 버튼 눌렀음
                            print('모험하기!')
                            break
                        if (cond_kkd_out):
                            Kingdom_ready('kkd_out')    # 창 떠있는 경우 삭제용
                            print('Play 버튼 클릭~!')
                            click(random.randint(730,785),random.randint(470,525))
                            time.sleep(10)
                    if Heart_new_numb() > heart_set_num:
                        print('하트 소진모드 들어감다')     # 마지막 들어간 곳이 센터정렬 되어서 그곳을 계속 돈다... 즉, 어둠모드는 아직 안됨 ㅠㅠ
                        Heart_sojin('8-29')         # 8-29라 쓰지만 의미 읍따는 ㅠㅠ
                    else:
                        print('하트 소진할 때가 아닙니다!')
                        Kingdom_ready('kkd_out')
                
                for i in range(delay_to_next_account):
                    print('다음 계정 실행까지', delay_to_next_account - i, '초 남았습니다. 현재 계정: ')
                    time.sleep(1)
                    if keyboard.is_pressed('end'):
                        print('end 눌러 종료합니다.')
                        break

                # 220203 추가 - 뽑기 일일 보상 획득
                # 220226 추가 - 뽑기 아이콘으로 완료여부 판단
                cond_bbopkki = Find_in_Area('cond_bbopkki', confidence=0.85, region=(535,460,30,30))
                if (cond_bbopkki):
                    click(532,504)
                    time.sleep(1)
                    cond_bbopkki2 = LocateCenterOnScreenshot('cond_bbopkki2', confidence=0.85,)
                    if (cond_bbopkki2):
                        click(cond_bbopkki2)
                        time.sleep(0.5)
                        while True:
                            cond_bbopkki3 = Find_in_Area('cond_bbopkki3', confidence=0.85, region=(743,458,152,53))
                            if (cond_bbopkki3):
                                click(cond_bbopkki3)
                                time.sleep(3)
                            else:
                                print('뽑기 일일보상 완료!')
                                click(892, 54)
                                time.sleep(1.5)
                                click(892, 54)
                                time.sleep(4)
                                Kingdom_ready('kkd_out')
                                print('현재 계정 = ',title_t)
                                break
                else:
                    print('뽑기 일일보상은 완료함')
                
                # 220302 추가 - 상점 일일보상 획득
                Angmu_Enter('shop')

                # 220309 추가 - 길드 일일보상 획득
                Angmu_Enter('guild')
                
                # 킹덤패스 보상 확인
                Kpass_reward()

                # 트로피칼 확인
                if bTropical:
                    if Tropical_Event():
                        Tropical_Fight()
                
                # 소원나무 쪽지 보내기
                Sowon_jjokji_action(jjokji_numb, jjokji_limit)
                
                # 220627 추가 : 아레나
                if Arena_Event():
                    Arena_action(set_max_power)
                break
                
                
                
            in_pos = LocateCenterOnScreenshot('bInPosition', 0.8)
            kkd_start = LocateCenterOnScreenshot('init_kkm', 0.9)
            Confirm_button = Find_in_Area('Cond_not_opened', 285,483,254,22, 0.9)
            lack_of_material = LocateCenterOnScreenshot('lack_material',0.95)
            pix_prod = Get_pixel_tuple(610,140)
            pix_end = Get_pixel_tuple(118,483) # 하단 화살
            pix_end1 = Get_pixel_tuple(115,415) # 중단 화살
            pix_end2 = Get_pixel_tuple(75,480) # 밑바닥칸
            pix_lackof = Get_pixel_tuple(545,745-540) # 재료부족창?

            if keyboard.is_pressed('space'):
                break
            # 이상한 창이 떠있나?
            
            if pix_lackof == pix_lackof1:
                print('꺼져!(off!)')
                click(545,205)
                time.sleep(0.3)
                click(892, 54)
                time.sleep(0.3)
                click(164,280)
                time.sleep(0.5)
            # 건물 내부 색상 파악
            elif pix_prod == pix_magic:
                print('Magic!')
                if not bProdHigh or magic_num == 1:
                    bSecond = False
                    # 작업 순방향 시작
                    if not (magic_lev1 == 0) and not bmagiccompleted:
                        if not prod_action('magic_lev1', 'magic_stby_lv1', magic_lev1):
                            if (magic_lev2 == 0):
                                bmagiccompleted = True
                            if not (magic_lev2 == 0) and not bmagiccompleted:
                                if not prod_action('magic_lev2', 'magic_stby_lv2', magic_lev2):
                                    if (magic_lev3 == 0):
                                        bmagiccompleted = True
                                    if not (magic_lev3 == 0) and not bmagiccompleted:
                                        if not prod_action('magic_lev3', 'magic_stby_lv3', magic_lev3):
                                            if (magic_lev4 == 0):
                                                bmagiccompleted = True
                                            if not (magic_lev4 == 0) and not bmagiccompleted:
                                                Updown('up')
                                                if not prod_action('magic_lev4', 'magic_stby_lv4', magic_lev4):
                                                    if (magic_lev5 == 0):
                                                        bmagiccompleted = True
                                                    if not (magic_lev5 == 0) and not bmagiccompleted:
                                                        Updown('up')
                                                        if not prod_action('magic_lev5', 'magic_stby_lv5', magic_lev5):
                                                            if (magic_lev6 == 0):
                                                                bmagiccompleted = True
                                                            if not (magic_lev6 == 0) and not bmagiccompleted:
                                                                Updown('up')
                                                                if not prod_action('magic_lev6', 'magic_stby_lv6', magic_lev6):
                                                                    if (magic_lev7 == 0):
                                                                        bmagiccompleted = True
                                                                    if not (magic_lev7 == 0) and not bmagiccompleted:
                                                                        Updown('up')
                                                                        if not prod_action('magic_lev7', 'magic_stby_lv7', magic_lev7):
                                                                            bmagiccompleted = True
                                                                        Skip_Next(prod_direction_left)
                                                                    else:
                                                                        Skip_Next(prod_direction_left)
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or magic_num == 1:
                        break
                    if bProdHigh and not bSecond and magic_num == 2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (magic_lev1 == 0):
                            if not prod_action('magic_lev1', 'magic_stby_lv1', magic_lev1):
                                if not (magic_lev2 == 0):
                                    if not prod_action('magic_lev2', 'magic_stby_lv2', magic_lev2):
                                        if not (magic_lev3 == 0):
                                            if not prod_action('magic_lev3', 'magic_stby_lv3', magic_lev3):
                                                if not (magic_lev4 == 0):
                                                    Updown('up')
                                                    if not prod_action('magic_lev4', 'magic_stby_lv4', magic_lev4):
                                                        if not (magic_lev5 == 0):
                                                            Updown('up')
                                                            if not prod_action('magic_lev5', 'magic_stby_lv5', magic_lev5):
                                                                if not (magic_lev6 == 0):
                                                                    Updown('up')
                                                                    if not prod_action('magic_lev6', 'magic_stby_lv6', magic_lev6):
                                                                        if not (magic_lev7 == 0):
                                                                            Updown('up')
                                                                            prod_action('magic_lev7', 'magic_stby_lv7', magic_lev7)
                                                                            Skip_Next(prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                        else:
                                                                            Skip_Next(prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                    else:
                                                                        Skip_Next(prod_direction_left)
                                                                        bSecond = True
                                                                        break
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and magic_num == 2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (magic_lev7 == 0):
                            if (magic_lev6 == 0):
                                if (magic_lev5 == 0):
                                    if (magic_lev4 == 0):
                                        if (magic_lev3 == 0):
                                            if (magic_lev2 == 0):
                                                prod_action('magic_lev1', 'magic_stby_lv1', magic_lev1)
                                                Skip_Next(prod_direction_left)
                                                bSecond = False
                                                break
                                            else:
                                                prod_action('magic_lev2', 'magic_stby_lv2', magic_lev2)
                                                Skip_Next(prod_direction_left)
                                                bSecond = False
                                                break
                                        else:
                                            prod_action('magic_lev3', 'magic_stby_lv3', magic_lev3)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        Updown('up')
                                        prod_action('magic_lev4', 'magic_stby_lv4', magic_lev4)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown('up')
                                    Updown('up')
                                    prod_action('magic_lev5', 'magic_stby_lv5', magic_lev5)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                Updown('up')
                                Updown('up')
                                prod_action('magic_lev6', 'magic_stby_lv6', magic_lev6)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            prod_action('magic_lev7', 'magic_stby_lv7', magic_lev7)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                        # 작업 역방향 끝
            
            elif pix_prod == pix_icecream:      # 마법 건물이면 prod_direction_left 오른쪽으로 돌려욧!
                pix_error_count = 0
                print('icecream!')
                # ++아이스크림 추가 흠...
                Skip_Next(prod_direction_left)
            
            elif pix_prod == pix_wood:
                pix_error_count = 0
                print('wood!')
                Wood_to_Cotton(wood_min, wood_max, wood_prod, prod_direction_left)
                cycle_check = cycle_check + 1
            
            elif pix_prod == pix_jelbean:
                pix_error_count = 0
                print('jelbean!')
                Wood_to_Cotton(jelbean_min, jelbean_max, jelbean_prod, prod_direction_left)
            
            elif pix_prod == pix_white:
                pix_error_count = 0
                print('sugar!')
                Wood_to_Cotton(sugar_min, sugar_max, sugar_prod, prod_direction_left)
                
            elif pix_prod == pix_biscuit:
                pix_error_count = 0
                print('biscuit!')
                jjokji_biscuit = Wood_to_Cotton(biscuit_min, biscuit_max, biscuit_prod, prod_direction_left)
            
            elif pix_prod == pix_berry:
                pix_error_count = 0
                print('berry!')
                jjokji_berry = Wood_to_Cotton(berry_min, berry_max, berry_prod, prod_direction_left)
            
            elif pix_prod == pix_milk:
                pix_error_count = 0
                print('milk!')
                jjokji_milk = Wood_to_Cotton(milk_min, milk_max, milk_prod, prod_direction_left)
            
            elif pix_prod == pix_cotton:
                pix_error_count = 0
                print('cotton!')
                jjokji_cotton = Wood_to_Cotton(cotton_min, cotton_max, cotton_prod, prod_direction_left)
            
            elif pix_prod == pix_smith:
                pix_error_count = 0
                print('smith!')
                if not bProdHigh or smith_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (smith_lev1==0) and not bsmithcompleted:
                        if not prod_action('smith_lev1', 'smith_stby_lv1', smith_lev1):
                            if (smith_lev2==0):
                                bsmithcompleted =  True
                            if not (smith_lev2==0) and not bsmithcompleted:
                                if not prod_action('smith_lev2', 'smith_stby_lv2', smith_lev2):
                                    if (smith_lev3==0):
                                        bsmithcompleted =  True
                                    if not (smith_lev3==0) and not bsmithcompleted:
                                        if not prod_action('smith_lev3', 'smith_stby_lv3', smith_lev3):
                                            if (smith_lev4==0):
                                                bsmithcompleted =  True
                                            if not (smith_lev4==0) and not bsmithcompleted:
                                                Updown('up')
                                                if not prod_action('smith_lev4', 'smith_stby_lv4', smith_lev4):
                                                    if (smith_lev5==0):
                                                        bsmithcompleted =  True
                                                    if not (smith_lev5==0) and not bsmithcompleted:
                                                        Updown('up')
                                                        if not prod_action('smith_lev5', 'smith_stby_lv5', smith_lev5):
                                                            if (smith_lev6==0):
                                                                bsmithcompleted =  True
                                                            if not (smith_lev6==0) and not bsmithcompleted:
                                                                Updown('up')
                                                                if not prod_action('smith_lev6', 'smith_stby_lv6', smith_lev6):
                                                                    if (smith_lev7==0):
                                                                        bsmithcompleted =  True
                                                                    if not (smith_lev7==0) and not bsmithcompleted:
                                                                        Updown('up')
                                                                        if not prod_action('smith_lev7', 'smith_stby_lv7', smith_lev7):
                                                                            bsmithcompleted =  True
                                                                        Skip_Next(prod_direction_left)
                                                                    else:
                                                                        Skip_Next(prod_direction_left)
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or smith_num==1:
                        break
                    if bProdHigh and not bSecond and smith_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (smith_lev1==0):
                            if not prod_action('smith_lev1', 'smith_stby_lv1', smith_lev1):
                                if not (smith_lev2==0):
                                    if not prod_action('smith_lev2', 'smith_stby_lv2', smith_lev2):
                                        if not (smith_lev3==0):
                                            if not prod_action('smith_lev3', 'smith_stby_lv3', smith_lev3):
                                                if not (smith_lev4==0):
                                                    Updown('up')
                                                    if not prod_action('smith_lev4', 'smith_stby_lv4', smith_lev4):
                                                        if not (smith_lev5==0):
                                                            Updown('up')
                                                            if not prod_action('smith_lev5', 'smith_stby_lv5', smith_lev5):
                                                                if not (smith_lev6==0):
                                                                    Updown('up')
                                                                    if not prod_action('smith_lev6', 'smith_stby_lv6', smith_lev6):
                                                                        if not (smith_lev7==0):
                                                                            Updown('up')
                                                                            prod_action('smith_lev7', 'smith_stby_lv7', smith_lev7)
                                                                            Skip_Next(prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                        else:
                                                                            Skip_Next(prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                    else:
                                                                        Skip_Next(prod_direction_left)
                                                                        bSecond = True
                                                                        break
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and smith_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (smith_lev7==0):
                            if (smith_lev6==0):
                                if (smith_lev5==0):
                                    if (smith_lev4==0):
                                        if (smith_lev3==0):
                                            if (smith_lev2==0):
                                                prod_action('smith_lev1', 'smith_stby_lv1', smith_lev1)
                                                Skip_Next(prod_direction_left)
                                                bSecond = False
                                                break
                                            else:
                                                prod_action('smith_lev2', 'smith_stby_lv2', smith_lev2)
                                                Skip_Next(prod_direction_left)
                                                bSecond = False
                                                break
                                        else:
                                            prod_action('smith_lev3', 'smith_stby_lv3', smith_lev3)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        Updown('up')
                                        prod_action('smith_lev4', 'smith_stby_lv4', smith_lev4)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown('up')
                                    Updown('up')
                                    prod_action('smith_lev5', 'smith_stby_lv5', smith_lev5)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                Updown('up')
                                Updown('up')
                                prod_action('smith_lev6', 'smith_stby_lv6', smith_lev6)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            prod_action('smith_lev7', 'smith_stby_lv7', smith_lev7)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                        # 작업 역방향 끝

            
            elif pix_prod == pix_jelly:
                pix_error_count = 0
                print('jelly!')
                if not bProdHigh or jelly_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (jelly_lev1==0) and not bjellycompleted:
                        if not prod_action('jelly_lev1', 'jelly_stby_lv1', jelly_lev1):
                            if (jelly_lev2==0):
                                bjellycompleted = True
                            if not (jelly_lev2==0) and not bjellycompleted:
                                if not prod_action('jelly_lev2', 'jelly_stby_lv2', jelly_lev2):
                                    if (jelly_lev3==0):
                                        bjellycompleted = True
                                    if not (jelly_lev3==0) and not bjellycompleted:
                                        if not prod_action('jelly_lev3', 'jelly_stby_lv3', jelly_lev3):
                                            if (jelly_lev4==0):
                                                bjellycompleted = True
                                            if not (jelly_lev4==0) and not bjellycompleted:
                                                Updown('up')
                                                if not prod_action('jelly_lev4', 'jelly_stby_lv4', jelly_lev4):
                                                    if (jelly_lev5==0):
                                                        bjellycompleted = True
                                                    if not (jelly_lev5==0) and not bjellycompleted:
                                                        Updown('up')
                                                        if not prod_action('jelly_lev5', 'jelly_stby_lv5', jelly_lev5):
                                                            bjellycompleted = True
                                                        Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or jelly_num==1:
                        break
                    if bProdHigh and not bSecond and jelly_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (jelly_lev1==0):
                            if not prod_action('jelly_lev1', 'jelly_stby_lv1', jelly_lev1):
                                if not (jelly_lev2==0):
                                    if not prod_action('jelly_lev2', 'jelly_stby_lv2', jelly_lev2):
                                        if not (jelly_lev3==0):
                                            if not prod_action('jelly_lev3', 'jelly_stby_lv3', jelly_lev3):
                                                if not (jelly_lev4==0):
                                                    Updown('up')
                                                    if not prod_action('jelly_lev4', 'jelly_stby_lv4', jelly_lev4):
                                                        if not (jelly_lev5==0):
                                                            Updown('up')
                                                            prod_action('jelly_lev5', 'jelly_stby_lv5', jelly_lev5)
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and jelly_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (jelly_lev5==0):
                            if (jelly_lev4==0):
                                if (jelly_lev3==0):
                                    if (jelly_lev2==0):
                                        prod_action('jelly_lev1', 'jelly_stby_lv1', jelly_lev1)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('jelly_lev2', 'jelly_stby_lv2', jelly_lev2)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('jelly_lev3', 'jelly_stby_lv3', jelly_lev3)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                prod_action('jelly_lev4', 'jelly_stby_lv4', jelly_lev4)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            prod_action('jelly_lev5', 'jelly_stby_lv5', jelly_lev5)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                        # 작업 역방향 끝

            
            elif pix_prod == pix_rollc:
                pix_error_count = 0
                print('rollc!')
                if not bProdHigh or rollc_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (rollc_lev1==0) and not brollccompleted:
                        if not prod_action('rollc_lev1', 'rollc_stby_lv1', rollc_lev1):
                            if (rollc_lev2==0):
                                brollccompleted = True
                            if not (rollc_lev2==0) and not brollccompleted:
                                if not prod_action('rollc_lev2', 'rollc_stby_lv2', rollc_lev2):
                                    if (rollc_lev3==0):
                                        brollccompleted = True
                                    if not (rollc_lev3==0) and not brollccompleted:
                                        if not prod_action('rollc_lev3', 'rollc_stby_lv3', rollc_lev3):
                                            if (rollc_lev4==0):
                                                brollccompleted = True
                                            if not (rollc_lev4==0) and not brollccompleted:
                                                Updown('up')
                                                if not prod_action('rollc_lev4', 'rollc_stby_lv4', rollc_lev4):
                                                    brollccompleted = True
                                                Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or rollc_num==1:
                        break
                    if bProdHigh and not bSecond and rollc_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (rollc_lev1==0):
                            if not prod_action('rollc_lev1', 'rollc_stby_lv1', rollc_lev1):
                                if not (rollc_lev2==0):
                                    if not prod_action('rollc_lev2', 'rollc_stby_lv2', rollc_lev2):
                                        if not (rollc_lev3==0):
                                            if not prod_action('rollc_lev3', 'rollc_stby_lv3', rollc_lev3):
                                                if not (rollc_lev4==0):
                                                    Updown('up')
                                                    prod_action('rollc_lev4', 'rollc_stby_lv4', rollc_lev4)
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and rollc_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (rollc_lev4==0):
                            if (rollc_lev3==0):
                                if (rollc_lev2==0):
                                    if (rollc_lev1==0):
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('rollc_lev1', 'rollc_stby_lv1', rollc_lev1)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('rollc_lev2', 'rollc_stby_lv2', rollc_lev2)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                prod_action('rollc_lev3', 'rollc_stby_lv3', rollc_lev3)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            prod_action('rollc_lev4', 'rollc_stby_lv4', rollc_lev4)                
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                        # 작업 역방향 끝

            
            elif pix_prod == pix_bread:
                pix_error_count = 0
                print('bread!')
                if not bProdHigh or bread_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (bread_lev1==0) and not bbreadcompleted:
                        if not prod_action('bread_lev1', 'bread_stby_lv1', bread_lev1):
                            if (bread_lev2==0):
                                bbreadcompleted = True
                            if not (bread_lev2==0) and not bbreadcompleted:
                                if not prod_action('bread_lev2', 'bread_stby_lv2', bread_lev2):
                                    if (bread_lev3==0):
                                        bbreadcompleted = True
                                    if not (bread_lev3==0) and not bbreadcompleted:
                                        if not prod_action('bread_lev3', 'bread_stby_lv3', bread_lev3):
                                            if (bread_lev4==0):
                                                bbreadcompleted = True
                                            if not (bread_lev4==0) and not bbreadcompleted:
                                                Updown('up')
                                                if not prod_action('bread_lev4', 'bread_stby_lv4', bread_lev4):
                                                    if (bread_lev5==0):
                                                        bbreadcompleted = True
                                                    if not (bread_lev5==0) and not bbreadcompleted:
                                                        Updown('up')
                                                        if not prod_action('bread_lev5', 'bread_stby_lv5', bread_lev5):
                                                            if (bread_lev6==0):
                                                                bbreadcompleted = True
                                                            if not (bread_lev6==0) and not bbreadcompleted:
                                                                Updown('up')
                                                                if not prod_action('bread_lev6', 'bread_stby_lv6', bread_lev6):
                                                                    bbreadcompleted = True
                                                                Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or bread_num==1:
                        break
                    if bProdHigh and not bSecond and bread_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (bread_lev1==0):
                            if not prod_action('bread_lev1', 'bread_stby_lv1', bread_lev1):
                                if not (bread_lev2==0):
                                    if not prod_action('bread_lev2', 'bread_stby_lv2', bread_lev2):
                                        if not (bread_lev3==0):
                                            if not prod_action('bread_lev3', 'bread_stby_lv3', bread_lev3):
                                                if not (bread_lev4==0):
                                                    Updown('up')
                                                    if not prod_action('bread_lev4', 'bread_stby_lv4', bread_lev4):
                                                        if not (bread_lev5==0):
                                                            Updown('up')
                                                            if not prod_action('bread_lev5', 'bread_stby_lv5', bread_lev5):
                                                                if not (bread_lev6==0):
                                                                    Updown('up')
                                                                    prod_action('bread_lev6', 'bread_stby_lv6', bread_lev6)
                                                                    Skip_Next(prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                                else:
                                                                    Skip_Next(prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and bread_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (bread_lev6==0):
                            if (bread_lev5==0):
                                if (bread_lev4==0):
                                    if (bread_lev3==0):
                                        if (bread_lev2==0):
                                            prod_action('bread_lev1', 'bread_stby_lv1', bread_lev1)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('bread_lev2', 'bread_stby_lv2', bread_lev2)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('bread_lev3', 'bread_stby_lv3', bread_lev3)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown('up')
                                    prod_action('bread_lev4', 'bread_stby_lv4', bread_lev4)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                Updown('up')
                                prod_action('bread_lev5', 'bread_stby_lv5', bread_lev5)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            prod_action('bread_lev6', 'bread_stby_lv6', bread_lev6)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                    # 작업 역방향 끝

            
            elif pix_prod == pix_jampy:
                pix_error_count = 0
                print('jampy!')
                if not bProdHigh or jampy_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (jampy_lev1==0) and not bjampycompleted:
                        if not prod_action('jampy_lev1', 'jampy_stby_lv1', jampy_lev1):
                            if (jampy_lev2==0):
                                bjampycompleted = True
                            if not (jampy_lev2==0) and not bjampycompleted:
                                if not prod_action('jampy_lev2', 'jampy_stby_lv2', jampy_lev2):
                                    if (jampy_lev3==0):
                                        bjampycompleted = True
                                    if not (jampy_lev3==0) and not bjampycompleted:
                                        if not prod_action('jampy_lev3', 'jampy_stby_lv3', jampy_lev3):
                                            if (jampy_lev4==0):
                                                bjampycompleted = True
                                            if not (jampy_lev4==0) and not bjampycompleted:
                                                Updown('up')
                                                if not prod_action('jampy_lev4', 'jampy_stby_lv4', jampy_lev4):
                                                    if (jampy_lev5==0):
                                                        bjampycompleted = True
                                                    if not (jampy_lev5==0) and not bjampycompleted:
                                                        Updown('up')
                                                        if not prod_action('jampy_lev5', 'jampy_stby_lv5', jampy_lev5):
                                                            if (jampy_lev6==0):
                                                                bjampycompleted = True
                                                            if not (jampy_lev6==0) and not bjampycompleted:
                                                                Updown('up')
                                                                if not prod_action('jampy_lev6', 'jampy_stby_lv6', jampy_lev6):
                                                                    bjampycompleted = True
                                                                Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or jampy_num==1:
                        break
                    if bProdHigh and not bSecond and jampy_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (jampy_lev1==0):
                            if not prod_action('jampy_lev1', 'jampy_stby_lv1', jampy_lev1):
                                if not (jampy_lev2==0):
                                    if not prod_action('jampy_lev2', 'jampy_stby_lv2', jampy_lev2):
                                        if not (jampy_lev3==0):
                                            if not prod_action('jampy_lev3', 'jampy_stby_lv3', jampy_lev3):
                                                if not (jampy_lev4==0):
                                                    Updown('up')
                                                    if not prod_action('jampy_lev4', 'jampy_stby_lv4', jampy_lev4):
                                                        if not (jampy_lev5==0):
                                                            Updown('up')
                                                            if not prod_action('jampy_lev5', 'jampy_stby_lv5', jampy_lev5):
                                                                if not (jampy_lev6==0):
                                                                    Updown('up')
                                                                    prod_action('jampy_lev6', 'jampy_stby_lv6', jampy_lev6)
                                                                    Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and jampy_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (jampy_lev6==0):
                            if (jampy_lev5==0):
                                if (jampy_lev4==0):
                                    if (jampy_lev3==0):
                                        if (jampy_lev2==0):
                                            prod_action('jampy_lev1', 'jampy_stby_lv1', jampy_lev1)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('jampy_lev2', 'jampy_stby_lv2', jampy_lev2)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('jampy_lev3', 'jampy_stby_lv3', jampy_lev3)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown('up')
                                    prod_action('jampy_lev4', 'jampy_stby_lv4', jampy_lev4)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                Updown('up')
                                prod_action('jampy_lev5', 'jampy_stby_lv5', jampy_lev5)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            prod_action('jampy_lev6', 'jampy_stby_lv6', jampy_lev6)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                    # 작업 역방향 끝
                
            
            elif pix_prod == pix_doye:
                pix_error_count = 0
                print('doye!')
                if not bProdHigh or doye_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (doye_lev1==0) and not bdoyecompleted:
                        if not prod_action('doye_lev1', 'doye_stby_lv1', doye_lev1):
                            if (doye_lev2==0):
                                bdoyecompleted = True
                                Skip_Next(prod_direction_left)
                            if not (doye_lev2==0) and not bdoyecompleted:
                                if not prod_action('doye_lev2', 'doye_stby_lv2', doye_lev2):
                                    if (doye_lev3==0):
                                        bdoyecompleted = True
                                        Skip_Next(prod_direction_left)
                                    if not (doye_lev3==0) and not bdoyecompleted:
                                        if not prod_action('doye_lev3', 'doye_stby_lv3', doye_lev3):
                                            if (doye_lev4==0):
                                                bdoyecompleted = True
                                                Skip_Next(prod_direction_left)
                                            if not (doye_lev4==0) and not bdoyecompleted:
                                                Updown('up')
                                                if not prod_action('doye_lev4', 'doye_stby_lv4', doye_lev4):
                                                    bdoyecompleted = True
                                                Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or doye_num==1:
                        break
                    if bProdHigh and not bSecond and doye_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (doye_lev1==0):
                            if not prod_action('doye_lev1', 'doye_stby_lv1', doye_lev1):
                                if not (doye_lev2==0):
                                    if not prod_action('doye_lev2', 'doye_stby_lv2', doye_lev2):
                                        if not (doye_lev3==0):
                                            if not prod_action('doye_lev3', 'doye_stby_lv3', doye_lev3):
                                                if not (doye_lev4==0):
                                                    Updown('up')
                                                    prod_action('doye_lev4', 'doye_stby_lv4', doye_lev4)
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and doye_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (doye_lev4==0):
                            if (doye_lev3==0):
                                if (doye_lev2==0):
                                    if (doye_lev1==0):
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('doye_lev1', 'doye_stby_lv1', doye_lev1)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('doye_lev2', 'doye_stby_lv2', doye_lev2)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                prod_action('doye_lev3', 'doye_stby_lv3', doye_lev3)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            prod_action('doye_lev4', 'doye_stby_lv4', doye_lev4)                
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                        # 작업 역방향 끝

            
            elif pix_prod == pix_flower:
                pix_error_count = 0
                print('flower!')
                if not bProdHigh or flower_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (flower_lev1==0) and not bflowercompleted:
                        if not prod_action('flower_lev1', 'flower_stby_lv1', flower_lev1):
                            if (flower_lev2==0):
                                bflowercompleted = True
                                Skip_Next(prod_direction_left)
                            if not (flower_lev2==0) and not bflowercompleted:
                                if not prod_action('flower_lev2', 'flower_stby_lv2', flower_lev2):
                                    if (flower_lev3==0):
                                        bflowercompleted = True
                                        Skip_Next(prod_direction_left)
                                    if not (flower_lev3==0) and not bflowercompleted:
                                        if not prod_action('flower_lev3', 'flower_stby_lv3', flower_lev3):
                                            if (flower_lev4==0):
                                                bflowercompleted = True
                                                Skip_Next(prod_direction_left)
                                            if not (flower_lev4==0) and not bflowercompleted:
                                                Updown('up')
                                                if not prod_action('flower_lev4', 'flower_stby_lv4', flower_lev4):
                                                    if (flower_lev5==0):
                                                        bflowercompleted = True
                                                        Skip_Next(prod_direction_left)
                                                    if not (flower_lev5==0) and not bflowercompleted:
                                                        Updown('up')
                                                        if not prod_action('flower_lev5', 'flower_stby_lv5', flower_lev5):
                                                            if (flower_lev6==0):
                                                                bflowercompleted = True
                                                                Skip_Next(prod_direction_left)
                                                            if not (flower_lev6==0) and not bflowercompleted:
                                                                Updown('up')
                                                                if not prod_action('flower_lev6', 'flower_stby_lv6', flower_lev6):
                                                                    bflowercompleted = True
                                                                Skip_Next(prod_direction_left)
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                else:
                                                    Skip_Next(prod_direction_left)
                                            else:
                                                Skip_Next(prod_direction_left)
                                        else:
                                            Skip_Next(prod_direction_left)
                                    else:
                                        Skip_Next(prod_direction_left)
                                else:
                                    Skip_Next(prod_direction_left)
                            else:
                                Skip_Next(prod_direction_left)
                        else:
                            Skip_Next(prod_direction_left)
                    else:
                        Skip_Next(prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or flower_num==1:
                        break
                    if bProdHigh and not bSecond and flower_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (flower_lev1==0):
                            if not prod_action('flower_lev1', 'flower_stby_lv1', flower_lev1):
                                if not (flower_lev2==0):
                                    if not prod_action('flower_lev2', 'flower_stby_lv2', flower_lev2):
                                        if not (flower_lev3==0):
                                            if not prod_action('flower_lev3', 'flower_stby_lv3', flower_lev3):
                                                if not (flower_lev4==0):
                                                    Updown('up')
                                                    if not prod_action('flower_lev4', 'flower_stby_lv4', flower_lev4):
                                                        if not (flower_lev5==0):
                                                            Updown('up')
                                                            if not prod_action('flower_lev5', 'flower_stby_lv5', flower_lev5):
                                                                if not (flower_lev6==0):
                                                                    Updown('up')
                                                                    prod_action('flower_lev6', 'flower_stby_lv6', flower_lev6)
                                                                    Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                            else:
                                                                Skip_Next(prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and flower_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (flower_lev6==0):
                            if (flower_lev5==0):
                                if (flower_lev4==0):
                                    if (flower_lev3==0):
                                        if (flower_lev2==0):
                                            prod_action('flower_lev1', 'flower_stby_lv1', flower_lev1)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('flower_lev2', 'flower_stby_lv2', flower_lev2)
                                            Skip_Next(prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('flower_lev3', 'flower_stby_lv3', flower_lev3)
                                        Skip_Next(prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown('up')
                                    prod_action('flower_lev4', 'flower_stby_lv4', flower_lev4)
                                    Skip_Next(prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown('up')
                                Updown('up')
                                prod_action('flower_lev5', 'flower_stby_lv5', flower_lev5)
                                Skip_Next(prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown('up')
                            Updown('up')
                            Updown('up')
                            prod_action('flower_lev6', 'flower_stby_lv6', flower_lev6)
                            Skip_Next(prod_direction_left)
                            bSecond = False
                            break
                    # 작업 역방향 끝

            
            elif pix_prod == pix_milky:
                pix_error_count = 0
                print('milky!')
                if not bmilkycompleted:
                    print('생산 확인...')
                    if not three_prod_action('milky_stby_lv1','milky_stby_lv2','milky_stby_lv3',milky_lev1,milky_lev2,milky_lev3, prod_direction_left):
                        bmilkycompleted = True
                else:
                    Skip_Next(prod_direction_left)

            
            elif pix_prod == pix_latte:
                pix_error_count = 0
                print('latte!')
                if not blattecompleted:
                    print('생산 확인...')
                    if not three_prod_action('latte_stby_lv1','latte_stby_lv2','latte_stby_lv3',latte_lev1,latte_lev2,latte_lev3, prod_direction_left):
                        blattecompleted = True
                else:
                    Skip_Next(prod_direction_left)


            elif pix_prod == pix_dolls:
                pix_error_count = 0
                print('dolls!')
                if not bdollcompleted:
                    print('생산 확인...')
                    if not three_prod_action('dolls_stby_lv1','dolls_stby_lv2','dolls_stby_lv3',dolls_lev1,dolls_lev2,dolls_lev3, prod_direction_left):
                        bdollcompleted = True
                else:
                    Skip_Next(prod_direction_left)
                
            
            elif pix_prod == pix_beer:
                pix_error_count = 0
                print('beer!')
                if not bbeercompleted:
                    print('생산 확인...')
                    if not three_prod_action('beer_stby_lv1','beer_stby_lv2','beer_stby_lv3',beer_lev1,beer_lev2,beer_lev3, prod_direction_left):
                        bbeercompleted = True
                else:
                    Skip_Next(prod_direction_left)
                

            elif pix_prod == pix_muffin:
                pix_error_count = 0
                print('muffin!')
                if not bmuffincompleted:
                    print('생산 확인...')
                    if not three_prod_action('muffin_stby_lv1','muffin_stby_lv2','muffin_stby_lv3',muffin_lev1,muffin_lev2,muffin_lev3, prod_direction_left):
                        bmuffincompleted = True
                else:
                    Skip_Next(prod_direction_left)
                
            
            elif pix_prod == pix_jewel:
                pix_error_count = 0
                print('jewel!')
                if not bjewelcompleted:
                    print('생산 확인...')
                    if not three_prod_action('jewel_stby_lv1','jewel_stby_lv2','jewel_stby_lv3',jewel_lev1,jewel_lev2,jewel_lev3, prod_direction_left):
                        bjewelcompleted = True
                else:
                    Skip_Next(prod_direction_left)
                

            elif (kkd_start):
                print('[생산중] 계정 튕김! 쿠킹덤을 실행합니다!')
                # 실행 체크
                # Check_Initiating()
                Kingdom_ready('kkd_out')
                #건물에 들어가기..
                Enter_Building()
            
            elif (lack_of_material):
                print('아이템이 부족하대요~ 다음으로 넘어갑니다아~')
                click(629,169)
                time.sleep(0.5)
                click(164,280)
                time.sleep(0.5)
            
            
            elif not Kingdom_ready('prod_in'):
                print('설마 여기 도나')
                Enter_Building()
            
            else:
                pix_error_count = pix_error_count + 1
                if prod_pix_confirm >= pix_error_count:
                    print('건물 안에서... 픽셀값 찾게 위로 올림')
                    for i in range(2):
                        prod_clock = LocateCenterOnScreenshot('prod_clock', 0.76)
                        if (prod_clock):
                            x_start, y_start = prod_clock[0], prod_clock[1]
                        else:
                            x_start, y_start = 610, 150
                        Drag(x_start, y_start, x_start, 540, 1)
                        time.sleep(1)
                else:
                    print('건물 안에서... 이게 아니라면... 우선 좌클릭')
                    click(158,279)
                    time.sleep(1)

            print('이 밖인가')
        




end = time.time()
print('총 매크로 동작 시간은 =', end-macro_start)