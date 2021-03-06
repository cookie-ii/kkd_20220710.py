from re import S
from PIL.ImageOps import grayscale
import pyautogui as pag
import cv2
import time
import keyboard
from PIL import Image
from PIL import ImageGrab
from pyscreeze import pixel
from pytesseract import *
import pytesseract
from pytesseract.pytesseract import TesseractNotFoundError, image_to_string
import cv2
import numpy as np
import random
pag.FAILSAFE = False
macro_start = time.time()     # 전체 사이클 타임확인을 위한 시작시간 체크

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
bAcc_A_First = True        # 계정 먼저 시작 순서(True일 때 A부터, 아니면 B부터)
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

fountain_set_time_A = 3000  # 분수 클릭 주기
cookie_set_time_A = 3000    # 쿠키하우스 클릭 주기
fountain_set_time_B = 3000  # 분수 클릭 주기
cookie_set_time_B = 6000    # 쿠키하우스 클릭 주기
how_many_cycle = 2          # 생산 사이클
delay_to_next_account = 1   # 다음 계정 동작 전 대기시간
heart_set_num = 170          # 하트가 이 숫자보다 많으면.. 모험 실행
man_mac_time = 6000         # 수동 매크로 돌리고 파이썬 실행한 경우, 이 시간 후에 수동 매크로 끄고 자동 돌림
prod_pix_confirm = 2        # 픽셀 못읽는거 n번(스크롤업 n*2 번) 해도 안되면 좌로 넘김
jjokji_numb = 6            # 소원나무 쪽지 보내는 횟수(4개 다 짤려도 그냥 나옴)
Producting_Time = 600       # 생산 최대 시간
tShort_Term_Set = 1800      # 쑛텀 생산 시간

wood_min_A = 1300
wood_max_A = 2000
wood_prod_A = 2

jelbean_min_A = 1800
jelbean_max_A = 3000
jelbean_prod_A = 2

sugar_min_A = 1800
sugar_max_A = 3000
sugar_prod_A = 2

biscuit_min_A = -1
biscuit_max_A = 3000
biscuit_prod_A = 2

berry_min_A = -1
berry_max_A = 3000
berry_prod_A = 2

milk_min_A = -1
milk_max_A = 3000
milk_prod_A = 1

cotton_min_A = -1
cotton_max_A = 2000
cotton_prod_A = 1

smith_num_A = 2          # 대장간 건물 수
smith_lev1_A = 300        # 도끼
smith_lev2_A = 300        # 곡괭이
smith_lev3_A = 250        # 톱
smith_lev4_A = 250        # 삽
smith_lev5_A = 150        # 말뚝
smith_lev6_A = 150        # 집게
smith_lev7_A = 200        # 망치

jelly_num_A = 2           # 젤리쨈 건물 수
jelly_lev1_A = 300      # 젤리빈
jelly_lev2_A = 300      # 스윗젤리 잼
jelly_lev3_A = 300      # 달고나 잼
jelly_lev4_A = 300      # 석류 잼
jelly_lev5_A = 0      # 톡톡베리 잼

rollc_num_A = 2           #롤케이크 건물 수
rollc_lev1_A = 300       # 솔방울새 인형
rollc_lev2_A = 299       # 도토리 램프
rollc_lev3_A = 270       # 뻐꾹뻐꾹 시계
rollc_lev4_A = 300       # 백조깃털 드림캐처

bread_num_A = 2           # 빵집 건물 수
bread_lev1_A = 130      # 든든한 호밀빵
bread_lev2_A = 80      # 달콤쫀득 잼파이
bread_lev3_A = 60      # 은행 포카치아
bread_lev4_A = 25      # 슈가코팅 도넛
bread_lev5_A = 100      # 폭신 카스테라
bread_lev6_A = 0      # 골드리치 크로와상

jampy_num_A = 2           # 잼파이 건물 수
jampy_lev1_A = 200      # 따끈따끈 젤리스튜
jampy_lev2_A = 100      # 곰젤리 버거
jampy_lev3_A = 100      # 캔디크림 파스타
jampy_lev4_A = 150      # 폭신폭신 오므라이스
jampy_lev5_A = 0      # 콤비네이션 피자젤리
jampy_lev6_A = 0      # 고급스러운 젤리빈 정식

doye_num_A = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_A = 350       # 비스킷 화분
doye_lev2_A = 250       # 반짝반짝 유리판
doye_lev3_A = 170       # 반짝이는 색동구슬
doye_lev4_A = 170       # 무지갯빛 디저트 보울

flower_num_A = 2          # 꽃가게 건물 수
flower_lev1_A = 300      # 캔디꽃
flower_lev2_A = 225      # 행복한 꽃화분
flower_lev3_A = 150      # 캔디꽃다발
flower_lev4_A = 210      # 롤리팝 꽃바구니
flower_lev5_A = 200      # 유리꽃 부케
flower_lev6_A = 0      # 찬란한 요거트 화환

milky_num_A = 2           # 우유 가공소 건물 수
milky_lev1_A = 100      # 크림
milky_lev2_A = 100      # 버터
milky_lev3_A = 100      # 수제 치즈

latte_num_A = 2         # 라떼 건물 수
latte_lev1_A = 200      # 젤리빈 라떼
latte_lev2_A = 110      # 몽글몽글 버블티
latte_lev3_A = 0      # 스윗베리 에이드

dolls_num_A = 1         # 러블리 인형공방 건물 수
dolls_lev1_A = 110      # 구름사탕 쿠션
dolls_lev2_A = 110      # 곰젤리 솜인형
dolls_lev3_A = 0      # 용과 드래곤 솜인형

beer_num_A = 1          # 오크통 쉼터 건물 수
beer_lev1_A = 35      # 크림 루트비어
beer_lev2_A = 35      # 레드베리 주스
beer_lev3_A = 35      # 빈티지 와일드 보틀

muffin_num_A = 1        # 퐁 드 파티세리 건물 수
muffin_lev1_A = 25      # 으스스 머핀
muffin_lev2_A = 25      # 생딸기 케이크
muffin_lev3_A = 25      # 파티파티 쉬폰케이크

jewel_num_A = 1          # 살롱 드 쥬얼리 건물 수
jewel_lev1_A = 25      # 글레이즈드 링
jewel_lev2_A = 25      # 루비베리 브로치
jewel_lev3_A = 0      # 로얄 곰젤리 크라운

# 마늘맛바게뜨---------------------------------------------

wood_min_B = 1300
wood_max_B = 2000
wood_prod_B = 2

jelbean_min_B = 1800
jelbean_max_B = 2200
jelbean_prod_B = 2

sugar_min_B = 1800
sugar_max_B = 2200
sugar_prod_B = 2

biscuit_min_B = 0
biscuit_max_B = 2800
biscuit_prod_B = 2

berry_min_B = 0
berry_max_B = 2800
berry_prod_B = 2

milk_min_B = 0
milk_max_B = 2800
milk_prod_B = 1

cotton_min_B = -1
cotton_max_B = 2000
cotton_prod_B = 1

smith_num_B = 1           # 대장간 건물 수
smith_lev1_B = 300        # 도끼
smith_lev2_B = 300        # 곡괭이
smith_lev3_B = 300        # 톱
smith_lev4_B = 300        # 삽
smith_lev5_B = 300        # 말뚝
smith_lev6_B = 300        # 집게
smith_lev7_B = 380        # 망치

jelly_num_B = 2           # 젤리쨈 건물 수
jelly_lev1_B = 299      # 젤리빈 잼
jelly_lev2_B = 299      # 스윗젤리 잼
jelly_lev3_B = 299      # 달고나 잼
jelly_lev4_B = 299      # 석류 잼
jelly_lev5_B = 0      # 톡톡베리 잼

rollc_num_B = 2           #롤케이크 건물 수
rollc_lev1_B = 350       # 솔방울새 인형
rollc_lev2_B = 299       # 도토리 램프
rollc_lev3_B = 299       # 뻐꾹뻐꾹 시계
rollc_lev4_B = 200       # 백조깃털 드림캐처

bread_num_B = 2           # 빵집 건물 수
bread_lev1_B = 230      # 든든한 호밀빵
bread_lev2_B = 250      # 달콤쫀득 잼파이
bread_lev3_B = 230      # 은행 포카치아
bread_lev4_B = 210      # 슈가코팅 도넛
bread_lev5_B = 225      # 폭신 카스테라
bread_lev6_B = 0      # 골드리치 크로와상

jampy_num_B = 2           # 잼파이 건물 수
jampy_lev1_B = 180      # 따끈따끈 젤리스튜
jampy_lev2_B = 129      # 곰젤리 버거
jampy_lev3_B = 35      # 캔디크림 파스타
jampy_lev4_B = 30      # 폭신폭신 오므라이스
jampy_lev5_B = 70      # 콤비네이션 피자젤리
jampy_lev6_B = 0      # 고급스러운 젤리빈 정식

doye_num_B = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_B = 349       # 비스킷 화분
doye_lev2_B = 249       # 반짝반짝 유리판
doye_lev3_B = 249       # 반짝이는 색동구슬
doye_lev4_B = 349       # 무지갯빛 디저트 보울

flower_num_B = 2          # 꽃가게 건물 수
flower_lev1_B = 139      # 캔디꽃
flower_lev2_B = 110      # 행복한 꽃화분
flower_lev3_B = 60      # 캔디꽃다발
flower_lev4_B = 40      # 롤리팝 꽃바구니
flower_lev5_B = 35      # 유리꽃 부케
flower_lev6_B = 72      # 찬란한 요거트 화환

milky_num_B = 2           # 우유 가공소 건물 수
milky_lev1_B = 200      # 크림
milky_lev2_B = 200      # 버터
milky_lev3_B = 200      # 수제 치즈

latte_num_B = 2         # 라떼 건물 수
latte_lev1_B = 290      # 젤리빈 라떼
latte_lev2_B = 240      # 몽글몽글 버블티
latte_lev3_B = 200      # 스윗베리 에이드

dolls_num_B = 2         # 러블리 인형공방 건물 수
dolls_lev1_B = 160      # 구름사탕 쿠션
dolls_lev2_B = 150      # 곰젤리 솜인형
dolls_lev3_B = 0      # 용과 드래곤 솜인형

beer_num_B = 2          # 오크통 쉼터 건물 수
beer_lev1_B = 65      # 크림 루트비어
beer_lev2_B = 65      # 레드베리 주스
beer_lev3_B = 65      # 빈티지 와일드 보틀

muffin_num_B = 2        # 퐁 드 파티세리 건물 수
muffin_lev1_B = 40      # 으스스 머핀
muffin_lev2_B = 40      # 생딸기 케이크
muffin_lev3_B = 40      # 파티파티 쉬폰케이크

jewel_num_B = 2          # 살롱 드 쥬얼리 건물 수
jewel_lev1_B = 70     # 글레이즈드 링
jewel_lev2_B = 70      # 루비베리 브로치
jewel_lev3_B = 60      # 로얄 곰젤리 크라운


def find_num(image, yPosition, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(620,yPosition+20,33,18))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def del_duplication(dif, list_origin):
    list_origin.sort()
    list_origin = list(set(list_origin))
    del_list = list()
    if len(list_origin) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
        for i in range(len(list_origin)-1):
            for j in range(len(list_origin)-1-i):
                # if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif and abs(int(list_origin[i][1])-int(list_origin[i+1+j][1])) < dif:
                if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif:
                    del_list.append(list_origin[i])
                if list_origin[i][0] == list_origin[i+1+j][0]:
                    del_list.append(list_origin[i])
    list_origin = [x for x in list_origin if x not in del_list]
    list_origin.sort()
    return list_origin

def prod_check(image, account):
    error_count = 0
    while True:
        if keyboard.is_pressed('end'):
            break
        its_location = pag.locateCenterOnScreen(image, region=(590,83+account*540, 30, 455), confidence=0.95)
        if not (its_location):
            error_count = error_count + 1
            time.sleep(0.5)
            pag.moveTo(610,295+account*540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610,295+account*540+5,1)   # 153인데 20 더 여유줌
            time.sleep(1)
            pag.mouseUp()
            time.sleep(1)
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
        find_num('prod_0.png', its_location[1], list_num_0)
        find_num('prod_1.png', its_location[1], list_num_1)
        find_num('prod_1_1.png', its_location[1], list_num_1)
        find_num('prod_2.png', its_location[1], list_num_2)
        find_num('prod_3.png', its_location[1], list_num_3)
        find_num('prod_3_1.png', its_location[1], list_num_3)
        find_num('prod_4.png', its_location[1], list_num_4)
        find_num('prod_4_1.png', its_location[1], list_num_4)
        find_num('prod_4_2.png', its_location[1], list_num_4)
        find_num('prod_5.png', its_location[1], list_num_5)
        find_num('prod_6.png', its_location[1], list_num_6)
        find_num('prod_7.png', its_location[1], list_num_7)
        find_num('prod_8.png', its_location[1], list_num_8)
        find_num('prod_8_1.png', its_location[1], list_num_8)
        find_num('prod_9.png', its_location[1], list_num_9)
        find_num('prod_9_1.png', its_location[1], list_num_9)
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

def find_upper_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(515,46+account*540,48,19))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def find_heart_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.83, grayscale=True, region=(376,48+account*540,26,15))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def Upper_numb(account):
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
    find_upper_num('up_0.png', account, list_num_0)
    find_upper_num('up_1.png', account, list_num_1)
    find_upper_num('up_2.png', account, list_num_2)
    find_upper_num('up_3.png', account, list_num_3)
    find_upper_num('up_4.png', account, list_num_4)
    find_upper_num('up_5.png', account, list_num_5)
    find_upper_num('up_6.png', account, list_num_6)
    find_upper_num('up_7.png', account, list_num_7)
    find_upper_num('up_8.png', account, list_num_8)
    find_upper_num('up_9.png', account, list_num_9)
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

def Heart_numb(account):
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
    find_heart_num('up_h0.png', account, list_num_0)
    find_heart_num('up_h0_1.png', account, list_num_0)
    find_heart_num('up_h1.png', account, list_num_1)
    # find_heart_num('up_h1_1.png', account, list_num_1)
    find_heart_num('up_h2.png', account, list_num_2)
    find_heart_num('up_h3.png', account, list_num_3)
    find_heart_num('up_h3_1.png', account, list_num_3)
    find_heart_num('up_h3_2.png', account, list_num_3)
    find_heart_num('up_h4.png', account, list_num_4)
    find_heart_num('up_h4_1.png', account, list_num_4)
    find_heart_num('up_h5.png', account, list_num_5)
    find_heart_num('up_h5_1.png', account, list_num_5)
    find_heart_num('up_h5_2.png', account, list_num_5)
    find_heart_num('up_h6.png', account, list_num_6)
    find_heart_num('up_h6_1.png', account, list_num_6)
    find_heart_num('up_h7.png', account, list_num_7)
    find_heart_num('up_h8.png', account, list_num_8)
    find_heart_num('up_h8_1.png', account, list_num_8)
    find_heart_num('up_h8_2.png', account, list_num_8)
    find_heart_num('up_h8_3.png', account, list_num_8)
    find_heart_num('up_h8_4.png', account, list_num_8)
    find_heart_num('up_h9.png', account, list_num_9)
    find_heart_num('up_h9_1.png', account, list_num_9)
    find_heart_num('up_h9_2.png', account, list_num_9)
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
    
    print('현재 하트 수량은 =', its_number)
    return its_number

def Heart_new_numb(account):
    # ++
    heart_new_heart = pag.locateCenterOnScreen('heart_new_heart.png',confidence=0.85,region=(30,430+account*540,40,42))
    if (heart_new_heart):
        print('heart_new_heart',heart_new_heart)
        x1 = heart_new_heart[0]+22
    else:
        print('하트를 못찾아요!')
        return 0
    heart_new_slash = pag.locateCenterOnScreen('heart_new_slash.png',confidence=0.95,region=(83,443+account*540,17,19))
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
    find_num_new_heart('up_hn_0.png', x1, x2, list_num_0, account)
    find_num_new_heart('up_hn_0_1.png', x1, x2, list_num_0, account)
    find_num_new_heart('up_hn_1.png', x1, x2, list_num_1, account)
    find_num_new_heart('up_hn_1_1.png', x1, x2, list_num_1, account)
    find_num_new_heart('up_hn_2.png', x1, x2, list_num_2, account)
    find_num_new_heart('up_hn_3.png', x1, x2, list_num_3, account)
    find_num_new_heart('up_hn_4.png', x1, x2, list_num_4, account)
    find_num_new_heart('up_hn_5.png', x1, x2, list_num_5, account)
    find_num_new_heart('up_hn_6.png', x1, x2, list_num_6, account)
    find_num_new_heart('up_hn_7.png', x1, x2, list_num_7, account)
    find_num_new_heart('up_hn_8.png', x1, x2, list_num_8, account)
    find_num_new_heart('up_hn_9.png', x1, x2, list_num_9, account)
    find_num_new_heart('up_hn_9_1.png', x1, x2, list_num_9, account)
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

def Heart_sojin(account,WhatToDo):
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
        now_time = time.time()
        if now_time - start_time > 900:
            End_kkd(account)                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        if keyboard.is_pressed('end'):
            return False

        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        play_halted1 = pag.locateCenterOnScreen('cond_g_play1.png', region=(2, 32 + account * 540, 917, 505))
        if (play_halted1):
            Check_Initiating(account)
            # End_kkd(account)
            Kingdom_ready(account, 'kkd_out')  # 재부팅

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False
        
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_in = (194, 144, 10)    # 생산건물 내
        pix_status_in_dark = (97, 72, 5)    #건물 안이긴 한데 창이 떠있음
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
        pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
        pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
        pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
        pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
        pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
        pix_status_adv = (0, 181, 255)   # 모험하기
        pix_status_kdpass = (42, 27, 19)  # 킹덤패스
        pix_status_warehouse = (55, 64, 105) # 창고 뜸
        pix_status_mail = (60, 70, 105)   # 우편함
        pix_lackof1 = (243, 233, 223)   # 베이지색
        pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
        pix_status_cookiehouse = (0, 129, 182)  # 엥 이게 다 달라?
        pix_status_lotto = (255, 189, 8)    # 뽑기, 해변교역소
        pix_status_mycookie = (0, 0, 0) #내 쿠키...으... 움직이면 틀어질텐데
        pix_status_fountain = (84, 93, 134) # 분수..
        pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
        pix_status_trade = (255, 216, 2)    # 해상무역센터 로비
        pix_status_wanted = (29, 10, 12)    # 오늘의 현상수배 선택하는 곳
        pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
        pix_status_fight_comp1 = (121, 98, 74)   # 모험 전투 후1

        # cond_adv_dark_mode = pag.locateCenterOnScreen('cond_adv_dark_mode.png', confidence=0.9, region=(200,60+account*540,30,17))  # 어둠모드 입니까?
        cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12,38+account*540,37,36))  # Play버튼 누른 후 모험하기 창
        adv_normal = pag.locateCenterOnScreen('adv_normal.png', confidence=0.85, region = (232,53+account*540,35,19))       # 에피소드에서 좌상단 일반/어둠 선택 확인하기
        cond_adv_out_1 = pag.locateCenterOnScreen('cond_adv_out_1.png', confidence=0.85, region=(2,32+account*540,917,505))   # 1렙 맵
        cond_adv_out_2 = pag.locateCenterOnScreen('cond_adv_out_2.png', confidence=0.85, region=(2,32+account*540,917,505))   # 2렙 맵
        cond_adv_out_3 = pag.locateCenterOnScreen('cond_adv_out_3.png', confidence=0.85, region=(2,32+account*540,917,505))   # 3렙 맵
        cond_adv_out_4 = pag.locateCenterOnScreen('cond_adv_out_4.png', confidence=0.85, region=(2,32+account*540,917,505))   # 4렙 맵
        cond_adv_out_5 = pag.locateCenterOnScreen('cond_adv_out_5.png', confidence=0.85, region=(2,32+account*540,917,505))   # 5렙 맵
        cond_adv_out_6 = pag.locateCenterOnScreen('cond_adv_out_6.png', confidence=0.85, region=(2,32+account*540,917,505))   # 6렙 맵
        cond_adv_out_7 = pag.locateCenterOnScreen('cond_adv_out_7.png', confidence=0.85, region=(2,32+account*540,917,505))   # 7렙 맵
        cond_adv_out_8 = pag.locateCenterOnScreen('cond_adv_out_8.png', confidence=0.85, region=(2,32+account*540,917,505))   # 8렙 맵
        cond_adv_out_9 = pag.locateCenterOnScreen('cond_adv_out_9.png', confidence=0.85, region=(2,32+account*540,917,505))   # 9렙 맵
        cond_adv_out_10 = pag.locateCenterOnScreen('cond_adv_out_10.png', confidence=0.85, region=(2,32+account*540,917,505))   # 10렙 맵
        cond_adv_out_11 = pag.locateCenterOnScreen('cond_adv_out_11.png', confidence=0.85, region=(2,32+account*540,917,505))   # 11렙 맵
        cond_adv_out_12 = pag.locateCenterOnScreen('cond_adv_out_12.png', confidence=0.85, region=(2,32+account*540,917,505))   # 12렙 맵
        adv_worldmap = pag.locateCenterOnScreen('adv_worldmap.png', confidence=0.85, region=(33,467+account*540,52,43))   # 좌하단 월드맵 아이콘
        adv_goto_wangkook = pag.locateCenterOnScreen('adv_goto_wangkook.png', confidence=0.85, region=(845,470+account*540,40,40))   # 우하단 왕국가기 아이콘
        adv_8_epi = pag.locateCenterOnScreen('adv_8_epi.png', confidence=0.85, region = (75,52+account*540,18,14))      # 에피소드 8 입니까?
        adv_8_25 = pag.locateCenterOnScreen('adv_8_25.png', confidence=0.83, region=(2,32+account*540,917,505))   # 8-25
        adv_8_26 = pag.locateCenterOnScreen('adv_8_26.png', confidence=0.83, region=(2,32+account*540,917,505))   # 8-26
        adv_8_28 = pag.locateCenterOnScreen('adv_8_28.png', confidence=0.83, region=(2,32+account*540,917,505))   # 8-28
        adv_8_29 = pag.locateCenterOnScreen('adv_8_29.png', confidence=0.83, region=(2,32+account*540,917,505))   # 8-29
        cond_adv_stage_select = pag.locateCenterOnScreen('cond_adv_stage_select.png', confidence=0.83, region=(408,39+account*540,100,50))   # 스테이지 고르는 화면
        cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국
        
        # 자동 전투 체크        
        if bEntered and not bAutoCheck:
            cond_adv_automode = pag.locateCenterOnScreen('cond_adv_automode.png', confidence=0.85, region=(39,433+account*540,12,14))   # 황금 "동" 글씨
            cond_adv_not_automode = pag.locateCenterOnScreen('cond_adv_not_automode.png', confidence=0.85, region=(39,433+account*540,12,14))   # 회색 "동" 글씨
            if (cond_adv_not_automode):
                time.sleep(1.5)
                pag.click(cond_adv_not_automode)
            if (cond_adv_automode):
                print('자동 전투 확인!')
                time.sleep(1.5)
                bAutoCheck = True

        # 속도 체크
        adv_speed1 = pag.locateCenterOnScreen('adv_speed1.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        adv_speed2 = pag.locateCenterOnScreen('adv_speed2.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        adv_speed3 = pag.locateCenterOnScreen('adv_speed3.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        
        if bEntered and (adv_speed1):
            pag.click(adv_speed1)
            time.sleep(0.5)
            bSpeedCheck = False
        if bEntered and (adv_speed2):
            pag.click(adv_speed2)
            time.sleep(0.5)
            bSpeedCheck = False
        if bEntered and not bSpeedCheck and (adv_speed3):
            print('1.5배 ok')
            bSpeedCheck = True

        # 오 이 버튼들은 동일한가 본데..
        cond_end_fight_t = pag.locateCenterOnScreen('cond_end_fight_t.png', confidence=0.95, region=(2,32+account*540,917,505))  # 전투종료에 8-29글자
        cond_end_fight1 = pag.locateCenterOnScreen('Cond_wanted_go_kingdom.png', confidence=0.95, region=(2,32+account*540,917,505))   # 왕국가기 버튼
        cond_end_fight2 = pag.locateCenterOnScreen('Cond_wanted_refignt.png', confidence=0.95, region=(2,32+account*540,917,505))   # 다시하기 버튼
        cond_end_fight3 = pag.locateCenterOnScreen('Cond_wanted_go_out.png', confidence=0.95, region=(2,32+account*540,917,505))   # 나가기 버튼

        if (cond_end_fight_t) and (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            time.sleep(1.5)
            pag.click((540,510+account*540))
            # bWanted_fight_ing = False
            bStep2_Adv = True
            bEntered = True
        
        if (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            time.sleep(1.5)
            pag.click((540,510+account*540))
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
            pag.click(760,500+account*540)
            time.sleep(3)
            bStep1_play = False             # 플레이 버튼을 눌렀는가?(조건은 모험하기 화면에서 다시 살리겠지)
            bStep2_Adv = False              # 모험하기에서 월드 탐험을 클릭했는가?
            bStep3_Epi = False              # 에피소드(1~12)중 하나 들어와 있는 경우
            bStep4_Epi_Confirm = False      # 원하는 에피소드에 들어왔니?
            bStep5_Epi_Select = False       # 에피소드 선택 화면이니?

        if not bEntered and bStep1_play and not bStep2_Adv and not bStep3_Epi and not bStep4_Epi_Confirm and not bStep5_Epi_Select:
            cond_wanted = pag.locateCenterOnScreen('cond_world_adventure.png', confidence=0.85, region=(2,32+account*540,917,505))
            if (cond_wanted):
                print('모험하기 - 월드탐험 있으니 들어가자!')
                pag.click(cond_wanted)
                time.sleep(5)
                
            if not (cond_wanted):
                print('드래그드래그')
                pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                pag.drag(300,0,2)       # 현상수배와 반대로.. 왼쪽으로 가야 하니깐 300으로 바꿔주고
                time.sleep(3)
                error_count = error_count+1
                if error_count > 3:
                    print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                    return
        
        # 원하는 에피소드인가?
        if not bEntered and bStep3_Epi and not bStep4_Epi_Confirm:
            # 나중에 다른 에피 추가할 때 여기다 하면 될듯..
            if ((WhatToDo == '8-29') or (WhatToDo == '8-25')):
                if (adv_8_epi):
                    print('에피소드 8에 잘 오셨습니다.')
                    bStep4_Epi_Confirm = True
                else:
                    print('8 에피 가야는데 여긴 아닌거 같습니다.')
                    if (adv_worldmap):
                        print('일반모드 선택하고 월드맵 나갑니다.')
                        pag.click(215,70+account*540)
                        time.sleep(0.5)
                        pag.click(215,70+account*540)
                        time.sleep(1.5)
                        pag.click(adv_worldmap)
                        time.sleep(2)
                        bStep3_Epi = False
                    else:
                        print('여긴 어디 나는 누구.. 우선 왕국으로?')
                        pag.click(284,15+account*540)
                        time.sleep(0.1)
                        pag.hotkey('esc')
                        time.sleep(0.5)
                        pag.hotkey('esc')
                        time.sleep(0.5)
                        pag.hotkey('esc')
                        time.sleep(0.5)

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
            screen = ImageGrab.grab()
            pix_status = screen.getpixel((605, 55 + account * 540))  # 상단골드
            if (pix_status == 74, 44, 34):      # 어둠모드야?
                pag.click(78,61+account*540)    # 일반모드 클릭해요
                time.sleep(1)
            print('도니')
            if ((WhatToDo == '8-29') or (WhatToDo == '8-25')):
                if (cond_adv_out_8):
                    pag.click(cond_adv_out_8)
                    time.sleep(3)
                    cond_adv_stage_select = pag.locateCenterOnScreen('adv_8_29.png', confidence=0.83, region=(408,39+account*540,100,50))   # 스테이지 고르는 화면
                    if not (cond_adv_stage_select):
                        bStep5_Epi_Select = False
                    else:
                        pag.click(cond_adv_out_8)
                        time.sleep(3)
                else:
                    if (cond_adv_out_9):
                        if cond_adv_out_9.x > 365+3:
                            pag.click(cond_adv_out_9.x-365,cond_adv_out_9.y+73)
                        else:
                            print('왼쪽으로 드래그드래그')
                            pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                            pag.drag(300,0,2)       # 왼 손으로 비비고
                            time.sleep(3)
                            
                    else:
                        if (cond_adv_out_1) or (cond_adv_out_2) or (cond_adv_out_3) or (cond_adv_out_4) or (cond_adv_out_5) or (cond_adv_out_6) or (cond_adv_out_7):
                            print('오른쪽으로 드래그드래그')
                            pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                            pag.drag(-300,0,2)       # 오른손으로 비비고
                            time.sleep(3)
                        if (cond_adv_out_9) or (cond_adv_out_10) or (cond_adv_out_11) or (cond_adv_out_12):
                            print('왼쪽으로 드래그드래그')
                            pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                            pag.drag(300,0,2)       # 왼 손으로 비비고
                            time.sleep(3)
            
        # 일반모드 해야하고, 에피소드 들어와 있으며, 노멀모드 선택을 아직 안한
        if bNormalMode and bStep3_Epi and not bNormalSelected and not bEntered and bStep4_Epi_Confirm:
            if (adv_normal):
                print('일반모드 확인')
                bNormalSelected = True
            else:
                print('일반모드 선택합니다.')
                pag.click(215,70+account*540)
                time.sleep(0.5)
                pag.click(215,70+account*540)
                time.sleep(1.5)

        # 에피소드 안에 들어와 있고, 아직 8-29에 들어가지 않았으면
        if (WhatToDo == '8-29') and bStep3_Epi and not bEntered and not bZoomOutComp and bNormalSelected: # 8-29 스테이지, 시작 안한 경우
            # 에피스드 8인지 확인
            adv_8_epi = pag.locateCenterOnScreen('adv_8_epi.png', confidence=0.85, region = (75,52+account*540,18,14))
            if (adv_8_epi):
                print('에피소드 8이네요!')
                # 줌아웃 하고
                pag.moveTo(366,375+account*540)
                time.sleep(0.1)
                pag.keyDown('ctrlleft')
                time.sleep(0.1)
                pag.scroll(-40)
                time.sleep(1)
                pag.scroll(-40)
                time.sleep(1)
                pag.scroll(-40)
                time.sleep(0.1)
                pag.keyUp('ctrlleft')
                time.sleep(1)
                print('줌아웃, 진입 준비 완료!')
                bZoomOutComp = True

        # 28 있으면 29 위치 클릭
        if (adv_8_28) and (WhatToDo == '8-29'):
            pag.click(adv_8_28.x+94,adv_8_28.y-50)
            time.sleep(1)
            adv_8_29_in = pag.locateCenterOnScreen('adv_8_29_in.png', confidence=0.9, region=(2,32+account*540,917,505))   # 8-29 클릭완료
            if (adv_8_29_in):
                print('8-29 클릭했네요')
                pag.click(715,490+account*540)          # 전투 준비 클릭(현상수배랑 글씨 사이즈가 다르네 씁..)
                time.sleep(1.5)
                pag.click(820,495+account*540)          # 전투 시작 클릭
                time.sleep(1)
                cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.9, region=(2,32+account*540,917,505))
                if (cond_balloon_lack_heart):
                    print('젤리고기 부족..')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(4)
                    return False
                else:
                    bEntered = True
        
        # 29 있으면 클릭
        if (adv_8_29) and (WhatToDo == '8-29'):
            pag.click(adv_8_29)
            time.sleep(1)
            adv_8_29_in = pag.locateCenterOnScreen('adv_8_29_in.png', confidence=0.9, region=(2,32+account*540,917,505))   # 8-29 클릭완료
            if (adv_8_29_in):
                print('8-29 클릭했네요')
                pag.click(715,490+account*540)          # 전투 준비 클릭(현상수배랑 글씨 사이즈가 다르네 씁..)
                time.sleep(1.5)
                pag.click(820,495+account*540)          # 전투 시작 클릭
                time.sleep(1)
                cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.9, region=(2,32+account*540,917,505))
                if (cond_balloon_lack_heart):
                    print('젤리고기 부족..')
                    pag.click(284,15+account*540)
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(4)
                    return False
                bEntered = True
            
        if(cond_end_fight3):   # 나가기 버튼이 있는데
            if (cond_end_fight2):   # 다시하기 버튼이 있으면
                print('다시하기 버튼!')
                pag.click(cond_end_fight2,clicks=1,interval=2.5) # 눌러~
                time.sleep(1)
                # bWanted_fight_ing = True
            else:
                pag.click(cond_end_fight1,clicks=1,interval=2.5)  # 왕국가기버튼 클릭. 나가기 버튼과 항상 함께 있어서 오류날 일 없겠지
                time.sleep(15)
                if Kingdom_ready(account,'kkd_out'):    # 어후 왕국에 잘 들어왔어
                    print('월드탐험 잘 마치고 종료합니다!')
                    return True

# 건물 안, 생산품으로 건물 확인? 재고+대기제품으로 확인?
bJewel = False
bMuffin = False
bBeer = False
bDolls = False
bLatte = False
bMilky = False
bFlower = False
bDoye = False
bJampy = False
bBread = False
bRollc = False
bJelly = False
bSmith = False
bCotton = False
bMilk = False
bBerry = False
bBiscuit = False
bSugar = False
bJellyBean = False
bWood = False


# 실제 생산하는 녀석.. 이렇게 보니 앞에 생산품도 함수로 만들수 있지 않을까
def prod_action(image, list_image, account, check_num):
    print('Prod_action함수!',image, list_image, account, check_num)
    start_time = time.time()
    error_count = 0

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.6)

    cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
    if (cond_halted):
        pag.click(740,310+account*540)
        End_kkd(account)
        Kingdom_ready(account,'kkd_out')            # 재부팅
        return False

    prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
        time.sleep(0.9)
    
    cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75-10,200-10+account*540,20,20))
    if (cond_2nd_clear):
        ShowTime = True
    else:
        return True
    
    while ShowTime:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.6)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        now_time = time.time()
        prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
        if not (prod_refresh):
            # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
            pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
            time.sleep(0.9)
        # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
        prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
        # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!1')
            # prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
            #                                               region=(339, 253 + account * 540, 175, 87))
            # time.sleep(1)
            # if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            #     print('욕심을 버리시오 중생이여..')
            #     pag.click(455, 379 + account * 540)
            #     time.sleep(0.3)
            #     pag.click(164, 280 + account * 540)
            #     time.sleep(0.3)
            # else:

            return True
        if now_time - start_time > 30:
            print('동작 최대시간 초과 입니다.')
            return False
        if keyboard.is_pressed('end'):
            return True

        ctr = pag.locateCenterOnScreen(image, confidence=0.85, region=(560,75+account*540,105,460))
        prd_done = pag.locateCenterOnScreen('prod_done.png', confidence=0.85, region=(2,32+account*540,917,505))
        list_full = pag.locateCenterOnScreen('Cond_makinglist_full.png', confidence=0.97, region=(2,32+account*540,917,505))
        list_full1 = pag.locateCenterOnScreen('Cond_makinglist_full1.png', confidence=0.97, region=(2,32+account*540,917,505))
        lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
        not_opened = pag.locateCenterOnScreen('Cond_not_opened.png',confidence=0.95, region=(2,32+account*540,917,505))
        ctr_list = pag.locateCenterOnScreen(list_image, confidence=0.9, region=(40,168+account*540,71,321))
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))

        if (play_halted):
            pag.click(play_halted)

        if (ctr):   # 이미지 찾음
            print('이미지 검색!',image)
            while True:
                if ctr.y < 465 + account*540:   # 최대 밑으로 스크롤 한 경우 464+540*account 이하여야 함. 넘어가면 불안쓰
                    print('이미지 범위 내에요!')
                    break
                else:
                    print('이미지가 너무 밑에 있어 올립니다.')
                    Updown(account,'up')    # 순방향 위로 드래그
                    ctr = pag.locateCenterOnScreen(image, confidence=0.85, region=(2,32+account*540,917,505))
            now_time = time.time()
            if now_time - start_time > 30:
                print('동작 최대시간 초과 입니다.')
                return False
            target_numb = check_num - prod_check(image, account)
            # 목표 수량 미만
            if target_numb > 0:
                print('목표 수량 미달!',target_numb)
                if (list_full) or (list_full1) or (prd_done):       # 생산 완료
                    print('목표 생산물 클릭 완료!!')
                    return True
                elif (lack_of_material):                            # 재료 부족
                    print('재료가 부족해요')
                    pag.click(284,15+account*540)
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    return False
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284,15+account*540)
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    return False
                else:                                               # 그거 아니면 생산 클릭
                    print('생산품 클릭!')
                    pag.moveTo(ctr[0]+177,ctr[1]+48)
                    time.sleep(0.5)
                    pag.mouseDown()
                    time.sleep(0.7)
                    pag.mouseUp()
                    time.sleep(0.5)

                    lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
                    if (lack_of_material):
                        print('재료가 부족해요')
                        pag.click(284,15+account*540)
                        time.sleep(0.5)
                        pag.hotkey('esc')
                        time.sleep(0.5)
                        return False

            # 목표 수량 초과
            if target_numb <= 0:
                print('목표 수량 초과!')
                if (ctr_list):
                    if 111 >= ctr_list.x >=40:
                        print('이 제품은 충분히 생산했으니 삭제하겠써요!')
                        pag.click(ctr_list)
                        time.sleep(0.7)
                else:
                    return False
        else:       # 이미지 못찾음
            print('이미지를 찾지 못했습니다.')
            if error_count > 2:                         # 그래도 못찾으면 에러
                return False
            if error_count == 1:
                pag.moveTo(610,295+account*540)
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(610,295+account*540+15,2)   # 15 내리고 이미지 다시 찾음
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(2)
                error_count = error_count+1
            if error_count == 0:
                pag.moveTo(610,295+account*540)
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(610,295+account*540-10,2)   # 10 올리고 이미지 다시 찾음
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(2)
                error_count = error_count+1

# 부팅 확인할 때 쓰는
def Check_Initiating(account):
    print('부팅여부 확인합니다.')
    bStart = False
    bTouchto = False
    kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence = 0.9, region=(2,32+account*540,917,505))
    kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence = 0.8, region=(2,32+account*540,917,505))
    kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence = 0.95, region=(2,32+account*540,917,505))
    kkd_start_bg = pag.locateCenterOnScreen('init_kkm_recent.png', confidence=0.9, region=(2, 32 + account * 540, 917, 505)) # 최근 항목이 없습니다.
    kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2, 32 + account * 540, 917, 505))
    
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.94, region = (376,354+account*540,159,45))
        if (cond_network):   # 네트워크오류인듯?
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.8)

        if (kkd_start_bg):   # 최근 항목이 없습니다.
            print('[부팅중] 계정 튕김! 창목록클릭중!')
            pag.hotkey('esc')
            time.sleep(1)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):     # 쿠킹덤이 중지됨!
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))

        if (play_halted):     # 구글플레이 확인버튼... 난 쓸일이 없는걸
            pag.click(play_halted)
        else:
            break

    if (kkd_start) or (kkd_touch) or (kkd_down) or (kkd_start_ire):
        while True:
            if (kkd_start_ire):
                pag.click(kkd_start_ire)
                time.sleep(1)
                break

            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.8)

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
            if (cond_halted):            # 쿠킹덤이 중지됨!
                pag.click(740,310+account*540)
                End_kkd(account)
                Kingdom_ready(account,'kkd_out')            # 재부팅
                return False

            if keyboard.is_pressed('end'):
                return

            while True:
                play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))
                if (play_halted):           # 쿠킹덤이 중지됨!
                    pag.click(play_halted)
                else:
                    break

            kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence = 0.9, region=(2,32+account*540,917,505))
            if (kkd_start):
                print('[부팅중] 계정 튕김! 쿠킹덤 아이콘 클릭!')
                pag.click(kkd_start)
                bStart = True
                time.sleep(1)

            if not (kkd_start):
                print('[부팅중] 계정 튕김! 쿠킹덤 아이콘 클릭 완료!')
                break

        # 쿠킹덤 아이콘 실행 후 Touch to start쪽. 조건 없이 없어질 때까지 클릭
        while True:
            if keyboard.is_pressed('end'):
                break
            kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence = 0.8, region=(2,32+account*540,917,505))
            kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence = 0.95, region=(2,32+account*540,917,505))
            while True:
                play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))
                if (play_halted):
                    pag.click(play_halted)
                else:
                    break

            if (kkd_touch):
                time.sleep(3)
                print('[부팅중] Touch to Start 터치!')
                pag.click(random.randint(410,410+101), random.randint(380,380+23)+account*540)
                bTouchto = True
            if (kkd_down):
                time.sleep(3)
                print('[부팅중] 다운로드 터치!')
                pag.click(kkd_down)
                bTouchto = True
            if (not (kkd_touch) and not (kkd_down)) and bTouchto:
                print('[부팅중] Touch to Start 터치 완료!')
                break
        if bTouchto:
            print('부팅 실행 했습니다.')
            time.sleep(15)
            return
    else:
        print('튕긴건 아니네요')
        return

# 오늘의 현상수배.. 우선은 수동으로 쓰고 있지만..
def Today_wanted(account,WhatToDo):
    error_count = 0
    bEntered = False
    # bWanted_fight_ing = False
    bWanted_fight_started = False
    bEnter_Wanted = False
    while True:
        if keyboard.is_pressed('end'):
            return False

        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_in = (194, 143, 10)    # 생산건물 내
        pix_status_in_dark = (97, 71, 5)    #건물 안이긴 한데 창이 떠있음
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
        pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
        pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점, 쿠하까지 동일
        pix_status_ballon = (64, 55, 45)  # 열기구 날아다니는 중
        pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
        pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
        pix_status_adv = (0, 181, 255)   # 모험하기
        pix_status_kdpass = (42, 27, 19)  # 킹덤패스
        pix_status_warehouse = (55, 64, 105) # 창고 뜸
        pix_status_mail = (60, 70, 105)   # 우편함
        pix_lackof1 = (243, 233, 223)   # 베이지색
        pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
        pix_status_cookiehouse = (0, 129, 182)  # 엥 이게 다 달라?
        pix_status_lotto = (255, 189, 8)    # 뽑기, 해변교역소
        pix_status_mycookie = (110, 18, 33) #내 쿠키...으... 움직이면 틀어질텐데
        pix_status_fountain = (84, 93, 134) # 분수..
        pix_stats_kkd_start = (11, 10, 44)  # 바탕화면 나갔네
        pix_status_trade = (255, 215, 3)    # 해상무역센터 로비
        pix_status_wanted = (29, 10, 12)    # 오늘의 현상수배 선택하는 곳
        pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
        pix_status_fight_comp1 = (78, 25, 21)   # 모험 전투 후1

        # if not bWanted_fight_started:   # 전투시작 후에는 cond_end_fight1,2,3 조건만 볼거니깐...
        cond_ready_fight = pag.locateCenterOnScreen('Cond_wanted_ready_fignt.png', confidence=0.95, region=(2,32+account*540,917,505))   # 전투준비 버튼
        cond_start_fight = pag.locateCenterOnScreen('Cond_wanted_start_fignt.png', confidence=0.9, region=(2,32+account*540,917,505))   # 전투시작 버튼

        # if bEntered and not bWanted_fight_ing:       # 입장 했고, 싸우는 중이 아닌 경우(전투 종료)
        cond_end_fight1 = pag.locateCenterOnScreen('Cond_wanted_go_kingdom.png', confidence=0.95, region=(2,32+account*540,917,505))   # 왕국가기 버튼
        cond_end_fight2 = pag.locateCenterOnScreen('Cond_wanted_refignt.png', confidence=0.95, region=(2,32+account*540,917,505))   # 다시하기 버튼
        cond_end_fight3 = pag.locateCenterOnScreen('Cond_wanted_go_out.png', confidence=0.95, region=(2,32+account*540,917,505))   # 나가기 버튼
        
        # 입장화면 스킬 파우더 확인
        cond_wanted_all = pag.locateCenterOnScreen('cond_wanted_all.png', confidence=0.95, region=(2,32+account*540,917,505))   # 주일, 전체



        if (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            pag.click((540,510+account*540))
            # bWanted_fight_ing = False
            bEnter_Wanted = True
            bEntered = True
        
        if (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            pag.click((540,510+account*540))
            # bWanted_fight_ing = False
            bEnter_Wanted = True
            bEntered = True

        if pix_status == pix_status_out:    # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
            print('현상수배 확인하러 들어갑니다~!')
            pag.click(random.randint(730,785),random.randint(470+account*540,525+account*540))
            time.sleep(3)
        

        if pix_status == pix_status_adv:    # 모험하기 화면이면 현상수배 찾기
            cond_wanted = pag.locateCenterOnScreen('cond_wanted.png', confidence=0.95, region=(2,32+account*540,917,505))
            if (cond_wanted):
                print('현상수배 있으니 들어가자!')
                pag.click(cond_wanted)
                bEnter_Wanted = True
                time.sleep(3)
            else:
                print('드래그드래그')
                pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                pag.drag(-300,0,2)
                time.sleep(2)
                error_count = error_count+1
                if error_count > 3:
                    print('없는 걸 보니... 현상수배 다 했나봐요!')
                    return True

        if (cond_ready_fight):  # 전투 준비. 보이면 걍 클릭 막 클릭
            pag.click(cond_ready_fight)
            time.sleep(1)
            bEntered = True

        if (cond_start_fight):      # 전투 시작 누르면 조건 살리고(한 번에 안들어가면 어카지.. 몰라 두 번 클릭해놓자)
            pag.click(cond_start_fight,clicks=2,interval=0.5)
            time.sleep(1)
            # bWanted_fight_ing = True
            bWanted_fight_started = True
            bEntered = True

        if bEnter_Wanted and (WhatToDo == 'all'): # 입장. 보이면 걍 클릭(주일)
            cond_wanted_enter = pag.locateCenterOnScreen('Cond_wanted_select1.png', confidence=0.95, region=(2,32+account*540,917,505))
            pag.click(cond_wanted_enter)
            bEntered = True
            time.sleep(1)

        if bEnter_Wanted and WhatToDo == '돌격' and not bEntered:
            print('돌격형 들어갑니다.')
            fist = pag.locateCenterOnScreen('Cond_wanted_fist.png', confidence=0.85, region=(2,32+account*540,917,505))
            pag.click(fist.x+147-74+18,fist.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '방어' and not bEntered:
            print('방어형 들어갑니다.')
            shield = pag.locateCenterOnScreen('Cond_wanted_shiled.png', confidence=0.7, region=(2,32+account*540,917,505))
            pag.click(shield.x+147-74+18,shield.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '침투' and not bEntered:
            print('침투형 들어갑니다.')
            sword = pag.locateCenterOnScreen('Cond_wanted_sword.png', confidence=0.7, region=(2,32+account*540,917,505))
            pag.click(sword.x+147-74+18,sword.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '지원' and not bEntered:
            print('지원형 들어갑니다.')
            assist = pag.locateCenterOnScreen('Cond_wanted_assist.png', confidence=0.8, region=(2,32+account*540,917,505))
            pag.click(assist.x+147-74+18,assist.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '폭발' and not bEntered:
            print('폭발형 들어갑니다.')
            bomb = pag.locateCenterOnScreen('Cond_wanted_bomb.png', confidence=0.75, region=(2,32+account*540,917,505))
            pag.click(bomb.x+147-74+18,bomb.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '사격' and not bEntered:
            print('사격형 들어갑니다.')
            shooting = pag.locateCenterOnScreen('Cond_wanted_shooting.png', confidence=0.75, region=(2,32+account*540,917,505))
            pag.click(shooting.x+147-74+18,shooting.y+448-416+10)
            bEntered = True
            time.sleep(1)
        if bEnter_Wanted and WhatToDo == '마법' and not bEntered:
            staff = pag.locateCenterOnScreen('Cond_wanted_staff.png', confidence=0.75, region=(2,32+account*540,917,505))
            if (staff): # 있으면 바로 들어감(화요일)
                print('마법형 들어갑니다.')
                pag.click(staff.x+147-74,staff.y+448-416)
                bEntered = True
                time.sleep(1)
            else:       # 없으면 우측으로 드래그
                pag.moveTo(730,490+account*540)
                time.sleep(0.1)
                pag.drag(-300,0,2)
                time.sleep(1)
        if bEnter_Wanted and WhatToDo == '회복' and not bEntered:
            recovery = pag.locateCenterOnScreen('Cond_wanted_recovery.png', confidence=0.75, region=(2,32+account*540,917,505))
            if (recovery): # 있으면 바로 들어감(화요일)
                print('회복형 들어갑니다.')
                pag.click(recovery.x+147-74,recovery.y+448-416)
                bEntered = True
                time.sleep(1)
            else:       # 없으면 우측으로 드래그
                pag.moveTo(730,490+account*540)
                time.sleep(0.1)
                pag.drag(-300,0,2)
                time.sleep(1)

        if(cond_end_fight3):   # 나가기 버튼이 있는데
            if (cond_end_fight2):   # 다시하기 버튼이 있으면
                pag.click(cond_end_fight2,clicks=2,interval=0.5) # 눌러~
                time.sleep(1)
                # bWanted_fight_ing = True
            else:
                pag.click(cond_end_fight1,clicks=2,interval=0.5)  # 왕국가기버튼 클릭. 나가기 버튼과 항상 함께 있어서 오류날 일 없겠지
                time.sleep(15)
                if Kingdom_ready(account,'kkd_out'):    # 어후 왕국에 잘 들어왔어
                    print('현상수배 잘 마치고 종료합니다!')
                    return True

# 건물에 들어가기
def Enter_Building(account):
    error_position = 0
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        if keyboard.is_pressed('end'):
            print('end버튼 눌러 종료됨')
            return False
        bWod_r = False
        bWod_l = False
        print('건물 들어가기 전 왕국 위치 확인')
        if not Kingdom_ready(account, 'prod_in'):
            # Check_Initiating(account)
            Kingdom_ready(account,'kkd_out')
        else:
            print('이미 건물 안이네요!')
            return True

        while True:
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)
            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
            if (cond_halted):
                pag.click(740,310+account*540)
                End_kkd(account)
                Kingdom_ready(account,'kkd_out')            # 재부팅
                return False

            if keyboard.is_pressed('end'):
                return False
            wod_r = pag.locateCenterOnScreen('wood_sign_r.png', confidence=0.85, region=(249+10, 78+account*540+10, 576-10, 382-10))
            wod_l = pag.locateCenterOnScreen('wood_sign_l.png', confidence=0.85, region=(249, 78+account*540+10, 576-10, 382-10))
            print(wod_r)
            print(wod_l)
            if (not (wod_r) and not (wod_l)):    # 왕국, 간판 없음
                print('간판이 없으니 스샷모드로 찾아볼까요')
                Enter_Screenshot_mode(account, 'left_down')

            if (wod_r) and not bWod_r:
                print('우간판 먼저 들어가 보고')
                pag.click(wod_r.x-10, wod_r.y+10)
                time.sleep(2)
                if Kingdom_ready(account, 'prod_in'):
                    print('우간판으로 건물 진입!')
                    return
                else:
                    print('우간판 클릭했지만 성공은 못했군..')
                    bWod_r = True
            if (wod_r) and bWod_r:
                print('한 번으로 못들어갔다면 다시 정조준')
                time.sleep(2)
                wod_r = pag.locateCenterOnScreen('wood_sign_r.png', confidence=0.85, region=(249+10, 78+account*540+10, 576-10, 382-10))
                if (wod_r):
                    pag.click(wod_r.x-10, wod_r.y+10)
                    time.sleep(2)
                    if Kingdom_ready(account, 'prod_in'):
                        print('우간판으로 건물 진입!')
                        return
                else:
                    print('어... 뭐야 왜 간판 사라짐...')
                    Kingdom_ready(account, 'kkd_out')
            if (wod_l):
                print('우간판이 없으니 좌간판이라도')
                pag.click(wod_l.x+10, wod_l.y-10)
                time.sleep(2)
                if Kingdom_ready(account, 'prod_in'):
                    print('좌간판으로 건물 진입!')
                    return
                else:
                    print('우간판 클릭했지만 성공은 못했군..')
                    bWod_l = True
            if (wod_l) and bWod_l:
                print('한 번으로 못들어갔다면 다시 정조준')
                time.sleep(2)
                wod_l = pag.locateCenterOnScreen('wood_sign_l.png', confidence=0.85, region=(249, 78+account*540+10, 576-10, 382-10))
                if (wod_l):
                    pag.click(wod_l.x+10, wod_l.y-10)
                    time.sleep(2)
                    if Kingdom_ready(account, 'prod_in'):
                        print('우간판으로 건물 진입!')
                        return
                else:
                    print('어... 뭐야 왜 간판 사라짐...')
                    Kingdom_ready(account, 'kkd_out')

def list_clear(account):
    while True:
        cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75-10,200-10+account*540,20,20))
        if (cond_2nd_clear):
            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
            if (prod_refresh):
                pag.click(prod_refresh) # >> 클릭(즉시생산)
                # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                time.sleep(0.8)
                remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                if (remain_time_less_minute):
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.8)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    return
                else:
                    print('1분 넘게 남아 삭제함돠1')
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                    time.sleep(0.2)
                    pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                    time.sleep(0.2)
                    return
            else:
                # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
                pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
                time.sleep(0.5)
                return True
        else:
            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
            if not (prod_refresh):
                # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
                pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
                time.sleep(0.5)
            # 둘째 칸 취소
            pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)+account*540)
        
        # 그새 생산 완료돼서 둘 째 칸 생산중이면 뜨는 취소창은 빼기
        cond_cancel = pag.locateCenterOnScreen('cond_cancel.png', confidence=0.96, region=(469,221+account*540,36,19))
        if (cond_cancel):
            pag.click(random.randint(628-5,628+5),random.randint(166-5,166+5)+account*540)
            time.sleep(0.5)
        # 안넣으니 클릭하고 바로 빈칸 캐치해서 멈출때가 있군....
        time.sleep(0.5)


def Wood_to_Cotton(account, Min_number, Max_number, Making_Level, prod_direction_left):   # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)

    cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
    if (cond_halted):
        pag.click(740,310+account*540)
        End_kkd(account)
        Kingdom_ready(account,'kkd_out')            # 재부팅
        return False

    prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
        time.sleep(0.5)
    # 클릭했는데도 리스트가 가득 차있다? 얘들은 좋지
    prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
    # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!2')
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
                                                      region=(339, 253 + account * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..')
            pag.click(455, 379 + account * 540)
            time.sleep(0.3)
            pag.click(164, 280 + account * 540)
            time.sleep(0.3)
        else:
            Skip_Next(account, prod_direction_left)
        return False
    # else:
    #     prod_empty = pag.locateAllOnScreen('prod_empty.png', confidence = 0.96, region = (42,97+account*540,66,391))
    #     prod_empty = list(prod_empty)
    #     empty_space = len(prod_empty)+1

    its_number = Upper_numb(account)
    print('확인한 상단 숫자 =', its_number)
    if Max_number*0.8 > its_number:     # 최대 수량의 80% 이하이면
        bujockhaeyo = True
    else:
        bujockhaeyo = False
    start_time = time.time()

    if Min_number < its_number < Max_number:
        print('중간수량 : 설정 레벨로 진행합니다.')
        pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+(Making_Level-1)*153+account*540) # 1렙이면 200. 2~3렙은 153씩 올라감
        pag.mouseDown()
        time.sleep(0.7)
        pag.mouseUp()
        time.sleep(0.5)
        Skip_Next(account, prod_direction_left)
        return bujockhaeyo
    
    if  Min_number >= its_number:  # 최소수량 이하이면 1렙 고정.
        print('위험수량 : 1레벨로 생산합니다.')

        while True:
            now_time = time.time()
            if now_time - start_time > 30:
                return
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)

            if keyboard.is_pressed('end'):
                print('end 누름')
                break
            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
            if (prod_refresh):
                pag.click(prod_refresh) # >> 클릭(즉시생산)
                # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                time.sleep(0.5)
                remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                remain_time_about_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                if (remain_time_less_minute) or (remain_time_about_minute):
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.8)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    break
                else:
                    print('1분 넘게 남아 삭제함돠2')
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                    time.sleep(0.2)
                    pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                    time.sleep(0.2)
            else:
                break
        pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+account*540)
        pag.mouseDown()
        time.sleep(1)
        pag.mouseUp()
        time.sleep(0.5)
        Skip_Next(account, prod_direction_left)
        return bujockhaeyo

    if its_number >= Max_number:
        print('최대수량 : 생산하지 않고 넘어갑니다.')
        screen = ImageGrab.grab()
        pix_lackof = screen.getpixel((545,745-540+account*540)) # 재료부족창?
        pix_lackof1 = (243, 233, 223)   # 베이지색
        if pix_lackof != pix_lackof1:
            pag.click(164,280+account*540)
            time.sleep(0.5)
        return bujockhaeyo

def Skip_Next(account, prod_direction_left):
    if prod_direction_left:    # 이레가 수정햇서
        pag.click(164,280+account*540)
        time.sleep(0.5)
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
                                                      region=(339, 253 + account * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..')
            pag.click(455, 379 + account * 540)
            time.sleep(0.3)
            pag.click(164, 280 + account * 540)
            time.sleep(0.3)
    else:
        pag.click(485,280+account*540)
        time.sleep(0.3)
    
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)
    # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
    # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
    dotdotdot_1 = pag.locateCenterOnScreen('dotdotdot_1.png', confidence=0.87, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_1_1 = pag.locateCenterOnScreen('dotdotdot_1.png', confidence=0.87, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    dotdotdot_2 = pag.locateCenterOnScreen('dotdotdot_2.png', confidence=0.9, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_2_1 = pag.locateCenterOnScreen('dotdotdot_2.png', confidence=0.9, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    dotdotdot_3 = pag.locateCenterOnScreen('dotdotdot_3.png', confidence=0.87, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_3_1 = pag.locateCenterOnScreen('dotdotdot_3.png', confidence=0.87, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    
    if (dotdotdot_1):
        print('dotdotdot_1 = ', dotdotdot_1)
        pag.click(dotdotdot_1)
        time.sleep(0.3)
    if (dotdotdot_1_1):
        print('dotdotdot_1_1 = ', dotdotdot_1_1)
        pag.click(dotdotdot_1_1)
        time.sleep(0.3)
    if (dotdotdot_2):
        print('dotdotdot_2 = ', dotdotdot_2)
        pag.click(dotdotdot_2)
        time.sleep(0.3)
    if (dotdotdot_2_1):
        print('dotdotdot_2_1 = ', dotdotdot_2_1)
        pag.click(dotdotdot_2_1)
        time.sleep(0.3)
    if (dotdotdot_3):
        print('dotdotdot_3 = ', dotdotdot_3)
        pag.click(dotdotdot_3)
        time.sleep(0.3)
    if (dotdotdot_3_1):
        print('dotdotdot_3_1 = ', dotdotdot_3_1)
        pag.click(dotdotdot_3_1)
        time.sleep(0.3)
    return

# 단순 오른쪽으로 돌리는 함수..
def Skip_Right(account):
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    # if prod_direction_left:    # 이레가 수정햇서
    #     pag.click(484,280+account*540)
    #     time.sleep(0.5)
    #     prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
    #                                                   region=(339, 253 + account * 540, 175, 87))
    #     time.sleep(1)
    #     if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
    #         print('욕심을 버리시오 중생이여..오른쪽')
    #         pag.click(455, 379 + account * 540) #확인버튼클릭
    #         time.sleep(0.5)
    #         pag.click(random.randint(462 - 5, 462 + 5), random.randint(377 - 5, 377 + 5) + account * 540)
    #         # pag.click(484, 280 + account * 540)   # 오른쪽으로 옮겨가요
    #         time.sleep(0.5)

    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95, region=(339, 253 + account * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..오른쪽')
            pag.click(455, 379 + account * 540) #확인버튼클릭
            time.sleep(0.5)
            pag.click(random.randint(462 - 5, 462 + 5), random.randint(377 - 5, 377 + 5) + account * 540)
            # pag.click(484, 280 + account * 540)   # 오른쪽으로 옮겨가요
            time.sleep(0.5)
    # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
    # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
    dotdotdot_1 = pag.locateCenterOnScreen('dotdotdot_1.png', confidence=0.87, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_1_1 = pag.locateCenterOnScreen('dotdotdot_1.png', confidence=0.87, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    dotdotdot_2 = pag.locateCenterOnScreen('dotdotdot_2.png', confidence=0.9, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_2_1 = pag.locateCenterOnScreen('dotdotdot_2.png', confidence=0.9, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    dotdotdot_3 = pag.locateCenterOnScreen('dotdotdot_3.png', confidence=0.87, region=(223,190+account*540,205,132))   # 화살표 피한 센터 위치
    dotdotdot_3_1 = pag.locateCenterOnScreen('dotdotdot_3.png', confidence=0.87, region=(150,323+account*540,370,110))   # 화살표 아래 넓은 위치
    
    if (dotdotdot_1):
        print('dotdotdot_1 = ', dotdotdot_1)
        pag.click(dotdotdot_1)
        time.sleep(0.3)
    if (dotdotdot_1_1):
        print('dotdotdot_1_1 = ', dotdotdot_1_1)
        pag.click(dotdotdot_1_1)
        time.sleep(0.3)
    if (dotdotdot_2):
        print('dotdotdot_2 = ', dotdotdot_2)
        pag.click(dotdotdot_2)
        time.sleep(0.3)
    if (dotdotdot_2_1):
        print('dotdotdot_2_1 = ', dotdotdot_2_1)
        pag.click(dotdotdot_2_1)
        time.sleep(0.3)
    if (dotdotdot_3):
        print('dotdotdot_3 = ', dotdotdot_3)
        pag.click(dotdotdot_3)
        time.sleep(0.3)
    if (dotdotdot_3_1):
        print('dotdotdot_3_1 = ', dotdotdot_3_1)
        pag.click(dotdotdot_3_1)
        time.sleep(0.3)
    return

def Wood_to_Cotton_Quick(account, Max_number, Making_Level, prod_direction_left):   # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
    prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
        time.sleep(0.5)
    # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
    prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
    # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!3')
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
                                                      region=(339, 253 + account * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..')
            pag.click(455, 379 + account * 540)
            time.sleep(0.3)
            pag.click(487, 280 + account * 540)
            time.sleep(0.3)
        else:
            Skip_Next(account, prod_direction_left)

        return True
    else:
        up_1 = pag.locateCenterOnScreen('up_1.png',confidence=0.8,region=(515,47+account*540,14,15))
        if (up_1):
            print('1천대!')
            its_number = 1000
        else:
            up_2 = pag.locateCenterOnScreen('up_2.png',confidence=0.8,region=(515,47+account*540,14,15))
            if (up_2):
                print('2천대!')
                its_number = 2000
            else:
                up_3 = pag.locateCenterOnScreen('up_3.png',confidence=0.8,region=(515,47+account*540,14,15))
                if (up_3):
                    print('3천대!')
                    its_number = 3000
                else:
                    up_4 = pag.locateCenterOnScreen('up_4.png',confidence=0.8,region=(515,47+account*540,14,15))
                    if (up_4):
                        print('4천대!')
                        its_number = 4000
                    else:
                        up_5 = pag.locateCenterOnScreen('up_5.png',confidence=0.8,region=(515,47+account*540,14,15))
                        if (up_5):
                            print('5천대!')
                            its_number = 5000
                        else:
                            up_6 = pag.locateCenterOnScreen('up_6.png',confidence=0.8,region=(515,47+account*540,14,15))
                            if (up_6):
                                print('6천대!')
                                its_number = 6000
                            else:
                                print('1000 미만...')
                                its_number = 999

        # 설정 수량보다 많아지면 걍 넘어가고
        if its_number >= Max_number:
            Skip_Next(account,prod_direction_left)
            return False
        # 설정 수량보다 적으면 생산 렙으로 생산
        else:
            wood_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
            jelbean_list_lv2 = pag.locateCenterOnScreen('jelbean_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
            sugar_list_lv2 = pag.locateCenterOnScreen('sugar_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
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
                    Skip_Next(account, prod_direction_left)
                    return True
                if not wood_clear and not jelbean_clear and not sugar_clear:
                    break
                if wood_clear:
                    wood_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (wood_list_lv2):
                        time.sleep(0.3)
                        pag.click(wood_list_lv2)
                        time.sleep(0.3)
                    else:
                        prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
                        if (prod_refresh):
                            pag.click(prod_refresh) # >> 클릭(즉시생산)
                            # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                            time.sleep(0.5)
                            remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            remain_time_about_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.5)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠3')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                time.sleep(0.2)
                                break
                if jelbean_clear:
                    jelbean_list_lv2 = pag.locateCenterOnScreen('jelbean_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (jelbean_list_lv2):
                        time.sleep(0.3)
                        pag.click(jelbean_list_lv2)
                        time.sleep(0.3)
                    else:
                        prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
                        if (prod_refresh):
                            pag.click(prod_refresh) # >> 클릭(즉시생산)
                            # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                            time.sleep(0.5)
                            remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            remain_time_about_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.5)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠4')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                time.sleep(0.2)
                                break
                if sugar_clear:
                    sugar_list_lv2 = pag.locateCenterOnScreen('sugar_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (sugar_list_lv2):
                        time.sleep(0.3)
                        pag.click(sugar_list_lv2)
                        time.sleep(0.3)
                    else:
                        prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
                        if (prod_refresh):
                            pag.click(prod_refresh) # >> 클릭(즉시생산)
                            # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                            time.sleep(0.5)
                            remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            remain_time_about_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                            if (remain_time_less_minute) or (remain_time_about_minute):
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.5)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠5')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                time.sleep(0.2)
                                break
            pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+(Making_Level-1)*153+account*540) # 1렙이면 200. 2~3렙은 153씩 올라감
            pag.mouseDown()
            time.sleep(1)
            pag.mouseUp()
            time.sleep(0.3)
            Skip_Next(account, prod_direction_left)
            return True


def Updown(account, updown):
    if updown == 'up':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.5)
        pag.moveTo(610,295+account*540-173,2)   # 153인데 20 더 여유줌
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(0.5)
        pag.click(262,328+account*540)
        time.sleep(2)
    if updown == 'down':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.5)
        pag.moveTo(610,295+account*540+173,2)   # 153인데 20 더 여유줌
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(0.5)
        pag.click(262,328+account*540)
        time.sleep(2)
    if updown == 'leftup':
        pag.moveTo(94, 295 + account * 540)
        pag.mouseDown()
        time.sleep(0.5)
        pag.moveTo(94, 295 + account * 540 - 173, 2)  # 153인데 20 더 여유줌
        time.sleep(0.5)
        pag.mouseUp()
        # time.sleep(0.5)
        # pag.click(262, 328 + account * 540)
        time.sleep(2)

def find_train_num(image, account, list_output, line):
    prod_num = pag.locateAllOnScreen(image, confidence=0.83, grayscale=True, region=(375,150+account*540+(line-1)*149,135,24))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def find_sowon_num(image, account, list_output, x1, x2):
    prod_num = pag.locateAllOnScreen(image, confidence=0.83, region=(x1,186+account*540,x2-x1,18))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def Sowon_numb(account):
    slash_found = False
    sowon_num_start_pos = pag.locateCenterOnScreen('sowon_num_start_pos.png', confidence=0.8, region = (439-12-11, 188+account*540, 24+11*2+5+3, 14+2))
    if (sowon_num_start_pos):
        print('sowon_num_start_pos',sowon_num_start_pos)
        x1 = sowon_num_start_pos[0] + 11
    else:
        print('량 : 을 못찾아 437+11로 고정합니다.')
        x1 = 437+11
    sowon_num_slash_1 = pag.locateCenterOnScreen('sowon_num_slash_1.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
    if (sowon_num_slash_1):
        print('sowon_num_slash_1',sowon_num_slash_1)
        x2 = sowon_num_slash_1[0]
        slash_found = True
    sowon_num_slash_2 = pag.locateCenterOnScreen('sowon_num_slash_2.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
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
    find_sowon_num('up_s0.png', account, list_num_0, x1, x2)
    find_sowon_num('up_s0_1.png', account, list_num_0, x1, x2)
    find_sowon_num('up_s1.png', account, list_num_1, x1, x2)
    find_sowon_num('up_s1_1.png', account, list_num_1, x1, x2)
    find_sowon_num('up_s2.png', account, list_num_2, x1, x2)
    find_sowon_num('up_s3.png', account, list_num_3, x1, x2)
    find_sowon_num('up_s4.png', account, list_num_4, x1, x2)
    find_sowon_num('up_s5.png', account, list_num_5, x1, x2)
    find_sowon_num('up_s5_1.png', account, list_num_5, x1, x2)
    find_sowon_num('up_s6.png', account, list_num_6, x1, x2)
    find_sowon_num('up_s7.png', account, list_num_7, x1, x2)
    find_sowon_num('up_s8.png', account, list_num_8, x1, x2)
    find_sowon_num('up_s9.png', account, list_num_9, x1, x2)
    find_sowon_num('up_s0.png', account, list_num_0, x1, x2)
    
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

def Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
    print('[Sowon_Prod_Check - ',pix_status)
    pix_upper_void = (46, 30, 50)    # 이미지 확인공간 대기상태(아무 생산품도 클릭 안함) 
    easy_prod = 0.7     # 1시간 이내 제품
    normal_prod = 0.9   # 1~2시간 제품
    hard_prod = 0.95    # 2시간 초과
    
    pix_wood = (173, 105, 68)
    pix_jelbean = (0, 251, 226)
    pix_sugar = (200, 205, 206)
    pix_biscuit = (178, 93, 24)
    pix_berry = (194, 38, 42)
    pix_milk = (255, 249, 217)
    pix_cotton = (255, 197, 215)
    
    pix_smith_lv1 = (36, 46, 65)
    pix_smith_lv2 = (137, 14, 14)
    pix_smith_lv3 = (75, 92, 112)
    pix_smith_lv4 = (107, 95, 88)
    pix_smith_lv5 = (192, 97, 53)
    pix_smith_lv6 = (120, 144, 163)
    pix_smith_lv7 = (255, 251, 235)
    
    pix_jelly_lv1 = (154, 218, 219)
    pix_jelly_lv2 = (237, 145, 151)
    pix_jelly_lv3 = (216, 141, 17)
    # pix_jelly_lv4 = (192, 3, 78)
    # pix_jelly_lv5 = 
    
    pix_rollc_lv1 = (158, 71, 37)
    pix_rollc_lv2 = (255, 251, 224)
    pix_rollc_lv3 = (107, 124, 52)
    pix_rollc_lv4 = (143, 78, 43)
    
    pix_bread_lv1 = (172, 79, 20)
    pix_bread_lv2 = (150, 11, 24)
    pix_bread_lv3 = (248, 181, 90)
    pix_bread_lv4 = (255, 244, 220)
    pix_bread_lv5 = (197, 120, 36)
    # pix_bread_lv6 = 
    
    pix_jampy_lv1 = (181, 42, 56)
    pix_jampy_lv2 = (230, 168, 67)
    pix_jampy_lv3 = (254, 202, 189)
    pix_jampy_lv4 = (227, 155, 29)
    # pix_jampy_lv5 = (253, 245, 202)
    # pix_jampy_lv6 = 
    
    pix_doye_lv1 = (206, 123, 71)
    pix_doye_lv2 = (175, 183, 220)
    pix_doye_lv3 = (159, 72, 21)
    pix_doye_lv4 = (254, 249, 235)
    
    pix_flower_lv1 = (246, 138, 221)
    pix_flower_lv2 = (136, 67, 16)
    pix_flower_lv3 = (179, 240, 228)
    pix_flower_lv4 = (204, 45, 80)
    pix_flower_lv5 = (184, 197, 232)
    # pix_flower_lv6 = (36, 46, 65)
    
    pix_milk_lv1 = (27, 91, 123)
    # pix_milk_lv2 = (251, 220, 99)
    # pix_milk_lv3 = (123, 171, 186)
    
    pix_latte_lv1 = (249, 244, 213)
    pix_latte_lv2 = (255, 235, 189)
    # pix_latte_lv3 = 
    
    pix_dolls_lv1 = (58, 166, 107)
    pix_dolls_lv2 = (223, 103, 82)
    # pix_dolls_lv3 = 

    pix_beer_lv1 = (208, 148, 91)
    pix_beer_lv2 = (62, 22, 55)
    pix_beer_lv3 = (252, 199, 137)
    
    pix_muffin_lv1 = (186, 89, 55)
    pix_muffin_lv2 = (231, 214, 195)
    # pix_muffin_lv3 = (223, 120, 145)
    
    # pix_jewel_lv1 = (89, 54, 16)
    # pix_jewel_lv2 = (255, 66, 142)
    # pix_jewel_lv3 = (134, 65, 12)
    
    if pix_status == pix_wood:
        print('나무')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_jelbean:
        print('젤리빈')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_sugar:
        print('각설탕')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_biscuit:
        print('비스킷 가루')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_berry:
        print('젤리베리')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_milk:
        print('우유')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False

    elif pix_status == pix_cotton:
        print('솜')
        if Sowon_numb(account) > 1000:
            return True
        else:
            return False
    
    elif pix_status == pix_smith_lv1:
        print('단단 도끼')
        if Sowon_numb(account) > smith_lev1*easy_prod:
            return True
        else:
            return False
    elif pix_status == pix_smith_lv2:
        print('튼튼 곡괭이',smith_lev2)
        if Sowon_numb(account) > smith_lev2*easy_prod:
            return True
        else:
            return False
    elif pix_status == pix_smith_lv3:
        print('슥삭슥삭 톱',smith_lev3)
        if Sowon_numb(account) > smith_lev3*easy_prod:
            return True
        else:
            return False
    elif pix_status == pix_smith_lv4:
        print('푹푹 삽',smith_lev4)
        if Sowon_numb(account) > smith_lev4*easy_prod:
            return True
        else:
            return False
    elif pix_status == pix_smith_lv5:
        print('신비한 프레첼 말뚝',smith_lev5)
        if Sowon_numb(account) > smith_lev5*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_smith_lv6:
        print('영롱한 푸른사탕 집게',smith_lev6)
        if Sowon_numb(account) > smith_lev6*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_smith_lv7:
        print('불변의 슈가 코팅 망치',smith_lev7)
        if Sowon_numb(account) > smith_lev7*hard_prod:
            return True
        else:
            return False


    elif pix_status == pix_jelly_lv1:
        print('젤리빈 잼',jelly_lev1)
        if Sowon_numb(account) > jelly_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_jelly_lv2:
        print('스윗젤리 잼',jelly_lev2)
        if Sowon_numb(account) > jelly_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_jelly_lv3:
        print('달고나 잼',jelly_lev3)
        if jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > jelly_lev3*easy_prod:
                return True
            else:
                return False

    # elif pix_status == pix_jelly_lv4:
    #     print('석류 잼',jelly_lev4)
    #     if jjokji_milk or jjokji_cotton:
    #         return False
    #     else:
    #         if Sowon_numb(account) > jelly_lev4*normal_prod:
    #             return True
    #         else:
    #             return False

    # elif pix_status == pix_jelly_lv5:
    #     print('톡톡베리 잼',jelly_lev5)
    #     if Sowon_numb(account) > jelly_lev5*hard_prod:
    #         return True
    #     else:
    #         return False

    
    elif pix_status == pix_rollc_lv1:
        print('솔방울새 인형',rollc_lev1)
        if Sowon_numb(account) > rollc_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_rollc_lv2:
        print('도토리 램프',rollc_lev2)
        if jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > rollc_lev2*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_rollc_lv3:
        print('뻐꾹뻐꾹 시계',rollc_lev3)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > rollc_lev3*normal_prod:
                return True
            else:
                return False

    elif pix_status == pix_rollc_lv4:
        print('백조깃털 드림캐쳐',rollc_lev4)
        if jjokji_biscuit or jjokji_berry or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > rollc_lev4*hard_prod:
                return True
            else:
                return False

    
    elif pix_status == pix_bread_lv1:
        print('든든한 호밀빵',bread_lev1)
        if jjokji_biscuit:
            return False
        else:
            if Sowon_numb(account) > bread_lev1*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_bread_lv2:
        print('달콤쫀득 잼파이',bread_lev2)
        if jjokji_biscuit:
            return False
        else:
            if Sowon_numb(account) > bread_lev2*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_bread_lv3:
        print('은행 포카치아',bread_lev3)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > bread_lev3*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_bread_lv4:
        print('슈가코팅 도넛',bread_lev4)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > bread_lev4*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_bread_lv5:
        print('폭신 카스테라',bread_lev5)
        if jjokji_milk:
            return False
        else:
            if Sowon_numb(account) > bread_lev5*normal_prod:
                return True
            else:
                return False

    # elif pix_status == pix_bread_lv6:
    #     print('골드리치 크로와상',bread_lev6)
    #     if Sowon_numb(account) > bread_lev6*hard_prod:
    #         return True
    #     else:
    #         return False
    
    elif pix_status == pix_jampy_lv1:
        print('따끈따끈 젤리스튜',jampy_lev1)
        if jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > jampy_lev1*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_jampy_lv2:
        print('곰젤리 버거',jampy_lev2)
        if jjokji_biscuit:
            return False
        else:
            if Sowon_numb(account) > jampy_lev2*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_jampy_lv3:
        print('캔디크림 파스타',jampy_lev3)
        if jjokji_biscuit or jjokji_milk:
            return False
        else:
            if Sowon_numb(account) > jampy_lev3*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_jampy_lv4:
        print('폭신폭신 오므라이스',jampy_lev4)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > jampy_lev4*normal_prod:
                return True
            else:
                return False

    # elif pix_status == pix_jampy_lv5:
    #     print('콤비네이션 피자젤리',jampy_lev5)
    #     if Sowon_numb(account) > jampy_lev5*hard_prod:
    #         return True
    #     else:
    #         return False

    # elif pix_status == pix_jampy_lv6:
    #     print('고급스러운 젤리빈 정식',jampy_lev6) 
    #     if Sowon_numb(account) > jampy_lev6*hard_prod:
    #         return True
    #     else:
    #         return False

    
    elif pix_status == pix_doye_lv1:
        print('비스킷 화분',doye_lev1)
        if jjokji_biscuit:
            return False
        else:
            if Sowon_numb(account) > doye_lev1*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_doye_lv2:
        print('반짝반짝 유리판',doye_lev2)
        if jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > doye_lev2*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_doye_lv3:
        print('반짝이는 색동구슬',doye_lev3)
        if jjokji_biscuit or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > doye_lev3*normal_prod:
                return True
            else:
                return False

    elif pix_status == pix_doye_lv4:
        print('무지갯빛 디저트 보울',doye_lev4)
        if jjokji_milk or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > doye_lev4*hard_prod:
                return True
            else:
                return False

    
    elif pix_status == pix_flower_lv1:
        print('캔디꽃',flower_lev1)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > flower_lev1*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_flower_lv2:
        print('행복한 꽃화분',flower_lev2)
        if jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > flower_lev2*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_flower_lv3:
        print('캔디꽃다발',flower_lev3)
        if jjokji_biscuit or jjokji_berry or jjokji_milk:
            return False
        else:
            if Sowon_numb(account) > flower_lev3*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_flower_lv4:
        print('롤리팝 꽃바구니',flower_lev4)
        if jjokji_biscuit:
            return False
        else:
            if Sowon_numb(account) > flower_lev4*normal_prod:
                return True
            else:
                return False

    elif pix_status == pix_flower_lv5:
        print('유리꽃 부케',flower_lev5)
        return False
        # if Sowon_numb(account) > flower_lev5*hard_prod:
        #     return True
        # else:
        #     return False

    # elif pix_status == pix_flower_lv6:
    #     print('찬란한 요거트 화환',flower_lev6)
    #     return False
    #     # if Sowon_numb(account) > flower_lev6*hard_prod:
    #     #     return True
    #     # else:
    #     #     return False

    
    elif pix_status == pix_milk_lv1:
        print('크림',milky_lev1)
        if jjokji_milk:
            return False
        else:
            if Sowon_numb(account) > milky_lev1*easy_prod:
                return True
            else:
                return False

    # elif pix_status == pix_milk_lv2:
    #     print('버터',milky_lev2)
    #     if Sowon_numb(account) > milky_lev2*normal_prod:
    #         return True
    #     else:
    #         return False

    # elif pix_status == pix_milk_lv3:
    #     print('수제 치즈',milky_lev3)
    #     if Sowon_numb(account) > milky_lev3*hard_prod:
    #         return True
    #     else:
    #         return False

    
    elif pix_status == pix_latte_lv1:
        print('젤리빈 라떼',latte_lev1)
        if jjokji_milk:
            return False
        else:
            if Sowon_numb(account) > latte_lev1*easy_prod:
                return True
            else:
                return False

    elif pix_status == pix_latte_lv2:
        print('몽글몽글 버블티',latte_lev2)
        if jjokji_biscuit or jjokji_berry or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > latte_lev2*hard_prod:
                return True
            else:
                return False

    # elif pix_status == pix_latte_lv3:
    #     print('스윗베리 에이드',latte_lev3) 
    #     if Sowon_numb(account) > latte_lev3*hard_prod:
    #         return True
    #     else:
    #         return False

    
    elif pix_status == pix_dolls_lv1:
        print('구름사탕 쿠션',dolls_lev1)
        if jjokji_biscuit or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > dolls_lev1*normal_prod:
                return True
            else:
                return False

    elif pix_status == pix_dolls_lv2:
        print('곰젤리 솜인형',dolls_lev2)
        if jjokji_biscuit or jjokji_berry or jjokji_milk or jjokji_cotton:
            return False
        else:
            if Sowon_numb(account) > dolls_lev2*hard_prod:
                return True
            else:
                return False

    # elif pix_status == pix_dolls_lv3:
    #     print('용과 드래곤 솜인형',dolls_lev3) 
    #     return False
    #     # if Sowon_numb(account) > dolls_lev3*hard_prod:
    #     #     return True
    #     # else:
    #     #     return False

    elif pix_status == pix_beer_lv1:
        print('크림 루트비어',beer_lev1)
        if jjokji_biscuit or jjokji_berry:
            return False
        else:
            if Sowon_numb(account) > beer_lev1*normal_prod:
                return True
            else:
                return False

    elif pix_status == pix_beer_lv2:
        print('레드베리 주스',beer_lev2)
        return False
        # if Sowon_numb(account) > beer_lev2*hard_prod:
        #     return True
        # else:
        #     return False

    elif pix_status == pix_beer_lv3:
        print('빈티지 와일드 보틀',beer_lev3)
        return False
        # if Sowon_numb(account) > beer_lev3*hard_prod:
        #     return True
        # else:
        #     return False

    
    # elif pix_status == pix_muffin_lv1:
    #     print('으스스 머핀',muffin_lev1)
    #     if jjokji_biscuit or jjokji_milk:
    #         return False
    #     else:
    #         if Sowon_numb(account) > muffin_lev1*normal_prod:
    #             return True
    #         else:
    #             return False
    #
    # elif pix_status == pix_muffin_lv2:
    #     print('생딸기 케이크',muffin_lev2)
    #     return False
        # if Sowon_numb(account) > muffin_lev2*easy_prod:
        #     return True
        # else:
        #     return False

    # elif pix_status == pix_muffin_lv3:
    #     print('파티파티 쉬폰케이크',muffin_lev3) 
    #     return False
    #     # if Sowon_numb(account) > muffin_lev3*hard_prod:
    #     #     return True
    #     # else:
    #     #     return False
    
    # elif pix_status == pix_jewel_lv1:
    #     print('글레이즈드 링',jewel_lev1)
    #     return False
    #     # if Sowon_numb(account) > jewel_lev1*normal_prod:
    #     #     return True
    #     # else:
    #     #     return False

    # elif pix_status == pix_jewel_lv2:
    #     print('루비베리 브로치',jewel_lev2)
    #     return False
    #     # if Sowon_numb(account) > jewel_lev2*hard_prod:
    #     #     return True
    #     # else:
    #     #     return False

    # elif pix_status == pix_jewel_lv3:
    #     print('로얄 곰젤리 크라운',jewel_lev3)
    #     return False
    #     # if Sowon_numb(account) > jewel_lev3*hard_prod:
    #     #     return True
    #     # else:
    #     #     return False
    
    else:
        if pix_status != pix_upper_void:
            print('뭐지 이건..',pix_status)
            time.sleep(0.5)
            
            pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
            time.sleep(0.5)

def jjokji_check(pos,account):
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        time.sleep(0.5)
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.5)

    jokji1_ok = True
    pix_upper_void = (46, 30, 50)    # 이미지 확인공간 대기상태(아무 생산품도 클릭 안함) 
    # 우하 확인
    pag.click(236+54+(pos-1)*165,317+54+account*540)
    time.sleep(1)
    screen = ImageGrab.grab()
    pix_status = screen.getpixel((460,90+account*540)) # 소원나무 확인 뽀인트
    if pix_status == pix_upper_void:
        print('우하 없고')
    else:
        if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
            pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
            time.sleep(0.5)
        else:
            jokji1_ok = False
            pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
            time.sleep(0.5)

    if jokji1_ok:
        # 좌하 확인
        pag.click(236+(pos-1)*165,317+54+account*540)
        time.sleep(1)
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((460,90+account*540)) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('좌하 없고')
        else:
            if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
    if jokji1_ok:
        # 우상 확인
        pag.click(236+54+(pos-1)*165,317+account*540)
        time.sleep(1)
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((460,90+account*540)) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('우상 없고')
        else:
            if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
    if jokji1_ok:
        # 좌상 확인
        pag.click(236+(pos-1)*165,317+account*540)
        time.sleep(1)
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((460,90+account*540)) # 소원나무 확인 뽀인트
        if pix_status == pix_upper_void:
            print('좌상 없고')
        else:
            if Sowon_Prod_Check(pix_status, jjokji_biscuit, jjokji_berry, jjokji_milk, jjokji_cotton):
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
    
    if jokji1_ok:
        time.sleep(0.5)
        pag.click(random.randint(232,232+60)+(pos-1)*165,random.randint(427,427+20)+account*540)
        print('쪽지 보냅니다!')
        time.sleep(0.5)
        return True
    
    if not jokji1_ok:
        time.sleep(0.5)
        pag.click(random.randint(230,230+65)+(pos-1)*165,random.randint(140,140+10)+account*540)
        time.sleep(0.5)
        print('쪽지 짤라!!')
        return False

# 소원나무 내부 픽셀, 이미지 조건 확인
def Sowon_jjokji_action(jjokji_numb, account, jjokji_limit):
    how_many_jjokji = jjokji_numb
    jjokji_sended = 0
    bEvent_checked = False
    error_count_num = 0
    sowon_jjokji_start = time.time()
    # 소원나무 들어가기
    while True:
        sowon_jjokji_now = time.time()
        if sowon_jjokji_now - sowon_jjokji_start > 30:
            End_kkd(account)
            # Check_Initiating(account)
            # time.sleep(10)
            Kingdom_ready(account,'kkd_out')
            sowon_jjokji_start = time.time()
            
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        act_popup_mark_x = pag.locateCenterOnScreen('act_popup_mark_x.png', confidence=0.9, region=(142,489+account*540,26,26)) # 왕국활동 팝업?
        if (act_popup_mark_x):
            print('팝업!!')
            act_sowon = pag.locateCenterOnScreen('act_sowon.png', confidence=0.9, region=(130,420+account*540,50,50)) # 왕국활동 팝업?
            if (act_sowon):
                print('소원나무 들어간닷!')
                pag.click(act_sowon)
                time.sleep(2)
            else:
                print('왕국 활동 - 소원나무 아이콘 어딨대요?')
                Kingdom_ready(account, 'kkd_out')


        else:
            cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430,45+account*540,31,35))    # 소원나무
            if (cond_kkd_sowon):
                print('소원나무 들어왔슴돠! 나감돠!')
                break
            else:
                print('왕국활동 눌러!')
                time.sleep(2)
                error_count_num =error_count_num +1
                if(error_count_num == 3):
                    Kingdom_ready(account, 'kkd_out')
                else:
                    screen = ImageGrab.grab()
                    pix_status = screen.getpixel((605, 55 + account * 540))  # 상단골드
                    pix_status_in = (194, 143, 10)  # 생산건물 내
                    pix_status_in_dark = (97, 72, 5)  # 건물 안이긴 한데 창이 떠있음
                    if (pix_status == pix_status_in) or (pix_status == pix_status_in_dark):
                        Kingdom_ready(account, 'kkd_out')
                    else:
                        time.sleep(1)
                        pag.click(random.randint(142,142+26),random.randint(489,489+26)+account*540)
                        time.sleep(1)

    wait_jjokji1 = True
    wait_jjokji2 = True
    wait_jjokji3 = True
    wait_jjokji4 = True
    if jjokji_limit:  # 쪽지 보상까지만 진행?
        jjokji_today_complete = pag.locateCenterOnScreen('jjokji_today_complete.png', confidence = 0.85, region = (53,428+account*540,68,25))
        if (jjokji_today_complete): # 오늘 보상 다 받았으면 나감
            pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
            time.sleep(3)
            Kingdom_ready(account,'kkd_out')
            return True
    wait_count = 0
    sowon_jjokji_start = time.time()
    # 소원나무 쪽지 작업 시작
    while True:
        sowon_jjokji_now = time.time()
        if sowon_jjokji_now - sowon_jjokji_start > 300:
            End_kkd(account)
            # Check_Initiating(account)
            # time.sleep(10)
            Kingdom_ready(account,'kkd_out')
            return
        
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        if not bEvent_checked:
            cond_sowon_event = pag.locateCenterOnScreen('cond_sowon_event.png', confidence=0.85, region=(104,317+account*540,30,14))    # 소원나무 x5 이벤트
            if (cond_sowon_event):
                bSowonEvent = True
                bEvent_checked = True

        screen = ImageGrab.grab()
        pix_status = screen.getpixel((460,90+account*540)) # 소원나무 확인 뽀인트
        pix_reward = screen.getpixel((36,339+account*540)) # 소원나무 일일보상 칸 좌상단
        pix_upper_void = (46, 30, 50)    # 이미지 확인공간 대기상태(아무 생산품도 클릭 안함)
        pix_give = (121, 207, 12)   # 건네주기(쪽지 열려 있음)
        # pix_wait = (0, 167, 255)    # 갱신하기 후 기다림
        pix_wait = (115, 224, 0)    # 갱신하기 후 기다림
        pix_no_reward = (33, 44, 64)    # 일일보상 대기상태
        pix_yes_reward = (255, 255, 251)    # 일일보상 뜸
        pix_jokji1 = screen.getpixel((265,450+account*540)) # 쪽지1
        pix_jokji2 = screen.getpixel((427,450+account*540)) # 쪽지2
        pix_jokji3 = screen.getpixel((589,450+account*540)) # 쪽지3
        pix_jokji4 = screen.getpixel((751,450+account*540)) # 쪽지4
        pix_jokji1_wait = screen.getpixel((705+85-165*3,224+account*540)) # 쪽지1
        pix_jokji2_wait = screen.getpixel((705+85-165*2,225+account*540)) # 쪽지2
        pix_jokji3_wait = screen.getpixel((705+85-165*1,225+account*540)) # 쪽지3
        pix_jokji4_wait = screen.getpixel((705+85,225+account*540)) # 쪽지4
        # pix_jokji1_wait = screen.getpixel((705-165*3,225+account*540)) # 쪽지1
        # pix_jokji2_wait = screen.getpixel((705-165*2,225+account*540)) # 쪽지2
        # pix_jokji3_wait = screen.getpixel((705-165*1,225+account*540)) # 쪽지3
        # pix_jokji4_wait = screen.getpixel((705,225+account*540)) # 쪽지4
        
        # 일일보상 확인
        if pix_reward == pix_no_reward:
            print('일일보상 No')
        elif pix_reward == pix_yes_reward:
            print('일일보상 받으세요~')
            pag.click(85,385+account*540, 2, 2)
            time.sleep(3.5)
            pag.click(85,385+account*540)
            time.sleep(2)
        else:
            print('뭐지!!!!!!!!!!!!!')
            pag.click(85, 321 + account * 540)
            time.sleep(1)
        
        # 실질적으로 쪽지 보내기
        if pix_status == pix_upper_void:
            print('아이템 확인 대기 상태')
            if pix_jokji1 == pix_give:
                print('쪽지 1 열려있다')
                if jjokji_check(1,account):
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
                        pag.click(190+75, 260+account*540)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji1_wait)
            if pix_jokji2 == pix_give:
                print('쪽지 2 열려있다')
                if jjokji_check(2,account):
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
                        pag.click(190+75+165*1, 260+account*540)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji2_wait)
            if pix_jokji3 == pix_give:
                print('쪽지 3 열려있다')
                if jjokji_check(3,account):
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
                        pag.click(190+75+165*2, 260+account*540)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji3_wait)
            if pix_jokji4 == pix_give:
                print('쪽지 4 열려있다')
                if jjokji_check(4,account):
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
                        pag.click(190+75+165*3, 260+account*540)
                        time.sleep(0.5)
                        print('뭘까??????????????????',pix_jokji4_wait)
        
        if (wait_jjokji1 or wait_jjokji2 or wait_jjokji3 or wait_jjokji4):
            wait_count = 0
        else:
            print('웨잇카운트 쁠쁠')
            wait_count = wait_count + 1
            if wait_count > 5:
                print('쪽지를 %s개 보냈지만 다 대기중이라 나가요!'%(jjokji_sended))
                pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
                time.sleep(4)
                Kingdom_ready(account,'kkd_out')
                return
        
        if jjokji_sended >= how_many_jjokji:
            print('쪽지를 %s개나 보냈어요!'%(jjokji_sended))
            pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
            time.sleep(4)
            Kingdom_ready(account,'kkd_out')
            return
        print('--------절취선--------')    

        time.sleep(1)


def Train_time(account, line):
    train_arrive_time = pag.locateCenterOnScreen('train_arrive_time.png', confidence=0.9, region=(280,150+account*540+(line-1)*149,75,28))
    start_time = time.time()
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        now_time = time.time()
        if now_time - start_time > 30:
            print('동작 최대시간 초과 입니다.')
            return False        
        if keyboard.is_pressed('end'):
            break
        if not (train_arrive_time):
            print('if not 조건')
            train_arrived = pag.locateCenterOnScreen('Cond_train_arrived.png', confidence=0.95, region=(492,118+account*540+(line-1)*149,333,111))
            
            if (train_arrived):
                pag.click(train_arrived)
                time.sleep(3)
            
            send_train = pag.locateCenterOnScreen('Cond_train_send.png', confidence=0.8, region=(500,110+account*540+(line-1)*149,290,120))
            # 색상 구분 못하네....
            send_train_error = pag.locateCenterOnScreen('Cond_train_send_error.png', confidence=0.8, region=(500,110+account*540+(line-1)*149,290,120))
            
            if (send_train):
                print('기차 보내자')
                pag.click(send_train)
                time.sleep(1)
                pag.click(send_train)
                time.sleep(1)
                break
            if (send_train_error):
                print('납품 불가한 제품이 있습니다.')
                time.sleep(1)
                return False
        train_arrive_time_re = pag.locateCenterOnScreen('train_arrive_time.png', confidence=0.9, region=(280,150+account*540+(line-1)*149,75,28))
        if (train_arrive_time_re):
            train_arrive_time = train_arrive_time_re
            break


    print('계정 ',account,' 라인 ',line,'조건')
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
        find_train_num('train_0.png', account, list_num_0, line)
        find_train_num('train_1.png', account, list_num_1, line)
        find_train_num('train_2.png', account, list_num_2, line)
        find_train_num('train_3.png', account, list_num_3, line)
        find_train_num('train_4.png', account, list_num_4, line)
        find_train_num('train_5.png', account, list_num_5, line)
        find_train_num('train_6.png', account, list_num_6, line)
        find_train_num('train_7.png', account, list_num_7, line)
        find_train_num('train_8.png', account, list_num_8, line)
        find_train_num('train_9.png', account, list_num_9, line)
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
            remain_time = time_h*3600+time_m*60
            print('남은 시간(초) =', remain_time)
            return remain_time
        else:
            print('숫자 넘어가는 순간 캐치한듯')
            return False

def Ballon_send(account):
    # bal_lev1 = pag.locateCenterOnScreen('cond_bal_lev1.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev2 = pag.locateCenterOnScreen('cond_bal_lev2.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev3 = pag.locateCenterOnScreen('cond_bal_lev3.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev4 = pag.locateCenterOnScreen('cond_bal_lev4.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev5 = pag.locateCenterOnScreen('cond_bal_lev5.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev6 = pag.locateCenterOnScreen('cond_bal_lev6.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev7 = pag.locateCenterOnScreen('cond_bal_lev7.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev8 = pag.locateCenterOnScreen('cond_bal_lev8.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev9 = pag.locateCenterOnScreen('cond_bal_lev9.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev10 = pag.locateCenterOnScreen('cond_bal_lev10.png', confidence=0.9, region=(2,32+account*540,917,505))
    # bal_lev11 = pag.locateCenterOnScreen('cond_bal_lev11.png', confidence=0.9, region=(2,32+account*540,917,505))
    
    # while True:     # 레벨 선택
    #     pag.click(540, 510+account*540)     #마침표랑 동일위치
    #     time.sleep(1)
    #     pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
    #     time.sleep(0.1)
    #     pag.drag(845,0,1)                   # 오른 아래까지1
    #     time.sleep(1.5)
    #     pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
    #     time.sleep(0.1)
    #     pag.drag(845,0,1)                   # 오른 아래까지2
    #     time.sleep(1.5)
    #     pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
    #     time.sleep(0.1)
    #     pag.drag(845,0,1)                   # 오른 아래까지3
    #     time.sleep(1.5)
    #     pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
    #     time.sleep(0.1)
    #     pag.drag(845,0,1)                   # 오른 아래까지4
    #     time.sleep(1.5)
    #     # pag.click(535,255+account*540)      # 이건 2렙이고
    #     pag.click(750,325+account*540)      # 이건 3렙이고
    #     # pag.click(895,400+account*540)      # 이건 4렙이고
    #     time.sleep(1)
    #     pag.click(345,505+account*540)      # 이건 자동선택이고
    #     time.sleep(0.7)
    #     pag.click(760,505+account*540)      # 이건 보내기고
    #     time.sleep(2)
    error_count = 0
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)
        if keyboard.is_pressed('end'):
            break
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        cond_kkd_balloon = pag.locateCenterOnScreen('cond_kkd_balloon.png', confidence=0.85, region=(9,36+account*540,25,35))               # 열기구 로비
        cond_kkd_balloon_ing = pag.locateCenterOnScreen('cond_kkd_balloon_ing.png', confidence=0.85, region=(364,85+account*540,28,37))     # 열기구 날아다니는 중
        cond_balloon_arrive = pag.locateCenterOnScreen('cond_balloon_arrive.png', confidence = 0.96, region = (2,32+account*540,917,505))   # 열기구 도착 화면
        cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.9, region=(2,32+account*540,917,505))    # 부족!
        pix_status_bal_what = (85, 63, 0)
        pix_status_bal_arrive = (170, 169, 168) # 열기구 보상수령(바닥 글씨 마침표)
        # pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
        pix_status_bal_lobby = (175, 131, 0)  # 열기구 로비
        pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
        pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
        
        if (pix_status == pix_status_bal_window) or (cond_balloon_lack_heart) or (pix_status == pix_status_bal_what):
            print('젤리고기 부족..')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.5)
            pag.hotkey('esc')
            time.sleep(0.3)
            Kingdom_ready(account,'kkd_out')
            break
        
        elif (cond_balloon_arrive):
            print('열기구 도착!')
            error_count = 0
            pag.click(cond_balloon_arrive)
            time.sleep(1)
            
        # 로비..
        elif pix_status == pix_status_bal_lobby or (cond_kkd_balloon):
            error_count = 0
            # pag.click(345,505+account*540)      # 이건 자동선택이고
            time.sleep(1)
            pag.click(760,505+account*540)      # 이건 보내기고
            time.sleep(3)
        
        # 잘 날아감
        elif pix_status == pix_status_ballon or (cond_kkd_balloon_ing):
            print('열기구 나는중!')
            Kingdom_ready(account,'kkd_out')
            return True
        
        else:
            print('열기구 - 남은 조건이 뭐가 있을까..')
            if error_count > 5:
                Kingdom_ready(account,'kkd_out')
                return False
            else:
                error_count = error_count + 1
                time.sleep(1)

def Kingdom_ready(account, whereto):    # 특정 위치 확인
    error_position = 0
    start_time = time.time()
    time.sleep(3)
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        now_time = time.time()
        if keyboard.is_pressed('end'):
            print('end버튼 눌러 종료됨')
            return
        
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status_scr = screen.getpixel((910,55+account*540)) # = 미세 오른쪽
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_in = (194, 143, 10)    # 생산건물 내
        pix_status_in_dark = (97, 72, 5)    #건물 안이긴 한데 창이 떠있음
        # pix_status_out = (0, 181,   255)    # 바탕화면(왕국), 트로피컬도 동일
        pix_status_out = (11, 194, 250)  # 바탕화면(왕국), 트로피컬도 동일  ㅁㅁㅁ수정
        # pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
        pix_status_out_window = (6, 95, 125)  # 창이 떠서 어두워짐
        # pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
        pix_status_out_esc = (6, 97, 124)  # 왕국.. ESC나 트로피컬 썬배드로 어두워진..ㅁㅁㅁ수정
        # pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
        pix_status_sowon = (255, 208, 3)  # 소원나무, 곰젤리열차, 상점 동일 헷갈려 ㅁㅁㅁ수정
        pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
        # pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
        pix_status_bal_lobby = (175, 131, 0)  # 열기구 로비
        pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
        pix_status_adv = (14, 167, 251)   # 모험하기
        pix_status_kdpass = (42, 27, 19)  # 킹덤패스
        pix_status_warehouse = (55, 64, 105) # 창고 뜸
        pix_status_mail = (60, 70, 105)   # 우편함
        pix_lackof1 = (243, 233, 223)   # 베이지색
        # pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
        pix_status_not_prod = (8, 133, 172)  # 건물 클릭했지만 생산 건물은 아님
        # pix_status_cookiehouse = (0, 129, 182)  # 엥 이게 다 달라?
        pix_status_cookiehouse = (84, 93, 134)  # 엥 이게 다 달라?
        # pix_status_lotto = (255, 189, 8)    # 뽑기, 해변교역소
        pix_status_lotto = (255, 208, 2)    # 뽑기, 해변교역소
        pix_status_mycookie = (0, 0, 0) #내 쿠키...으... 움직이면 틀어질텐데
        pix_status_fountain = (84, 93, 134) # 분수..
        # pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
        pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
        pix_status_trade = (255, 216, 2)    # 해상무역센터 로비
        pix_status_wanted = (29, 10, 12)    # 오늘의 현상수배 선택하는 곳
        pix_status_fight_comp = (168, 167, 167) # 모험 전투 후

        pix_status_scr1 = screen.getpixel((65, 505 + account * 540))  # = 왼쪽아래 건설하기 아이콘쪽
        pix_status1_tropical = (255, 98, 170)   # 트로피칼이다
        pix_status1_tropical_windowopen = (127, 49, 85)   # 트로피칼에 메뉴창 떠있다

        
        # 220203 추가 - 이미지 확인방식 추가(업뎃 후 픽셀값 변경...)
        cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국
        cond_kkd_train = pag.locateCenterOnScreen('cond_kkd_train.png', confidence=0.85, region=(30,42+account*540,25,33))  # 곰젤리열차
        cond_kkd_tro = pag.locateCenterOnScreen('cond_kkd_tro.png', confidence=0.85, region=(18,448+account*540,45,40))    # 트로피칼(좌하단 파라솔 꽃)
        cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430,45+account*540,31,35))    # 소원나무
        cond_kkd_sangjum = pag.locateCenterOnScreen('cond_kkd_sangjum1.png', confidence=0.85, region=(14,40+account*540,46,29))   # 상점
        cond_kkd_balloon = pag.locateCenterOnScreen('cond_kkd_balloon.png', confidence=0.85, region=(9,36+account*540,25,35))   # 열기구(대기)
        cond_kkd_balloon_ing = pag.locateCenterOnScreen('cond_kkd_balloon_ing.png', confidence=0.85, region=(364,85+account*540,28,37))   # 열기구(대기)
        adv_worldmap = pag.locateCenterOnScreen('adv_worldmap.png', confidence=0.85, region=(33,467+account*540,52,43))   # 좌하단 월드맵 아이콘(트로피칼과 차이점)
        cond_gold = pag.locateCenterOnScreen('cond_gold.png', confidence=0.8, region=(310,35+account*540,555,50))           # 골드 위치
        cond_gnome = pag.locateCenterOnScreen('cond_gnome.png', confidence=0.8, region=(310,35+account*540,555,50))         # 노움 위치
        cond_diamond = pag.locateCenterOnScreen('cond_diamond.png', confidence=0.8, region=(310,35+account*540,555,50))     # 다이아 위치
        cond_meatjelly = pag.locateCenterOnScreen('cond_meatjelly.png', confidence=0.8, region=(310,35+account*540,555,50))   # 고기젤리 위치
        in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8, region=(2,32+account*540,917,505))             # 건물 안
        cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12,38+account*540,37,36))  # Play버튼 누른 후 모험하기 창
        cond_kkd_arena = pag.locateCenterOnScreen('cond_kkd_arena.png', confidence=0.8, region=(2,32+account*540,917,505))      # 킹덤아레나
        cond_reward = pag.locateCenterOnScreen('cond_reward.png', confidence=0.8, region=(2,32+account*540,917,505))      # 미션 보상받기
        mark_x_mission = pag.locateCenterOnScreen('mark_x_mission.png', confidence=0.8, region=(778,124+account*540,50,50))      # 미션 취소
        cond_error_page = pag.locateCenterOnScreen('cond_error_page.png', confidence=0.8, region=(2,32+account*540,917,505))      # 검은 바탕... 렉 등에 의한 오류?
        kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8,region=(2, 32 + account * 540, 917, 505))
        print('[Kingdom_ready] 현재 픽셀값 : ', pix_status)
        print('[Kingdom_ready] 실행 %s초 지났습니다.'%(now_time - start_time))

        if(kkd_start_ire):
            Check_Initiating(account)

        if (cond_gold):
            # 혹시 또 1픽셀씩 오갈 수 있..으니?
            if 593 >= cond_gold.x >= 591:
                # 소원,열차,상점,쿠키성 중 하나!
                if not (cond_kkd_sowon) and not (cond_kkd_train) and not (cond_kkd_sangjum):
                    print('쿠키성이네요!')
                    pag.click(284,15+account*540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(1)
            # if 593 >= cond_gold.x >= 591:
            #     print('ggg')
        
        if (cond_reward):
            pag.click(cond_reward)
            time.sleep(2)
        
        if (mark_x_mission):
            pag.click(mark_x_mission)
            time.sleep(1)
        
        # 상하단 픽셀 위치 모두 (0, 0, 0)이고 esc 누른 경우
        if pix_status == (0, 0, 0) and pix_status == (0, 0, 0) and (cond_error_page):
            End_kkd(account)                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
            Kingdom_ready(account,'kkd_out')            # 재부팅

        if pix_status == pix_status_in or (in_pos):   # 건물 안 ok
            print('건물 안이네요!')
            if (pix_status == whereto) or (whereto == 'prod_in'):
                return True
            else:
                if whereto == 'prod_in':
                    return False
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(0.3)
            
        elif pix_status == pix_status_in_dark:    # 건물 안에서 창이 떠있으면 esc
            print('건물 내부 : 창은 닫자.')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(0.3)

        elif pix_status == pix_status_trade:    # 무역센터
            print('무역센터 내부!')
            if (pix_status == whereto) or (whereto == 'trade_in'):
                print('무역센터야!')
                return True
            else:
                if whereto == 'trade_in':
                    return False
                print('무역센터 아니야!')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)
        
        elif (cond_gnome):
            if whereto == 'research_in':
                print('연구소 옥희')
                return True
            else:
                print('연구소 안희야')
                pag.click(891,54+account*540)
                time.sleep(3)
                
        elif pix_status == pix_status_fountain:    # 분수 내부
            print('분수 내부!')
            if (pix_status == whereto) or (whereto == 'fountain_in'):
                print('분수?')
                return True
            else:
                if whereto == 'fountain_in':
                    return False
                print('분수 아니야!')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

        elif pix_status == pix_status_adv:    # 모험하기
            if (pix_status == whereto) or (whereto == 'mohum'):
                print('모험하기?')
                return True
            else:
                if whereto == 'mohum':
                    return False
                print('모험은 아...직?')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

        elif pix_status == pix_status_wanted:    # 현상수배 하기
            if (pix_status == whereto) or (whereto == 'wanted'):
                print('현상수배하기?')
                return True
            else:
                if whereto == 'wanted':
                    return False
                print('현상수배 선택 창이네?')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

        elif pix_status2 == pix_status_wanted:    # 현상수배 전투 종료
            if (pix_status == whereto) or (whereto == 'wanted_end'):
                print('현상수배 전투 완료!!')
                pag.click(540,510+account*540)
                time.sleep(2)
                return True
            else:
                if whereto == 'wanted_end':
                    print('현상수배 전투중!')    
                    return False
                print('현상수배 전투중!')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

        elif pix_status == pix_status_kdpass:    # 킹덤패스
            print('킹덤패스! 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(0.3)

        elif pix_status == pix_status_warehouse:    # 창고
            print('창고! 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(0.3)
    
        elif pix_status == pix_status_lotto:    # 뽑기
            print('뽑기 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(0.3)

        elif pix_status == pix_status_mycookie:    # 내 쿠키..
            print('내쿠키 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(0.3)            
        
        elif pix_status == pix_status_not_prod:     # 건물 클릭했지만 쿠하나 일반건물
            print('이상한 건물!')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(1)

        elif (cond_kkd_train):
            if (whereto == 'train_in'):
                print('곰젤리 열차입니다!')
                return True
            else:
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)
                
        elif (cond_kkd_sowon):
            if (whereto == 'sowon_in'):
                print('소원나무 입니다!')
                return True
            else:
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)
             
        elif (cond_kkd_sangjum):
            if (whereto == 'sangjum_in'):
                print('상점 입니다!')
                return True
            else:
                print('상점으로 가려던 게 아니니 나갑니다.')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)

        elif pix_status == pix_status_cookiehouse:
            print('쿠키하우스 안이에요')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(1)

        elif pix_status == pix_status_out_window:
            print('창을 닫아요~')
            pag.click(284,15+account*540)
            time.sleep(0.3)
            pag.hotkey('esc')
            time.sleep(1)
        
        elif pix_status == pix_status_out_esc:
            if (pix_status_scr1 == pix_status1_tropical):   # 트로피컬 메인화면
                pag.click(869, 494+account*540) # 왕국가기 버튼 클릭
                time.sleep(0.5)
                pag.hotkey('esc')
                time.sleep(1)
            
            if(pix_status_scr1 == pix_status1_tropical_windowopen): # 트로피컬 메뉴화면
                pag.hotkey('esc')
                pag.click(869, 494+account*540) # 왕국가기 버튼 클릭
                time.sleep(0.5)
                pag.hotkey('esc')
                time.sleep(1)
            
            else:
                print('esc 취소')
                cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.96, region=(2,32+account*540,917,505))
                if (cond_balloon_lack_heart):
                    print('cond_balloon_lack_heart',cond_balloon_lack_heart)
                    pag.click(cond_balloon_lack_heart)
        
        elif (cond_kkd_out):
            if (cond_gold):
                if (cond_kkd_arena):
                    print('킹덤아레나인가요?')
                    pag.click(605,55+account*540)
                    time.sleep(1)
                else:
                    print('왕국이네요!')
                    if (whereto == 'kkd_out'):
                        return True
                    elif (whereto == 'tropical_in'):
                        print('왕국인데 트로피칼 볼래요')
                        if Tropical_Event(account):     # 트로피칼에 이벤트 없으면
                            print('트로피칼 입장!')
                            return True
                        else:
                            print('트로피칼 이벤트 없어서 들어가지 않습니다.')
                            return False
                    else:
                        return False
                        
            else:
                print('왕국이긴 한데 이상한 건물인가 봅니다.')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.7)
        
        elif pix_status == pix_stats_kkd_start:
            print('꺼졌네요... 재실행')
            Check_Initiating(account)
            Kingdom_ready(account,'kkd_out')

        elif pix_status == pix_status_ballon or (cond_kkd_balloon_ing):    # 열기구
            print('열기구 날아다니는 중!')
            if (pix_status == whereto) or (whereto == 'balloon_in'):
                return True
            else:
                if whereto == 'balloon_in':
                    return False
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(2)
        
        elif pix_status == pix_status_bal_lobby or (cond_kkd_balloon):
            if (pix_status == whereto) or (whereto == 'balloon_in'):
                print('열기구 놀고 있네요')
                return True
            else:
                print('열기구 보내고 나갈께요!')
                Ballon_send(account)
                return False
        
        elif (cond_kkd_tro):
            if (whereto == 'tropical_in'):
                print('트로피칼 들어왔습니다!')
                return True
            else:
                # print('트로피칼 들어와서 돌리고 나갑니다.')
                # Tropical_Fight(account)
                print('트로피칼이 목적지가 아님니닷')
                pag.click(284,15+account*540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(2)
                pag.hotkey('esc')
                time.sleep(2)
        
        else:
            # 여기를 수정할거야 이레
            if not (pix_status2 == 'wanted_end'):
                print('그 모든 게 아니라면....')
                if error_position == 0:
                    pag.click(284,45+account*540)
                    time.sleep(2)
                    pag.hotkey('esc')
                    time.sleep(2)
                    pag.hotkey('alt','up')
                    time.sleep(2)
                if error_position == 1:
                    pag.click(284, 45 + account * 540)
                    time.sleep(2)
                    pag.hotkey('esc')
                    time.sleep(2)
                    # pag.hotkey('alt', 'up')
                if error_position == 2:
                    # pag.click(284, 45 + account * 540)
                    time.sleep(3)
                    pag.hotkey('esc')
                    time.sleep(3)
                    pag.hotkey('esc')
                if error_position == 3:
                    pag.click(605,55+account*540)
                    time.sleep(5)
                if error_position == 6:
                    pag.click(284,45+account*540)
                    time.sleep(2)
                    pag.hotkey('alt','up')
                    time.sleep(2)
                if error_position == 7:
                    time.sleep(2)
                    pag.hotkey('alt', 'up')
                    time.sleep(2)
                if error_position > 7:
                    pag.click(944,520+account*540)
                    time.sleep(7)
                    pag.click(687, 84 + account * 540)
                    time.sleep(7)
                    Check_Initiating(account)
                    time.sleep(3)
                    error_position = 0
                print('Error count =', error_position)
                error_position = error_position +1
            else:
                print('여긴 안도니')
                time.sleep(5)
                return False

# 테두리 사라져서 한참 반복하는 경우 재부팅
def End_kkd(account):
    pag.click(284,15+account*540)
    time.sleep(0.3)
    pag.click(940,520+account*540)
    time.sleep(3)
    pag.click(677,137+account*540)
    time.sleep(5)
    return

# 220201 모험하기 때 속도 x1.5 체크하기
def Adv_SpeedChk(account):
    start_time = time.time()
    # 자동 전투 켜져있는지 확인
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            return
        now_time = time.time()
        cond_adv_automode = pag.locateCenterOnScreen('cond_adv_automode.png', confidence=0.85, region=(39,433+account*540,12,14))   # 황금 "동" 글씨
        cond_adv_not_automode = pag.locateCenterOnScreen('cond_adv_not_automode.png', confidence=0.85, region=(39,433+account*540,12,14))   # 회색 "동" 글씨
        if (cond_adv_not_automode):
            pag.click(cond_adv_not_automode)
        if (cond_adv_automode):
            print('자동 모드 돌고 있네요!')
            break
    # x1.5배 전투인지 확인
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            return
        now_time = time.time()
        adv_speed1 = pag.locateCenterOnScreen('adv_speed1.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        adv_speed2 = pag.locateCenterOnScreen('adv_speed2.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        adv_speed3 = pag.locateCenterOnScreen('adv_speed3.png', confidence=0.85, region=(35,497+account*540,20,15))   # 12렙 맵
        if (adv_speed1):
            pag.click(adv_speed1)
            time.sleep(0.5)
        if (adv_speed2):
            pag.click(adv_speed2)
            time.sleep(0.5)
        if (adv_speed3):
            print('1.5배 ok')
            print(now_time - start_time)
            break
        if now_time - start_time > 10:
            print('[시간초과] 모험하기 속도 x1.5인지 확인하세요!')
            break
    return

def Tropical_Event(account):
    bStep1_play = False        # 플레이 버튼을 눌렀는가?
    error_count = 0
    start_time = time.time()
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            return False
        now_time = time.time()
        if now_time - start_time > 900:
            End_kkd(account)                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12,38+account*540,37,36))  # Play버튼 누른 후 모험하기 창
        cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국
        cond_adv_tro_mode = pag.locateCenterOnScreen('cond_adv_tro_mode.png', confidence=0.85, region=(2,32+account*540,917,505))   # 트로피컬 소다제도의 '도'
        cond_adv_tro = pag.locateCenterOnScreen('cond_adv_tro.png', confidence=0.85, region=(2,32+account*540,917,505))             # '도' 위에 이벤트 있는 경우 빨간 말풍선
        time.sleep(2)
        # 바탕화면도 모험하기도 아니면 우선 바탕화면으로
        if not (cond_kkd_out) and not (cond_adv_mode_select):
            print('왕국도 모험하기 화면도 아니네요!')
            Kingdom_ready(account,'kkd_out')
            
        # 모험하기 화면
        if not bStep1_play and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if (pix_status == pix_status_out or (cond_kkd_out)) and not bStep1_play:
            print('트로피칼 확인해볼까? Play 버튼 클릭~!')
            pag.click(random.randint(730,785),random.randint(470+account*540,525+account*540))
            time.sleep(3)

        if bStep1_play:
            if (cond_adv_tro_mode):
                print('트로피컬 소다제도 글씨 확인!')
                if (cond_adv_tro):
                    print('재점령 당한 곳이 있어 트로피칼 들어갑니다!')
                    pag.click(cond_adv_tro)
                    return True
                else:
                    print('이벤트 없어서 복귀합니다!')
                    pag.click(892,54+account*540)
                    time.sleep(8)
                    return False
                    
            if not (cond_adv_tro_mode):
                print('드래그드래그')
                pag.moveTo(random.randint(730,785),random.randint(470+account*540,525+account*540))
                pag.drag(-300,0,2)       # 현상수배와 반대로.. 왼쪽으로 가야 하니깐 300으로 바꿔주고
                time.sleep(3)
                error_count = error_count+1
                if error_count > 5:
                    print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                    pag.click(892,54+account*540)
                    time.sleep(8)
                    return False

def Tropical_Fight(account):
    bFighting = False
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        if keyboard.is_pressed('end'):
            return
        
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status_scr = screen.getpixel((910,55+account*540)) # = 미세 오른쪽
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_in = (194, 143, 10)    # 생산건물 내
        pix_status_in_dark = (97, 72, 5)    #건물 안이긴 한데 창이 떠있음
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        # pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
        pix_status_out_window = (6, 95, 125)  # 창이 떠서 어두워짐
        pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
        pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
        pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
        pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
        pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
        pix_status_adv = (14, 167, 251)   # 모험하기
        pix_status_kdpass = (42, 27, 19)  # 킹덤패스
        pix_status_warehouse = (55, 64, 105) # 창고 뜸
        pix_status_mail = (60, 70, 105)   # 우편함
        pix_lackof1 = (243, 233, 223)   # 베이지색
        pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
        pix_status_cookiehouse = (0, 129, 182)  # 엥 이게 다 달라?
        pix_status_lotto = (255, 189, 8)    # 뽑기, 해변교역소
        pix_status_mycookie = (0, 0, 0) #내 쿠키...으... 움직이면 틀어질텐데
        pix_status_fountain = (84, 93, 134) # 분수..
        pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
        pix_status_trade = (255, 216, 2)    # 해상무역센터 로비
        pix_status_wanted = (29, 10, 12)    # 오늘의 현상수배 선택하는 곳
        pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
        pix_status_fight_comp1 = (121, 98, 74)   # 모험 전투 후1

        cond_kkd_tro = pag.locateCenterOnScreen('cond_kkd_tro.png', confidence=0.85, region=(18,448+account*540,45,40))    # 트로피칼(좌하단 파라솔 꽃)
        Cond_tropical_knife = pag.locateCenterOnScreen('Cond_tropical_knife.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 재점령당한 칼모양
        # Cond_tropical_knife_new = pag.locateCenterOnScreen('Cond_tropical_knife_new.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 재점령당한 칼모양
        Cond_tropical_fight = pag.locateCenterOnScreen('Cond_tropical_fight.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 전투 준비, 시작도 동일한가?
        cond_quick = pag.locateCenterOnScreen('cond_quick.png', confidence=0.8, region=(2,32+account*540,917,505))             # 빨리감기
        cond_quick_button = pag.locateCenterOnScreen('cond_quick_button.png', confidence=0.8, region=(2,32+account*540,917,505))             # 빨리감기 시작 버튼
        cond_end_fight3 = pag.locateCenterOnScreen('Cond_wanted_go_out.png', confidence=0.95, region=(2,32+account*540,917,505))        # 나가기 버튼

        cond_tropical_exclamation = pag.locateCenterOnScreen('cond_tropical_exclamation.png', confidence=0.95, region=(2,32+account*540,917,505))        # 느낌표

        if bFighting and (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            time.sleep(1)

            pag.click((540,510+account*540))
            bFighting = False

            time.sleep(2)
        
        if bFighting and (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            time.sleep(1)

            pag.click((540,510+account*540))
            bFighting = False

            time.sleep(2)

        # 빨리감기와 전투 버튼이 같이 있으면
        if not bFighting and (cond_quick) and (Cond_tropical_fight):
            # 빨리감기 쓸 경우
            if bQuickUse:
                print('빨리감기 버튼 클릭')
                time.sleep(0.5)
                pag.click(cond_quick)
                time.sleep(1)
            # 빨리감기 안쓸 경우
            else:
                print('빨리감기 아닌 전투 시작')
                pag.click(807,493+account*540)
                bFighting = True

        # 새로 열린 영토 느낌표
        if not bFighting and (cond_tropical_exclamation):
            pag.click(cond_tropical_exclamation)
            time.sleep(2)
            Kingdom_ready(account,'tropical_in')
                
        
        # 칼모양 있고 전투 버튼 없으면 칼을 클릭
        if not bFighting and (Cond_tropical_knife) and not (Cond_tropical_fight):
            print('재점령 당한 곳 클릭!')
            pag.click(Cond_tropical_knife)
            time.sleep(2)
        
        # if not bFighting and (Cond_tropical_knife_new) and not (Cond_tropical_fight):
        #     print('새로 연 곳 클릭!')
        #     pag.click(Cond_tropical_knife_new)
        #     time.sleep(2)
        
        # 칼모양 있고 전투 버튼 있으면 전투 클릭
        if not bFighting and (Cond_tropical_knife) and (Cond_tropical_fight):
            print('전투 로비 들어가기!1')
            pag.click(Cond_tropical_fight)
            time.sleep(2)

        # 칼모양 없고 전투 버튼 있고 빨리감기 없으면 전투 클릭
        if not bFighting and not (Cond_tropical_knife) and (Cond_tropical_fight) and not (cond_quick):
            print('전투 로비 들어가기!2')
            pag.click(Cond_tropical_fight)
            time.sleep(2)
        
        if not bFighting and (cond_quick_button):
            print('빨리감기 시작')
            pag.click(cond_quick_button)
            time.sleep(6)
            pag.click(460,415+account*540)
            time.sleep(2)
        
        if (cond_end_fight3):   # 나가기 버튼이 있으면
            pag.click(cond_end_fight3) # 눌러~
            time.sleep(3)

        if not bFighting and (cond_kkd_tro) and not (Cond_tropical_knife):
            print('더 돌 곳이 없네요!')
            pag.click(865,492+account*540)
            time.sleep(1)
            pag.click(892,55+account*540)
            time.sleep(1)
            Kingdom_ready(account,'kkd_out')
            return True
        
        print('[트로피칼] 실행중...')

def Enter_Screenshot_mode(account, left_where):
    error_count = 0
    reboot = 0
    drag_times = 0
    Kingdom_ready(account, 'kkd_out')
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        screen = ImageGrab.grab()
        pix_status_scr = screen.getpixel((910,55+account*540)) # = 미세 오른쪽
        pix_clicked = (28, 39, 51)      # 클릭해서 어두워짐

        screen_mode_clicked = pag.locateCenterOnScreen('screen_mode_clicked.png', confidence=0.95, region=(876,42+account*540,27,26))
        screen_mode_not_clicked = pag.locateCenterOnScreen('screen_mode_not_clicked.png', confidence=0.95, region=(874,43+account*540,27,25))
        # 876->874

        print('pix',pix_status_scr)
        if (screen_mode_clicked) or (pix_status_scr == pix_clicked):
            # print('클릭했다!')
            screenshot_mode = pag.locateCenterOnScreen('screenshot_mode.png', confidence=0.95, region=(703,325-55+account*540,112,20+110))
            if (screenshot_mode):
                pag.click(screenshot_mode)
                time.sleep(0.5)
                bScreenshotClicked = True
        elif (screen_mode_not_clicked):
            # print('클릭 안했다!',screen_mode_not_clicked)
            pag.click(random.randint(889-10,889+10),random.randint(45-10,45+10)+account*540)
        else:
            if bScreenshotClicked:
                print('스샷모드 들어왔나 봅니다')
                error_count = 0
                break
            else:
                print('클릭도 안했는데, 어.. 없다면')
                # esc 한번 해보고..
                if error_count == 0:
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                # 쓰기 싫지만 얘도 함 써보고
                if error_count == 1:
                    Kingdom_ready(account,'kkd_out')
                # 재부팅도 함 해보고
                if error_count == 2:
                    End_kkd(account)
                    Kingdom_ready(account,'kkd_out')
                    error_count = 0
                    if reboot == 1:
                        print('재부팅해도 안되는 건 화면 재조정 뿐임다')
                        if account == 0:
                            pag.moveTo(0,280)
                            time.sleep(0.3)
                            pag.dragTo(50,280,1)
                            time.sleep(0.3)
                            pag.hotkey('alt','up')
                            time.sleep(0.5)
                            pag.click(284,15)
                        if account == 1:
                            pag.moveTo(400,1078)
                            time.sleep(0.3)
                            pag.dragTo(400,1028,1)
                            time.sleep(0.3)
                            pag.hotkey('alt','up')
                            time.sleep(0.5)
                            pag.click(284,15+540)
                    if reboot == 2:
                        print('뭐지 왜지 뭘까 왤까 업뎃중이니?')
                    reboot = reboot + 1
                error_count = error_count + 1
        time.sleep(1)
    while bScreenshotClicked:
        print('줌아웃')
        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        pag.moveTo(366,375+account*540)
        time.sleep(0.1)
        pag.keyDown('ctrlleft')
        time.sleep(0.1)
        pag.scroll(-40)
        time.sleep(1)
        pag.scroll(-40)
        time.sleep(1)
        pag.scroll(-40)
        time.sleep(0.1)
        pag.keyUp('ctrlleft')
        time.sleep(1)
        break
    
    while (left_where == 'left_up') and (drag_times < 4):
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
        time.sleep(0.1)
        pag.drag(200, 300, 0.3)
        time.sleep(0.7)
        drag_times = drag_times + 1

    while (left_where == 'left_down') and (drag_times < 4):
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        pag.moveTo(random.randint(215,480),random.randint(375,530)+account*540)     # 왼쪽 아래로 드래그
        time.sleep(0.1)
        pag.drag(random.randint(250,500), random.randint(-300,-150),0.3)
        time.sleep(0.7)
        drag_times = drag_times + 1
    
    pag.click(284,15+account*540)
    time.sleep(0.1)
    pag.hotkey('esc')
    time.sleep(0.5)
    return print('위치 이동 완료!')
    kingdom_ready(account, 'kkd_out')


def Angmu_Enter(account, whereto):
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

    '''
    # 이건 음... 꼭 해야 할까 싶긴 한데 걍 친구 일일 선물 싹 돌리는 거
    while True:
        cond_friends = pag.locateCenterOnScreen('cond_friends.png', confidence=0.9, region=(740,53+account*540,31,17))
        if (cond_friends):
            pag.click(cond_friends)
            time.sleep(1)
        cond_friends_tab = pag.locateCenterOnScreen('cond_friends_tab.png', confidence=0.9, region=(17,130+account*540,31,49))
        if (cond_friends_tab):
            pag.click(cond_friends_tab)
            time.sleep(1)
        cond_friends_send = pag.locateCenterOnScreen('cond_friends_send.png', confidence=0.9, region=(540,495+account*540,35,38))
        if (cond_friends_send):
            pag.click(cond_friends_send)
            time.sleep(1)
        cond_friends_sended = pag.locateCenterOnScreen('cond_friends_sended.png', confidence=0.9, region=(540,495+account*540,35,38))
        if (cond_friends_sended):
            print('친구 보내기 끗!')
            time.sleep(1)
            break
    '''
    event_check_time = time.time()
    # 먼저, 이벤트 있는지 확인
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        event_now_time = time.time()
        if event_now_time - event_check_time > 60:
            print('1분 이상 조건 확인 못함...')
            return True
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        act_popup_mark_x = pag.locateCenterOnScreen('act_popup_mark_x.png', confidence=0.9, region=(142,489+account*540,26,26))

        if whereto == 'fountain':
            print('[왕국활동] 좌상 드래그 한 상태라 가정')
            act_fountain1 = pag.locateCenterOnScreen('act_fountain1.png', confidence=0.88, region=(2,32+account*540,917,505))
            act_fountain2 = pag.locateCenterOnScreen('act_fountain2.png', confidence=0.88, region=(2,32+account*540,917,505))
            act_fountain3 = pag.locateCenterOnScreen('act_fountain3.png', confidence=0.88, region=(2,32+account*540,917,505))
            # 2번이 젤 잘 인식되나..
            if (act_fountain2):
                print('act_fountain2',act_fountain2)
                pag.click(act_fountain2[0]-130,act_fountain2[1]+24)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            elif (act_fountain1):
                print('act_fountain1',act_fountain1)
                pag.click(act_fountain1[0]-130,act_fountain1[1]+24+35)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            elif (act_fountain3):
                print('act_fountain3',act_fountain3)
                pag.click(act_fountain3[0]-130,act_fountain3[1]+24-21)
                time.sleep(0.5)
                bFountain = True
                time.sleep(2)
                break
            else:
                print('화면에 없는뎁쇼...?')
                Enter_Screenshot_mode(account, 'left_up')
        elif whereto == 'guild':
            cond_guild = pag.locateCenterOnScreen('cond_guild.png', confidence=0.9, region=(470,465+account*540,18,19))
            if (cond_guild):
                print('cond_guild',cond_guild)
                time.sleep(2)
                pag.click(cond_guild)
                time.sleep(7)
            else:
                print('길드 보상 수령 완료!')
                return
            cond_guild_in = pag.locateCenterOnScreen('cond_guild_in.png', confidence=0.9, region=(626,477+account*540,19,19))
            if (cond_guild_in):
                time.sleep(2)
                print('cond_guild_in',cond_guild_in)
                pag.click(450,380+account*540)
                time.sleep(3)
                pag.click(450,380+account*540)
                time.sleep(3)
                pag.click(865,500+account*540)
                time.sleep(5)
                Kingdom_ready(account,'kkd_out')
                return
        elif whereto == 'shop':
            cond_shop = pag.locateCenterOnScreen('cond_shop.png', confidence=0.9, region=(45,111+account*540,23,21))
            cond_shop1 = pag.locateCenterOnScreen('cond_shop1.png', confidence=0.9,
                                                 region=(45, 111 + account * 540, 23, 21))
            if (cond_shop) or (cond_shop1):
                if(cond_shop):
                    print('숍1')
                    pag.click(cond_shop)
                elif(cond_shop1):
                    pag.click(cond_shop1)
                    print('숍2')
                time.sleep(1)
                pag.click(44, 138+account*540)
                time.sleep(2)
                bShop = True
                break
                # if Kingdom_ready(account,'sangjum_in'):
                #     bShop = True
                #     break
                # else:
                #     print('상점 진입 실패!')
                #     return False
            else:
                print('[상점] 이벤트 없음')
                Kingdom_ready(account, 'kkd_out')
                return False

        else:
            print('왕국활동 창이 켜져 있으면!')
            # 왕국활동 창이 켜져 있으면
            if (act_popup_mark_x):
                if whereto == 'trade':
                    # 이미지 확인(무역센터 느낌표)
                    activity_trade1 = pag.locateCenterOnScreen('activity_trade1.png', confidence=0.95,
                                                               region=(115, 95 + account * 540, 80, 80))
                    if (activity_trade1):
                        print('[왕국활동] 무역센터 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 무역센터로 들어갑니다.')
                        activity_trade2 = pag.locateCenterOnScreen('activity_trade2.png', confidence=0.95, region=(115, 95 + account * 540, 80, 80))
                        print('[왕국활동] 무역센터로 들어갑니다.111')
                        pag.click(163, 133 + account * 540)
                        time.sleep(2)
                        bTradeEvent = True
                        break
                        # if (activity_trade2):
                        #     # time.sleep(1)
                        #     # pag.click(activity_trade2)
                        #     # bTradeEvent = True
                        #     # break
                        #     print('[왕국활동] 무역센터로 들어갑니다.111')
                        #     pag.click(163, 133 + account * 540)
                        #     time.sleep(2)
                        #     bTradeEvent = True
                        #     break
                        # else:
                        #     print('왜 없어?')
                        #     return False
                        # pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540)
                        # time.sleep(2)
                        # bTradeEvent = True
                        # break
                if whereto == 'research':
                    # 이미지 확인(연구소 느낌표)
                    if Kingdom_ready(account, 'research_in'):
                        bResearchEvent = True
                        break
                    else:
                        activity_research = pag.locateCenterOnScreen('activity_research.png', confidence=0.95,
                                                                     region=(115, 95 + 76 * 1 + account * 540, 80, 80))
                        if (activity_research):
                            print('[왕국활동] 연구소 이벤트가 없습니다.')
                            return False
                        else:
                            print('[왕국활동] 연구소 들어갑니다.')
                            pag.click(random.randint(155 - 10, 155 + 10),
                                      random.randint(135 - 10, 135 + 10) + account * 540 + 76)
                            time.sleep(2)
                            bResearchEvent = True
                            break

                if whereto == 'balloon':
                    # 이미지 확인(열기구 느낌표)
                    activity_balloon = pag.locateCenterOnScreen('activity_balloon.png', confidence=0.95,
                                                                region=(115, 95 + 76 * 2 + account * 540, 80, 80))
                    if (activity_balloon):
                        print('[왕국활동] 열기구 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 열기구 들어갑니다.')
                        pag.click(random.randint(155 - 10, 155 + 10),
                                  random.randint(135 - 10, 135 + 10) + account * 540 + 76 * 2)
                        time.sleep(2)
                        bBalloonEvent = True
                        break
                if whereto == 'train':
                    # 이미지 확인(열차 느낌표)
                    activity_train = pag.locateCenterOnScreen('activity_train.png', confidence=0.95,
                                                              region=(115, 95 + 76 * 3 + account * 540, 80, 80))
                    if (activity_train):
                        print('[왕국활동] 곰젤리 열차 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 곰젤리 열차 들어갑니다.')
                        pag.click(random.randint(155 - 10, 155 + 10),
                                  random.randint(135 - 10, 135 + 10) + account * 540 + 76 * 3)
                        time.sleep(1)
                        bTrainEvent = True
                        break
                if whereto == 'sowon':
                    print('[왕국활동] 소원나무는 그냥 들어가 드립니다.')
                    pag.click(random.randint(155 - 10, 155 + 10),
                              random.randint(135 - 10, 135 + 10) + account * 540 + 76 * 4)
                    time.sleep(1)
                    bTradeEvent = True
            else:
                if whereto == 'trade' and Kingdom_ready(account, 'trade_in'):
                    bTradeEvent = True
                    break
                elif whereto == 'research' and Kingdom_ready(account, 'research_in'):
                    bResearchEvent = True
                    break
                elif whereto == 'balloon' and Kingdom_ready(account, 'balloon_in'):
                    bBalloonEvent = True
                    break
                elif whereto == 'train' and Kingdom_ready(account, 'train_in'):
                    bTrainEvent = True
                    break
                else:
                    Kingdom_ready(account, 'kkd_out')

            print('왕국활동 창 꺼져있는 상태에선')
            # 왕국활동 창 꺼져있는 상태에선
            act_check_mark = pag.locateCenterOnScreen('act_check_mark.png', confidence=0.9,
                                                      region=(174, 458 + account * 540, 13, 11))  # 체크 마크
            act_nukimpyo_mark = pag.locateCenterOnScreen('act_nukimpyo_mark.png', confidence=0.9,
                                                         region=(174, 458 + account * 540, 13, 11))  # 느낌표 마크

            if (act_check_mark) or (act_nukimpyo_mark):  # 뭐라도 있으면
                pag.click(155, 490 + account * 540)  # 클릭해!
                time.sleep(1)
            else:
                print('[왕국활동]아무 이벤트도 없습니다.')
                return False

        # else:
        #     # 왕국활동 창이 켜져 있으면
        #     if (act_popup_mark_x):
        #         if whereto == 'trade':
        #             # 이미지 확인(무역센터 느낌표)
        #             time.sleep(23)
        #             activity_trade1 = pag.locateCenterOnScreen('activity_trade1.png', confidence=0.95, region=(115,95+account*540,80,80))
        #             if (activity_trade1):
        #                 print('[왕국활동] 무역센터 이벤트가 없습니다.')
        #                 return False
        #             else:
        #                 print('[왕국활동] 무역센터로 들어갑니다.')
        #                 activity_trade2 = pag.locateCenterOnScreen('activity_trade2.png', confidence=0.95, region=(115,95+account*540,80,80))
        #                 if (activity_trade2):
        #                     time.sleep(1)
        #                     pag.click(activity_trade2)
        #                     time.sleep(1)
        #                     bTradeEvent = True
        #                     time.sleep(1)
        #                     break
        #                 else:
        #                     print('왜 없어?')
        #                     return False
        #             # else:
        #             #     print('[왕국활동] 무역센터로 들어갑니다.')
        #             #     pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540)
        #             #     time.sleep(2)
        #             #     bTradeEvent = True
        #             #     break
        #         if whereto == 'research':
        #             # 이미지 확인(연구소 느낌표)
        #             if Kingdom_ready(account,'research_in'):
        #                 bResearchEvent = True
        #                 break
        #             else:
        #                 activity_research = pag.locateCenterOnScreen('activity_research.png', confidence=0.95, region=(115,95+76*1+account*540,80,80))
        #                 if (activity_research):
        #                     print('[왕국활동] 연구소 이벤트가 없습니다.')
        #                     return False
        #                 else:
        #                     print('[왕국활동] 연구소 들어갑니다.')
        #                     pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76)
        #                     time.sleep(2)
        #                     bResearchEvent = True
        #                     break
        #
        #         if whereto == 'balloon':
        #             # 이미지 확인(열기구 느낌표)
        #             activity_balloon = pag.locateCenterOnScreen('activity_balloon.png', confidence=0.95, region=(115,95+76*2+account*540,80,80))
        #             if (activity_balloon):
        #                 print('[왕국활동] 열기구 이벤트가 없습니다.')
        #                 return False
        #             else:
        #                 print('[왕국활동] 열기구 들어갑니다.')
        #                 pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*2)
        #                 time.sleep(2)
        #                 bBalloonEvent = True
        #                 break
        #         if whereto == 'train':
        #             # 이미지 확인(열차 느낌표)
        #             activity_train = pag.locateCenterOnScreen('activity_train.png', confidence=0.95, region=(115,95+76*3+account*540,80,80))
        #             if (activity_train):
        #                 print('[왕국활동] 곰젤리 열차 이벤트가 없습니다.')
        #                 return False
        #             else:
        #                 print('[왕국활동] 곰젤리 열차 들어갑니다.')
        #                 pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*3)
        #                 time.sleep(2)
        #                 bTrainEvent = True
        #                 break
        #         if whereto == 'sowon':
        #             print('[왕국활동] 소원나무는 그냥 들어가 드립니다.')
        #             pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*4)
        #             time.sleep(2)
        #             bTradeEvent = True
        #
        #
        #     else:
        #         if whereto == 'trade' and Kingdom_ready(account,'trade_in'):
        #             bTradeEvent = True
        #             break
        #         elif whereto == 'research' and Kingdom_ready(account,'research_in'):
        #             bResearchEvent = True
        #             break
        #         elif whereto == 'balloon' and Kingdom_ready(account,'balloon_in'):
        #             bBalloonEvent = True
        #             break
        #         elif whereto == 'train' and Kingdom_ready(account,'train_in'):
        #             bTrainEvent = True
        #             break
        #         else:
        #             Kingdom_ready(account,'kkd_out')
        #
        #         # 왕국활동 창 꺼져있는 상태에선
        #         act_check_mark = pag.locateCenterOnScreen('act_check_mark.png', confidence=0.9, region=(174,458+account*540,13,11))         # 체크 마크
        #         act_nukimpyo_mark = pag.locateCenterOnScreen('act_nukimpyo_mark.png', confidence=0.9, region=(174,458+account*540,13,11))   # 느낌표 마크
        #
        #         if (act_check_mark) or (act_nukimpyo_mark): # 뭐라도 있으면
        #             pag.click(155,490+account*540)          # 클릭해!
        #             time.sleep(1)
        #         else:
        #             print('[왕국활동]아무 이벤트도 없습니다.')
        #             return False

    activity_monitor_time = time.time()
    # 분수 입장
    while bFountain:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        activity_now_time = time.time()
        if activity_now_time - activity_monitor_time > 60:
            return False
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        Cond_fountain = pag.locateCenterOnScreen('Cond_fountain.png', confidence=0.9, region = (512,63+account*540,44,30))
        screen = ImageGrab.grab()
        pix_prod = screen.getpixel((630,470+account*540))       # 보상 수령 가능여부
        pix_green = (121,207,12)
        if (Cond_fountain):
            if (pix_prod == pix_green):
                pag.click(random.randint(655-25,655+25),random.randint(465-5,465+5)+account*540)
            else:
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(2)
                return print('분수 보상 수령할 게 없네요!')
        # 있었는데요. 없습니다.
        Cond_fountain_result = pag.locateCenterOnScreen('Cond_fountain_result.png', confidence=0.9, region = (2,32+account*540,917,505))
        if (Cond_fountain_result):
            pag.click(295,60+account*540)
            time.sleep(0.3)
            Cond_fountain_result = pag.locateCenterOnScreen('Cond_fountain_result.png', confidence=0.9, region = (2,32+account*540,917,505))
            if not (Cond_fountain_result):
                Kingdom_ready(account,'kkd_out')
                return print('분수 보상 수령 완료!')
        time.sleep(1)
    
    # 상점 입장
    while bShop:
        print('상점 일일보상 받으러 들어왔다!')
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        activity_now_time = time.time()
        if activity_now_time - activity_monitor_time > 60:
            return False
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        cond_shop_red_dot = pag.locateCenterOnScreen('cond_shop_red_dot.png', confidence=0.9, region=(160,32+account*540,19,505))
        cond_shop_red_check = pag.locateCenterOnScreen('cond_shop_red_check.png', confidence=0.9, region=(160,32+account*540,19,505))
        cond_shop_jaehwa = pag.locateCenterOnScreen('cond_shop_jaehwa.png', confidence=0.9, region=(53,505+account*540,75,33))
        if (cond_shop_red_check) and not (cond_shop_red_dot):
            print('cond_shop_red_check',cond_shop_red_check)
            pag.click(cond_shop_red_check)
            time.sleep(1)
            cond_shop_dobby_is = pag.locateCenterOnScreen('cond_shop_dobby_is.png', confidence=0.9, region=(180,485+account*540,740,27))
            if (cond_shop_dobby_is):
                pag.click(cond_shop_dobby_is)
                time.sleep(2)
        if (cond_shop_red_dot):
            print('cond_shop_red_dot',cond_shop_red_dot)
            pag.click(cond_shop_red_dot)
            time.sleep(1)
        if not (cond_shop_red_check) and not (cond_shop_red_dot):
            print('없넹?')
            if not (cond_shop_jaehwa):
                pag.click(35,55+account*540)
                time.sleep(1)
                pag.moveTo(25,505+account*540)
                pag.dragTo(25,100+account*540,2)
                time.sleep(1)
            else:
                print('상점보상 끝!')
                time.sleep(1)
                # pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
                pag.click(890, 55)
                time.sleep(3)
                Kingdom_ready(account,'kkd_out')
                return True
        time.sleep(1)    
    # 무역센터 진입
    while bTradeEvent:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        activity_now_time = time.time()
        if activity_now_time - activity_monitor_time > 60:
            return False
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        cond_trade_event = pag.locateCenterOnScreen('cond_trade_event.png', confidence=0.85, region=(170,102+account*540,9,14))             # 해상무역센터 이벤트 발생
        cond_trade_perl = pag.locateCenterOnScreen('cond_trade_perl.png', confidence=0.85, region=(2,30+account*540,917,505))               # 해상무역센터 위치 확인
        cond_trade_angmu = pag.locateCenterOnScreen('cond_trade_angmu.png', confidence=0.85, region=(150,320+account*540,29,25))            # 해상무역센터 앵무 교역소 이벤트
        cond_trade_refresh = pag.locateCenterOnScreen('cond_trade_refresh.png', confidence=0.85, region=(733,500+account*540,34,18))        # 해상무역센터 앵무 교역소 새로고침
        cond_trade_angmu_confirm = pag.locateCenterOnScreen('cond_trade_angmu_confirm.png', confidence=0.85, region=(420,80+account*540,58,33))   # 해상무역센터 앵무 교역소 위치 확인
        if not bStep2_Angmu and (cond_trade_event):
            print('cond_trade_event',cond_trade_event)
        if not bStep2_Angmu and (cond_trade_perl):
            print('cond_trade_perl',cond_trade_perl)
            if (cond_trade_angmu):
                print('cond_trade_angmu',cond_trade_angmu)
                pag.click(x=cond_trade_angmu.x-26,y=cond_trade_angmu.y+24)

                time.sleep(2)
            else:
                print('앵무 교역소 아닌 이벤트 입니다!')
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(6)
                Kingdom_ready(account,'kkd_out')
                return False

        if bStep2_Angmu and (cond_trade_refresh):       # 앵무 교역소, 무료 새로고침인 경우
            print('cond_trade_refresh',cond_trade_refresh)
            pag.click(cond_trade_refresh)
        
        if bStep2_Angmu and not (cond_trade_refresh):   # 앵무 교역소, 새로고침 클릭 완료
            print('[앵무엔터] 교역소 들어와 새로고침도 완료 했습니다!')
            return True
        
        if not bStep2_Angmu and (cond_trade_angmu_confirm):
            print('[교역소 in] 앵무 교역소 in!',cond_trade_angmu_confirm)
            bStep2_Angmu = True
        time.sleep(1)

    # 연구소 입장 확인까지만
    while bResearchEvent:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        activity_now_time = time.time()
        if activity_now_time - activity_monitor_time > 60:
            return False
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        cond_research = pag.locateCenterOnScreen('cond_research.png', confidence=0.9, region=(12,36+account*540,36,36))  # 연구소 노움 얼굴
        if (cond_research):
            return True
        Cond_research_comp = pag.locateCenterOnScreen('Cond_research_comp.png', confidence=0.945, region = (2,32+account*540,917,505))
        if (Cond_research_comp):
            print('Cond_research_comp',Cond_research_comp)
            pag.click(random.randint(205,205+515), random.randint(95,95+400)+account*540)
        time.sleep(1)
    
    # 열기구 입장 확인 및 보내기.
    while bBalloonEvent:
        complete_confirm = 0
        error_count = 0
        while True:
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)

            activity_now_time = time.time()
            # print('동작시간?', activity_now_time - activity_monitor_time)
            if activity_now_time - activity_monitor_time > 60:
                return False
            if keyboard.is_pressed('end'):
                print('end 누름')
                return False
            cond_kkd_balloon = pag.locateCenterOnScreen('cond_kkd_balloon.png', confidence=0.85, region=(9,36+account*540,25,35))               # 열기구 로비
            cond_kkd_balloon_ing = pag.locateCenterOnScreen('cond_kkd_balloon_ing.png', confidence=0.85, region=(364,85+account*540,28,37))     # 열기구 날아다니는 중
            cond_balloon_arrive = pag.locateCenterOnScreen('cond_balloon_arrive.png', confidence = 0.96, region = (2,32+account*540,917,505))   # 열기구 도착 화면
            if (cond_balloon_arrive):
                error_count = 0
                complete_confirm = 0
                pag.click(cond_balloon_arrive)
                time.sleep(0.3)
            elif (cond_kkd_balloon_ing):
                print('열기구 날아다니는 중인데 왜 들어왔지?')
                complete_confirm = 0
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
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
                if error_count > 10: # 이레가 추가
                    pag.click(740, 310 + account * 540)
                    End_kkd(account)
                    Kingdom_ready(account, 'kkd_out')  # 재부팅
                    error_count = 0
                    return False

    # 기차 입장 확인까지만
    while bTrainEvent:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        activity_now_time = time.time()
        if activity_now_time - activity_monitor_time > 60:
            return False
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        cond_kkd_train = pag.locateCenterOnScreen('cond_kkd_train.png', confidence=0.85, region=(30,42+account*540,25,33))  # 곰젤리열차
        cond_kkd_train1 = pag.locateCenterOnScreen('cond_kkd_train1.png', confidence=0.85,
                                                  region=(30, 42 + account * 540, 25, 33))  # 곰젤리열차
        if (cond_kkd_train) or (cond_kkd_train1):
            return True
        time.sleep(1)

def find_num_x(image, x1, x2, list_output, account):
    prod_num = pag.locateAllOnScreen(image, confidence=0.85, region=(x1,440+account*540,x2-x1,26))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    # print(image,list_output)
    return

def find_num_new_heart(image, x1, x2, list_output, account):
    prod_num = pag.locateAllOnScreen(image, confidence=0.85, region=(x1,444+account*540,x2-x1,15))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def Angmu_Action(prd_name, ctr, account):
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)

    item_check = pag.locateCenterOnScreen(prd_name, confidence=0.85, region=(ctr[0]+35,345+account*540,60,50))
    if (item_check):
        if Angmu_check(ctr[0]+9,account) > 324:
            print('어머 이건 사야해!')
            pag.click(item_check)
            time.sleep(1)
            pag.click(random.randint(420,500),random.randint(370,400)+account*540)
            time.sleep(2)
            trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472,221+account*540,25,17))
            if (trade_not_enough):
                print('앗 부족..')
                pag.click(random.randint(629,629+13),random.randint(153,153+13)+account*540,2,0.3)
            
            return True
        else:
            print('사지 않고 넘어갑니다!')
            return True
    else:
        return False

def Angmu_check(x1, account):

    trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(x1,439+account*540,90,28))
    trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(x1,439+account*540,90,28))
    trade_slash_real_mini = pag.locateCenterOnScreen('trade_slash_real_mini.png', confidence=0.85, region=(x1,439+account*540,90,28))
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
    find_num_x('up_th0.png', x1, x2, list_num_0, account)
    find_num_x('up_th1.png', x1, x2, list_num_1, account)
    find_num_x('up_th1_1.png', x1, x2, list_num_1, account)
    find_num_x('up_th2.png', x1, x2, list_num_2, account)
    find_num_x('up_th3.png', x1, x2, list_num_3, account)
    find_num_x('up_th3_1.png', x1, x2, list_num_3, account)
    find_num_x('up_th4.png', x1, x2, list_num_4, account)
    find_num_x('up_th5.png', x1, x2, list_num_5, account)
    find_num_x('up_th6.png', x1, x2, list_num_6, account)
    find_num_x('up_th7.png', x1, x2, list_num_7, account)
    find_num_x('up_th8.png', x1, x2, list_num_8, account)
    find_num_x('up_th9.png', x1, x2, list_num_9, account)
    find_num_x('up_ths_0.png', x1, x2, list_num_0, account)
    find_num_x('up_thm_0.png', x1, x2, list_num_0, account)
    find_num_x('up_ths_0_1.png', x1, x2, list_num_0, account)
    find_num_x('up_ths_0_2.png', x1, x2, list_num_0, account)
    find_num_x('up_ths_1.png', x1, x2, list_num_1, account)
    find_num_x('up_thm_1.png', x1, x2, list_num_1, account)
    find_num_x('up_ths_2.png', x1, x2, list_num_2, account)
    find_num_x('up_ths_2_1.png', x1, x2, list_num_2, account)
    find_num_x('up_ths_3.png', x1, x2, list_num_3, account)
    find_num_x('up_thm_3.png', x1, x2, list_num_3, account)
    find_num_x('up_ths_4.png', x1, x2, list_num_4, account)
    find_num_x('up_thm_4.png', x1, x2, list_num_4, account)
    find_num_x('up_ths_5.png', x1, x2, list_num_5, account)
    find_num_x('up_ths_5_1.png', x1, x2, list_num_5, account)
    find_num_x('up_ths_6.png', x1, x2, list_num_6, account)
    find_num_x('up_ths_6_1.png', x1, x2, list_num_6, account)
    find_num_x('up_ths_7.png', x1, x2, list_num_7, account)
    find_num_x('up_ths_7_1.png', x1, x2, list_num_7, account)
    find_num_x('up_ths_8.png', x1, x2, list_num_8, account)
    find_num_x('up_ths_8_1.png', x1, x2, list_num_8, account)
    find_num_x('up_ths_8_2.png', x1, x2, list_num_8, account)
    find_num_x('up_ths_9.png', x1, x2, list_num_9, account)
    find_num_x('up_thm_9.png', x1, x2, list_num_9, account)
    find_num_x('up_ths_9_1.png', x1, x2, list_num_9, account)
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
    
    # print('sort 이후',list_real_num)

    # del_list = list()
    # if len(list_real_num) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
    #     for i in range(len(list_real_num)-1):
    #         for j in range(len(list_real_num)-1-i):
    #             if abs(int(list_real_num[i][0])-int(list_real_num[i+1+j][0])) < 2 and abs(int(list_real_num[i][1])-int(list_real_num[i+1+j][1])) < 2:
    #                 del_list.append(list_real_num[i])
    # list_real_num = [x for x in list_real_num if x not in del_list]
    

    print('set 이전',list_real_num)
    
    # list_real_num1 = set(list_real_num)
    
    # print('set 이후',list_real_num1)
    
    for i in range(len(list_real_num)): # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1]*10**(len(list_real_num)-i-1)

    print('현재 재고는 =', its_number)
    return its_number


def Angmu_Aft_Refresh(account):
    Scroll_count = 0
    start_time = time.time()
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        now_time = time.time()
        if keyboard.is_pressed('end'):
            print('end 누름')
            break

        if now_time - start_time > 300:
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')

        if Scroll_count == 0:
            trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2,350+account*540,917,45))
            trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2,350+account*540,917,45))
            trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2,350+account*540,917,45))
            # trade_tro_1 = pag.locateCenterOnScreen('trade_tro_1.png', confidence=0.85, region=(2,350+account*540,917,40))
            # trade_tro_2 = pag.locateCenterOnScreen('trade_tro_2.png', confidence=0.85, region=(2,350+account*540,917,40))


            if (trade_kidung):
                kidung_numb = Angmu_check(trade_kidung[0] - 26, account)
            else:
                kidung_numb = 0
            if (trade_block):
                block_numb = Angmu_check(trade_block[0] - 26, account)
            else:
                block_numb = 0
            if (trade_nachimban):
                nachimban_numb = Angmu_check(trade_nachimban[0] - 26, account)
            else:
                nachimban_numb = 0
            max_numb = max(kidung_numb, block_numb, nachimban_numb)
            if kidung_numb > 0 and kidung_numb == max_numb:
                pag.click(trade_kidung)
                time.sleep(0.5)
                pag.click(random.randint(420,500),random.randint(370,400)+account*540)
                time.sleep(2)
            if block_numb > 0 and block_numb == max_numb:
                pag.click(trade_block)
                time.sleep(0.5)
                pag.click(random.randint(420,500),random.randint(370,400)+account*540)
                time.sleep(2)
            if nachimban_numb > 0 and nachimban_numb == max_numb:
                pag.click(trade_nachimban)
                time.sleep(0.5)
                pag.click(random.randint(420,500),random.randint(370,400)+account*540)
                time.sleep(2)
            # Angmu_Action('trade_tro_1', trade_tro_1)
            # Angmu_Action('trade_tro_2', trade_tro_2)
        
        if Scroll_count == 1:
            trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2,325+account*540,750,26))
            trade_baseline_list = list(trade_baseline)
            if len(trade_baseline_list) != 0:
                for p in trade_baseline_list:
                    ctr = pag.center(p)
                    # 범위 내 조건 확인
                    if Angmu_Action('trade_assist_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_assist_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_bomb_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_bomb_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_fist_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_fist_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_recovery_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_recovery_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_shield_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_shield_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_shooting_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_shooting_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_staff_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_staff_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_sword_lv1.png', ctr, account):
                        print('판별 완료',ctr)
                    elif Angmu_Action('trade_sword_lv2.png', ctr, account):
                        print('판별 완료',ctr)
                    else:
                        print('여긴 어디 나는 누구')

            
        if 4 > Scroll_count >= 2:
            trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2,325+account*540,750,26))
            trade_baseline_list = list(trade_baseline)
            if len(trade_baseline_list) != 0:
                for p in trade_baseline_list:
                    ctr = pag.center(p)
                    print('생산품까지 확인')
                    if account == 0:
                        if Angmu_Action('trade_cotton.png', ctr, account):
                            print('판별 완료',ctr)
                        elif Angmu_Action('trade_berry.png', ctr, account):
                            print('판별 완료',ctr)
                        # elif Angmu_Action('trade_biscuit.png', ctr, account):
                        #     print('판별 완료',ctr)
                        # elif Angmu_Action('trade_milk.png', ctr, account):
                        #     print('판별 완료',ctr)
                        else:
                            print('여긴 어디 나는 누구')
                    if account == 1:
                        if Angmu_Action('trade_berry.png', ctr, account):
                            print('판별 완료',ctr)
                        # elif Angmu_Action('trade_cotton.png', ctr, account):
                        #     print('판별 완료',ctr)
                        # elif Angmu_Action('trade_biscuit.png', ctr, account):
                        #     print('판별 완료',ctr)
                        # elif Angmu_Action('trade_biscuit.png', ctr, account):
                        #     print('판별 완료',ctr)
                        else:
                            print('여긴 어디 나는 누구')


        # if Scroll_count >= 2:
        #     print('아이고 힘들다 2~')
        #     trade_assist_lv3 = pag.locateCenterOnScreen('trade_assist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_bomb_lv3 = pag.locateCenterOnScreen('trade_bomb_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_fist_lv3 = pag.locateCenterOnScreen('trade_fist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_recovery_lv3 = pag.locateCenterOnScreen('trade_recovery_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_shield_lv3 = pag.locateCenterOnScreen('trade_shield_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_shooting_lv3 = pag.locateCenterOnScreen('trade_shooting_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_staff_lv3 = pag.locateCenterOnScreen('trade_staff_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        #     trade_sword_lv3 = pag.locateCenterOnScreen('trade_sword_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
        
        # 드래그드래그
        pag.moveTo(random.randint(786,820),random.randint(480+account*540,490+account*540))
        pag.mouseDown()
        time.sleep(0.5)
        pag.moveTo(random.randint(786,820)-157*4,random.randint(480+account*540,490+account*540),5)   # 153인데 20 더 여유줌
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(0.5)
        
        # ++ 작업 후 >= 3으로변경
        if Scroll_count >= 4:
            print('완료')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(2)
            pag.hotkey('esc')
            time.sleep(6)
            return
        
        start_lineup = time.time()
        while True:
            now_lineup = time.time()
            if now_lineup - start_lineup > 30:
                print('뭐얏...')
                break
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)

            cond_trade_angmu_confirm = pag.locateCenterOnScreen('cond_trade_angmu_confirm.png', confidence=0.85, region=(420,80+account*540,58,33))   # 해상무역센터 앵무 교역소 위치 확인
            if not (cond_trade_angmu_confirm):
                print('튕기거나 빠져나갔나봐요...')
                Kingdom_ready(account,'kkd_out')
                return
            
            trade_baseline_gray = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.9, region=(2,32+account*540,917,505))
            if (trade_baseline_gray):
                if (92 >= trade_baseline_gray[0] > 70) or (92+157 >= trade_baseline_gray[0] > 70+157):
                    print('오우예')
                    Scroll_count = Scroll_count + 1
                    break
                else:
                    pag.moveTo(790,random.randint(480+account*540,490+account*540))
                    pag.mouseDown()
                    time.sleep(0.5)
                    pag.moveTo(790+50,random.randint(480+account*540,490+account*540),2)   # 한 번 움직여보고
                    time.sleep(0.5)
                    trade_baseline_gray_new = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.95, region=(2,32+account*540,917,505))
                    if (trade_baseline_gray_new):
                        pag.moveTo(790+50-trade_baseline_gray_new[0]+73,random.randint(480+account*540,490+account*540),3)   # 153인데 20 더 여유줌
                    time.sleep(0.5)
                    pag.mouseUp()
                    time.sleep(0.5)
            
            trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.9, region=(2,32+account*540,917,505))
            if (trade_baseline):
                if (92 >= trade_baseline[0] > 70) or (92+157 >= trade_baseline[0] > 70+157):
                    print('오우예')
                    Scroll_count = Scroll_count + 1
                    break
                else:
                    pag.moveTo(790,random.randint(480+account*540,490+account*540))
                    pag.mouseDown()
                    time.sleep(0.5)
                    pag.moveTo(790+50,random.randint(480+account*540,490+account*540),2)   # 한 번 움직여보고
                    time.sleep(0.5)
                    trade_baseline_new = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.95, region=(2,32+account*540,917,505))
                    if (trade_baseline_new):
                        pag.moveTo(790+50-trade_baseline_new[0]+73,random.randint(480+account*540,490+account*540),3)   # 153인데 20 더 여유줌
                    time.sleep(0.5)
                    pag.mouseUp()
                    time.sleep(0.5)
    return print('Angmu_Aft_Refresh 완료!')

# 킹덤패스 일일/시즌미션, 시즌 보상 수령
def Kpass_reward(account):
    screen = ImageGrab.grab()
    pix_pass_reward = screen.getpixel((901,138+account*540)) # 패스 보상
    pix_pass_reward_exist = (254, 0, 0)
    if pix_pass_reward == pix_pass_reward_exist:
        pag.click(870,155+account*540)
        time.sleep(1)
    else:
        print('킹덤패스 보상 없음!')
        return
    
    bPass1 = False
    bPass2 = False
    bPass3 = False
    while True:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        if keyboard.is_pressed('end'):
            print('end 누름')
            break

        bClicked = False
        screen = ImageGrab.grab()
        pix_kpass1 = screen.getpixel((16,101+account*540))          # 데일리 미션
        pix_kpass2 = screen.getpixel((16+143,101+account*540))      # 시즌 미션
        pix_kpass3 = screen.getpixel((16-1+143*2,101+account*540))  # 시즌 보상
        pix_reward = screen.getpixel((770,520+account*540))         # 모두 받기
        bSelected = (255, 255, 255)         # 어느 탭인지 확인
        bReward = (121, 207, 16)            # 모두 받기 활성화
        if pix_kpass1 == bSelected: # 데일리 미션
            if pix_reward == bReward:
                pag.click(random.randint(786,786+80), random.randint(506,506+26)+account*540)
                time.sleep(0.5)
            else:
                bPass1 = True
            
        if pix_kpass2 == bSelected: # 시즌 미션
            if pix_reward == bReward:
                pag.click(random.randint(786,786+80), random.randint(506,506+26)+account*540)
                time.sleep(0.5)
            else:
                bPass2 = True
        if pix_kpass3 == bSelected: # 시즌 보상
            if pix_reward == bReward:
                pag.click(random.randint(786,786+80), random.randint(506,506+26)+account*540)
                time.sleep(0.5)
            else:
                bPass3 = True
        if not bPass1:
            pag.click(random.randint(35,35+90), random.randint(100,100+25)+account*540)
            time.sleep(0.5)
        elif not bPass2:
            pag.click(random.randint(35,35+90)+143*1, random.randint(100,100+25)+account*540)
            time.sleep(0.5)
        elif not bPass3:
            pag.click(random.randint(35,35+90)+143*2, random.randint(100,100+25)+account*540)
            time.sleep(0.5)
        else:
            print('다 수령했네요')
            pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
            time.sleep(1.5)
            return
        time.sleep(1)

def numb_new_recog(prod_pin, line):
    its_number = 0
    how_many_nums = 0
    pos_numb = 0        # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
    num_list = list()
    print('라인 %s번 진행합니다!'%(line))
    screen = ImageGrab.grab()
    # 3렙 건물인 경우 무조건 prod_pin = (612,95)
    # print('?', prod_pin[0]+19,prod_pin[1]+81+153*(line-1))
    pix_jaritsu1_1 = screen.getpixel((prod_pin[0]+19,prod_pin[1]+81+153*(line-1))) # 상
    # print('pix_자릿수1_1:', pix_jaritsu1_1)
    pix_jaritsu1_2 = screen.getpixel((prod_pin[0]+19,prod_pin[1]+87+153*(line-1))) # 하
    # print('pix_자릿수1_2:', pix_jaritsu1_2)
    if ((pix_jaritsu1_1) == (255, 255, 255)) and ((pix_jaritsu1_2) == (255, 255, 255)):
        pix_zero_1 = screen.getpixel((prod_pin[0]+24,prod_pin[1]+82+153*(line-1))) # 상
        # print('pix_zero_1:', pix_zero_1)
        pix_zero_2 = screen.getpixel((prod_pin[0]+24,prod_pin[1]+85+153*(line-1))) # 하
        # print('pix_zero_2:', pix_zero_2)
        print('pos_numb', pos_numb)
        for p in pix_zero_1:
            if p < 252:
                pos_numb = 1
        for p in pix_zero_2:
            if p < 252:
                pos_numb = 1
        if pos_numb == 0:
            print('이 숫자는 0 입니다!')
            its_number = 0
            return 0
        # if pos_numb == 1:
            # print('이 숫자는 한 자릿 수 입니다!')
    else:
        pix_jaritsu2_1 = screen.getpixel((prod_pin[0]+14,prod_pin[1]+81+153*(line-1))) # 상
        # print('pix_자릿수2_1:', pix_jaritsu2_1)
        pix_jaritsu2_2 = screen.getpixel((prod_pin[0]+14,prod_pin[1]+81+153*(line-1))) # 하
        # print('pix_자릿수2_2:', pix_jaritsu2_2)
        if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
            # print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            # print('이 숫자는 세 자릿 수 입니다!')
            pos_numb = 3
    print('자릿수 다시 확인', pos_numb)
    if pos_numb == 1:
        # print('한 자릿 수 범위 확인1',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_1):
            return 1
        num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_1_1):
            return 1
        num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_2):
            return 2
        num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_3):
            return 3
        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_3_1):
            return 3
        num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_4):
            return 4
        num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_4_2):
            return 4
        num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_5):
            return 5
        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_6):
            return 6
        num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_7):
            return 7
        num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_8):
            return 8
        num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_8_1):
            return 8
        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_9):
            return 9
        num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
        if (num_9_1):
            return 9
        return 0
        
    if pos_numb == 2:
        print('두 자릿 수 범위 확인2',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),10,14)
        # 10의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),11,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                print('십의 자리 숫자 확인 에러!!')
        # 1의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5+10,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                print('일의 자리 숫자 확인 에러!!')
        return its_number
    if pos_numb == 3:
        print('세 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 900
                                                            else:
                                                                print('백의 자리 숫자 확인 에러!!')
        # 10의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(631,prod_pin[1]+85-7+153*(line-1),10,14))
                                                                if (num_0):
                                                                    print('십의 자리 0!!')
                                                                else:
                                                                    print('10의 자리 못읽음..')
        # 1의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(640,prod_pin[1]+85-7+153*(line-1),10,14))
                                                                if (num_0):
                                                                    print('1의 자리 0!!')
                                                                else:
                                                                    print('1의 자리 못읽음..')
        return its_number

def three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left):
    start_time = time.time()

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)

    prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.955, region = (90,145+account*540,24,20))
    if not (prod_refresh):
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
        time.sleep(0.5)
    
    cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75-10,200-10+account*540,20,20))
    if not (cond_2nd_clear):
        Skip_Next(account, prod_direction_left)
        return True
    
    # 풀리스트인 경우 넘어감
    prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
    if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!4')
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
                                                      region=(339, 253 + account * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..')
            pag.click(455, 379 + account * 540)
            time.sleep(0.3)
            pag.click(164, 280 + account * 540)
            time.sleep(0.3)
        else:
            Skip_Next(account, prod_direction_left)

        return True

    # 3렙건물이니 고정
    prod_pin = (612, 95+account*540)
    print('prod_pin:', prod_pin)
    target_numb1 = check_num1 - numb_new_recog(prod_pin, 1)
    print('1st ok')
    print('prod_pin:', prod_pin)
    target_numb2 = check_num2 - numb_new_recog(prod_pin, 2)
    print('2nd ok')
    print('prod_pin:', prod_pin)
    target_numb3 = check_num3 - numb_new_recog(prod_pin, 3)
    print('3rd ok')
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
            list_numb1 = pag.locateAllOnScreen(check_list_img1, confidence=0.95, region = (42,169+account*540,66,318))
            list_numb1 = list(list_numb1)
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
            list_numb2 = pag.locateAllOnScreen(check_list_img2, confidence=0.95, region = (42,169+account*540,66,318))
            list_numb2 = list(list_numb2)
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
            list_numb3 = pag.locateAllOnScreen(check_list_img3, confidence=0.95, region = (42,169+account*540,66,318))
            list_numb3 = list(list_numb3)
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
        now_time = time.time()
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)
        
        # 풀리스트인 경우 넘어감
        prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
        if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!5')
            prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95,
                                                          region=(339, 253 + account * 540, 175, 87))
            time.sleep(1)
            if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
                print('욕심을 버리시오 중생이여..')
                pag.click(455, 379 + account * 540)
                time.sleep(0.3)
                pag.click(164, 280 + account * 540)
                time.sleep(0.3)
            else:
                Skip_Next(account, prod_direction_left)
            return True
        # 동작시간 확인
        if now_time - start_time > 30:
            print('동작 최대시간 초과 입니다.')
            Skip_Next(account, prod_direction_left)
            return False
        
        # 강제종료
        if keyboard.is_pressed('end'):
            return False

        #조건 확인
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))

        # 구글 플레이 종료 뭐시기
        if (play_halted):
            pag.click(play_halted)
        
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
            Skip_Next(account, prod_direction_left)
            return False
        else:
            max_numb = max(compare_numb1, compare_numb2, compare_numb3)
            if max_numb == compare_numb1 and not prod_line1_completed:
                pag.click(random.randint(745,745+10),random.randint(190,190+15)+account*540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png',confidence=0.95, region=(2,32+account*540,917,505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line1_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line1_clicked = 999             # 나락으로 보내버력!
                else:
                    line1_clicked = line1_clicked + 1
            if max_numb == compare_numb2 and not prod_line2_completed:
                pag.click(random.randint(745,745+10),random.randint(190,190+15)+153+account*540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png',confidence=0.95, region=(2,32+account*540,917,505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line2_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line2_clicked = 999             # 나락으로 보내버력!
                else:
                    line2_clicked = line2_clicked + 1
            if max_numb == compare_numb3 and not prod_line3_completed:
                pag.click(random.randint(745,745+10),random.randint(190,190+15)+153*2+account*540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png',confidence=0.95, region=(2,32+account*540,917,505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line3_clicked = 999             # 나락으로 보내버력!
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line3_clicked = 999             # 나락으로 보내버력!
                else:
                    line3_clicked = line3_clicked + 1

def find_image_in(account,where_to):
    its_name = where_to
    its_format = "_in.png"
    its_image = pag.locateCenterOnScreen(its_name+its_format, confidence=0.96, region=(2,32+account*540,917,505))
    if (its_image):
        return True
    else:
        return False

def find_and_check(account,where_to):
    its_name = where_to
    its_format = ".png"
    its_image = pag.locateCenterOnScreen(its_name+its_format, confidence=0.85, region=(2,32+account*540,917,505))
    if (its_image):
        pag.click(its_image)
        time.sleep(0.3)
        if find_image_in(account,where_to):
            return True
        else:
            print('비슷한 이미지였나봄')
            # 뭔가 창이 떠있는 경우 닫기(X)
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
            if (research_window):
                pag.click(research_window)
                time.sleep(0.3)
            return False
    else:
        print('비슷한 이미지도 없음')
        return False


def research_action(account,what_research,where_to):
    research_position = 0

    research_ing = pag.locateCenterOnScreen('research_ing.png', confidence = 0.945, region = (230,115+account*540,24,18))
    if (research_ing):
        print('엇.. 뭔가 연구중입니다.')
        Kingdom_ready(account,'kkd_out')
        return False

    # 왕국이냐 쿠키냐 선택
    while True:
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
        if (research_window):
            pag.click(research_window)
            time.sleep(0.3)

        if what_research == 'W':
            screen = ImageGrab.grab()
            pix_research_wangkook = screen.getpixel((330,515+account*540)) # 왕국 연구
            pix_research_selected = (58, 73, 109)
            if pix_research_wangkook == pix_research_selected:
                print('왕국 연구 선택됨!')
                # where_to 숫자 변환
                del_text = 'research_W_'
                aft_del = [x for x in where_to if x not in del_text]
                num_where_to = int(aft_del[0])*10+int(aft_del[1])
                break
            else:
                pag.click(330,515+account*540)
                time.sleep(0.3)

        if what_research == 'C':
            screen = ImageGrab.grab()
            pix_research_cookie = screen.getpixel((500,515+account*540)) # 쿠키 연구
            pix_research_selected = (58, 73, 109)
            if pix_research_cookie == pix_research_selected:
                print('쿠키 연구 선택됨!')
                # where_to 숫자 변환
                del_text = 'research_C_'
                aft_del = [x for x in where_to if x not in del_text]
                print(aft_del)
                num_where_to = int(aft_del[0])*10+int(aft_del[1])
                break
            else:
                pag.click(500,515+account*540)
                time.sleep(0.3)    
    # 선택했으니 해당 위치 찾아가기
    bPosition_Checked = False   # 현재 위치 감지했냐?
    first_move_right = False    # 처음은 오른쪽으로 이동 해보냐?
    position_err = 0            # 위치 확인 에러 횟수
    start_research_search_t = time.time()
    while True:
        print('위치 찾아가기')
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False
        print('pos_now')
        if keyboard.is_pressed('end'):
            print('end 누름')
            return False

        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return False

        torrent_error = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (torrent_error):
            pag.click(torrent_error)
            time.sleep(0.3)
        
        now_research_search_t = time.time()
        if now_research_search_t - start_research_search_t > 120:
            return False

        # 뭔가 창이 떠있는 경우
        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
        if (research_window):
            pag.click(research_window)
            time.sleep(0.3)
            
        if what_research == 'W':
            research_W_03 = pag.locateCenterOnScreen('research_W_03.png', confidence=0.925, region=(2,32+account*540,917,505))
            if (research_W_03):
                position_now = 3
                bPosition_Checked = True
            else:
                research_W_062 = pag.locateCenterOnScreen('research_W_062.png', confidence=0.925, region=(2,32+account*540,917,505))
                if (research_W_062):
                    position_now = 6
                    bPosition_Checked = True
                else:
                    research_W_09 = pag.locateCenterOnScreen('research_W_09.png', confidence=0.925, region=(2,32+account*540,917,505))
                    if (research_W_09):
                        position_now = 9
                        bPosition_Checked = True
                    else:
                        research_W_12 = pag.locateCenterOnScreen('research_W_12.png', confidence=0.925, region=(2,32+account*540,917,505))
                        if (research_W_12):
                            position_now = 12
                            bPosition_Checked = True
                        else:
                            research_W_152 = pag.locateCenterOnScreen('research_W_152.png', confidence=0.925, region=(2,32+account*540,917,505))
                            if (research_W_152):
                                position_now = 15
                                bPosition_Checked = True
                            else:
                                research_W_18 = pag.locateCenterOnScreen('research_W_18.png', confidence=0.925, region=(2,32+account*540,917,505))
                                if (research_W_18):
                                    position_now = 18
                                    bPosition_Checked = True
                                else:
                                    research_W_212 = pag.locateCenterOnScreen('research_W_212.png', confidence=0.925, region=(2,32+account*540,917,505))
                                    if (research_W_212):
                                        position_now = 21
                                        bPosition_Checked = True
                                    else:
                                        research_W_24 = pag.locateCenterOnScreen('research_W_24.png', confidence=0.925, region=(2,32+account*540,917,505))
                                        if (research_W_24):
                                            position_now = 24
                                            bPosition_Checked = True
                                        else:
                                            bPosition_Checked = False

        if what_research == 'C':
            research_C_033 = pag.locateCenterOnScreen('research_C_033.png', confidence=0.925, region=(2,32+account*540,917,505))
            if (research_C_033):
                pag.click(research_C_033)
                time.sleep(0.3)
                if find_image_in(account,"research_C_033"):
                    # 뭔가 창이 떠있는 경우 닫기(X)
                    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                    if (research_window):
                        pag.click(research_window)
                        time.sleep(0.3)
                    position_now = 3
                    bPosition_Checked = True
                else:
                    if find_image_in(account,"research_C_173"):
                        # 뭔가 창이 떠있는 경우 닫기(X)
                        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                        if (research_window):
                            pag.click(research_window)
                            time.sleep(0.3)
                        position_now = 17
                        bPosition_Checked = True
            else:
                research_C_061 = pag.locateCenterOnScreen('research_C_061.png', confidence=0.925, region=(2,32+account*540,917,505))
                if (research_C_061):
                    pag.click(research_C_061)
                    time.sleep(0.3)
                    if find_image_in(account,"research_C_061"):
                        # 뭔가 창이 떠있는 경우 닫기(X)
                        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                        if (research_window):
                            pag.click(research_window)
                            time.sleep(0.3)
                        position_now = 6
                        bPosition_Checked = True
                    else:
                        if find_image_in(account,"research_C_24"):
                            # 뭔가 창이 떠있는 경우 닫기(X)
                            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                            if (research_window):
                                pag.click(research_window)
                                time.sleep(0.3)
                            position_now = 24
                            bPosition_Checked = True
                else:
                    research_C_092 = pag.locateCenterOnScreen('research_C_092.png', confidence=0.925, region=(2,32+account*540,917,505))
                    if (research_C_092):
                        pag.click(research_C_092)
                        time.sleep(0.3)
                        if find_image_in(account,"research_C_092"):
                            # 뭔가 창이 떠있는 경우 닫기(X)
                            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                            if (research_window):
                                pag.click(research_window)
                                time.sleep(0.3)
                            position_now = 9
                            bPosition_Checked = True
                        else:
                            if find_image_in(account,"research_C_222"):
                                # 뭔가 창이 떠있는 경우 닫기(X)
                                research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                if (research_window):
                                    pag.click(research_window)
                                    time.sleep(0.3)
                                position_now = 22
                                bPosition_Checked = True
                    else:
                        research_C_12 = pag.locateCenterOnScreen('research_C_12.png', confidence=0.925, region=(2,32+account*540,917,505))
                        if (research_C_12):
                            pag.click(research_C_12)
                            time.sleep(0.3)
                            if find_image_in(account,"research_C_12"):
                                # 뭔가 창이 떠있는 경우 닫기(X)
                                research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                if (research_window):
                                    pag.click(research_window)
                                    time.sleep(0.3)
                                position_now = 12
                                bPosition_Checked = True
                            else:
                                if find_image_in(account,"research_C_02"):
                                    # 뭔가 창이 떠있는 경우 닫기(X)
                                    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                    if (research_window):
                                        pag.click(research_window)
                                        time.sleep(0.3)
                                    position_now = 2
                                    bPosition_Checked = True
                        else:
                            research_C_15 = pag.locateCenterOnScreen('research_C_15.png', confidence=0.925, region=(2,32+account*540,917,505))
                            if (research_C_15):
                                position_now = 15
                                bPosition_Checked = True
                            else:
                                research_C_182 = pag.locateCenterOnScreen('research_C_182.png', confidence=0.925, region=(2,32+account*540,917,505))
                                if (research_C_182):
                                    pag.click(research_C_182)
                                    time.sleep(0.3)
                                    if find_image_in(account,"research_C_182"):
                                        # 뭔가 창이 떠있는 경우 닫기(X)
                                        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                        if (research_window):
                                            pag.click(research_window)
                                            time.sleep(0.3)
                                        position_now = 18
                                        bPosition_Checked = True
                                    else:
                                        if find_image_in(account,"research_C_04"):
                                            # 뭔가 창이 떠있는 경우 닫기(X)
                                            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                            if (research_window):
                                                pag.click(research_window)
                                                time.sleep(0.3)
                                            position_now = 4
                                            bPosition_Checked = True
                                else:
                                    research_C_212 = pag.locateCenterOnScreen('research_C_212.png', confidence=0.925, region=(2,32+account*540,917,505))
                                    if (research_C_212):
                                        pag.click(research_C_212)
                                        time.sleep(0.3)
                                        if find_image_in(account,"research_C_212"):
                                            # 뭔가 창이 떠있는 경우 닫기(X)
                                            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                            if (research_window):
                                                pag.click(research_window)
                                                time.sleep(0.3)
                                            position_now = 21
                                            bPosition_Checked = True
                                        else:
                                            if find_image_in(account,"research_C_082"):
                                                # 뭔가 창이 떠있는 경우 닫기(X)
                                                research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                                if (research_window):
                                                    pag.click(research_window)
                                                    time.sleep(0.3)
                                                position_now = 8
                                                bPosition_Checked = True
                                    else:
                                        research_C_24 = pag.locateCenterOnScreen('research_C_24.png', confidence=0.925, region=(2,32+account*540,917,505))
                                        if (research_C_24):
                                            pag.click(research_C_24)
                                            time.sleep(0.3)
                                            if find_image_in(account,"research_C_24"):
                                                # 뭔가 창이 떠있는 경우 닫기(X)
                                                research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                                if (research_window):
                                                    pag.click(research_window)
                                                    time.sleep(0.3)
                                                position_now = 24
                                                bPosition_Checked = True
                                            else:
                                                if find_image_in(account,"research_C_061"):
                                                    # 뭔가 창이 떠있는 경우 닫기(X)
                                                    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                                    if (research_window):
                                                        pag.click(research_window)
                                                        time.sleep(0.3)
                                                    position_now = 6
                                                    bPosition_Checked = True
                                        else:
                                            research_C_27 = pag.locateCenterOnScreen('research_C_27.png', confidence=0.925, region=(2,32+account*540,917,505))
                                            if (research_C_27):
                                                pag.click(research_C_27)
                                                time.sleep(0.3)
                                                if find_image_in(account,"research_C_27"):
                                                    # 뭔가 창이 떠있는 경우 닫기(X)
                                                    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
                                                    if (research_window):
                                                        pag.click(research_window)
                                                        time.sleep(0.3)
                                                    position_now = 27
                                                    bPosition_Checked = True
                                                else:
                                                    bPosition_Checked = False
        # print('bPosition_Checked',bPosition_Checked)
        # print('num_where_to',num_where_to)
        # print('position_now',position_now)
        if bPosition_Checked: # 어떤 이미지라도 읽었으면
            position_err = 0  # 에러 횟수 초기화
            if abs(num_where_to - position_now) >= 1:
                if num_where_to - position_now >= 2:    # 가려는 곳이 지금보다 오른쪽, 2칸 이상
                    pag.moveTo(900,484+account*540)
                    pag.mouseDown()
                    time.sleep(0.3)
                    pag.moveTo(870,484+account*540,0.2)
                    pag.moveTo(870-295*2,484+account*540,0.5)   # 한 칸 간격 295
                    time.sleep(0.3)
                    pag.mouseUp()
                    pos_direction = 1       # 양의 방향으로 움직임
                elif position_now - num_where_to >= 2:  # 가려는 곳이 지금보다 왼쪽, 2칸 이상
                    pag.moveTo(50,484+account*540)
                    pag.mouseDown()
                    time.sleep(0.3)
                    pag.moveTo(80,484+account*540,0.2)
                    pag.moveTo(80+295*2,484+account*540,0.5)
                    time.sleep(0.3)
                    pag.mouseUp()
                    pos_direction = -1      # 음의 방향으로 움직임
                elif num_where_to - position_now == 1:  # 가려는 곳이 지금보다 오른쪽, 1칸
                    if find_and_check(account,where_to):    # 해당 이미지 찾아 들어갔으면 다음 스텝으로..
                        break
                    else:                       # 못 찾았으면 오른쪽으로
                        pag.moveTo(450,484+account*540)
                        pag.mouseDown()
                        time.sleep(0.3)
                        pag.moveTo(420,484+account*540,0.2)
                        pag.moveTo(420-295*1,484+account*540,0.5)
                        time.sleep(0.3)
                        pag.mouseUp()
                        pos_direction = 1       # 양의 방향으로 움직임
                        
                elif position_now - num_where_to == 1:  # 가려는 곳이 지금보다 왼쪽, 1칸
                    print('여긴?1')
                    if find_and_check(account,where_to):    # 해당 이미지 찾아 들어갔으면 다음 스텝으로..
                        break
                    else:                       # 못 찾았으면 왼쪽으로
                        print('여긴?')
                        pag.moveTo(450,484+account*540)
                        pag.mouseDown()
                        time.sleep(0.3)
                        pag.moveTo(480,484+account*540,0.2)
                        pag.moveTo(480+295*1,484+account*540,0.5)
                        time.sleep(0.3)
                        pag.mouseUp()
                        pos_direction = -1      # 음의 방향으로 움직임
                else:       # 현재 위치가 목표 지점인 경우
                    if find_and_check(account,where_to):    # 해당 이미지 찾아 들어갔으면 다음 스텝으로..
                        break
                    else:
                        print('우째 이런일이;;;')
                        Kingdom_ready(account,'kkd_out')
                        return False
        else:
            if pos_direction == 0:
                if 2 > position_err >= 0:
                    print('초기 위치 못잡음! 오른쪽으로 이동 해본다!')
                    pag.moveTo(450,484+account*540)
                    pag.mouseDown()
                    time.sleep(0.3)
                    pag.moveTo(420,484+account*540,0.2)
                    pag.moveTo(420-295*1,484+account*540,0.5)
                    time.sleep(0.3)
                    pag.mouseUp()
                if 6 > position_err >= 2:
                    print('초기 위치 못잡음! 왼쪽으로 이동 해본다!')
                    pag.moveTo(450,484+account*540)
                    pag.mouseDown()
                    time.sleep(0.3)
                    pag.moveTo(420,484+account*540,0.2)
                    pag.moveTo(420-295*1,484+account*540,0.5)
                    time.sleep(0.3)
                    pag.mouseUp()
                if position_err >= 6:
                    print('뭔가 에러 났나.... 위치를 못찾아요!')
                    Kingdom_ready(account,'kkd_out')
                    return False
                position_err = position_err + 1
            if pos_direction == 1:      # 양의 방향으로 움직이다 놓친 경우
                pag.moveTo(450,484+account*540)
                pag.mouseDown()
                time.sleep(0.3)
                pag.moveTo(420,484+account*540,0.2)
                pag.moveTo(420-295*1,484+account*540,0.5)
                time.sleep(0.3)
                pag.mouseUp()
            if pos_direction == -1:     # 음의 방향으로 움직이다 놓친 경우
                pag.moveTo(450,484+account*540)
                pag.mouseDown()
                time.sleep(0.3)
                pag.moveTo(480,484+account*540,0.2)
                pag.moveTo(480+295*1,484+account*540,0.5)
                time.sleep(0.3)
                pag.mouseUp()

    # 들어갔으나, 아직 열지 않은 경우
    research_not_opened = pag.locateCenterOnScreen('research_not_opened.png', confidence=0.9, region=(390,200+account*540,97,22))
    if (research_not_opened):
        print('아직 열지 않은 연구입니다!')
        # 뭔가 창이 떠있는 경우 닫기(X)
        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
        if (research_window):
            pag.click(research_window)
            time.sleep(0.3)
            Kingdom_ready(account,'kkd_out')
        return False
    
    # 들어갔으나, 만렙인 경우
    research_maximum = pag.locateCenterOnScreen('research_maximum.png', confidence=0.9, region=(426,284+account*540,66,19))
    if (research_maximum):
        print('이미 만렙 찍었습니다!')
        # 뭔가 창이 떠있는 경우 닫기(X)
        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
        if (research_window):
            pag.click(research_window)
            time.sleep(0.3)
            Kingdom_ready(account,'kkd_out')
        return False
    
    research_ing_in = pag.locateCenterOnScreen('research_ing_in.png', confidence=0.9, region=(549,361+account*540,88,27))
    if (research_ing_in):
        print('해당 연구가 이미 진행중입니다.')
        # 뭔가 창이 떠있는 경우 닫기(X)
        research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600,35+account*540,245,130))
        if (research_window):
            pag.click(research_window)
            time.sleep(0.3)
            Kingdom_ready(account,'kkd_out')
        return False
    
    screen = ImageGrab.grab()
    pix_research_ok_check = screen.getpixel((500,465+account*540)) # 연구 가능
    pix_green = (121, 207, 12)      # 녹색(가능)
    pix_grey = (160, 160, 160)      # 회색(불가능)
    
    if pix_research_ok_check == pix_green:
        pag.click(500,465+account*540)
        time.sleep(3)
        Kingdom_ready(account,'kkd_out')
        return True

# def Smith_action(account, prod_direction_left bsmithcompleted):
#     # prod_action의 return값은 continue?이고
#     # 생산함수를 합친 action 함수 return값은 completed?이다
#     if bsmithcompleted:
#         Skip_Next(account, prod_direction_left)
#         return True
    
#     Max_lev = 0
#     # 최대 레벨 확인
#     if smith_lev7 > 0:
#         Max_lev = 7
#     elif smith_lev6 > 0:
#         Max_lev = 6
#     elif smith_lev5 > 0:
#         Max_lev = 5
#     elif smith_lev4 > 0:
#         Max_lev = 4
#     elif smith_lev3 > 0:
#         Max_lev = 3
#     elif smith_lev2 > 0:
#         Max_lev = 2
#     elif smith_lev1 > 0:
#         Max_lev = 1
#     else:
#         print('대장간 생간 목표수량이 없습니다.')
#         Skip_Next(account, prod_direction_left)
#         return True
    
#     if 3 >= Max_lev > 0:
        
    
#     if not (smith_lev1==0) and not bsmithcompleted and Max_lev >= 1:
#         if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
#             if (smith_lev2==0):
#                 return True
#             if not (smith_lev2==0) and not bsmithcompleted and Max_lev >= 2:
#                 if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
#                     if (smith_lev3==0):
#                         return True
#                     if not (smith_lev3==0) and not bsmithcompleted and Max_lev >= 3:
#                         if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
#                             if (smith_lev4==0):
#                                 return True
#                             if not (smith_lev4==0) and not bsmithcompleted and Max_lev >= 4:
#                                 Updown(account,'up')
#                                 if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
#                                     if (smith_lev5==0):
#                                         return True
#                                     if not (smith_lev5==0) and not bsmithcompleted and Max_lev >= 5:
#                                         Updown(account,'up')
#                                         if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
#                                             if (smith_lev6==0):
#                                                 return True
#                                             if not (smith_lev6==0) and not bsmithcompleted and Max_lev >= 6:
#                                                 Updown(account,'up')
#                                                 if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
#                                                     if (smith_lev7==0):
#                                                         return True
#                                                     if not (smith_lev7==0) and not bsmithcompleted and Max_lev >= 7:
#                                                         Updown(account,'up')
#                                                         if not prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7):
#                                                             return True
#                                                         Skip_Next(account, prod_direction_left)
#                                                         return False
#                                                     else:
#                                                         Skip_Next(account, prod_direction_left)
#                                                         return False
#                                                 else:
#                                                     Skip_Next(account, prod_direction_left)
#                                                     return False
#                                             else:
#                                                 Skip_Next(account, prod_direction_left)
#                                                 return False
#                                         else:
#                                             Skip_Next(account, prod_direction_left)
#                                             return False
#                                     else:
#                                         Skip_Next(account, prod_direction_left)
#                                         return False
#                                 else:
#                                     Skip_Next(account, prod_direction_left)
#                                     return False
#                             else:
#                                 Skip_Next(account, prod_direction_left)
#                                 return False
#                         else:
#                             Skip_Next(account, prod_direction_left)
#                             return False
#                     else:
#                         Skip_Next(account, prod_direction_left)
#                         return False
#                 else:
#                     Skip_Next(account, prod_direction_left)
#                     return False
#             else:
#                 Skip_Next(account, prod_direction_left)
#                 return False
#         else:
#             Skip_Next(account, prod_direction_left)
#             return False
#     else:
#         Skip_Next(account, prod_direction_left)
#         return False
# 새 함수 추가가 필요할 경우 이 위에다 추가(++)



man_macro_chk_time = time.time()
while True:
    man_macroA = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.85, region=(635,5,22,22))
    man_macroB = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.85, region=(635,5+540,22,22))
    now_time = time.time()
    if now_time - man_macro_chk_time > man_mac_time:
        print('수동 매크로 동작 시간 초과하여 자동 매크로로 넘어갑니다.')
        if (man_macroA):
            pag.click(man_macroA)
            time.sleep(1)
        if (man_macroB):
            pag.click(man_macroB)
            time.sleep(1)
        break
    
    if keyboard.is_pressed('END'):
        break
    
    if (man_macroA) or (man_macroB):
        print('수동 매크로 동작중...',man_mac_time-now_time+man_macro_chk_time)
        time.sleep(5)
    else:
        print('수동 매크로 동작이 아니므로 자동 매크로 시작합니다.')
        time.sleep(1)
        break

while True: # 여기서부턴 실제 생산
    start_timeA = time.time()
    if keyboard.is_pressed('END'):
        break

    print('start time = ', start_timeA)
    
    while True:
        print('계정 스위칭...')
        if keyboard.is_pressed('END'):
            break

        #아무 계정도 돌고있지 않다. 할 때 A부터 시작함
        if (not bAccountA) and (not bAccountB):
            if bAcc_A_First:
                print('A 계정 시작합니다.')
                bAccountA = True
                bAccountB = False
                account = 0
                break
            else:
                print('B 계정 시작합니다.')
                bAccountA = False
                bAccountB = True
                account = 1
                break

        # A 돌고 오면 B 돌릴 차례
        if bAccountA and not bAccountB:
            man_macro_chk_time = time.time()
            man_macroB = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.85, region=(635,5+540,22,22))
            if (man_macroB):
                if macro_start - man_macro_chk_time > man_mac_time:
                    print('수동 매크로 동작 시간 초과하여 자동 매크로로 넘어갑니다.')
                    pag.click(man_macroB)
                    time.sleep(1)
                else:
                    print('B 계정 시작해야 하는데.. 매크로 돌고 있어 계속 A 돌립니다.')
                    break
            print('B 계정 시작합니다.')
            bAccountA = False
            bAccountB = True
            account = 1
            break

        # B 돌고 나면 A... 음 좀 이상한데 둘 다 돌면 끝낼까
        if not bAccountA and bAccountB:
            man_macro_chk_time = time.time()
            man_macroA = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.85, region=(635,5,22,22))
            if (man_macroA):
                if macro_start - man_macro_chk_time > man_mac_time:
                    print('수동 매크로 동작 시간 초과하여 자동 매크로로 넘어갑니다.')
                    pag.click(man_macroA)
                    time.sleep(1)
                else:
                    print('A 계정 시작해야 하는데.. 매크로 돌고 있어 계속 B 돌립니다.')
                    break
            print('A 계정 시작합니다.')
            bAccountA = True
            bAccountB = False
            account = 0
            break
        
        # 버그...면 우선 죽이고 보자
        if bAccountA and bAccountB:
            bAccountA = False
            bAccountB = False
            account = 0
            break

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
    if not bFirstCookhouA:
        cookie_time_A = time.time()
    if not bFirstFountainA:
        fountain_time_A = time.time()
    if not bFirstCookhouB:
        cookie_time_B = time.time()
    if not bFirstFountainB:
        fountain_time_B = time.time()

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
    if (cond_network):
        pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
        time.sleep(0.3)
    
    if account == 0:
        # print('A 계정 돕니다.')
        bTropical = bTropicalAction_A           # 트로피칼 돌릴래
        bResearch_auto = bResearch_auto_A       # 연구소 자동 돌릴래
        jjokji_limit = jjokji_limit_A           # 쪽지 보상까지만 돌릴래
        check_mark_action = check_mark_action_A # 건물 업글중 체크마크 클릭 안함
        jjokji_biscuit = jjokji_biscuit_A       # 비스킷 아낌모드
        jjokji_berry = jjokji_berry_A           # 젤리베리 아낌모드
        jjokji_milk = jjokji_milk_A             # 우유 아낌모드
        jjokji_cotton = jjokji_cotton_A         # 솜사탕 아낌모드
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
        fountain_set_time = fountain_set_time_A # 분수 클릭 주기
        cookie_set_time = cookie_set_time_A     # 쿠하 클릭 주기
    if account == 1:
        # print('B 계정 돕니다.')
        bTropical = bTropicalAction_B           # 트로피칼 돌릴래
        bResearch_auto = bResearch_auto_B       # 연구소 자동 돌릴래
        jjokji_limit = jjokji_limit_B           # 쪽지 보상까지만 돌릴래
        check_mark_action = check_mark_action_B # 건물 업글중 체크마크 클릭 안함
        jjokji_biscuit = jjokji_biscuit_B       # 비스킷 아낌모드
        jjokji_berry = jjokji_berry_B           # 젤리베리 아낌모드
        jjokji_milk = jjokji_milk_B             # 우유 아낌모드
        jjokji_cotton = jjokji_cotton_B         # 솜사탕 아낌모드
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
        fountain_set_time = fountain_set_time_B # 분수 클릭 주기
        cookie_set_time = cookie_set_time_B     # 쿠하 클릭 주기

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
        if Angmu_Enter(account,'trade'):
            Angmu_Aft_Refresh(account)
        
        # 연구소 돌리기...
        if bResearch_auto:
            if account == 0:
                if Angmu_Enter(account,'research'):
                    research_action(account,'C','research_C_23')   # 케이크 충전 가속
            if account == 1:
                if Angmu_Enter(account,'research'):
                    research_action(account,'C','research_C_283')   # 케이크 충전 가속

        # 열차
        if Angmu_Enter(account,'train'):     # 느낌표 떠있으면 들어감, 아니면 패스
            train_1 = Train_time(account,1)   # 왔으면 보내고;;
            train_2 = Train_time(account,2)
            train_3 = Train_time(account,3)
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
            Kingdom_ready(account,'kkd_out')
            # 시간 체크를 정확히 하려면 Train_time함수를 while True: 안에 넣어서 return 값이 True가 되는 조건으로...

        # 열기구 보내기
        if Angmu_Enter(account, 'balloon'):
            Ballon_send(account)

        # 21.12.04 추가 - 체크 마크 클릭하기
        check_mark_time = time.time()   # 혹시 모르니 시간 제한도 넣고..
        while True:
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
            if (cond_halted):
                pag.click(740,310+account*540)
                End_kkd(account)
                Kingdom_ready(account,'kkd_out')            # 재부팅

            now_time = time.time()
            check_check = pag.locateCenterOnScreen('check.png', confidence=0.95, region=(2,32+account*540,917,505))
            if (check_check):   # 있으면 클릭하긴 하는데..
                pag.click(check_check)
                time.sleep(1)   # 2초쯤 기다리면 되려나..
                # ++ 여기다 열차, 열기구, 연구소, 트로피칼, 건물 완료, 왕국 미션 완료 다 때려박아야할듯..
                Kingdom_ready(account, 'kkd_out')   # 이쯤 되니 헷갈리네....그냥 빠져나오는 거였나..
            if not (check_check):
                print('체크 마크 없네요!')
                break
            if (now_time - check_mark_time) > 120:  # 설마 2분은 안넘겠지..
                print('체크 마크 동작 시간 초과!')
                break
            time.sleep(1)

        # 실행 체크
        # Check_Initiating(account)
        Kingdom_ready(account,'kkd_out')
        #건물에 들어가기..
        Enter_Building(account)
        # 건물 안에 들어왔으니 생산 시작
        # 초기화
        cycle_check = 0
        prod_direction_left = True
        # 쑛텀 생산 시작
        while True:
            if keyboard.is_pressed('end'):
                break
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
            if (cond_network):
                pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
                time.sleep(0.3)

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
            if (cond_halted):
                pag.click(740,310+account*540)
                End_kkd(account)
                Kingdom_ready(account,'kkd_out')            # 재부팅
                break

            # urgent_now_t = time.time()
            # 설정 시간 지나면 나가기... 우선 1시간으로? 아님 시간 설정?
            # if urgent_now_t - urgent_start_t > 3600:
            #     pag.click(891,54+account*540)
            #     break
            if (cycle_check > 4):
                print('쑛텀 : %s계정 마치고 다음 계정 들어갑니다.'%(account))
                Kingdom_ready(account,'kkd_out')
                time.sleep(2)
                break
                
            kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence = 0.9, region=(2,32+account*540,917,505))
            lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
            pix_lackof = screen.getpixel((545,745-540+account*540)) # 재료부족창?

            pix_lackof1 = (243, 233, 223)   # 베이지색
            pix_wood = (117, 59, 41)	    #나무
            pix_jelbean = (1, 239, 236)	    #젤리빈
            pix_sugar = (255, 255, 255)	    #설탕
            pix_biscuit = (206, 132, 58)	#비스킷
            pix_berry = (187, 41, 46)	    #젤리베리
            pix_milk = (233, 242, 242)	    #우유
            pix_cotton = (255, 247, 255)	#솜
            
            pix_smith = (163, 117, 85)	    # 도끼 스미스
            pix_jelly = (13, 172, 202)	    # 젤리빈 잼 젤리
            pix_rollc = (214, 147, 102)	    # 솔새 롤케
            pix_bread = (142, 66, 9)	    # 호밀빵 브레드
            pix_jampy = (166, 30, 44)	    # 젤리스튜 잼파이
            pix_doye = (157, 84, 43)	    # 비스킷 화분 - 도예
            pix_flower = (255, 31, 130)	    # 캔디꽃 - flower
            pix_milky = (214, 230, 230)	    # 크림 - milky
            pix_latte = (255, 251, 239)	    # 젤리빈 라떼 - latte
            pix_dolls = (109, 235, 249)	    # 쿠션 - dolls
            pix_beer = (152, 102, 65)	    # 크림루트비어 - beer
            pix_muffin = (192, 91, 59)	    # 머핀 - muffin
            pix_jewel = (130, 90, 53)	    # 글레이즈드링 - jewel

            screen = ImageGrab.grab()
            pix_prod = screen.getpixel((610,140+account*540))
            
            if pix_lackof == pix_lackof1:
                print('꺼져!(off!)')
                pag.click(545,205+account*540)
                pag.keyDown('ESC')
                time.sleep(0.1)
                pag.keyUp('ESC')
                time.sleep(0.3)
                Skip_Next(account, prod_direction_left)
            
            if pix_prod == pix_wood:
                pix_error_count = 0
                print('wood!')
                Wood_to_Cotton_Quick(account, wood_max, 1, prod_direction_left)
                if prod_direction_left:
                    cycle_check = cycle_check + 1
            
            elif pix_prod == pix_jelbean:
                pix_error_count = 0
                print('jelbean!')
                Wood_to_Cotton_Quick(account, jelbean_max, 1, prod_direction_left)
            
            elif pix_prod == pix_sugar:
                pix_error_count = 0
                print('sugar!')
                Wood_to_Cotton_Quick(account, sugar_max, 1, prod_direction_left)

            elif pix_prod == pix_biscuit:
                pix_error_count = 0
                print('biscuit!')
                Wood_to_Cotton_Quick(account, biscuit_max, 2, prod_direction_left)
                
            elif pix_prod == pix_berry:
                pix_error_count = 0
                print('berry!')
                Wood_to_Cotton_Quick(account, berry_max, 2, prod_direction_left)
                
            elif pix_prod == pix_milk:
                pix_error_count = 0
                print('milk!')
                Wood_to_Cotton_Quick(account, milk_max, 1, prod_direction_left)
            
            elif pix_prod == pix_cotton:
                pix_error_count = 0
                print('cotton!')
                Wood_to_Cotton_Quick(account, cotton_max, cotton_prod, prod_direction_left)

            elif pix_prod == pix_smith:
                pix_error_count = 0
                print('smith!')
                # 작업 순방향 시작
                if not (smith_lev1==0) and not bsmithcompleted:
                    if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
                        if (smith_lev2==0):
                            bsmithcompleted =  True
                        if not (smith_lev2==0) and not bsmithcompleted:
                            if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
                                if (smith_lev3==0):
                                    bsmithcompleted =  True
                                if not (smith_lev3==0) and not bsmithcompleted:
                                    if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
                                        if (smith_lev4==0):
                                            bsmithcompleted =  True
                                        if not (smith_lev4==0) and not bsmithcompleted:
                                            Updown(account,'up')
                                            if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
                                                if (smith_lev5==0):
                                                    bsmithcompleted =  True
                                                if not (smith_lev5==0) and not bsmithcompleted:
                                                    Updown(account,'up')
                                                    if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
                                                        if (smith_lev6==0):
                                                            bsmithcompleted =  True
                                                        if not (smith_lev6==0) and not bsmithcompleted:
                                                            Updown(account,'up')
                                                            if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
                                                                if (smith_lev7==0):
                                                                    bsmithcompleted =  True
                                                                if not (smith_lev7==0) and not bsmithcompleted:
                                                                    Updown(account,'up')
                                                                    if not prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7):
                                                                        bsmithcompleted =  True
                                                                    Skip_Next(account, prod_direction_left)
                                                                else:
                                                                    Skip_Next(account, prod_direction_left)
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                else:
                    Skip_Next(account, prod_direction_left)
                # 작업 순방향 끝
            
            elif pix_prod == pix_jelly:
                pix_error_count = 0
                print('jelly!')
                # 작업 순방향 시작
                if not (jelly_lev1==0) and not bjellycompleted:
                    if not prod_action('jelly_lev1.png', 'jelly_stby_lv1.png', account, jelly_lev1):
                        if (jelly_lev2==0):
                            bjellycompleted = True
                        if not (jelly_lev2==0) and not bjellycompleted:
                            if not prod_action('jelly_lev2.png', 'jelly_stby_lv2.png', account, jelly_lev2):
                                if (jelly_lev3==0):
                                    bjellycompleted = True
                                if not (jelly_lev3==0) and not bjellycompleted:
                                    if not prod_action('jelly_lev3.png', 'jelly_stby_lv3.png', account, jelly_lev3):
                                        if (jelly_lev4==0):
                                            bjellycompleted = True
                                        if not (jelly_lev4==0) and not bjellycompleted:
                                            Updown(account,'up')
                                            if not prod_action('jelly_lev4.png', 'jelly_stby_lv4.png', account, jelly_lev4):
                                                if (jelly_lev5==0):
                                                    bjellycompleted = True
                                                if not (jelly_lev5==0) and not bjellycompleted:
                                                    Updown(account,'up')
                                                    if not prod_action('jelly_lev5.png', 'jelly_stby_lv5.png', account, jelly_lev5):
                                                        bjellycompleted = True
                                                    Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                else:
                    Skip_Next(account, prod_direction_left)
                # 작업 순방향 끝
            
            elif pix_prod == pix_rollc:
                pix_error_count = 0
                print('rollc!')
                # 작업 순방향 시작
                if not (rollc_lev1==0) and not brollccompleted:
                    if not prod_action('rollc_lev1.png', 'rollc_stby_lv1.png', account, rollc_lev1):
                        if (rollc_lev2==0):
                            brollccompleted = True
                        if not (rollc_lev2==0) and not brollccompleted:
                            if not prod_action('rollc_lev2.png', 'rollc_stby_lv2.png', account, rollc_lev2):
                                if (rollc_lev3==0):
                                    brollccompleted = True
                                if not (rollc_lev3==0) and not brollccompleted:
                                    if not prod_action('rollc_lev3.png', 'rollc_stby_lv3.png', account, rollc_lev3):
                                        if (rollc_lev4==0):
                                            brollccompleted = True
                                        if not (rollc_lev4==0) and not brollccompleted:
                                            Updown(account,'up')
                                            if not prod_action('rollc_lev4.png', 'rollc_stby_lv4.png', account, rollc_lev4):
                                                brollccompleted = True
                                            Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                else:
                    Skip_Next(account, prod_direction_left)
                # 작업 순방향 끝

            elif pix_prod == pix_bread:
                pix_error_count = 0
                print('bread!')
                prod_direction_left = True
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_jampy:
                pix_error_count = 0
                print('jampy!')
                prod_direction_left = True
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_doye:
                pix_error_count = 0
                print('doye!')
                prod_direction_left = True
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_flower:
                pix_error_count = 0
                print('flower!')
                prod_direction_left = True
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_milky:
                pix_error_count = 0
                print('milky!')
                prod_direction_left = True
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_latte:
                pix_error_count = 0
                print('latte!')
                prod_direction_left = False
                Skip_Next(account, prod_direction_left)


            elif pix_prod == pix_dolls:
                pix_error_count = 0
                print('dolls!')
                prod_direction_left = False
                Skip_Next(account, prod_direction_left)
                
            
            elif pix_prod == pix_beer:
                pix_error_count = 0
                print('beer!')
                prod_direction_left = False
                Skip_Next(account, prod_direction_left)

            elif pix_prod == pix_muffin:
                pix_error_count = 0
                print('muffin!')
                prod_direction_left = False
                Skip_Next(account, prod_direction_left)
            
            elif pix_prod == pix_jewel:
                pix_error_count = 0
                print('jewel!')
                prod_direction_left = False
                Skip_Next(account, prod_direction_left)

            elif (kkd_start):
                print('[생산중] 계정 튕김! 쿠킹덤을 실행합니다!')
                # 실행 체크
                Check_Initiating(account)
                # 줌아웃, 좌하단으로 화면이동. 간판 하나라도 찾으면 True.. 없을조건..도 만들어야겠네
                # Check_Prod_Ready(account)
                #건물에 들어가기..
                Enter_Building(account)
            
            elif (lack_of_material):
                print('아이템이 부족하대요~ 다음으로 넘어갑니다아~')
                pag.click(629,169+account*540)
                time.sleep(0.5)
                Skip_Next(account, prod_direction_left)
            
            elif not Kingdom_ready(account, 'prod_in'):
                print('설마 여기 도나')
                Enter_Building(account)
            
            else:
                pix_error_count = pix_error_count + 1
                if prod_pix_confirm >= pix_error_count:
                    print('건물 안에서... 픽셀값 찾게 위로 올림')
                    pag.moveTo(610,random.randint(140,160)+account*540)
                    time.sleep(0.1)
                    pag.mouseDown()
                    time.sleep(0.1)
                    pag.moveTo(610,160+350+account*540,0.3)
                    pag.mouseUp()
                    time.sleep(2)
                else:
                    print('건물 안에서... 이게 아니라면... 우선 좌클릭')
                    Skip_Next(account, prod_direction_left)
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
        # Check_Initiating(account)
        Kingdom_ready(account,'kkd_out')
        #건물에 들어가기..
        Enter_Building(account)
        # 건물 안에 들어왔으니 생산 시작
        Product_Start_Time = time.time()
        while True: # 건물 내 작업만 주구장창..?
            if keyboard.is_pressed('END'):
                break
            print('생산을 집도한다! 계정 = %s, 싸이클 = %s'%(account, cycle_check))
            Product_Now_Time = time.time()

            # 싸이클 완료 조건
            if (cycle_check > how_many_cycle*2) or ((Product_Now_Time - Product_Start_Time) > Producting_Time):
                print('싸이클 완료. 왕국 활동 진행 후 말미를 드립니다.')
                Kingdom_ready(account,'kkd_out')
                
                # 개별 계정 돌려야 하는 경우 : 쿠하만?
                now_time = time.time()  # 현재 시각은?
                if account == 0:
                    bAccount_A_Completed = True
                    # 분수 클릭(자연스레 좌상으로 화면 이동)
                    if not bFirstFountainA:
                        Angmu_Enter(account,'fountain')
                        fountain_time_A = time.time()  # 클릭한 시간을 다시 저장
                        bFirstFountainA = True
                    else:
                        if (now_time - fountain_time_A) > fountain_set_time_A:
                            Angmu_Enter(account,'fountain')
                            fountain_time_A = time.time()  # 클릭한 시간을 다시 저장

                    # 쿠하 클릭
                    if not bFirstCookhouA:
                        print('[쿠하] 계정 A 첫 클릭')
                        pag.click(pag.locateCenterOnScreen('Cond_cookiehouse.png', confidence=0.9,
                                                        region=(249, 78 + account * 540, 576, 382)))  # 917->845
                        cookie_time_A = time.time()  # 클릭한 시간을 다시 저장
                        bFirstCookhouA = True
                    else:
                        if (now_time - cookie_time_A) > cookie_set_time:
                            print('[쿠하] 설정 시간이 지나서 클릭합니다.', now_time - cookie_time_A)
                            pag.click(pag.locateCenterOnScreen('Cond_cookiehouse.png', confidence=0.9,
                                                            region=(249, 78 + account * 540, 576, 382)))  # 917->845
                            cookie_time_A = time.time()  # 클릭한 시간을 다시 저장
        
                        
                if account == 1:
                    bAccount_B_Completed = True
                    # 분수 클릭(자연스레 좌상으로 화면 이동)
                    if not bFirstFountainB:
                        Angmu_Enter(account,'fountain')
                        fountain_time_B = time.time()  # 클릭한 시간을 다시 저장
                        bFirstFountainB = True
                    else:
                        if (now_time - fountain_time_B) > fountain_set_time_B:
                            Angmu_Enter(account,'fountain')
                            fountain_time_B = time.time()  # 클릭한 시간을 다시 저장

                    # 쿠하 클릭
                    if not bFirstCookhouB:
                        print('[쿠하] 계정 B 첫 클릭')
                        pag.click(pag.locateCenterOnScreen('Cond_cookiehouse.png', confidence=0.9,
                                                        region=(2, 32 + account * 540, 845, 454)))  # 917->845
                        cookie_time_B = time.time()  # 클릭한 시간을 다시 저장
                        bFirstCookhouB = True
                    else:
                        if (now_time - cookie_time_B) > cookie_set_time:
                            print('[쿠하] 설정 시간이 지나서 클릭합니다.', now_time - cookie_time_B)
                            pag.click(pag.locateCenterOnScreen('Cond_cookiehouse.png', confidence=0.9,
                                                            region=(2, 32 + account * 540, 845, 454)))  # 917->845
                            cookie_time_B = time.time()  # 클릭한 시간을 다시 저장
                        
                
                
                # 여기서부턴 계정 자동 구분 되는 넘들
                # 211206 추가 - 하트 남은 수량 확인해서... 마지막으로 돈 곳을 다시 돌기.(위치 클릭)
                # 220203 추가 - 하트 클릭했을 때 밑에 시간 뜨면 조건확인, 안뜨면 바로 소진
                Kingdom_ready(account,'kkd_out')
                pag.screenshot('heart_full_check.png', region=(380, 65+account*540, 51, 14))
                pag.click(357,55+account*540)
                time.sleep(1)
                diff_check = pag.locateCenterOnScreen('heart_full_check.png', confidence=0.95, grayscale=True, region=(380, 65+account*540, 51, 14))
                if (diff_check):
                    print('하트 수량 Full입니다!')
                    pag.click(396,386+account*540)
                    time.sleep(1)
                    print('하트 소진모드 들어감다1')     # 마지막 들어간 곳이 센터정렬 되어서 그곳을 계속 돈다... 즉, 어둠모드는 아직 안됨 ㅠㅠ
                    time.sleep(1)
                    Heart_sojin(account,'8-29')         # 8-29라 쓰지만 의미 읍따는 ㅠㅠ
                else:
                    print('하트 수량 Full이 아닙니다.')
                    pag.click(396,386+account*540)
                    time.sleep(1)
                    while True:
                        cond_kkd_out\
                            = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국
                        cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12, 38 + account * 540, 37, 36))  # Play버튼 누른 후 모험하기 창
                        if (cond_adv_mode_select):      # 플레이 버튼 눌렀음
                            print('모험하기!')
                            break
                        if (cond_kkd_out):
                            Kingdom_ready(account,'kkd_out')    # 창 떠있는 경우 삭제용
                            print('하트소진모드 Play 버튼 클릭~!')
                            pag.click(random.randint(730,785),random.randint(470+account*540,525+account*540))
                            time.sleep(1)
                    if Heart_new_numb(account) > heart_set_num:
                        time.sleep(1)
                        print('하트 소진모드 들어감다2')     # 마지막 들어간 곳이 센터정렬 되어서 그곳을 계속 돈다... 즉, 어둠모드는 아직 안됨 ㅠㅠ
                        time.sleep(1)
                        Heart_sojin(account,'8-29')         # 8-29라 쓰지만 의미 읍따는 ㅠㅠ
                    else:
                        pag.click(2,2)
                        Kingdom_ready(account, 'kkd_out')
                
                for i in range(delay_to_next_account):
                    print('다음 계정 실행까지', delay_to_next_account - i, '초 남았습니다. 현재 계정: ', account)
                    time.sleep(1)
                    if keyboard.is_pressed('end'):
                        print('end 눌러 종료합니다.')
                        break

                # 220203 추가 - 뽑기 일일 보상 획득
                # 220226 추가 - 뽑기 아이콘으로 완료여부 판단
                cond_bbopkki = pag.locateCenterOnScreen('cond_bbopkki.png', confidence=0.85, region=(535,460+account*540,30,30))
                if (cond_bbopkki):
                    pag.click(532,504+account*540)
                    time.sleep(1)
                    cond_bbopkki2 = pag.locateCenterOnScreen('cond_bbopkki2.png', confidence=0.85, region=(60,315+account*540,22,22))
                    if (cond_bbopkki2):
                        pag.click(46,357+account*540)
                        time.sleep(0.5)
                        while True:
                            cond_bbopkki3 = pag.locateCenterOnScreen('cond_bbopkki3.png', confidence=0.85, region=(743,458+account*540,152,53))
                            if (cond_bbopkki3):
                                pag.click(cond_bbopkki3)
                                time.sleep(1)
                            else:
                                print('뽑기 일일보상 완료!')
                                pag.click(889,55+account*540)
                                Kingdom_ready(account,'kkd_out')
                                print('현재 계정 = ',account)
                                break
                else:
                    print('뽑기 일일보상은 완료함')
                time.sleep(2)
                print('상점들어가볼까')
                # 220302 추가 - 상점 일일보상 획득
                Angmu_Enter(account,'shop')

                # 220309 추가 - 길드 일일보상 획득
                Angmu_Enter(account,'guild')
                
                # 킹덤패스 보상 확인
                Kpass_reward(account)

                # 트로피칼 확인
                if bTropical:
                    if Tropical_Event(account):
                        Tropical_Fight(account)
                
                # 소원나무 쪽지 보내기
                Sowon_jjokji_action(jjokji_numb, account, jjokji_limit)
                break            
                
            in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8, region=(2,32+account*540,917,505))
            kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence = 0.9, region=(2,32+account*540,917,505))
            Confirm_button = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.9, region=(285,483+account*540,254,22))
            lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
            screen = ImageGrab.grab()
            pix_prod = screen.getpixel((610,140+account*540))
            pix_end = screen.getpixel((118,483+account*540)) # 하단 화살
            pix_end1 = screen.getpixel((115,415+account*540)) # 중단 화살
            pix_end2 = screen.getpixel((75,480+account*540)) # 밑바닥칸
            pix_lackof = screen.getpixel((545,745-540+account*540)) # 재료부족창?
            
            pix_arrow = (253, 252, 251)    # 하단 화살표
            pix_arrow1 = (251, 248, 246)    # 중단 화살표
            pix_arrow2 = (251, 248, 246)    # 밑바닥칸
            pix_lackof1 = (243, 233, 223)   # 베이지색
            pix_wood = (117, 59, 41)	#나무
            pix_jelbean = (1, 239, 236)	#젤리빈
            pix_sugar = (255, 255, 255)	#설탕
            pix_biscuit = (206, 132, 58)	#비스킷
            pix_berry = (187, 41, 46)	#젤리베리
            pix_milk = (233, 242, 242)	#우유
            pix_cotton = (255, 247, 255)	#솜
            pix_smith = (163, 117, 85)	#도끼 스미스
            pix_jelly = (13, 172, 202)	#젤리빈 잼 젤리
            pix_rollc = (214, 147, 102)	#솔새 롤케
            pix_bread = (142, 66, 9)	#호밀빵 브레드
            pix_jampy = (166, 30, 44)	# 젤리스튜 잼파이
            pix_doye = (157, 84, 43)	#비스킷 화분 - 도예
            pix_flower = (255, 31, 130)	#캔디꽃 - flower
            pix_milky = (214, 230, 230)	#크림 - milky
            pix_latte = (255, 251, 239)	#젤리빈 라떼 - latte
            pix_dolls = (109, 235, 249)	#쿠션 - dolls
            pix_beer = (152, 102, 65)	#크림루트비어 - beer
            pix_muffin = (192, 91, 59)	#머핀 - muffin
            pix_jewel = (130, 90, 53)	#글레이즈드링 - jewel
            pix_status_in = (194, 144, 10)    # 생산건물 내


            if keyboard.is_pressed('space'):
                break
            # 이상한 창이 떠있나?
            
            if pix_lackof == pix_lackof1:
                print('꺼져!(off!)')
                pag.click(545,205+account*540)
                pag.keyDown('ESC')
                time.sleep(0.1)
                pag.keyUp('ESC')
                time.sleep(0.3)
                pag.click(164,280+account*540)
                time.sleep(0.5)
            # 건물 내부 색상 파악
            elif pix_prod == pix_wood:
                pix_error_count = 0
                print('wood!')
                Wood_to_Cotton(account, wood_min, wood_max, wood_prod, prod_direction_left)
                cycle_check = cycle_check + 1
            
            elif pix_prod == pix_jelbean:
                pix_error_count = 0
                print('jelbean!')
                Wood_to_Cotton(account, jelbean_min, jelbean_max, jelbean_prod, prod_direction_left)
            
            elif pix_prod == pix_sugar:
                pix_error_count = 0
                print('sugar!')
                Wood_to_Cotton(account, sugar_min, sugar_max, sugar_prod, prod_direction_left)
                
            elif pix_prod == pix_biscuit:
                pix_error_count = 0
                print('biscuit!')
                jjokji_biscuit = Wood_to_Cotton(account, biscuit_min, biscuit_max, biscuit_prod, prod_direction_left)
            
            elif pix_prod == pix_berry:
                pix_error_count = 0
                print('berry!')
                jjokji_berry = Wood_to_Cotton(account, berry_min, berry_max, berry_prod, prod_direction_left)
            
            elif pix_prod == pix_milk:
                pix_error_count = 0
                print('milk!')
                jjokji_milk = Wood_to_Cotton(account, milk_min, milk_max, milk_prod, prod_direction_left)
            
            elif pix_prod == pix_cotton:
                pix_error_count = 0
                print('cotton!')
                jjokji_cotton = Wood_to_Cotton(account, cotton_min, cotton_max, cotton_prod, prod_direction_left)
            
            elif pix_prod == pix_smith:
                pix_error_count = 0
                print('smith!')
                if not bProdHigh or smith_num == 1:
                    bSecond=False
                    # 작업 순방향 시작
                    if not (smith_lev1==0) and not bsmithcompleted:
                        if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
                            if (smith_lev2==0):
                                bsmithcompleted =  True
                            if not (smith_lev2==0) and not bsmithcompleted:
                                if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
                                    if (smith_lev3==0):
                                        bsmithcompleted =  True
                                    if not (smith_lev3==0) and not bsmithcompleted:
                                        if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
                                            if (smith_lev4==0):
                                                bsmithcompleted =  True
                                            if not (smith_lev4==0) and not bsmithcompleted:
                                                Updown(account,'up')
                                                if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
                                                    if (smith_lev5==0):
                                                        bsmithcompleted =  True
                                                    if not (smith_lev5==0) and not bsmithcompleted:
                                                        Updown(account,'up')
                                                        if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
                                                            if (smith_lev6==0):
                                                                bsmithcompleted =  True
                                                            if not (smith_lev6==0) and not bsmithcompleted:
                                                                Updown(account,'up')
                                                                if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
                                                                    if (smith_lev7==0):
                                                                        bsmithcompleted =  True
                                                                    if not (smith_lev7==0) and not bsmithcompleted:
                                                                        Updown(account,'up')
                                                                        if not prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7):
                                                                            bsmithcompleted =  True
                                                                        Skip_Next(account, prod_direction_left)
                                                                    else:
                                                                        Skip_Next(account, prod_direction_left)
                                                                else:
                                                                    Skip_Next(account, prod_direction_left)
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or smith_num==1:
                        break
                    if bProdHigh and not bSecond and smith_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (smith_lev1==0):
                            if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
                                if not (smith_lev2==0):
                                    if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
                                        if not (smith_lev3==0):
                                            if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
                                                if not (smith_lev4==0):
                                                    Updown(account,'up')
                                                    if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
                                                        if not (smith_lev5==0):
                                                            Updown(account,'up')
                                                            if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
                                                                if not (smith_lev6==0):
                                                                    Updown(account,'up')
                                                                    if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
                                                                        if not (smith_lev7==0):
                                                                            Updown(account,'up')
                                                                            prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7)
                                                                            Skip_Next(account, prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                        else:
                                                                            Skip_Next(account, prod_direction_left)
                                                                            bSecond = True
                                                                            break
                                                                    else:
                                                                        Skip_Next(account, prod_direction_left)
                                                                        bSecond = True
                                                                        break
                                                                else:
                                                                    Skip_Next(account, prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
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
                                                prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1)
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = False
                                                break
                                            else:
                                                prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2)
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = False
                                                break
                                        else:
                                            prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        Updown(account, 'up')
                                        prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown(account, 'up')
                                    Updown(account, 'up')
                                    prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown(account, 'up')
                                Updown(account, 'up')
                                Updown(account, 'up')
                                prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account, 'up')
                            Updown(account, 'up')
                            Updown(account, 'up')
                            Updown(account, 'up')
                            prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7)
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('jelly_lev1.png', 'jelly_stby_lv1.png', account, jelly_lev1):
                            if (jelly_lev2==0):
                                bjellycompleted = True
                            if not (jelly_lev2==0) and not bjellycompleted:
                                if not prod_action('jelly_lev2.png', 'jelly_stby_lv2.png', account, jelly_lev2):
                                    if (jelly_lev3==0):
                                        bjellycompleted = True
                                    if not (jelly_lev3==0) and not bjellycompleted:
                                        if not prod_action('jelly_lev3.png', 'jelly_stby_lv3.png', account, jelly_lev3):
                                            if (jelly_lev4==0):
                                                bjellycompleted = True
                                            if not (jelly_lev4==0) and not bjellycompleted:
                                                Updown(account,'up')
                                                if not prod_action('jelly_lev4.png', 'jelly_stby_lv4.png', account, jelly_lev4):
                                                    if (jelly_lev5==0):
                                                        bjellycompleted = True
                                                    if not (jelly_lev5==0) and not bjellycompleted:
                                                        Updown(account,'up')
                                                        if not prod_action('jelly_lev5.png', 'jelly_stby_lv5.png', account, jelly_lev5):
                                                            bjellycompleted = True
                                                        Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or jelly_num==1:
                        break
                    if bProdHigh and not bSecond and jelly_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (jelly_lev1==0):
                            if not prod_action('jelly_lev1.png', 'jelly_stby_lv1.png', account, jelly_lev1):
                                if not (jelly_lev2==0):
                                    if not prod_action('jelly_lev2.png', 'jelly_stby_lv2.png', account, jelly_lev2):
                                        if not (jelly_lev3==0):
                                            if not prod_action('jelly_lev3.png', 'jelly_stby_lv3.png', account, jelly_lev3):
                                                if not (jelly_lev4==0):
                                                    Updown(account,'up')
                                                    if not prod_action('jelly_lev4.png', 'jelly_stby_lv4.png', account, jelly_lev4):
                                                        if not (jelly_lev5==0):
                                                            Updown(account,'up')
                                                            prod_action('jelly_lev5.png', 'jelly_stby_lv5.png', account, jelly_lev5)
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and jelly_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (jelly_lev5==0):
                            if (jelly_lev4==0):
                                if (jelly_lev3==0):
                                    if (jelly_lev2==0):
                                        prod_action('jelly_lev1.png', 'jelly_stby_lv1.png', account, jelly_lev1)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('jelly_lev2.png', 'jelly_stby_lv2.png', account, jelly_lev2)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('jelly_lev3.png', 'jelly_stby_lv3.png', account, jelly_lev3)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown(account,'up')
                                prod_action('jelly_lev4.png', 'jelly_stby_lv4.png', account, jelly_lev4)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account,'up')
                            Updown(account,'up')
                            prod_action('jelly_lev5.png', 'jelly_stby_lv5.png', account, jelly_lev5)
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('rollc_lev1.png', 'rollc_stby_lv1.png', account, rollc_lev1):
                            if (rollc_lev2==0):
                                brollccompleted = True
                            if not (rollc_lev2==0) and not brollccompleted:
                                if not prod_action('rollc_lev2.png', 'rollc_stby_lv2.png', account, rollc_lev2):
                                    if (rollc_lev3==0):
                                        brollccompleted = True
                                    if not (rollc_lev3==0) and not brollccompleted:
                                        if not prod_action('rollc_lev3.png', 'rollc_stby_lv3.png', account, rollc_lev3):
                                            if (rollc_lev4==0):
                                                brollccompleted = True
                                            if not (rollc_lev4==0) and not brollccompleted:
                                                Updown(account,'up')
                                                if not prod_action('rollc_lev4.png', 'rollc_stby_lv4.png', account, rollc_lev4):
                                                    brollccompleted = True
                                                Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or rollc_num==1:
                        break
                    if bProdHigh and not bSecond and rollc_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (rollc_lev1==0):
                            if not prod_action('rollc_lev1.png', 'rollc_stby_lv1.png', account, rollc_lev1):
                                if not (rollc_lev2==0):
                                    if not prod_action('rollc_lev2.png', 'rollc_stby_lv2.png', account, rollc_lev2):
                                        if not (rollc_lev3==0):
                                            if not prod_action('rollc_lev3.png', 'rollc_stby_lv3.png', account, rollc_lev3):
                                                if not (rollc_lev4==0):
                                                    Updown(account,'up')
                                                    prod_action('rollc_lev4.png', 'rollc_stby_lv4.png', account, rollc_lev4)
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and rollc_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (rollc_lev4==0):
                            if (rollc_lev3==0):
                                if (rollc_lev2==0):
                                    if (rollc_lev1==0):
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('rollc_lev1.png', 'rollc_stby_lv1.png', account, rollc_lev1)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('rollc_lev2.png', 'rollc_stby_lv2.png', account, rollc_lev2)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                prod_action('rollc_lev3.png', 'rollc_stby_lv3.png', account, rollc_lev3)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account,'up')
                            prod_action('rollc_lev4.png', 'rollc_stby_lv4.png', account, rollc_lev4)                
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('bread_lev1.png', 'bread_stby_lv1.png', account, bread_lev1):
                            if (bread_lev2==0):
                                bbreadcompleted = True
                            if not (bread_lev2==0) and not bbreadcompleted:
                                if not prod_action('bread_lev2.png', 'bread_stby_lv2.png', account, bread_lev2):
                                    if (bread_lev3==0):
                                        bbreadcompleted = True
                                    if not (bread_lev3==0) and not bbreadcompleted:
                                        if not prod_action('bread_lev3.png', 'bread_stby_lv3.png', account, bread_lev3):
                                            if (bread_lev4==0):
                                                bbreadcompleted = True
                                            if not (bread_lev4==0) and not bbreadcompleted:
                                                Updown(account,'up')
                                                if not prod_action('bread_lev4.png', 'bread_stby_lv4.png', account, bread_lev4):
                                                    if (bread_lev5==0):
                                                        bbreadcompleted = True
                                                    if not (bread_lev5==0) and not bbreadcompleted:
                                                        Updown(account,'up')
                                                        if not prod_action('bread_lev5.png', 'bread_stby_lv5.png', account, bread_lev5):
                                                            if (bread_lev6==0):
                                                                bbreadcompleted = True
                                                            if not (bread_lev6==0) and not bbreadcompleted:
                                                                Updown(account,'up')
                                                                if not prod_action('bread_lev6.png', 'bread_stby_lv6.png', account, bread_lev6):
                                                                    bbreadcompleted = True
                                                                Skip_Next(account, prod_direction_left)
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or bread_num==1:
                        break
                    if bProdHigh and not bSecond and bread_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (bread_lev1==0):
                            if not prod_action('bread_lev1.png', 'bread_stby_lv1.png', account, bread_lev1):
                                if not (bread_lev2==0):
                                    if not prod_action('bread_lev2.png', 'bread_stby_lv2.png', account, bread_lev2):
                                        if not (bread_lev3==0):
                                            if not prod_action('bread_lev3.png', 'bread_stby_lv3.png', account, bread_lev3):
                                                if not (bread_lev4==0):
                                                    Updown(account,'up')
                                                    if not prod_action('bread_lev4.png', 'bread_stby_lv4.png', account, bread_lev4):
                                                        if not (bread_lev5==0):
                                                            Updown(account,'up')
                                                            if not prod_action('bread_lev5.png', 'bread_stby_lv5.png', account, bread_lev5):
                                                                if not (bread_lev6==0):
                                                                    Updown(account,'up')
                                                                    prod_action('bread_lev6.png', 'bread_stby_lv6.png', account, bread_lev6)
                                                                    Skip_Next(account, prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                                else:
                                                                    Skip_Next(account, prod_direction_left)
                                                                    bSecond = True
                                                                    break
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
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
                                            prod_action('bread_lev1.png', 'bread_stby_lv1.png', account, bread_lev1)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('bread_lev2.png', 'bread_stby_lv2.png', account, bread_lev2)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('bread_lev3.png', 'bread_stby_lv3.png', account, bread_lev3)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown(account, 'up')
                                    prod_action('bread_lev4.png', 'bread_stby_lv4.png', account, bread_lev4)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown(account, 'up')
                                Updown(account, 'up')
                                prod_action('bread_lev5.png', 'bread_stby_lv5.png', account, bread_lev5)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account, 'up')
                            Updown(account, 'up')
                            Updown(account, 'up')
                            prod_action('bread_lev6.png', 'bread_stby_lv6.png', account, bread_lev6)
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('jampy_lev1.png', 'jampy_stby_lv1.png', account, jampy_lev1):
                            if (jampy_lev2==0):
                                bjampycompleted = True
                            if not (jampy_lev2==0) and not bjampycompleted:
                                if not prod_action('jampy_lev2.png', 'jampy_stby_lv2.png', account, jampy_lev2):
                                    if (jampy_lev3==0):
                                        bjampycompleted = True
                                    if not (jampy_lev3==0) and not bjampycompleted:
                                        if not prod_action('jampy_lev3.png', 'jampy_stby_lv3.png', account, jampy_lev3):
                                            if (jampy_lev4==0):
                                                bjampycompleted = True
                                            if not (jampy_lev4==0) and not bjampycompleted:
                                                Updown(account,'up')
                                                if not prod_action('jampy_lev4.png', 'jampy_stby_lv4.png', account, jampy_lev4):
                                                    if (jampy_lev5==0):
                                                        bjampycompleted = True
                                                    if not (jampy_lev5==0) and not bjampycompleted:
                                                        Updown(account,'up')
                                                        if not prod_action('jampy_lev5.png', 'jampy_stby_lv5.png', account, jampy_lev5):
                                                            if (jampy_lev6==0):
                                                                bjampycompleted = True
                                                            if not (jampy_lev6==0) and not bjampycompleted:
                                                                Updown(account,'up')
                                                                if not prod_action('jampy_lev6.png', 'jampy_stby_lv6.png', account, jampy_lev6):
                                                                    bjampycompleted = True
                                                                Skip_Next(account, prod_direction_left)
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or jampy_num==1:
                        break
                    if bProdHigh and not bSecond and jampy_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (jampy_lev1==0):
                            if not prod_action('jampy_lev1.png', 'jampy_stby_lv1.png', account, jampy_lev1):
                                if not (jampy_lev2==0):
                                    if not prod_action('jampy_lev2.png', 'jampy_stby_lv2.png', account, jampy_lev2):
                                        if not (jampy_lev3==0):
                                            if not prod_action('jampy_lev3.png', 'jampy_stby_lv3.png', account, jampy_lev3):
                                                if not (jampy_lev4==0):
                                                    Updown(account,'up')
                                                    if not prod_action('jampy_lev4.png', 'jampy_stby_lv4.png', account, jampy_lev4):
                                                        if not (jampy_lev5==0):
                                                            Updown(account,'up')
                                                            if not prod_action('jampy_lev5.png', 'jampy_stby_lv5.png', account, jampy_lev5):
                                                                if not (jampy_lev6==0):
                                                                    Updown(account,'up')
                                                                    prod_action('jampy_lev6.png', 'jampy_stby_lv6.png', account, jampy_lev6)
                                                                    Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
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
                                            prod_action('jampy_lev1.png', 'jampy_stby_lv1.png', account, jampy_lev1)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('jampy_lev2.png', 'jampy_stby_lv2.png', account, jampy_lev2)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('jampy_lev3.png', 'jampy_stby_lv3.png', account, jampy_lev3)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown(account, 'up')
                                    prod_action('jampy_lev4.png', 'jampy_stby_lv4.png', account, jampy_lev4)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown(account, 'up')
                                Updown(account, 'up')
                                prod_action('jampy_lev5.png', 'jampy_stby_lv5.png', account, jampy_lev5)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account, 'up')
                            Updown(account, 'up')
                            Updown(account, 'up')
                            prod_action('jampy_lev6.png', 'jampy_stby_lv6.png', account, jampy_lev6)
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('doye_lev1.png', 'doye_stby_lv1.png', account, doye_lev1):
                            if (doye_lev2==0):
                                bdoyecompleted = True
                                Skip_Next(account, prod_direction_left)
                            if not (doye_lev2==0) and not bdoyecompleted:
                                if not prod_action('doye_lev2.png', 'doye_stby_lv2.png', account, doye_lev2):
                                    if (doye_lev3==0):
                                        bdoyecompleted = True
                                        Skip_Next(account, prod_direction_left)
                                    if not (doye_lev3==0) and not bdoyecompleted:
                                        if not prod_action('doye_lev3.png', 'doye_stby_lv3.png', account, doye_lev3):
                                            if (doye_lev4==0):
                                                bdoyecompleted = True
                                                Skip_Next(account, prod_direction_left)
                                            if not (doye_lev4==0) and not bdoyecompleted:
                                                Updown(account,'up')
                                                if not prod_action('doye_lev4.png', 'doye_stby_lv4.png', account, doye_lev4):
                                                    bdoyecompleted = True
                                                Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or doye_num==1:
                        break
                    if bProdHigh and not bSecond and doye_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (doye_lev1==0):
                            if not prod_action('doye_lev1.png', 'doye_stby_lv1.png', account, doye_lev1):
                                if not (doye_lev2==0):
                                    if not prod_action('doye_lev2.png', 'doye_stby_lv2.png', account, doye_lev2):
                                        if not (doye_lev3==0):
                                            if not prod_action('doye_lev3.png', 'doye_stby_lv3.png', account, doye_lev3):
                                                if not (doye_lev4==0):
                                                    Updown(account,'up')
                                                    prod_action('doye_lev4.png', 'doye_stby_lv4.png', account, doye_lev4)
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
                            bSecond = True
                            break
                        # 작업 순방향 끝
                    if bProdHigh and bSecond and doye_num==2:  # 두 번째 건물 작업
                        # 작업 역방향 시작
                        if (doye_lev4==0):
                            if (doye_lev3==0):
                                if (doye_lev2==0):
                                    if (doye_lev1==0):
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                    else:
                                        prod_action('doye_lev1.png', 'doye_stby_lv1.png', account, doye_lev1)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    prod_action('doye_lev2.png', 'doye_stby_lv2.png', account, doye_lev2)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                prod_action('doye_lev3.png', 'doye_stby_lv3.png', account, doye_lev3)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account,'up')
                            prod_action('doye_lev4.png', 'doye_stby_lv4.png', account, doye_lev4)                
                            Skip_Next(account, prod_direction_left)
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
                        if not prod_action('flower_lev1.png', 'flower_stby_lv1.png', account, flower_lev1):
                            if (flower_lev2==0):
                                bflowercompleted = True
                                Skip_Next(account, prod_direction_left)
                            if not (flower_lev2==0) and not bflowercompleted:
                                if not prod_action('flower_lev2.png', 'flower_stby_lv2.png', account, flower_lev2):
                                    if (flower_lev3==0):
                                        bflowercompleted = True
                                        Skip_Next(account, prod_direction_left)
                                    if not (flower_lev3==0) and not bflowercompleted:
                                        if not prod_action('flower_lev3.png', 'flower_stby_lv3.png', account, flower_lev3):
                                            if (flower_lev4==0):
                                                bflowercompleted = True
                                                Skip_Next(account, prod_direction_left)
                                            if not (flower_lev4==0) and not bflowercompleted:
                                                Updown(account,'up')
                                                if not prod_action('flower_lev4.png', 'flower_stby_lv4.png', account, flower_lev4):
                                                    if (flower_lev5==0):
                                                        bflowercompleted = True
                                                        Skip_Next(account, prod_direction_left)
                                                    if not (flower_lev5==0) and not bflowercompleted:
                                                        Updown(account,'up')
                                                        if not prod_action('flower_lev5.png', 'flower_stby_lv5.png', account, flower_lev5):
                                                            if (flower_lev6==0):
                                                                bflowercompleted = True
                                                                Skip_Next(account, prod_direction_left)
                                                            if not (flower_lev6==0) and not bflowercompleted:
                                                                Updown(account,'up')
                                                                if not prod_action('flower_lev6.png', 'flower_stby_lv6.png', account, flower_lev6):
                                                                    bflowercompleted = True
                                                                Skip_Next(account, prod_direction_left)
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                else:
                                    Skip_Next(account, prod_direction_left)
                            else:
                                Skip_Next(account, prod_direction_left)
                        else:
                            Skip_Next(account, prod_direction_left)
                    else:
                        Skip_Next(account, prod_direction_left)
                    # 작업 순방향 끝
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if not bProdHigh or flower_num==1:
                        break
                    if bProdHigh and not bSecond and flower_num==2:  # 첫 번째 건물 작업
                        # 작업 순방향 시작
                        if not (flower_lev1==0):
                            if not prod_action('flower_lev1.png', 'flower_stby_lv1.png', account, flower_lev1):
                                if not (flower_lev2==0):
                                    if not prod_action('flower_lev2.png', 'flower_stby_lv2.png', account, flower_lev2):
                                        if not (flower_lev3==0):
                                            if not prod_action('flower_lev3.png', 'flower_stby_lv3.png', account, flower_lev3):
                                                if not (flower_lev4==0):
                                                    Updown(account,'up')
                                                    if not prod_action('flower_lev4.png', 'flower_stby_lv4.png', account, flower_lev4):
                                                        if not (flower_lev5==0):
                                                            Updown(account,'up')
                                                            if not prod_action('flower_lev5.png', 'flower_stby_lv5.png', account, flower_lev5):
                                                                if not (flower_lev6==0):
                                                                    Updown(account,'up')
                                                                    prod_action('flower_lev6.png', 'flower_stby_lv6.png', account, flower_lev6)
                                                                    Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                            else:
                                                                Skip_Next(account, prod_direction_left)
                                                                bSecond = True
                                                                break
                                                        else:
                                                            Skip_Next(account, prod_direction_left)
                                                            bSecond = True
                                                            break
                                                    else:
                                                        Skip_Next(account, prod_direction_left)
                                                        bSecond = True
                                                        break
                                                else:
                                                    Skip_Next(account, prod_direction_left)
                                                    bSecond = True
                                                    break
                                            else:
                                                Skip_Next(account, prod_direction_left)
                                                bSecond = True
                                                break
                                        else:
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = True
                                            break
                                    else:
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = True
                                        break
                                else:
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = True
                                    break
                            else:
                                Skip_Next(account, prod_direction_left)
                                bSecond = True
                                break
                        else:
                            Skip_Next(account, prod_direction_left)
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
                                            prod_action('flower_lev1.png', 'flower_stby_lv1.png', account, flower_lev1)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                        else:
                                            prod_action('flower_lev2.png', 'flower_stby_lv2.png', account, flower_lev2)
                                            Skip_Next(account, prod_direction_left)
                                            bSecond = False
                                            break
                                    else:
                                        prod_action('flower_lev3.png', 'flower_stby_lv3.png', account, flower_lev3)
                                        Skip_Next(account, prod_direction_left)
                                        bSecond = False
                                        break
                                else:
                                    Updown(account, 'up')
                                    prod_action('flower_lev4.png', 'flower_stby_lv4.png', account, flower_lev4)
                                    Skip_Next(account, prod_direction_left)
                                    bSecond = False
                                    break
                            else:
                                Updown(account, 'up')
                                Updown(account, 'up')
                                prod_action('flower_lev5.png', 'flower_stby_lv5.png', account, flower_lev5)
                                Skip_Next(account, prod_direction_left)
                                bSecond = False
                                break
                        else:
                            Updown(account, 'up')
                            Updown(account, 'up')
                            Updown(account, 'up')
                            prod_action('flower_lev6.png', 'flower_stby_lv6.png', account, flower_lev6)
                            Skip_Next(account, prod_direction_left)
                            bSecond = False
                            break
                    # 작업 역방향 끝

            
            elif pix_prod == pix_milky:
                pix_error_count = 0
                print('milky!')
                if not bmilkycompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'milky_stby_lv1.png','milky_stby_lv2.png','milky_stby_lv3.png',milky_lev1,milky_lev2,milky_lev3, prod_direction_left):
                        bmilkycompleted = True
                else:
                    Skip_Next(account, prod_direction_left)

            
            elif pix_prod == pix_latte:
                pix_error_count = 0
                print('latte!')
                if not blattecompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'latte_stby_lv1.png','latte_stby_lv2.png','latte_stby_lv3.png',latte_lev1,latte_lev2,latte_lev3, prod_direction_left):
                        blattecompleted = True
                else:
                    Skip_Next(account, prod_direction_left)


            elif pix_prod == pix_dolls:
                pix_error_count = 0
                print('dolls!')
                if not bdollcompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'dolls_stby_lv1.png','dolls_stby_lv2.png','dolls_stby_lv3.png',dolls_lev1,dolls_lev2,dolls_lev3, prod_direction_left):
                        bdollcompleted = True
                else:
                    Skip_Next(account, prod_direction_left)
                
            
            elif pix_prod == pix_beer:
                pix_error_count = 0
                print('beer!')
                if not bbeercompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'beer_stby_lv1.png','beer_stby_lv2.png','beer_stby_lv3.png',beer_lev1,beer_lev2,beer_lev3, prod_direction_left):
                        bbeercompleted = True
                else:
                    Skip_Next(account, prod_direction_left)
                

            elif pix_prod == pix_muffin:
                pix_error_count = 0
                print('muffin!')
                if not bmuffincompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'muffin_stby_lv1.png','muffin_stby_lv2.png','muffin_stby_lv3.png',muffin_lev1,muffin_lev2,muffin_lev3, prod_direction_left):
                        bmuffincompleted = True
                else:
                    Skip_Next(account, prod_direction_left)
                
            
            elif pix_prod == pix_jewel:
                pix_error_count = 0
                print('jewel!')
                if not bjewelcompleted:
                    print('생산 확인...')
                    if not three_prod_action(account,'jewel_stby_lv1.png','jewel_stby_lv2.png','jewel_stby_lv3.png',jewel_lev1,jewel_lev2,jewel_lev3, prod_direction_left):
                        bjewelcompleted = True
                else:
                    Skip_Next(account, prod_direction_left)
                

            elif (kkd_start):
                print('[생산중] 계정 튕김! 쿠킹덤을 실행합니다!')
                # 실행 체크
                # Check_Initiating(account)
                Kingdom_ready(account,'kkd_out')
                #건물에 들어가기..
                Enter_Building(account)
            
            elif (lack_of_material):
                print('아이템이 부족하대요~ 다음으로 넘어갑니다아~')
                pag.click(629,169+account*540)
                time.sleep(0.5)
                pag.click(164,280+account*540)
                time.sleep(0.5)
            
            
            elif not Kingdom_ready(account, 'prod_in'):
                print('설마 여기 도나')
                Enter_Building(account)
            
            else:
                pix_error_count = pix_error_count + 1
                if prod_pix_confirm >= pix_error_count:
                    print('건물 안에서... 픽셀값 찾게 위로 올림')
                    pag.moveTo(610,random.randint(140,160)+account*540)
                    time.sleep(0.1)
                    pag.mouseDown()
                    time.sleep(0.1)
                    pag.moveTo(610,160+350+account*540,0.3)
                    pag.mouseUp()
                    time.sleep(1.5)
                else:
                    print('건물 안에서... 이게 아니라면... 우선 좌클릭')
                    pag.click(158,279+account*540)
                    time.sleep(1)

            print('이 밖인가')
        




end = time.time()
print('총 매크로 동작 시간은 =', end-macro_start)