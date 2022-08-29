from abc import abstractproperty
from cgitb import text
from glob import glob
from re import A
import string
from PIL.ImageOps import grayscale
import pyautogui as pag
import time
import keyboard
from PIL import Image
from PIL import ImageGrab
from pyscreeze import pixel
from pytesseract import *
import pytesseract
from pytesseract.pytesseract import TesseractNotFoundError, image_to_string, kill
import cv2
import numpy as np
import random

# //// 여기부턴 조건 확인용
bWood_Quick = False         # 나무 쾌속생산!
bJelbean_Quick = False      # 젤리빈 쾌속생산!
bSugar_Quick = False        # 각설탕 쾌속생산!
bSmith_Quick = False        # 대장간 쾌속생산!
bJelbean_Quick = False      # 잼가게 쾌속생산!
bRollc_Quick = False        # 공작소 쾌속생산!
bTropicalAction_A = True    # 트로피칼 A 계정 돌릴거냐
bTropicalAction_B = True    # 트로피칼 B 계정 돌릴거냐
bResearch_auto_A = True     # 연구소 자동돌림(명확히 지정해줘야만 함..)
bResearch_auto_B = True     # 연구소 자동돌림(명확히 지정해줘야만 함..)
jjokji_limit_A = False       # 쪽지 제한 걸기(오늘 보상 다 받으면 끝냄)
jjokji_limit_B = True       # 쪽지 제한 걸기(오늘 보상 다 받으면 끝냄)
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

# -------------------------계정별 조건-------------------------
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
magic_lev3_A = 20    # 향기로운 포도주스
magic_lev4_A = 20    # 칼슘 튼튼 우유 
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

icecream_num_A = 2  # 아이스크림 트럭 건물 수
icecream_lev1_A = 20  # 낮의 별가루 스프링클 아이스크림
icecream_lev2_A = 30  # 밤의 별가루 스프링클 아이스크림
icecream_lev3_A = 30  # 꿈꾸는 성의 아이스크림 바닐라 샌드
icecream_lev4_A = 30  # 꿈꾸는 성의 아이스크림 초코 샌드
icecream_lev5_A = 30  # 밀키웨이 아이스바
to_do_list_A = list()       # 할거

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
jelly_lev4_B = 60      # 석류 잼
jelly_lev5_B = 0      # 톡톡베리 잼

rollc_num_B = 2           #롤케이크 건물 수
rollc_lev1_B = 200       # 솔방울새 인형
rollc_lev2_B = 200       # 도토리 램프
rollc_lev3_B = 80       # 뻐꾹뻐꾹 시계
rollc_lev4_B = 80       # 백조깃털 드림캐처

bread_num_B = 2           # 빵집 건물 수
bread_lev1_B = 140      # 든든한 호밀빵
bread_lev2_B = 120      # 달콤쫀득 잼파이
bread_lev3_B = 120      # 은행 포카치아
bread_lev4_B = 80      # 슈가코팅 도넛
bread_lev5_B = 80      # 폭신 카스테라
bread_lev6_B = 0      # 골드리치 크로와상

jampy_num_B = 2           # 잼파이 건물 수
jampy_lev1_B = 160      # 따끈따끈 젤리스튜
jampy_lev2_B = 140      # 곰젤리 버거
jampy_lev3_B = 100      # 캔디크림 파스타
jampy_lev4_B = 110      # 폭신폭신 오므라이스
jampy_lev5_B = 0      # 콤비네이션 피자젤리
jampy_lev6_B = 0      # 고급스러운 젤리빈 정식

doye_num_B = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_B = 200       # 비스킷 화분
doye_lev2_B = 200       # 반짝반짝 유리판
doye_lev3_B = 200       # 반짝이는 색동구슬
doye_lev4_B = 60       # 무지갯빛 디저트 보울

flower_num_B = 2          # 꽃가게 건물 수
flower_lev1_B = 200      # 캔디꽃
flower_lev2_B = 220      # 행복한 꽃화분
flower_lev3_B = 200      # 캔디꽃다발
flower_lev4_B = 60      # 롤리팝 꽃바구니
flower_lev5_B = 40      # 유리꽃 부케
flower_lev6_B = 0      # 찬란한 요거트 화환

milky_num_B = 2           # 우유 가공소 건물 수
milky_lev1_B = 200      # 크림
milky_lev2_B = 60      # 버터
milky_lev3_B = 40      # 수제 치즈

latte_num_B = 2         # 라떼 건물 수
latte_lev1_B = 200      # 젤리빈 라떼
latte_lev2_B = 60      # 몽글몽글 버블티
latte_lev3_B = 0      # 스윗베리 에이드

dolls_num_B = 2         # 러블리 인형공방 건물 수
dolls_lev1_B = 100      # 구름사탕 쿠션
dolls_lev2_B = 80      # 곰젤리 솜인형
dolls_lev3_B = 0      # 용과 드래곤 솜인형

beer_num_B = 2          # 오크통 쉼터 건물 수
beer_lev1_B = 40      # 크림 루트비어
beer_lev2_B = 60      # 레드베리 주스
beer_lev3_B = 50      # 빈티지 와일드 보틀

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

icecream_num_B = 2  # 아이스크림 트럭 건물 수
icecream_lev1_B = 20  # 낮의 별가루 스프링클 아이스크림
icecream_lev2_B = 30  # 밤의 별가루 스프링클 아이스크림
icecream_lev3_B = 30  # 꿈꾸는 성의 아이스크림 바닐라 샌드
icecream_lev4_B = 30  # 꿈꾸는 성의 아이스크림 초코 샌드
icecream_lev5_B = 30  # 밀키웨이 아이스바
to_do_list_B = list()       # 할거
# -----------------------------------------------------------

# 글로벌 조건 입력하는 곳(어느 곳이든 동일)
# ----------- 전체 조건 -------------
easy_prod = 0.7                 # 1시간 이내 제품
normal_prod = 0.9               # 1~2시간 제품
hard_prod = 0.95                # 2시간 초과
# 킹덤패스
bReward = (121, 207, 16)        # 모두 받기 활성화
pix_pass_reward_exist = (255, 0, 0)

# 건물 내부 색상
pix_wood = (117, 59, 40)        # 나무
pix_jelbean = (4, 239, 237)     # 젤리빈
pix_white = (255, 255, 255)     # 설탕
pix_biscuit = (205, 132, 63)    # 비스킷
pix_berry = (187, 40, 44)       # 젤리베리
pix_milk = (236, 241, 241)      # 우유
pix_cotton = (255, 247, 255)    # 솜
pix_smith = (163, 118, 85)      # 도끼 스미스
pix_jelly = (15, 174, 202)      # 젤리빈 잼 젤리
pix_rollc = (214, 146, 105)     # 솔새 롤케
pix_rollc_d = (237, 197, 122)   # 솔새 롤케 내린 상태
pix_bread = (142, 66, 8)        # 호밀빵 브레드
pix_bread_d = (242, 223, 195)   # 빵집 내린 상태
pix_jampy = (168, 29, 42)       # 젤리스튜 잼파이
pix_jampy_d = (171, 183, 59)    # 젤리스튜 내린 상태
pix_doye = (157, 84, 43)        # 비스킷 화분 - 도예
pix_doye_d = (183, 177, 249)    # 도예 내린 상태
pix_flower = (255, 30, 130)     # 캔디꽃 - flower
pix_flower_d = (211, 136, 227)  # 꽃가게 내린 상태
pix_milky = (213, 229, 234)     # 크림 - milky
pix_latte = (255, 251, 238)     # 젤리빈 라떼 - latte
pix_dolls = (109, 235, 249)     # 쿠션 - dolls
pix_beer = (153, 103, 67)       # 크림루트비어 - beer
pix_muffin = (190, 92, 59)      # 머핀 - muffin
pix_jewel = (143, 99, 63)       # 글레이즈드링 - jewel
pix_magic = (93, 55, 48)        # 마법공방 - magic
pix_icecream = (254, 253, 229)  # 디즈니 아이스크림 트럭
pix_icecream_d = (225, 161, 92) # 아이스크림 내린 상태
pix_status_in = (227, 163, 2)   # 생산건물 내 07.31. 수정
pix_status_in_dark = (113, 81, 1)   # 건물 안이긴 한데 창이 떠있음
pix_status_in_magic_dark = (109, 81, 9)     # 마법공방이고 생산품 보상이 떠있음

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
pix_status_lotto = (255, 208, 2)  # 뽑기, 해변교역소
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

# 그 외, 기타, 차이점, 미사용
pix_stats_kkd_start = (11, 10, 42) # 바탕화면 나갔네
pix_status_arena_lobby = (197, 196, 194) # 아레나 로비화면!
pix_status_boldline_yes = (13, 16, 48)
pix_status_temple = (177, 123, 153) # 찬란한 영웅들의 신전 대기화면, 석상화면 같음
pix_status_temple_dark = (88, 61, 76) # 찬란한 영웅들의 신전 화면 어두워졌을 때(슬롯 확장 잘못누름)

prod_build_num_list = ('몰라요', '나무', '젤리빈', '각설탕', '비스킷', '젤리베리', '우유', '솜', '대장간', '잼가게', '공작소', '빵집', '잼파이', '도예', '꽃가게', '우유 가공소', '라떼', '인형공방', '오크통 쉼터', '퐁 드 파티세리', '살롱 드 주얼리', '마법공방', '아이스크림')
prod_build_prod_max = (0,3,3,3,3,3,3,3,7,5,4,6,6,4,6,3,3,3,3,3,3,14,5)
prod_build_number = (0,3,3,3,3,3,3,11,7,5,6,6,4,6,3,3,3,3,3,3,14,5)
prod_build_now = 0  # 초기값 : 몰라요
# ----------------------------------



def del_duplication_clock(dif, list_origin):
    del_list = list()
    if len(list_origin) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
        for i in range(len(list_origin)-1):
            for j in range(len(list_origin)-1-i):
                # if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif and abs(int(list_origin[i][1])-int(list_origin[i+1+j][1])) < dif:
                if abs(int(list_origin[i][1])-int(list_origin[i+1+j][1])) < dif:
                    del_list.append(list_origin[i])
                if list_origin[i][1] == list_origin[i+1+j][1]:
                    del_list.append(list_origin[i])
    list_origin = [x for x in list_origin if x not in del_list]
    return list_origin

def While_True_Condition(account, start_time, max_act_time):  # Ture:정상상태(다음 동작 가능), False:이상상태(다음 동작 안함-최대시간 초과 등)
    now_time = time.time()
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440 + (account // 2) * 960,363 + (account % 2) * 540,43,29))
    cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2 + (account // 2) * 960,32 + (account % 2) * 540,917,505))
    if start_time - now_time > max_act_time:
        End_kkd(account)                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
        Kingdom_ready(account,'kkd_out')            # 재부팅
        return False
    elif keyboard.is_pressed('end'):
        return False
    elif (cond_network):
        pag.click(462 + random.randint(-5,5) + (account // 2) * 960,377 + random.randint(-5,5) + (account % 2) * 540)
        time.sleep(0.3)
    elif (cond_halted):
        pag.click(740 + (account // 2) * 960,310 + (account % 2) * 540)
        End_kkd(account)
        Kingdom_ready(account,'kkd_out')            # 재부팅
    else:
        return True
def Account_Change():
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

    global icecream_lev1
    global icecream_lev2
    global icecream_lev3
    global icecream_lev4
    global icecream_lev5
    global icecream_num
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
        print('A조건으로 변경')
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

        icecream_lev1 = icecream_lev1_A
        icecream_lev2 = icecream_lev2_A
        icecream_lev3 = icecream_lev3_A
        icecream_lev4 = icecream_lev4_A
        icecream_lev5 = icecream_lev5_A
        icecream_num = icecream_num_A
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
        account = 0
        print('B조건으로 변경')
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
        icecream_lev1 = icecream_lev1_B
        icecream_lev2 = icecream_lev2_B
        icecream_lev3 = icecream_lev3_B
        icecream_lev4 = icecream_lev4_B
        icecream_lev5 = icecream_lev5_B
        icecream_num = icecream_num_B        
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
        print('계정 3은 이곳에 추가')
    return

# confidence에 따라서 숫자 잘못읽는 경우가 있어 전체 조정하는 tot_confidence 추가..
def numb_new_recog(prod_pin, line):
    its_number = 0
    tot_confidence = 0.83
    how_many_nums = 0
    pos_numb = 0        # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
    num_list = list()
    print('라인 %s번 진행합니다!'%(line))
    screen = ImageGrab.grab()
    # 3렙 건물인 경우 무조건 prod_pin = (612,95)
    pix_jaritsu1_1 = screen.getpixel((prod_pin[0]+19,prod_pin[1]+81+153*(line-1))) # 상
    pix_jaritsu1_2 = screen.getpixel((prod_pin[0]+19,prod_pin[1]+87+153*(line-1))) # 하
    if ((pix_jaritsu1_1) == (255, 255, 255)) and ((pix_jaritsu1_2) == (255, 255, 255)):
        pix_zero_1 = screen.getpixel((prod_pin[0]+24,prod_pin[1]+82+153*(line-1))) # 상
        pix_zero_2 = screen.getpixel((prod_pin[0]+24,prod_pin[1]+85+153*(line-1))) # 하
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
        pix_jaritsu2_1 = screen.getpixel((prod_pin[0]+14,prod_pin[1]+81+153*(line-1))) # 상
        pix_jaritsu2_2 = screen.getpixel((prod_pin[0]+14,prod_pin[1]+81+153*(line-1))) # 하
        if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
            # print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            # print('이 숫자는 세 자릿 수 입니다!')
            pos_numb = 3
    # print('자릿수 다시 확인', pos_numb)
    if pos_numb == 1:
        # print('한 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_1):
            return 1
        num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_1_1):
            return 1
        num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_2):
            return 2
        num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_3):
            return 3
        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_3_1):
            return 3
        num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_4):
            return 4
        num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_4_2):
            return 4
        num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_5):
            return 5
        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_6):
            return 6
        num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_7):
            return 7
        num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_8):
            return 8
        num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_8_1):
            return 8
        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_9):
            return 9
        num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_9_1):
            return 9
        return 0
        
    if pos_numb == 2:
        # print('두 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),10,14)
        # 10의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                print('십의 자리 숫자 확인 에러!!')
        # 1의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                print('일의 자리 숫자 확인 에러!!')
        return its_number
    if pos_numb == 3:
        # print('세 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 900
                                                            else:
                                                                print('백의 자리 숫자 확인 에러!!')
        # 10의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=tot_confidence, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                                if (num_0):
                                                                    print('십의 자리 0!!')
                                                                else:
                                                                    print('10의 자리 못읽음..')
        # 1의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=tot_confidence, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                                if (num_0):
                                                                    print('1의 자리 0!!')
                                                                else:
                                                                    print('1의 자리 못읽음..')
        return its_number


def Building_Num_Check(account):
    start_time = time.time()
    max_act_time = 180
    pix_error_count = 0
    while True:
        if not While_True_Condition(account, start_time, max_act_time):
            return 0
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605 + (account // 2) * 960,55 + (account % 2) * 540)) # 상단골드
        pix_prod = screen.getpixel((610 + (account // 2) * 960,140 + (account % 2) * 540))   # 생산품 이미지 확인
        in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8, region=(2 + (account // 2) * 960,32 + (account % 2) * 540,917,505))             # 건물 안
        
        if pix_status == pix_status_in or (in_pos):   # 건물 안 ok
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
                print('smith!')
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
                pag.moveTo(610 + (account // 2) * 960,random.randint(140,160) + (account % 2) * 540)
                time.sleep(0.1)
                pag.mouseDown()
                time.sleep(0.1)
                pag.moveTo(610 + (account // 2) * 960,160+350 + (account % 2) * 540,0.3)
                pag.mouseUp()
                time.sleep(2)
                pix_error_count = pix_error_count + 1
                if pix_error_count == 2:
                    return 0
        else:
            print('건물 안이 아니다!')
            Enter_Building(account)

def Building_Moving(account,want_to_go):
    start_time_bn = time.time()
    bDirection_Confirm = False  # 어디로 이동할 지 결정했니
    prod_direction_left = False # 시작은 우측부터..
    while True:
        if not While_True_Condition(account, start_time_bn, 180):
            print('동작 최대시간 초과 or End버튼 누름')
            return
        
        prod_build_now = Building_Num_Check(account)
        if prod_build_now == 0:
            print('왜 못찾는겨!!')
            prod_build_now = Building_Num_Check(account)
        
        print('현재 건물은:',prod_build_num_list[prod_build_now])
        time.sleep(0.5)
        
        # 건물 안, 좌/우 조건 확인 전
        if prod_build_now == want_to_go:
            print('여기!',prod_direction_left)
            # 첫 건물에 찾고, 그 건물 개수가 2개인 경우가 나무밖에 없나?
            return prod_direction_left
        else:
            if bDirection_Confirm:
                Skip_Next(account, prod_direction_left)
            else:   # 어디로 움직일 지 확정 했으면 걍 그쪽으로 쭉-
                Move_Right_Count = want_to_go - prod_build_now # 우측으로 갈 때
                if Move_Right_Count < 0:
                    Move_Right_Count = Move_Right_Count + 22
                print('우로 가려면',Move_Right_Count)
                if Move_Right_Count < 11:  # 우측 가는 게 10번 이하면 우측으로
                    print('우측 이동')
                    prod_direction_left = False
                else:
                    print('좌측 이동')  # 우측 가는 게 11번 이상이면 좌측으로
                    prod_direction_left = True
                bDirection_Confirm = True

def Updown_Confidence(account, updown):
    if updown == 'up':
        pag.moveTo(610 + (account // 2) * 960,530 + (account % 2) * 540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610 + (account // 2) * 960,530 + (account % 2) * 540 - 153*3,2)  # 딱 맞게 이동..이지만 그럴리 없지
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(1)
    if updown == 'down':
        pag.moveTo(610 + (account // 2) * 960,100 + (account % 2) * 540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610 + (account // 2) * 960,100 + (account % 2) * 540 + 400,2)    # 딱 맞게 이동..이지만 그럴리 없지
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(1)

    start_time_bn = time.time()
    while True:
        print('정교 위치 체크중...')
        if not While_True_Condition(account, start_time_bn, 20):
            print('동작 최대시간 초과 or End버튼 누름')
            return
        # 두 번째 시계
        time.sleep(0.5)
        prod_clock = pag.locateCenterOnScreen('prod_clock.png',confidence=0.8, region=(554 + (account // 2) * 960,198 + (account % 2) * 540,20,153))
        # y좌표 208이 원래 제일 위. 맨 아랫칸으로 가면 215. 225쯤 되면 맨 아래 짤림
        if (prod_clock):
            print('prod_clock',prod_clock)
            if 216 + (account % 2) * 540 > prod_clock[1] > 200 + (account % 2) * 540:
                print('오우예')
                return
            else:
                pag.moveTo(prod_clock)
                pag.mouseDown()
                time.sleep(0.2)
                pag.moveTo(prod_clock[0],prod_clock[1]-20,1)   # 한 번 움직여보고
                pag.moveTo(prod_clock[0],prod_clock[1],1)   # 두 번 움직여보고
                time.sleep(1)
                prod_clock_new = pag.locateCenterOnScreen('prod_clock.png',confidence=0.8, region=(554 + (account // 2) * 960,198 + (account % 2) * 540,20,153))
                if (prod_clock_new):    # 새 위치 찾아서
                    print('prod_clock_new',prod_clock_new)
                    if 212 + (account % 2) * 540 > prod_clock_new[1] > 204 + (account % 2) * 540:
                        print('오우예')
                        pag.mouseUp()
                        return
                    else:
                        pag.moveTo(prod_clock[0],prod_clock[1] + (208 + (account % 2) * 540 - prod_clock_new[1]),2)   # 현재 마우스 위치에서 목표(y:208까지의 차이값 만큼 빼줌)
                time.sleep(1)
                pag.mouseUp()
        else:
            print('왜 못찾냐 시계를...')
            return

def new_prod_check(account, Active_Line1, Active_Line2, Active_Line3):
    # 3개인 경우 다 체크.
    # How_Many_From_Back = 3이면 다 체크, 2면 2,3번 체크, 1이면 3번만 체크
    prod_clock = pag.locateAllOnScreen('prod_clock.png',confidence=0.85, region=(2 + (account // 2) * 960,32 + (account % 2) * 540,917,505))
    if (prod_clock):
        list_clock = list()
        for p in prod_clock:
            ctr = pag.center(p)
            list_clock.append(ctr)
    else:
        print('시계 3개 못찾음!!!')
        return False
    list_clock = del_duplication_clock(3, list_clock)
    print('list_clock',list_clock)
    list_return = list()
    if Active_Line1:
        list_return.append(numb_new_recog((list_clock[0][0]+48,list_clock[0][1]-113),1))

    if Active_Line2:
        list_return.append(numb_new_recog((list_clock[1][0]+48,list_clock[1][1]-113),1))

    if Active_Line3:
        list_return.append(numb_new_recog((list_clock[2][0]+48,list_clock[2][1]-113),1))
    return list_return

def All_Prod_Num_Check(account):
    # 아.. 픽셀 _d 못쓰겠네.. 올려야 1렙부터 확인이구나
    start_time_bn = time.time()
    for want_to_go in range(8,23):
        if not While_True_Condition(account, start_time_bn, 180):
            print('동작 최대시간 초과 or End버튼 누름')
            return
        Building_Moving(account,want_to_go)     # 원하는 건물로 이동해써
        # its_max_lev = prod_build_prod_max[i]    # 최고렙까지 재고 파악해(열든 안열었든이군..)
        its_list = new_prod_check(account, 1, 1, 1)
        if want_to_go == 8: # 대장간
            Stock_8 = its_list
            Updown_Confidence(account, 'up')
            Stock_8 = Stock_8 + new_prod_check(account, 1, 1, 1)
            Updown_Confidence(account, 'up')
            Stock_8 = Stock_8 + new_prod_check(account, 1, 0, 0)
        if want_to_go == 9: # 잼가게
            Stock_9 = its_list
            Updown_Confidence(account, 'up')
            Stock_9 = Stock_9 + new_prod_check(account, 0, 1, 1)
        if want_to_go == 10: # 공작소
            Stock_10 = its_list
            Updown_Confidence(account, 'up')
            Stock_10 = Stock_10 + new_prod_check(account, 0, 0, 1)
        if want_to_go == 11: # 빵집
            Stock_11 = its_list
            Updown_Confidence(account, 'up')
            Stock_11 = Stock_11 + new_prod_check(account, 1, 1, 1)
        if want_to_go == 12: # 레스토랑
            Stock_12 = its_list
            Updown_Confidence(account, 'up')
            Stock_12 = new_prod_check(account, 1, 1, 1)
        if want_to_go == 13: # 도예
            Stock_13 = its_list
            Updown_Confidence(account, 'up')
            Stock_13 = Stock_13 + new_prod_check(account, 0, 0, 1)
        if want_to_go == 14: # 꽃가게
            Stock_14 = its_list
            Updown_Confidence(account, 'up')
            Stock_14 = Stock_14 + new_prod_check(account, 1, 1, 1)
        if want_to_go == 15: # 우유 가공소
            Stock_15 = its_list
        if want_to_go == 16: # 카페라떼
            Stock_16 = its_list
        if want_to_go == 17: # 인형
            Stock_17 = its_list
        if want_to_go == 18: # 비어
            Stock_18 = its_list
        if want_to_go == 19: # 머핀
            Stock_19 = its_list
        if want_to_go == 20: # 주얼리
            Stock_20 = its_list
        if want_to_go == 21: # 매직;;; 다 해야하나
            Stock_21 = its_list
            Updown_Confidence(account, 'up')
            Stock_21 = Stock_21 + new_prod_check(account, 1, 1, 1)   # 4,5,6
            Updown_Confidence(account, 'up')
            Stock_21 = Stock_21 + new_prod_check(account, 1, 1, 1)   # 7,8,9
            Updown_Confidence(account, 'up')
            Stock_21 = Stock_21 + new_prod_check(account, 1, 1, 1)   # 10,11,12
            Updown_Confidence(account, 'up')
            Stock_21 = Stock_21 + new_prod_check(account, 0, 1, 1)   # 13,14
        if want_to_go == 22: # 아스크림
            Stock_22 = its_list
            Updown_Confidence(account, 'up')
            Stock_22 = Stock_22 + new_prod_check(account, 0, 1, 1)
        
    for i in range(8,23):
        Stock_List = eval('Stock_'+str(i))
        print('%s 건물 재고 리스트는 %s 입니다.'%(prod_build_num_list[i], Stock_List))

    return

# check_start_time = time.time()
# All_Prod_Num_Check(0)
# check_end_time = time.time()
# print('재고 파악 시간 = ', check_end_time - check_start_time)


# 디즈니 이벤틋... 좀 쉬자 재고없다
bLineEnd_1 = False
bLineEnd_2 = False
bLineEnd_3 = False
iHowMany = 0
tStart_Disney = time.time()
while True:
    tNow_Disney = time.time()
    if tNow_Disney - tStart_Disney > 120:
        print('제한 시간 초과!')
        Kingdom_ready(account, 'kkd_out')
        break
    if keyboard.is_pressed('end'):
        print('end 누름')
        break

    cond_event_butak = pag.locateCenterOnScreen('cond_event_butak.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 700, 540))  # 특별한 '부탁' 인지 확인
    if not (cond_event_butak):
        cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825 + (account // 2) * 960,490 + (account % 2) * 540,45,40))    # 쿠키왕국
        if (cond_kkd_out):  # 왕국이면... 조건 추가..를 해야하남
            pag.click(45+random.randint(-5,5) + (account // 2) * 960,200+random.randint(-5,5) + (account % 2) * 540)    # 이벤트 아이콘 클릭
            time.sleep(1)
        else:   # 왕국 아니면
            cond_event_in = pag.locateCenterOnScreen('cond_event_in.png', confidence=0.95, region=(13 + (account // 2) * 960, 40 + (account % 2) * 540, 70, 30))    # 이벤트 내부?
            if (cond_event_in):
                cond_event_up = pag.locateCenterOnScreen('cond_event_up.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 700, 540))    # 이벤트 내부인데 부탁이 없다?
                if not (cond_event_up):
                    pag.moveTo(90+random.randint(-5,5) + (account // 2) * 960,140+random.randint(-5,5) + (account % 2) * 540)
                    pag.drag(0,350,2)       # 좌상에서 좌하로 350 이동
                    time.sleep(1)
                else:
                    pag.click(85+random.randint(-5,5) + (account // 2) * 960,410+random.randint(-5,5) + (account % 2) * 540)    # 좌상 끌어올렸으면 해당 이벤트 클릭
                    time.sleep(1)
            else:
                Kingdom_ready(account, 'kkd_out')
    else:
        pix_refresh = (243, 90, 28)		    # 새로고침 버튼(눌렸음)
        pix_can_give = (97, 211, 0)		    # 줄 수 있는 녹색 체크
        pix_cannot_give = (154, 154, 154)	# 줄 수 없는 회색 체크
        pix_refresh = (191, 175, 143)	    # _1 새로고침(어두워짐)
        pix_purple = (113, 88, 146) 	    # _2, _3 보라색
        pix_not_refresh = (255, 233, 191)	# _1 열려있음(밝음)
        
        for i in range(3):
            screen = ImageGrab.grab()
            # 상단
            pix_1_1 = screen.getpixel((330+228*i + (account // 2) * 960,225 + (account % 2) * 540))
            # 새로고침
            pix_1_2 = screen.getpixel((280+228*i + (account // 2) * 960,430 + (account % 2) * 540))
            # 체크박스
            pix_1_3 = screen.getpixel((390+228*i + (account // 2) * 960,430 + (account % 2) * 540))
            if pix_1_3 == pix_can_give: # 건넬 수 있고 다야나 태엽 있으면 건넴
                disney_star = pag.locateCenterOnScreen('disney_star.png', confidence=0.85, region=(215+228*i + (account // 2) * 960,465 + (account % 2) * 540,205,40))
                disney_dia = pag.locateCenterOnScreen('disney_dia.png', confidence=0.85, region=(215+228*i + (account // 2) * 960,465 + (account % 2) * 540,205,40))
                disney_quick = pag.locateCenterOnScreen('disney_dia.png', confidence=0.85, region=(215+228*i + (account // 2) * 960,465 + (account % 2) * 540,205,40))
                if (disney_star) or (disney_dia) or (disney_quick):
                    pag.click(390+228*i+random.randint(-5,5) + (account // 2) * 960,430+random.randint(-5,5) + (account % 2) * 540)
                    iHowMany = iHowMany + 1
                    time.sleep(1)
                else:   # 줄만한 거 아녀도 새로고침.. 물론.. 잘 주면 토핑까지 있겠지만
                    pag.click(280+228*i+random.randint(-5,5) + (account // 2) * 960,430+random.randint(-5,5) + (account % 2) * 540)
                    time.sleep(1)
            elif pix_1_3 == pix_cannot_give:    # 건넬 수 없으면 새로고침
                pag.click(280+228*i+random.randint(-5,5) + (account // 2) * 960,430+random.randint(-5,5) + (account % 2) * 540)
                time.sleep(1)
            else:   # 둘 다 아니면 상단 체크
                if pix_1_1 == pix_refresh:
                    print('%s번 새로고침중...'%(i+1))
                    if i == 0:
                        bLineEnd_1 = True
                    if i == 1:
                        bLineEnd_2 = True
                    if i == 2:
                        bLineEnd_3 = True
                else:
                    pag.click(330+228*i + (account // 2) * 960,225 + (account % 2) * 540) # 정확해야 해서 랜덤함수 뺌..
                    time.sleep(1)
        # if iHowMany >= 3:
        #     print('%s번 돌렸다!' % (iHowMany))
        #     pag.click(892 + (account // 2) * 960, 54 + (account % 2) * 540)
        #     time.sleep(2)
        #     Kingdom_ready(account, 'kkd_out')
        #     break
        if bLineEnd_1 and bLineEnd_2 and bLineEnd_3:
            print('다 새로고침 상태.. %s번 돌림'%(iHowMany))
            pag.click(892 + (account // 2) * 960,54 + (account % 2) * 540)
            time.sleep(4)
            Kingdom_ready(account, 'kkd_out')
            break
    time.sleep(0.5)
    
Stock_8 = [400, 120, 150, 80, 80, 80, 80]
for account in range(2):
    Lackof_Stock_8 = list()
    Account_Change()
    for i in range(7):
        print(eval('smith_lev'+str(i+1)))
        Lackof_Stock_8.extend({1-Stock_8[i]/eval('smith_lev'+str(i+1))})   # (목표-재고)/목표
    if account == 0:
        print('Account 0 = ',Lackof_Stock_8)
    if account == 1:
        print('Account 1 = ',Lackof_Stock_8)