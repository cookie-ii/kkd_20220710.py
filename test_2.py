from abc import abstractproperty
from cgitb import text
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

account = 1
# //// 여기부턴 조건 확인용
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
fountain_set_time_A = 1800  # 분수 클릭 주기
cookie_set_time_A = 1800    # 쿠키하우스 클릭 주기
fountain_set_time_B = 1800  # 분수 클릭 주기
cookie_set_time_B = 1800    # 쿠키하우스 클릭 주기
how_many_cycle = 2          # 생산 사이클
delay_to_next_account = 1   # 다음 계정 동작 전 대기시간
heart_set_num = 70          # 하트가 이 숫자보다 많으면.. 모험 실행
man_mac_time = 6000         # 수동 매크로 돌리고 파이썬 실행한 경우, 이 시간 후에 수동 매크로 끄고 자동 돌림
prod_pix_confirm = 2        # 픽셀 못읽는거 n번(스크롤업 n*2 번) 해도 안되면 좌로 넘김

smith_num_A = 2           # 대장간 건물 수
smith_lev1_A = 200        # 도끼
smith_lev2_A = 200        # 곡괭이
smith_lev3_A = 200        # 톱
smith_lev4_A = 200        # 삽
smith_lev5_A = 100        # 말뚝
smith_lev6_A = 140        # 집게
smith_lev7_A = 140        # 망치

jelly_num_A = 2           # 젤리쨈 건물 수
jelly_lev1_A = 200      # 젤리빈
jelly_lev2_A = 200      # 스윗젤리 잼
jelly_lev3_A = 200      # 달고나 잼
jelly_lev4_A = 60      # 석류 잼
jelly_lev5_A = 0      # 톡톡베리 잼

rollc_num_A = 2           #롤케이크 건물 수
rollc_lev1_A = 200       # 솔방울새 인형
rollc_lev2_A = 140       # 도토리 램프
rollc_lev3_A = 80       # 뻐꾹뻐꾹 시계
rollc_lev4_A = 50       # 백조깃털 드림캐처

bread_num_A = 2           # 빵집 건물 수
bread_lev1_A = 120      # 든든한 호밀빵
bread_lev2_A = 120      # 달콤쫀득 잼파이
bread_lev3_A = 120      # 은행 포카치아
bread_lev4_A = 80      # 슈가코팅 도넛
bread_lev5_A = 80      # 폭신 카스테라
bread_lev6_A = 0      # 골드리치 크로와상

jampy_num_A = 2           # 잼파이 건물 수
jampy_lev1_A = 100       # 따끈따끈 젤리스튜
jampy_lev2_A = 60       # 곰젤리 버거
jampy_lev3_A = 60       # 캔디크림 파스타
jampy_lev4_A = 40       # 폭신폭신 오므라이스
jampy_lev5_A = 50       # 콤비네이션 피자젤리
jampy_lev6_A = 0        # 고급스러운 젤리빈 정식

doye_num_A = 2            # 토닥토닥 도예공방 건물 수
doye_lev1_A = 200        # 비스킷 화분
doye_lev2_A = 140        # 반짝반짝 유리판
doye_lev3_A = 140        # 반짝이는 색동구슬
doye_lev4_A = 70        # 무지갯빛 디저트 보울

flower_num_A = 2          # 꽃가게 건물 수
flower_lev1_A = 100      # 캔디꽃
flower_lev2_A = 100      # 행복한 꽃화분
flower_lev3_A = 40      # 캔디꽃다발
flower_lev4_A = 30      # 롤리팝 꽃바구니
flower_lev5_A = 30      # 유리꽃 부케
flower_lev6_A = 40      # 찬란한 요거트 화환

milky_num_A = 2           # 우유 가공소 건물 수
milky_lev1_A = 80        # 크림
milky_lev2_A = 40       # 버터
milky_lev3_A = 40       # 수제 치즈

latte_num_A = 2         # 라떼 건물 수
latte_lev1_A = 100       # 젤리빈 라떼
latte_lev2_A = 80       # 몽글몽글 버블티
latte_lev3_A = 0        # 스윗베리 에이드

dolls_num_A = 2         # 러블리 인형공방 건물 수
dolls_lev1_A = 70      # 구름사탕 쿠션
dolls_lev2_A = 28      # 곰젤리 솜인형
dolls_lev3_A = 0      # 용과 드래곤 솜인형

beer_num_A = 1          # 오크통 쉼터 건물 수
beer_lev1_A = 40        # 크림 루트비어
beer_lev2_A = 24        # 레드베리 주스
beer_lev3_A = 24        # 빈티지 와일드 보틀

muffin_num_A = 1        # 퐁 드 파티세리 건물 수
muffin_lev1_A = 20      # 으스스 머핀
muffin_lev2_A = 14      # 생딸기 케이크
muffin_lev3_A = 20      # 파티파티 쉬폰케이크

jewel_num_A = 1          # 살롱 드 쥬얼리 건물 수
jewel_lev1_A = 25      # 글레이즈드 링
jewel_lev2_A = 30      # 루비베리 브로치
jewel_lev3_A = 30      # 로얄 곰젤리 크라운



smith_num_B = 2           # 대장간 건물 수
smith_lev1_B = 200        # 도끼
smith_lev2_B = 200        # 곡괭이
smith_lev3_B = 200        # 톱
smith_lev4_B = 200        # 삽
smith_lev5_B = 100        # 말뚝
smith_lev6_B = 100        # 집게
smith_lev7_B = 140        # 망치

jelly_num_B = 2           # 젤리쨈 건물 수
jelly_lev1_B = 200      # 젤리빈 잼
jelly_lev2_B = 200      # 스윗젤리 잼
jelly_lev3_B = 300      # 달고나 잼
jelly_lev4_B = 0      # 석류 잼
jelly_lev5_B = 0      # 톡톡베리 잼

rollc_num_B = 2           #롤케이크 건물 수
rollc_lev1_B = 200       # 솔방울새 인형
rollc_lev2_B = 160       # 도토리 램프
rollc_lev3_B = 80       # 뻐꾹뻐꾹 시계
rollc_lev4_B = 90       # 백조깃털 드림캐처

bread_num_B = 2           # 빵집 건물 수
bread_lev1_B = 160      # 든든한 호밀빵
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
doye_lev3_B = 220       # 반짝이는 색동구슬
doye_lev4_B = 0       # 무지갯빛 디저트 보울

flower_num_B = 2          # 꽃가게 건물 수
flower_lev1_B = 200      # 캔디꽃
flower_lev2_B = 220      # 행복한 꽃화분
flower_lev3_B = 200      # 캔디꽃다발
flower_lev4_B = 80      # 롤리팝 꽃바구니
flower_lev5_B = 0      # 유리꽃 부케
flower_lev6_B = 0      # 찬란한 요거트 화환

milky_num_B = 2           # 우유 가공소 건물 수
milky_lev1_B = 200      # 크림
milky_lev2_B = 0      # 버터
milky_lev3_B = 0      # 수제 치즈

latte_num_B = 2         # 라떼 건물 수
latte_lev1_B = 200      # 젤리빈 라떼
latte_lev2_B = 0      # 몽글몽글 버블티
latte_lev3_B = 0      # 스윗베리 에이드

dolls_num_B = 2         # 러블리 인형공방 건물 수
dolls_lev1_B = 80      # 구름사탕 쿠션
dolls_lev2_B = 100      # 곰젤리 솜인형
dolls_lev3_B = 0      # 용과 드래곤 솜인형

beer_num_B = 1          # 오크통 쉼터 건물 수
beer_lev1_B = 30      # 크림 루트비어
beer_lev2_B = 10      # 레드베리 주스
beer_lev3_B = 10      # 빈티지 와일드 보틀

muffin_num_B = 1        # 퐁 드 파티세리 건물 수
muffin_lev1_B = 143      # 으스스 머핀
muffin_lev2_B = 0      # 생딸기 케이크
muffin_lev3_B = 0      # 파티파티 쉬폰케이크

jewel_num_B = 1          # 살롱 드 쥬얼리 건물 수
jewel_lev1_B = 30      # 글레이즈드 링
jewel_lev2_B = 0      # 루비베리 브로치
jewel_lev3_B = 0      # 로얄 곰젤리 크라운

if account == 0:
    print('A 계정 돕니다.')
    smith_lev1 = smith_lev1_A        # 도끼
    smith_lev2 = smith_lev2_A         # 곡괭이
    smith_lev3 = smith_lev3_A         # 톱
    smith_lev4 = smith_lev4_A        # 삽
    smith_lev5 = smith_lev5_A         # 말뚝
    smith_lev6 = smith_lev6_A         # 집게
    smith_lev7 = smith_lev7_A         # 망치
    jelly_lev1 = jelly_lev1_A     # 젤리빈
    jelly_lev2 = jelly_lev2_A       # 스윗젤리 잼
    jelly_lev3 = jelly_lev3_A      # 달고나 잼
    jelly_lev4 = jelly_lev4_A       # 석류 잼
    jelly_lev5 = jelly_lev5_A      # 톡톡베리 잼
    rollc_lev1 = rollc_lev1_A        # 솔방울새 인형
    rollc_lev2 = rollc_lev2_A        # 도토리 램프
    rollc_lev3 = rollc_lev3_A        # 뻐꾹뻐꾹 시계
    rollc_lev4 = rollc_lev4_A        # 백조깃털 드림캐처
    bread_lev1 = bread_lev1_A      # 든든한 호밀빵
    bread_lev2 = bread_lev2_A       # 달콤쫀득 잼파이
    bread_lev3 = bread_lev3_A       # 은행 포카치아
    bread_lev4 = bread_lev4_A       # 슈가코팅 도넛
    bread_lev5 = bread_lev5_A       # 폭신 카스테라
    bread_lev6 = bread_lev6_A      # 골드리치 크로와상
    jampy_lev1 = jampy_lev1_A      # 따끈따끈 젤리스튜
    jampy_lev2 = jampy_lev2_A      # 곰젤리 버거
    jampy_lev3 = jampy_lev3_A      # 캔디크림 파스타
    jampy_lev4 = jampy_lev4_A      # 폭신폭신 오므라이스
    jampy_lev5 = jampy_lev5_A      # 콤비네이션 피자젤리
    jampy_lev6 = jampy_lev6_A      # 고급스러운 젤리빈 정식
    doye_lev1 = doye_lev1_A       # 비스킷 화분
    doye_lev2 = doye_lev2_A       # 반짝반짝 유리판
    doye_lev3 = doye_lev3_A       # 반짝이는 색동구슬
    doye_lev4 = doye_lev4_A       # 무지갯빛 디저트 보울
    flower_lev1 = flower_lev1_A      # 캔디꽃
    flower_lev2 = flower_lev2_A      # 행복한 꽃화분
    flower_lev3 = flower_lev3_A      # 캔디꽃다발
    flower_lev4 = flower_lev4_A      # 롤리팝 꽃바구니
    flower_lev5 = flower_lev5_A      # 유리꽃 부케
    flower_lev6 = flower_lev6_A      # 찬란한 요거트 화환
    milky_lev1 = milky_lev1_A      # 크림
    milky_lev2 = milky_lev2_A      # 버터
    milky_lev3 = milky_lev3_A      # 수제 치즈
    latte_lev1 = latte_lev1_A      # 젤리빈 라떼
    latte_lev2 = latte_lev2_A      # 몽글몽글 버블티
    latte_lev3 = latte_lev3_A      # 스윗베리 에이드
    dolls_lev1 = dolls_lev1_A      # 구름사탕 쿠션
    dolls_lev2 = dolls_lev2_A      # 곰젤리 솜인형
    dolls_lev3 = dolls_lev3_A      # 용과 드래곤 솜인형
    beer_lev1 = beer_lev1_A      # 크림 루트비어
    beer_lev2 = beer_lev2_A      # 레드베리 주스
    beer_lev3 = beer_lev3_A      # 빈티지 와일드 보틀
    muffin_lev1 = muffin_lev1_A      # 으스스 머핀
    muffin_lev2 = muffin_lev2_A      # 생딸기 케이크
    muffin_lev3 = muffin_lev3_A      # 파티파티 쉬폰케이크
    jewel_lev1 = jewel_lev1_A      # 글레이즈드 링
    jewel_lev2 = jewel_lev2_A      # 루비베리 브로치
    jewel_lev3 = jewel_lev3_A      # 로얄 곰젤리 크라운
    smith_num = smith_num_A     # 대장간 건물 수
    jelly_num = jelly_num_A     # 젤리쨈 건물 수
    rollc_num = rollc_num_A     #롤케이크 건물 수
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
    cookie_set_time = cookie_set_time_A      # 쿠하 클릭 주기
if account == 1:
    print('B 계정 돕니다.')
    smith_lev1 = smith_lev1_B        # 도끼
    smith_lev2 = smith_lev2_B         # 곡괭이
    smith_lev3 = smith_lev3_B         # 톱
    smith_lev4 = smith_lev4_B        # 삽
    smith_lev5 = smith_lev5_B         # 말뚝
    smith_lev6 = smith_lev6_B         # 집게
    smith_lev7 = smith_lev7_B         # 망치
    jelly_lev1 = jelly_lev1_B     # 젤리빈
    jelly_lev2 = jelly_lev2_B       # 스윗젤리 잼
    jelly_lev3 = jelly_lev3_B      # 달고나 잼
    jelly_lev4 = jelly_lev4_B       # 석류 잼
    jelly_lev5 = jelly_lev5_B      # 톡톡베리 잼
    rollc_lev1 = rollc_lev1_B        # 솔방울새 인형
    rollc_lev2 = rollc_lev2_B        # 도토리 램프
    rollc_lev3 = rollc_lev3_B        # 뻐꾹뻐꾹 시계
    rollc_lev4 = rollc_lev4_B        # 백조깃털 드림캐처
    bread_lev1 = bread_lev1_B      # 든든한 호밀빵
    bread_lev2 = bread_lev2_B       # 달콤쫀득 잼파이
    bread_lev3 = bread_lev3_B       # 은행 포카치아
    bread_lev4 = bread_lev4_B       # 슈가코팅 도넛
    bread_lev5 = bread_lev5_B       # 폭신 카스테라
    bread_lev6 = bread_lev6_B      # 골드리치 크로와상
    jampy_lev1 = jampy_lev1_B      # 따끈따끈 젤리스튜
    jampy_lev2 = jampy_lev2_B      # 곰젤리 버거
    jampy_lev3 = jampy_lev3_B      # 캔디크림 파스타
    jampy_lev4 = jampy_lev4_B      # 폭신폭신 오므라이스
    jampy_lev5 = jampy_lev5_B      # 콤비네이션 피자젤리
    jampy_lev6 = jampy_lev6_B      # 고급스러운 젤리빈 정식
    doye_lev1 = doye_lev1_B       # 비스킷 화분
    doye_lev2 = doye_lev2_B       # 반짝반짝 유리판
    doye_lev3 = doye_lev3_B       # 반짝이는 색동구슬
    doye_lev4 = doye_lev4_B       # 무지갯빛 디저트 보울
    flower_lev1 = flower_lev1_B      # 캔디꽃
    flower_lev2 = flower_lev2_B      # 행복한 꽃화분
    flower_lev3 = flower_lev3_B      # 캔디꽃다발
    flower_lev4 = flower_lev4_B      # 롤리팝 꽃바구니
    flower_lev5 = flower_lev5_B      # 유리꽃 부케
    flower_lev6 = flower_lev6_B      # 찬란한 요거트 화환
    milky_lev1 = milky_lev1_B      # 크림
    milky_lev2 = milky_lev2_B      # 버터
    milky_lev3 = milky_lev3_B      # 수제 치즈
    latte_lev1 = latte_lev1_B      # 젤리빈 라떼
    latte_lev2 = latte_lev2_B      # 몽글몽글 버블티
    latte_lev3 = latte_lev3_B      # 스윗베리 에이드
    dolls_lev1 = dolls_lev1_B      # 구름사탕 쿠션
    dolls_lev2 = dolls_lev2_B      # 곰젤리 솜인형
    dolls_lev3 = dolls_lev3_B      # 용과 드래곤 솜인형
    beer_lev1 = beer_lev1_B      # 크림 루트비어
    beer_lev2 = beer_lev2_B      # 레드베리 주스
    beer_lev3 = beer_lev3_B      # 빈티지 와일드 보틀
    muffin_lev1 = muffin_lev1_B      # 으스스 머핀
    muffin_lev2 = muffin_lev2_B      # 생딸기 케이크
    muffin_lev3 = muffin_lev3_B      # 파티파티 쉬폰케이크
    jewel_lev1 = jewel_lev1_B      # 글레이즈드 링
    jewel_lev2 = jewel_lev2_B      # 루비베리 브로치
    jewel_lev3 = jewel_lev3_B      # 로얄 곰젤리 크라운
    smith_num = smith_num_B     # 대장간 건물 수
    jelly_num = jelly_num_B     # 젤리쨈 건물 수
    rollc_num = rollc_num_B     #롤케이크 건물 수
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
    cookie_set_time = cookie_set_time_B      # 쿠하 클릭 주기

# import schedule

# def printhello():
#     print("Hello!")
# schedule.every(5).seconds.do(printhello)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# 각 이미지 저장
# ofs = 0
# pag.screenshot('cotton_stby_lv1.png', region=(51, 176, 48, 48))
# pag.screenshot('cotton_stby_lv2.png', region=(51, 249, 48, 48))
# pag.screenshot('cotton_stby_lv3.png', region=(51, 319, 48, 48))
# pag.screenshot('flower_stby_lv4.png', region=(51, 391, 48, 48))
# a = pag.locateAllOnScreen('latte_stby_lv1.png')
# b = pag.locateAllOnScreen('latte_stby_lv2.png')
# c = pag.locateAllOnScreen('milky_stby_lv3.png')
# d = pag.locateAllOnScreen('flower_stby_lv4.png')
# a = list(a)
# b = list(b)
# c = list(c)
# d = list(d)
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))

# 소원나무 이미지 확인
# pag.screenshot('cotton_stby_lv1.png', region=(51, 176, 48, 48))
# pag.screenshot('cotton_stby_lv2.png', region=(51, 249, 48, 48))
# pag.screenshot('cotton_stby_lv3.png', region=(51, 319, 48, 48))
# pag.screenshot('flower_stby_lv4.png', region=(51, 391, 48, 48))

# bAccA = False
# bAccB = False
# i = 0
# while True:
#     if not bAccA and not bAccB:
#         print('A 시작')
#         bAccA = True
#         time.sleep(1)
#     if i == 0:
#         start_Time = time.time()
#     if i > 0:
#         end_Time = time.time()
#         if (end_Time):
#             if end_Time - start_Time > 13:
#                 print('13초 지남!')
#                 break
#     while bAccA:
#         Acc_A_Time = time.time()
#         while True:
#             print('A작업작업작업')
#             time.sleep(1)
#             Acc_A_end_Time = time.time()
#             print(Acc_A_end_Time - Acc_A_Time)
#             if Acc_A_end_Time - Acc_A_Time > 5:
#                 print('A를 5초 작업함')
#                 break
#         bAccB = True
#         bAccA = False
#         break
#     while bAccB:
#         Acc_B_Time = time.time()
#         while True:
#             print('B작업작업작업')
#             time.sleep(1)
#             Acc_B_end_Time = time.time()
#             print(Acc_B_end_Time - Acc_B_Time)
#             if Acc_B_end_Time - Acc_B_Time > 5:
#                 print('B를 5초 작업함')
#                 break
#         bAccB = False
#         bAccA = True
#         break
#     i = i+1

# pag.screenshot('wood_number.png', region=(500,46+540,49,18))
# img_read = cv2.imread('wood_number.png', cv2.IMREAD_GRAYSCALE)
# img_read_exp = cv2.resize(img_read, dsize=(0,0), fx=20, fy=20)
# text = pytesseract.image_to_string(img_read_exp, lang='eng')
# print('인식한 숫자 = ', text)
# print('len(text) = ', len(text))
# if len(text) >= 5:
#     text.split()
#     text = list(text)
#     print(text)
#     wood_numb = int(text[0])*1000 + int(text[2])*100 + int(text[3])*10 + int(text[4])
# else:
#     wood_numb = int(text)
# print(wood_numb)

# in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8)
# print(in_pos)

# a = "1,245"
# for i in range(len(a)):
#     if '0' <= a[i][0] <= '9':
#         print('yes!')
#     else:
#         print('no!!!')
# account = 0
# prd_done = pag.locateCenterOnScreen('Cond_prod_done.png', confidence=0.9, region=(0,0+account*540,960,540))
# prd_ing = pag.locateCenterOnScreen('Cond_prod_ing.png', confidence=0.9, region=(0,0+account*540,960,540))

# if (prd_done):
#     print('Found complete!')
#     pag.click(340,280,1)

# if (prd_ing):
#     print('Found ing!')


# for i in range(4):
#     x = random.randint(-400, 400)
#     y = random.randint(-300, 300)
#     print(x)
#     print(y)

def Skip_Next(account):
    pag.click(164,280+account*540)
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


def Updown(account, updown):
    if updown == 'up':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610,295+account*540-173,2)   # 153인데 20 더 여유줌
        time.sleep(0.2)
        pag.mouseUp()
        time.sleep(0.2)
        pag.click(262,328+account*540)
        time.sleep(2)
    if updown == 'down':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610,295+account*540+173,2)   # 153인데 20 더 여유줌
        time.sleep(0.2)
        pag.mouseUp()
        time.sleep(0.2)
        pag.click(262,328+account*540)
        time.sleep(2)


def Prod_Max_Numb(account):
    Max_7 = pag.locateCenterOnScreen('Max_7.png', confidence=0.95, region=(87,65+account*540,8,12))   # 쩜


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

def Train_time(account, line):
    train_arrive_time = pag.locateCenterOnScreen('train_arrive_time.png', confidence=0.9, region=(280,150+account*540+(line-1)*149,75,28))
    
    while True:
        if not (train_arrive_time):
            print('if not 조건')
            train_arrived = pag.locateCenterOnScreen('Cond_train_arrived.png', confidence=0.95, region=(492,118+account*540+(line-1)*149,333,111))
            
            if (train_arrived):
                pag.click(train_arrived)
                time.sleep(3)
            
            send_train = pag.locateCenterOnScreen('Cond_train_send.png', confidence=0.85, region=(500,110+account*540+(line-1)*149,290,120))
            send_train_error = pag.locateCenterOnScreen('Cond_train_send_error.png', confidence=0.95, region=(500,110+account*540+(line-1)*149,290,120))
            
            if (send_train):
                print('기차 보내자')
                pag.click(send_train)
                time.sleep(5)
            
            if (send_train_error):
                print('납품 불가한 제품이 있습니다.')
                time.sleep(1)
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




# start = time.time()

# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     screen = ImageGrab.grab()
#     pix_status = screen.getpixel((605,55+account*540)) # 상단골드
#     pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
#     print('status = ', pix_status)
#     print('status2 = ',pix_status2)
#     pix_status_bal_arrive = (170, 168, 168) # 열기구 보상수령(바닥 글씨 마침표)
#     pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
#     pix_status_bal_choice = (74, 44, 34)    # 탐사지 변경 누르면
#     pix_status_ballon = (64, 55, 45)  # 열기구 날아다니는 중
#     pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐

#     if pix_status2 == pix_status_bal_arrive: # 잘못하면 뽑기로 드감
#         print('열기구! 화면을 터치해 완료하세요.')
#         pag.click(540, 510+account*540)
#         time.sleep(2)

#     if pix_status == pix_status_bal_lobby:
#         print('이걸로 끝낼 수 있을까..!')
#         pag.click(540, 510+account*540)     #마침표랑 동일위치
#         time.sleep(1)
#         pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
#         time.sleep(0.1)
#         pag.drag(845,0,1)                   # 오른 아래까지1
#         time.sleep(1.5)
#         pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
#         time.sleep(0.1)
#         pag.drag(845,0,1)                   # 오른 아래까지2
#         time.sleep(1.5)
#         pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
#         time.sleep(0.1)
#         pag.drag(845,0,1)                   # 오른 아래까지3
#         time.sleep(1.5)
#         pag.moveTo(45,510+account*540)      # 왼쪽 아래에서
#         time.sleep(0.1)
#         pag.drag(845,0,1)                   # 오른 아래까지4
#         time.sleep(1.5)
#         # pag.click(535,255+account*540)      # 이건 2렙이고
#         pag.click(750,325+account*540)      # 이건 3렙이고
#         # pag.click(895,400+account*540)      # 이건 4렙이고
#         time.sleep(1)
#         pag.click(345,505+account*540)      # 이건 자동선택이고
#         time.sleep(0.7)
#         pag.click(760,505+account*540)      # 이건 보내기고
#         time.sleep(2)
    
#     if pix_status == pix_status_bal_window:
#         pag.click(284,15+account*540)
#         time.sleep(0.1)
#         pag.hotkey('esc')
#         time.sleep(0.5)
#         pag.hotkey('esc')
#         time.sleep(0.3)
#         print('젤리가 부족한가벼..')
#         break



#     if pix_status == pix_status_bal_choice:
#         pag.moveTo(45,510+account*540)     # 왼쪽 아래로 드래그
#         time.sleep(0.1)
#         pag.drag(845,0,1)

#     if pix_status == pix_status_ballon:
#         print('완성!')
#         break

#     time.sleep(1)

# 일정 시간 이후 동작하는거
# action_a1 = 0
# while True:
#     time_now = time.time()
#     print('a 계정 작업 1 시작')
#     if action_a1 == 0:
#         print('1을 처음 시작했습니다.')
#         time_a1 = time.time()
#         action_a1 = action_a1 + 1
    
#     if time_now - time_a1 < 5:
#         print('1 작업 시작 후 ', time_now - time_a1)
#     else:
#         print('1작업 후 5초 지나서 리셋합니다.')
#         time_a1 = time.time()
    
#     if keyboard.is_pressed('end'):
#         print('end를 눌러 종료합니다.')
#         break
#     time.sleep(1)

# iProdA = 2
# iProdB = 1
# iProdC = 1
# bProdRev = True
# bSecond = False
# iThisA = 1
# iThisB = 2
# a=False
# b=False
# i=0
# j=0
# while True:
#     while True:
#         print('condition =',a, b, j)
#         time.sleep(1)
#         if not a and not b:
#             print('act1')
#             a = True
#             break
#         if a and not b:
#             print('act2')
#             a = False
#             b = True
#             break
#         if (not a and b) and (j == 0):
#             print('act3')
#             j = j+1
#             break
#         if (not a and b) and (j != 0):
#             print('act4')
#             a = True
#             b = False
#             j = 0
#             break
#     while True:
#         print('action =', a,b,i)
#         if a:
#             print('a')
#             if not bProdRev or iThisA == 1:
#                 bSecond = False
#                 print('a1')
#                 print('a2')
#                 print('a3')
#                 time.sleep(1)
#             while True:
#                 if bProdRev and not bSecond and iThisA==2:
#                     print('a1')
#                     print('a2')
#                     print('a3')
#                     bSecond=True
#                     time.sleep(1)
#                     break
#                 if bProdRev and bSecond and iThisA==2:
#                     print('a3')
#                     print('a2')
#                     print('a1')
#                     bSecond=False
#                     time.sleep(1)
#                     break
#         if b:
#             print('b')
#             if not bProdRev or iThisB == 1:
#                 bSecond = False
#                 print('b1')
#                 print('b2')
#                 print('b3')
#                 time.sleep(1)
#             while True:
#                 if bProdRev and not bSecond and iThisB==2:
#                     print('b1')
#                     print('b2')
#                     print('b3')
#                     bSecond=True
#                     time.sleep(1)
#                     break
#                 if bProdRev and bSecond and iThisB==2:
#                     print('b3')
#                     print('b2')
#                     print('b1')
#                     bSecond=False
#                     time.sleep(1)
#                     break
#         i=i+1
#         break
#     if i>5:
#         break

# pag.click(284,15+account*540)
# time.sleep(0.1)
# pag.hotkey('esc')
# time.sleep(2)
# pag.click(910,random.randint(53,55)+account*540) # =표시 클릭
# time.sleep(1.5)
# print('스샷모드 들어감다')
# pag.click(760,335+account*540)  # 스샷모드
# time.sleep(1.5)
# print('줌아웃 하고')
# pag.moveTo(366,375+account*540)
# time.sleep(0.1)
# pag.keyDown('Ctrlleft')
# time.sleep(0.1)
# pag.scroll(-40)
# time.sleep(1)
# pag.scroll(-40)
# time.sleep(1)
# pag.scroll(-40)
# time.sleep(0.1)
# pag.keyUp('Ctrlleft')
# time.sleep(1)
# print('드래그')
# pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
# time.sleep(0.1)
# pag.drag(200, 300, 0.3)
# time.sleep(0.7)
# pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
# time.sleep(0.1)
# pag.drag(200, 300, 0.3)
# time.sleep(0.7)
# pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
# time.sleep(0.1)
# pag.drag(200, 300, 0.3)
# time.sleep(0.7)
# pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
# time.sleep(0.1)
# pag.drag(200, 300, 0.3)
# time.sleep(0.7)
# pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
# time.sleep(0.1)
# pag.drag(200, 300, 0.3)
# time.sleep(1)
# pag.click(284,15+account*540)
# time.sleep(0.5)
# pag.hotkey('esc')
# time.sleep(2)
# pag.click(690,350+account*540)
# time.sleep(2)
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((605,55+account*540)) # 상단골드
# print(pix_status)
# pix_status_fountain = (84, 93, 134) # 분수..
# pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
# if pix_status == pix_status_fountain:
#     pag.click(680,470+account*540)
#     time.sleep(5)
# pag.click(300,115+account*540)
# time.sleep(1)
# pag.click(1351+account*451,145) # 수동매크로.. 하... 곰젤리열차
# time.sleep(40)
# if pix_status == pix_status_sowon:
#     pag.hotkey('esc')
#     time.sleep(2)
# pag.click(pag.locateCenterOnScreen('Cond_cookiehouse.png',confidence=0.9, region=(2,32+account*540,917,505)))

# wanted_enter = pag.locateAllOnScreen('Cond_wanted.png', confidence=0.95)
# wanted_select = pag.locateAllOnScreen('Cond_wanted_select.png', confidence=0.95)

# wanted_enter = list(wanted_enter)
# list_wanted = list()
# for p in wanted_enter:
#     ctr = pag.center(p)
#     list_wanted.append(ctr)

# print(list_wanted)

# wanted_select = list(wanted_select)
# list_wanted = list()
# for p in wanted_select:
#     ctr = pag.center(p)
#     list_wanted.append(ctr)

# print(list_wanted)



# train_A_1 = Train_time(0,1)
# train_A_2 = Train_time(0,2)
# train_A_3 = Train_time(0,3)
# train_B_1 = Train_time(1,1)
# train_B_2 = Train_time(1,2)
# train_B_3 = Train_time(1,3)
# if train_A_1:
#     print(train_A_1)
# else:
#     print(Train_time(0,1))
# if train_A_2:
#     print(train_A_2)
# else:
#     print(Train_time(0,1))
# if train_A_3:
#     print(train_A_3)
# else:
#     print(Train_time(0,1))
# if train_B_1:
#     print(train_B_1)
# else:
#     print(Train_time(0,1))
# if train_B_2:
#     print(train_B_2)
# else:
#     print(Train_time(0,1))
# if train_B_3:
#     print(train_B_3)
# else:
#     print(Train_time(0,1))

def Kingdom_ready(account, whereto):    # 특정 위치 확인
    error_position = 0
    start_time = time.time()
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
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
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
        
        # 220203 추가 - 이미지 확인방식 추가(업뎃 후 픽셀값 변경...)
        cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국
        cond_kkd_train = pag.locateCenterOnScreen('cond_kkd_train.png', confidence=0.85, region=(30,42+account*540,25,33))  # 곰젤리열차
        cond_kkd_tro = pag.locateCenterOnScreen('cond_kkd_tro.png', confidence=0.85, region=(18,448+account*540,45,40))    # 트로피칼(좌하단 파라솔 꽃)
        cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430,45+account*540,31,35))    # 소원나무
        cond_kkd_sangjum = pag.locateCenterOnScreen('cond_kkd_sangjum.png', confidence=0.85, region=(14,40+account*540,46,29))   # 상점
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
        
        print('[Kingdom_ready] 현재 픽셀값 : ', pix_status)
        print('[Kingdom_ready] 실행 %s초 지났습니다.'%(now_time - start_time))
        
        if (cond_gold):
            # 혹시 또 1픽셀씩 오갈 수 있..으니?
            if 593 >= cond_gold.x >= 591:
                # 소원,열차,상점,쿠키성 중 하나!
                if not (cond_kkd_sowon) and not (cond_kkd_train) and not (cond_kkd_sangjum):
                    print('쿠키성이네요!')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
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
            time.sleep(0.1)
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
                time.sleep(0.1)
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
                time.sleep(0.1)
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
                time.sleep(0.1)
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
                time.sleep(0.1)
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
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(0.3)

        elif pix_status == pix_status_kdpass:    # 킹덤패스
            print('킹덤패스! 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.3)

        elif pix_status == pix_status_warehouse:    # 창고
            print('창고! 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.3)
    
        elif pix_status == pix_status_lotto:    # 뽑기
            print('뽑기 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.3)

        elif pix_status == pix_status_mycookie:    # 내 쿠키..
            print('내쿠키 아냐!')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.3)            
        
        elif pix_status == pix_status_not_prod:     # 건물 클릭했지만 쿠하나 일반건물
            print('이상한 건물!')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(1)

        elif (cond_kkd_train):
            if (whereto == 'train_in'):
                print('곰젤리 열차입니다!')
                return True
            else:
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(1)
                
        elif (cond_kkd_sowon):
            if (whereto == 'sowon_in'):
                print('소원나무 입니다!')
                return True
            else:
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(1)
             
        elif (cond_kkd_sangjum):
            if (whereto == 'sangjum_in'):
                print('상점 입니다!')
                return True
            else:
                print('상점으로 가려던 게 아니니 나갑니다.')
                pag.click(284,15+account*540)
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(1)

        elif pix_status == pix_status_cookiehouse:
            print('쿠키하우스 안이에요')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(1)

        elif pix_status == pix_status_out_window:
            print('창을 닫아요~')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(1)
        
        elif pix_status == pix_status_out_esc:
            print('esc 취소')
            pag.click(284,15+account*540)
            time.sleep(0.1)
            pag.hotkey('esc')
            time.sleep(0.7)
        
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
                time.sleep(0.1)
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
                time.sleep(0.1)
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
                time.sleep(0.1)
                pag.hotkey('esc')
                time.sleep(2)
                pag.hotkey('esc')
                time.sleep(2)
        
        else:
            if not (pix_status2 == 'wanted_end'):
                print('그 모든 게 아니라면....')
                if error_position == 0:
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(1)
                    pag.hotkey('ctrl','alt','up')
                if error_position > 3:
                    pag.click(605,55+account*540)
                    time.sleep(5)
                if error_position == 6:
                    pag.click(284,15+account*540)
                    pag.hotkey('ctrl','alt','up')
                if error_position > 7:
                    End_kkd(account)
                    Check_Initiating(account)
                    error_position = 0
                print('Error count =', error_position)
                error_position = error_position +1
            else:
                print('여긴 안도니')
                time.sleep(5)
                return False

def Check_Initiating(account):
    print('부팅여부 확인합니다.')
    bStart = False
    bTouchto = False
    kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence = 0.9, region=(2,32+account*540,917,505))
    kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence = 0.8, region=(2,32+account*540,917,505))
    kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence = 0.95, region=(2,32+account*540,917,505))
    while True:
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))

        if (play_halted):
            pag.click(play_halted)
        else:
            break

    if (kkd_start) or (kkd_touch) or (kkd_down):
        while True:
            if keyboard.is_pressed('end'):
                return
            
            while True:
                play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))
                if (play_halted):
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

def Updown(account, updown):
    if updown == 'up':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610,295+account*540-173,2)   # 153인데 20 더 여유줌
        time.sleep(0.2)
        pag.mouseUp()
        time.sleep(0.2)
        pag.click(262,328+account*540)
        time.sleep(2)
    if updown == 'down':
        pag.moveTo(610,295+account*540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(610,295+account*540+173,2)   # 153인데 20 더 여유줌
        time.sleep(0.2)
        pag.mouseUp()
        time.sleep(0.2)
        pag.click(262,328+account*540)
        time.sleep(2)

def prod_check(image, account):
    error_count = 0
    while True:
        if keyboard.is_pressed('end'):
            break
        its_location = pag.locateCenterOnScreen(image, grayscale=True, region=(590,83+account*540, 30, 455), confidence=0.95)
        if not (its_location):
            error_count = error_count + 1
            time.sleep(0.5)
            pag.moveTo(610,295+account*540)
            pag.mouseDown()
            time.sleep(0.2)
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

def Heart_new_numb(account):
    # ++
    heart_new_heart = pag.locateCenterOnScreen('heart_new_heart.png',confidence=0.85,region=(30,430+account*540,40,42))
    if (heart_new_heart):
        print('heart_new_heart',heart_new_heart)
        x1 = heart_new_heart[0]+22
    else:
        print('하트를 못찾아요!')
        return
    heart_new_slash = pag.locateCenterOnScreen('heart_new_slash.png',confidence=0.95,region=(83,443+account*540,17,19))
    if (heart_new_slash):
        print('heart_new_slash',heart_new_slash)
        x2 = heart_new_slash[0]-3
    else:
        print('슬래시를 못찾아요!')
        return

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

def warehouse_check(x, y):
    error_count = 0
    if keyboard.is_pressed('end'):
        print('end 누름')        
        return
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
    find_ware_num('up_t0.png', x, y, list_num_0)
    find_ware_num('up_t1.png', x, y, list_num_1)
    find_ware_num('up_t2.png', x, y, list_num_2)
    find_ware_num('up_t3.png', x, y, list_num_3)
    find_ware_num('up_t4.png', x, y, list_num_4)
    find_ware_num('up_t5.png', x, y, list_num_5)
    find_ware_num('up_t6.png', x, y, list_num_6)
    find_ware_num('up_t7.png', x, y, list_num_7)
    find_ware_num('up_t8.png', x, y, list_num_8)
    find_ware_num('up_t9.png', x, y, list_num_9)
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

def find_num(image, yPosition, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(620,yPosition+20,33,18))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def find_ware_num(image, x, y, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(x-1,y+15,47,20))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

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


def three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3):
    start_time = time.time()
    # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
    pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
    time.sleep(0.5)
    # 풀리스트인 경우 넘어감
    prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
    prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
    if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
        print('리스트 full!')
        Skip_Next(account)
        return True

    # 3렙건물이니 고정
    prod_pin = (612, 95+account*540)

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

    print('numbb1,2,3', list_numbb1,list_numbb2,list_numbb3)
    while True:
        now_time = time.time()
        
        # 풀리스트인 경우 넘어감
        prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
        prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
        if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!')
            Skip_Next(account)
            return True
        # 동작시간 확인
        if now_time - start_time > 30:
            print('동작 최대시간 초과 입니다.')
            Skip_Next(account)
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
            Skip_Next(account)
            return True
        else:
            max_numb = max(compare_numb1, compare_numb2, compare_numb3)
            if max_numb == compare_numb1 and not prod_line1_completed:
                pag.click(random.randint(745,745+65),random.randint(190,190+15)+account*540)
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
                pag.click(random.randint(745,745+65),random.randint(190,190+15)+153+account*540)
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
                pag.click(random.randint(745,745+65),random.randint(190,190+15)+153*2+account*540)
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


# pix_status_bal_arrive = (170, 168, 168) # 열기구 보상수령(바닥 글씨 마침표)
# pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
# if pix_status2 == pix_status_fight_comp:
#     print('마침표!')
# print(Enter_activity(account,'train'))

# while True:
#     if keyboard.is_pressed('end'):
#         break
#     if (Kingdom_ready(account,'train_in')):
#         send_train_error1 = pag.locateCenterOnScreen('Cond_train_send_error.png', confidence=0.95, region=(500,110+account*540,290,120))
#         send_train_error2 = pag.locateCenterOnScreen('Cond_train_send_error.png', confidence=0.95, region=(500,110+account*540+1*149,290,120))
#         send_train_error3 = pag.locateCenterOnScreen('Cond_train_send_error.png', confidence=0.95, region=(500,110+account*540+2*149,290,120))
#         if not (send_train_error1):
#             Train_time(account,1)
#         if not (send_train_error2):
#             Train_time(account,2)
#         if not (send_train_error3):
#             Train_time(account,3)
#             # 이 사이에 저 에러코드 음...
#         print('모든 시간을 받았다...')
#         break
#     else:
#         if not Enter_activity(account,'train'):
#             print('할 게 없대요')
#             break
#         else:
#             pag.click(155,360+account*540)

# 분수 남은 시간 확인... 테서렉트로...?
# 이것도 노가다로 하면 혹시?
# while True:
#     pag.screenshot('fountain_t.png', region=(758,66,87,21))
#     img_read = cv2.imread('fountain_t.png', cv2.IMREAD_GRAYSCALE)
#     img_read_exp = cv2.resize(img_read, dsize=(0,0), fx=10, fy=10)
#     text = pytesseract.image_to_string(img_read_exp, lang='kor')
#     print('인식한 숫자 = ', text)
#     time.sleep(1)

#     if keyboard.is_pressed('end'):
#         break


# while True:
#     if keyboard.is_pressed('end'):
#         break

#     pag.screenshot('fountain_t.png', region=(758,66,87,21))
#     img_read = cv2.imread('fountain_t.png', cv2.IMREAD_GRAYSCALE)
#     img_read_exp = cv2.resize(img_read, dsize=(0,0), fx=10, fy=10)
#     text = pytesseract.image_to_string(img_read_exp, lang='kor')
#     print('인식한 텍스트 = ', text)
#     text_l = text.split()
#     print(text_l)
#     if len(text_l)==3:
#     if len(text_l)==2:
#     if len(text_l)==1:

#     time.sleep(1)
    

# text = '1시간 47초'
# # text = '15분 47초'
# hour_split = text.split()
# print(hour_split)

# num_1 = hour_split[0].split()
# num_2 = hour_split[1].split()
# print(num_1)
# print(num_2)
# min_split = text.split(sep="분 ", maxsplit=1)
# sec_split = text.split(sep="초", maxsplit=1)
# if len(hour_split)==2:
#     text_hour = hour_split[0]
#     print(text_hour,'시간')
# if len(min_split)==2:
#     text_min = min_split[0]
#     print(text_min,'분')
# if len(sec_split)==2:
#     text_sec = sec_split[0]
#     print(text_sec,'초')
# print('h',text_hour,'m',text_min,'s',text_sec)
# bTrue = False
# print(bTrue)
# while True:
#     if keyboard.is_pressed('end'):
#         break
#     while True:
#         if not bTrue:
#             print('첫 실행')
#             bTrue = True
#             time.sleep(1)
#             break
#         if bTrue:
#             print('2 이후 실행')
#             time.sleep(1)
#             break
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
        pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
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
            pag.click(345,505+account*540)      # 이건 자동선택이고
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




# a=0
# b=19000
# c=True
# print('a: %s, b: %s, c: %s'%(a,b,c))


# account=1
# line=1
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((605,55+account*540)) # 상단골드
# pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
# print(pix_status)
# pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
# pix_status_ballon = (64, 55, 45)  # 열기구 날아다니는 중
# pix_status_bal_window = (127, 95, 4)    #열기구 창 떠서 어두워짐
# print('status = ', pix_status)
# print('status2 = ',pix_status2)
# ctr = pag.locateCenterOnScreen('bread_lev5.png', region=(2,32+account*540,917,505))
# pag.moveTo(ctr)
# print('Fist : %s, Shield : %s, Sword : %s, Staff : %s'%(fist,shield,sword,staff))
# pag.click(fist.x+147-74,fist.y+448-416)
# 월(돌격/침투), 화(방어/마법), 수(사격/폭발), 목(지원/회복)
# 금(돌격/방어/침투/마법), 토(사격/폭발/지원/회복)
# 주(all)
# Today_wanted(0,'all')
# Today_wanted(1,'all')
# Heart_sojin(0,'8-29')
# Heart_sojin(1,'8-29')
# pix_status_list3 = screen.getpixel((75,343+account*540)) # 상단골드
# pix_status_list4 = screen.getpixel((75,343+71+account*540)) # 상단골드
# print('list 3 =', pix_status_list3)
# print('list 4 =', pix_status_list4)

def End_kkd(account):
    pag.click(284,15+account*540)
    time.sleep(0.3)
    pag.click(940,520+account*540)
    time.sleep(3)
    pag.click(677,137+account*540)
    time.sleep(5)
    return


def find_upper_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(515,46+account*540,48,19))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def find_heart_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.83, grayscale=True, region=(352,46+account*540,39,18))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

def find_powder_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.85, region=(512,46+account*540,43,18))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    return

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
    find_heart_num('up_h1_1.png', account, list_num_1)
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


def Heart_sojin(account,WhatToDo):
    error_count = 0
    bNormalMode = True          # 일반모드 해야할 때 True
    bZoomOutComp = False        # 줌아웃 했늬
    bSpeedCheck = False         # 1.5배 속도 체크
    
    bStep1_play = False         # 플레이 버튼을 눌렀는가?
    bStep2_Adv = False          # 모험하기에서 월드 탐험을 클릭했는가?
    bStep3_Epi = False          # 에피소드(1~12)중 하나 들어와 있는 경우
    bStep4_Epi_Confirm = False  # 원하는 에피소드에 들어왔니?
    bStep5_Epi_Select = False   # 에피소드 선택 화면이니?
    bEntered = False            # 스테이지 골라서 전투 시작을 눌렀는가?
    bNormalSelected = False     # 에피소드 들어와서 일반모드 확인한 경우
    start_time = time.time()
    
    while True:
        if keyboard.is_pressed('end'):
            return False
        now_time = time.time()
        if now_time - start_time > 900:
            End_kkd(account)                            # 쿠킹덤 종료. 15분 안엔 끝나겠지.
            Kingdom_ready(account,'kkd_out',600)            # 재부팅
            return False
        screen = ImageGrab.grab()
        pix_status = screen.getpixel((605,55+account*540)) # 상단골드
        pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
        pix_status_in = (194, 144, 10)    # 생산건물 내
        pix_status_in_dark = (97, 71, 5)    #건물 안이긴 한데 창이 떠있음
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
        pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
        pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
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

        # cond_adv_dark_mode = pag.locateCenterOnScreen('cond_adv_dark_mode.png', confidence=0.9, region=(200,60+account*540,30,17))  # 어둠모드 입니까?
        # cond_adv_normal_mode = pag.locateCenterOnScreen('cond_adv_normal_mode.png', confidence=0.9, region=(60,50+account*540,35,20))   # 맵 선택에서 일반모드 입니까?
        cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12,38+account*540,37,36))  # Play버튼 누른 후 모험하기 창
        adv_normal = pag.locateCenterOnScreen('adv_normal.png', confidence=0.85, region = (200,60+account*540,32,18))       # 에피소드에서 좌상단 일반/어둠 선택 확인하기
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
        cond_end_fight1 = pag.locateCenterOnScreen('Cond_wanted_go_kingdom.png', confidence=0.95, region=(2,32+account*540,917,505))   # 왕국가기 버튼
        cond_end_fight2 = pag.locateCenterOnScreen('Cond_wanted_refignt.png', confidence=0.95, region=(2,32+account*540,917,505))   # 다시하기 버튼
        cond_end_fight3 = pag.locateCenterOnScreen('Cond_wanted_go_out.png', confidence=0.95, region=(2,32+account*540,917,505))   # 나가기 버튼
        
        if (pix_status2 == pix_status_fight_comp):    # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료1 조건!')
            pag.click((540,510+account*540))
            # bWanted_fight_ing = False
            bStep2_Adv = True
            bEntered = True
        
        if (pix_status != pix_status_out) and (pix_status2 == pix_status_fight_comp1):   # 전투 종료하면 클릭 후 조건 죽이고
            print('전투 종료2 조건!')
            pag.click((540,510+account*540))
            # bWanted_fight_ing = False
            bStep2_Adv = True
            bEntered = True
        
        # 좌하단 우하단 아이콘으로 현재 에피소드 중 하나에 들어와 있는지를 확인.. 스테이지 넘나들려면 리셋해야나
        if (adv_worldmap) and (adv_goto_wangkook):
            print('스테이지 들어와 있습니다!')
            bEntered = False            # 스테이지 골라서 전투 시작을 눌렀는가?
            bStep1_play = True          # 플레이 버튼을 눌렀는가?
            bStep2_Adv = True           # 모험하기에서 월드 탐험을 클릭했는가?
            bStep3_Epi = True           # 에피소드(1~12)중 하나 들어와 있는 경우
        else:
            bStep3_Epi = False          # 에피소드(1~12)중 하나 들어와 있는 경우
            
        # 모험하기 화면
        if not bEntered and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if not bEntered and ((pix_status == pix_status_out) or (cond_kkd_out)) and not bStep1_play:
            Kingdom_ready(account,'kkd_out')    # 창 떠있는 경우 삭제용
            print('Play 버튼 클릭~!')
            pag.click(random.randint(730,785),random.randint(470+account*540,525+account*540))
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
                pag.keyDown('Ctrlleft')
                time.sleep(0.1)
                pag.scroll(-40)
                time.sleep(1)
                pag.scroll(-40)
                time.sleep(1)
                pag.scroll(-40)
                time.sleep(0.1)
                pag.keyUp('Ctrlleft')
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
                bEntered = True
            
        if(cond_end_fight3):   # 나가기 버튼이 있는데
            if (cond_end_fight2):   # 다시하기 버튼이 있으면
                print('다시하기 버튼!')
                pag.click(cond_end_fight2,clicks=2,interval=0.5) # 눌러~
                time.sleep(1)
                # bWanted_fight_ing = True
            else:
                pag.click(cond_end_fight1,clicks=2,interval=0.5)  # 왕국가기버튼 클릭. 나가기 버튼과 항상 함께 있어서 오류날 일 없겠지
                time.sleep(15)
                if Kingdom_ready(account,'kkd_out'):    # 어후 왕국에 잘 들어왔어
                    print('월드탐험 잘 마치고 종료합니다!')
                    return True


def LeftRight(account,left_right):
    if left_right == 'left':
        pag.moveTo(300,295+account*540)
        pag.mouseDown()
        time.sleep(0.2)
        pag.moveTo(640,295+account*540,2)   # 153인데 10 더 여유줌
        time.sleep(0.2)
        pag.mouseUp()
        time.sleep(0.5)


# Heart_numb(0)
# Heart_numb(1)
# Heart_sojin(1,'8-29')

# account=1
# cond_bbopkki = pag.locateCenterOnScreen('cond_bbopkki.png', confidence=0.85, region=(535,460+account*540,30,30))
# if (cond_bbopkki):
#     pag.click(532,504+account*540)
#     time.sleep(1)
#     cond_bbopkki2 = pag.locateCenterOnScreen('cond_bbopkki2.png', confidence=0.85, region=(60,315+account*540,22,22))
#     if (cond_bbopkki2):
#         pag.click(46,357+account*540)
#         time.sleep(0.5)
#         cond_bbopkki3 = pag.locateCenterOnScreen('cond_bbopkki3.png', confidence=0.85, region=(743,458+account*540,152,53))
#         if (cond_bbopkki3):
#             print('굿')
# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     account=0
#     prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
#     prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45,60+account*540,55,22))
#     prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45,60+account*540,55,22))
#     prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45,60+account*540,55,22))
#     prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45,60+account*540,55,22))
#     if (prod_full_list3):
#         print('prod_full_list3', prod_full_list3)
#     if (prod_full_list4):
#         print('prod_full_list4', prod_full_list4)
#     if (prod_full_list5):
#         print('prod_full_list5', prod_full_list5)
#     if (prod_full_list6):
#         print('prod_full_list6', prod_full_list6)
#     if (prod_full_list7):
#         print('prod_full_list7', prod_full_list7)
#     print('-------------')
#     time.sleep(1)


# pag.screenshot('cond_kkd_train.png', region=(32, 44+account*540, 21, 29))

# pag.screenshot('heart_full_check.png', region=(380, 65+account*540, 51, 14))
# pag.click(357,55+account*540)
# time.sleep(1)
# diff_check = pag.locateCenterOnScreen('heart_full_check.png', confidence=0.95, grayscale=True, region=(380, 65+account*540, 51, 14))
# if (diff_check):
#     print('하트 수량 Full입니다!')
#     pag.click(396,386+account*540)
    
# else:
#     print('하트 수량 Full이 아닙니다.')
#     pag.click(396,386+account*540)

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
        pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
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
        Cond_tropical_knife_new = pag.locateCenterOnScreen('Cond_tropical_knife_new.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 재점령당한 칼모양
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
        
        if not bFighting and (Cond_tropical_knife_new) and not (Cond_tropical_fight):
            print('새로 연 곳 클릭!')
            pag.click(Cond_tropical_knife_new)
            time.sleep(2)
        
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
        
        # print('Cond_tropical_knife',Cond_tropical_knife)
        # pag.moveTo(Cond_tropical_knife)
        # print('Cond_tropical_fight',Cond_tropical_fight)
        # pag.moveTo(Cond_tropical_fight)
        # print('cond_quick',cond_quick)
        # pag.moveTo(cond_quick)
        # print('cond_quick_button',cond_quick_button)
        # pag.moveTo(cond_quick_button)
        # print('cond_end_fight3',cond_end_fight3)
        # pag.moveTo(cond_end_fight3)
        # print('cond_kkd_tro',cond_kkd_tro)
        # pag.moveTo(cond_kkd_tro)
        # print(bFighting)

        # print('계속 도나')

# Cond_tropical_knife = pag.locateCenterOnScreen('Cond_tropical_knife.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 재점령당한 칼모양
# Cond_tropical_fight = pag.locateCenterOnScreen('Cond_tropical_fight.png', confidence=0.8, region=(2,32+account*540,917,505))    # 트로피칼 전투 준비, 시작도 동일한가?
# cond_quick = pag.locateCenterOnScreen('cond_quick.png', confidence=0.8, region=(2,32+account*540,917,505))             # 빨리감기
# cond_quick_button = pag.locateCenterOnScreen('cond_quick_button.png', confidence=0.8, region=(2,32+account*540,917,505))             # 빨리감기 시작 버튼
# cond_end_fight3 = pag.locateCenterOnScreen('Cond_wanted_go_out.png', confidence=0.95, region=(2,32+account*540,917,505))        # 나가기 버튼
# print('Cond_tropical_knife',Cond_tropical_knife)
# pag.moveTo(Cond_tropical_knife)
# print('Cond_tropical_fight',Cond_tropical_fight)
# pag.moveTo(Cond_tropical_fight)
# print('cond_quick',cond_quick)
# pag.moveTo(cond_quick)
# print('cond_quick_button',cond_quick_button)
# pag.moveTo(cond_quick_button)
# print('cond_end_fight3',cond_end_fight3)
# pag.moveTo(cond_end_fight3)



def Tropical_Event(account):
    bStep1_play = False        # 플레이 버튼을 눌렀는가?
    error_count = 0
    start_time = time.time()
    while True:
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

        # 바탕화면도 모험하기도 아니면 우선 바탕화면으로
        if not (cond_kkd_out) and not (cond_adv_mode_select):
            print('왕국도 모험하기 화면도 아니네요!')
            Kingdom_ready(account,'kkd_out')
            
        # 모험하기 화면
        if not bStep1_play and (cond_adv_mode_select):
            bStep1_play = True         # 플레이 버튼만 눌렸지..

        # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
        if (pix_status == pix_status_out or (cond_kkd_out)) and not bStep1_play:
            print('Play 버튼 클릭~!')
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





# 조건 전체 모음?
# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     screen = ImageGrab.grab()
#     pix_status = screen.getpixel((605,55+account*540)) # 상단골드
#     pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
#     cond_kkd_train = pag.locateCenterOnScreen('cond_kkd_train.png', confidence=0.85, region=(30,42+account*540,25,33))  # 곰젤리열차
#     cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825,490+account*540,45,40))    # 쿠키왕국(우하단 플레이)
#     cond_kkd_tro = pag.locateCenterOnScreen('cond_kkd_tro.png', confidence=0.85, region=(825,490+account*540,45,40))    # 트로피칼(단, 좌하단 월드맵 아이콘 없는 경우 - 월드탐험 동일)
#     cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430,45+account*540,31,35))    # 소원나무
#     cond_kkd_sangjum = pag.locateCenterOnScreen('cond_kkd_sangjum.png', confidence=0.85, region=(14,40+account*540,46,29))   # 상점
#     cond_kkd_balloon = pag.locateCenterOnScreen('cond_kkd_balloon.png', confidence=0.85, region=(9,36+account*540,25,35))   # 열기구(대기)
#     cond_kkd_balloon_ing = pag.locateCenterOnScreen('cond_kkd_balloon_ing.png', confidence=0.85, region=(364,85+account*540,28,37))   # 열기구(대기)
#     cond_gold = pag.locateCenterOnScreen('cond_gold.png', confidence=0.8, region=(310,35+account*540,555,50))           # 골드 위치
#     cond_gnome = pag.locateCenterOnScreen('cond_gnome.png', confidence=0.8, region=(310,35+account*540,555,50))         # 노움 위치
#     cond_diamond = pag.locateCenterOnScreen('cond_diamond.png', confidence=0.8, region=(310,35+account*540,555,50))     # 다이아 위치
#     cond_meatjelly = pag.locateCenterOnScreen('cond_meatjelly.png', confidence=0.8, region=(310,35+account*540,555,50))   # 고기젤리 위치
#     adv_worldmap = pag.locateCenterOnScreen('adv_worldmap.png', confidence=0.85, region=(33,467+account*540,52,43))   # 좌하단 월드맵 아이콘(트로피칼과 차이점)
#     adv_worldmap = pag.locateCenterOnScreen('adv_worldmap.png', confidence=0.85, region=(33,467+account*540,52,43))   # 좌하단 월드맵 아이콘(트로피칼과 차이점)
#     in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8, region=(2,32+account*540,917,505))             # 건물 안
#     cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12,38+account*540,37,36))  # Play버튼 누른 후 모험하기 창
#     cond_kkd_arena = pag.locateCenterOnScreen('cond_kkd_arena.png', confidence=0.8, region=(2,32+account*540,917,505))      # 킹덤아레나
#     if (cond_gold):
#         print('cond_gold', cond_gold)
#     if (cond_gnome):
#         print('cond_gnome', cond_gnome)
#     if (cond_diamond):
#         print('cond_diamond', cond_diamond)
#     if (cond_meatjelly):
#         print('cond_meatjelly', cond_meatjelly)
#     if (cond_kkd_sangjum):
#         print('cond_kkd_sangjum',cond_kkd_sangjum)
#     print('account',account)
#     print('status = ', pix_status)
#     print('status2 = ',pix_status2)
#     while True:
#         if account == 0:
#             account=1
#             break
#         if account == 1:
#             account=0
#             break
#     time.sleep(1.5)

# pag.screenshot('cond_kkd_warehouse.png', region=(590, 492, 23, 23))
# adv_wanted_no = pag.locateCenterOnScreen('adv_wanted_no.png', confidence=0.85, region=(2,32+account*540,917,505))               # 현상수"배" 옆에 빨간 느낌표 없는 경우
# adv_wanted_yes = pag.locateCenterOnScreen('adv_wanted_yes.png', confidence=0.85, region=(2,32+account*540,917,505))             # 현상수"배" 옆에 빨간 느낌표 없는 경우
# Cond_go_Original = pag.locateCenterOnScreen('Cond_go_Original.png', confidence=0.85, region=(2,32+account*540,917,505))         # 창고 뜸
# cond_kkd_warehouse = pag.locateCenterOnScreen('cond_kkd_warehouse.png', confidence=0.85, region=(2,32+account*540,917,505))     # 창고 뜸

# account=1
# offset = 92-73+157*1      # baseline 첫 위치값 - 73 + 157 * 0~4(화면에 5개 아이템 정렬)
# pag.screenshot('trade_topping_choco.png', region=(112+offset,350+account*540,50,40))
# account=0
# trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2,325+account*540,750,26))
# trade_baseline_list = list(trade_baseline)
# list_output = list()
# if len(trade_baseline_list) != 0:
#     for p in trade_baseline_list:
#         ctr = pag.center(p)
#         list_output.append(ctr)
#         pag.moveTo(ctr)
#         time.sleep(1)
# print('list_output',list_output)

# 딴 이미지는 50x40
# trade_wood = pag.locateCenterOnScreen('trade_wood.png', confidence=0.95, region=(2,32+account*540,917,505))
# if (trade_wood):
#     print('trade_wood', trade_wood)


# pag.moveTo(860,1020)
# pag.mouseDown()
# time.sleep(0.5)
# pag.moveTo(860-785,1020,3)
# time.sleep(2)
# pag.mouseUp()


def Powder_numb(account):
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
    find_powder_num('up_h0.png', account, list_num_0)
    find_powder_num('up_h0_1.png', account, list_num_0)
    find_powder_num('up_h1.png', account, list_num_1)
    find_powder_num('up_h2.png', account, list_num_2)
    find_powder_num('up_h2_1.png', account, list_num_2)
    find_powder_num('up_h3.png', account, list_num_3)
    find_powder_num('up_h3_1.png', account, list_num_3)
    find_powder_num('up_h3_2.png', account, list_num_3)
    find_powder_num('up_h4.png', account, list_num_4)
    find_powder_num('up_h4_1.png', account, list_num_4)
    find_powder_num('up_h5.png', account, list_num_5)
    find_powder_num('up_h5_1.png', account, list_num_5)
    find_powder_num('up_h5_2.png', account, list_num_5)
    find_powder_num('up_h6.png', account, list_num_6)
    find_powder_num('up_h6_1.png', account, list_num_6)
    find_powder_num('up_h7.png', account, list_num_7)
    find_powder_num('up_h8.png', account, list_num_8)
    find_powder_num('up_h8_1.png', account, list_num_8)
    find_powder_num('up_h8_2.png', account, list_num_8)
    find_powder_num('up_h8_3.png', account, list_num_8)
    find_powder_num('up_h8_4.png', account, list_num_8)
    find_powder_num('up_h9.png', account, list_num_9)
    find_powder_num('up_h9_1.png', account, list_num_9)
    find_powder_num('up_h9_2.png', account, list_num_9)
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
    
    print('현재 상단 파우더 수량은 =', its_number)
    return its_number

# Powder_numb(0)
# up_h2 = pag.locateCenterOnScreen('up_h2.png',confidence=0.85, region=(2,32+account*540,917,505))
# if (up_h2):
#     print('up_h2',up_h2)
# pag.screenshot('fist.')


    


# bStage1 = False # 새로고침 후 첫화면. 기둥, 블록, 나침반, 트로피칼1,2
# bStage2 = False # 왼쪽으로 157*4 간 후. 트로피칼2, 스킬파우더 4개
# bStage3 = False # 이걸 음 어케 구분한다... 기본 생산품만 4종인가?
# Scroll_count = 0    # 스크롤 횟수로?

# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_tro_1 = pag.locateCenterOnScreen('trade_tro_1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_tro_2 = pag.locateCenterOnScreen('trade_tro_2.png', confidence=0.85, region=(2,350+account*540,917,40))

#     trade_10m = pag.locateCenterOnScreen('trade_10m.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_candy = pag.locateCenterOnScreen('trade_candy.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472,221+account*540,25,17))
#     if (trade_not_enough):
#         pag.click(random.randint(629,629+13),random.randint(153+account*540,153+account*540+13),2,0.3)
    
#     trade_assist_lv1 = pag.locateCenterOnScreen('trade_assist_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_assist_lv2 = pag.locateCenterOnScreen('trade_assist_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_assist_lv3 = pag.locateCenterOnScreen('trade_assist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     trade_bomb_lv1 = pag.locateCenterOnScreen('trade_bomb_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_bomb_lv2 = pag.locateCenterOnScreen('trade_bomb_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_bomb_lv3 = pag.locateCenterOnScreen('trade_bomb_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     # trade_fist_lv1 = pag.locateCenterOnScreen('trade_fist_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_fist_lv2 = pag.locateCenterOnScreen('trade_fist_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_fist_lv3 = pag.locateCenterOnScreen('trade_fist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     trade_recovery_lv1 = pag.locateCenterOnScreen('trade_recovery_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_recovery_lv2 = pag.locateCenterOnScreen('trade_recovery_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_recovery_lv3 = pag.locateCenterOnScreen('trade_recovery_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     # trade_shield_lv1 = pag.locateCenterOnScreen('trade_shield_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_shield_lv2 = pag.locateCenterOnScreen('trade_shield_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     # trade_shield_lv3 = pag.locateCenterOnScreen('trade_shield_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     # trade_shooting_lv1 = pag.locateCenterOnScreen('trade_shooting_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_shooting_lv2 = pag.locateCenterOnScreen('trade_shooting_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_shooting_lv3 = pag.locateCenterOnScreen('trade_shooting_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     # trade_staff_lv1 = pag.locateCenterOnScreen('trade_staff_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_staff_lv2 = pag.locateCenterOnScreen('trade_staff_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_staff_lv3 = pag.locateCenterOnScreen('trade_staff_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     trade_sword_lv1 = pag.locateCenterOnScreen('trade_sword_lv1.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_sword_lv2 = pag.locateCenterOnScreen('trade_sword_lv2.png', confidence=0.85, region=(2,350+account*540,917,40))
#     trade_sword_lv3 = pag.locateCenterOnScreen('trade_sword_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
    
#     print('Scroll_count', Scroll_count)
    
#     if Scroll_count == 0: # 새로고침 후 첫 동작(5개 항목)
#         kidung_numb = Angmu_Action('trade_kidung', trade_kidung)
#         block_numb = Angmu_Action('trade_block', trade_block)
#         nachimban_numb = Angmu_Action('trade_nachimban', trade_nachimban)
#         max_numb = max(kidung_numb, block_numb, nachimban_numb)
#         if kidung_numb > 0 and kidung_numb == max_numb:
#             pag.click(trade_kidung)
#             time.sleep(0.2)
#             pag.click(random.randint(420,500),random.randint(370,400))
#             time.sleep(1.5)
#         if block_numb > 0 and block_numb == max_numb:
#             pag.click(block_numb)
#             time.sleep(0.2)
#             pag.click(random.randint(420,500),random.randint(370,400))
#             time.sleep(1.5)
#         if nachimban_numb > 0 and nachimban_numb == max_numb:
#             pag.click(nachimban_numb)
#             time.sleep(0.2)
#             pag.click(random.randint(420,500),random.randint(370,400))
#             time.sleep(1.5)
#         # Angmu_Action('trade_tro_1', trade_tro_1)
#         # Angmu_Action('trade_tro_2', trade_tro_2)
    
#     if Scroll_count == 1:   # 1,2렙 스킬파우더

#         Angmu_Action('trade_assist_lv1', trade_assist_lv1)
#         Angmu_Action('trade_bomb_lv1', trade_bomb_lv1)
#         # Angmu_Action('trade_fist_lv1', trade_fist_lv1)
#         # Angmu_Action('trade_shield_lv1', trade_shield_lv1)
#         # Angmu_Action('trade_shooting_lv1', trade_shooting_lv1)
#         # Angmu_Action('trade_staff_lv1', trade_staff_lv1)
#         # Angmu_Action('trade_sword_lv1', trade_sword_lv1)
        
#         Angmu_Action('trade_assist_lv2', trade_assist_lv2)
#         Angmu_Action('trade_bomb_lv2', trade_bomb_lv2)
#         Angmu_Action('trade_fist_lv2', trade_fist_lv2)
#         Angmu_Action('trade_shield_lv2', trade_shield_lv2)
#         Angmu_Action('trade_shooting_lv2', trade_shooting_lv2)
#         Angmu_Action('trade_staff_lv2', trade_staff_lv2)
#         Angmu_Action('trade_sword_lv2', trade_sword_lv2)

#     # if (trade_nachimban):
#     #     print('trade_nachimban',trade_nachimban)
#     #     Angmu_check(trade_nachimban[0]-26,account)
#     # if (trade_10m):
#     #     print('trade_10m',trade_10m)
#     #     Angmu_check(trade_10m[0]-26,account)
#     # if (trade_tro_2):
#     #     print('trade_tro_2',trade_tro_2)
#     #     Angmu_check(trade_tro_2[0]-26,account)
#     # if (trade_candy):
#     #     print('trade_candy',trade_candy)
#     #     Angmu_check(trade_candy[0]-26,account)
#     # if (trade_shooting_lv3):
#     #     print('trade_shooting_lv3',trade_shooting_lv3)
#     #     Angmu_check(trade_shooting_lv3[0]-26,account)
    
#     # x좌표 끝점 : trade_slash - 5
#     # x좌표 시작점 : kidung - 26
#     pag.moveTo(random.randint(786,820),random.randint(480+account*540,490+account*540))
#     pag.mouseDown()
#     time.sleep(0.2)
#     pag.moveTo(random.randint(786,820)-157*4,random.randint(480+account*540,490+account*540),5)   # 153인데 20 더 여유줌
#     time.sleep(0.5)
#     pag.mouseUp()
#     time.sleep(0.2)
#     Scroll_count = Scroll_count + 1
#     # while True:
#     #     if keyboard.is_pressed('end'):
#     #         print('end 누름')
#     #         break
#     #     if account == 0:
#     #         account=1
#     #         break
#     #     if account == 1:
#     #         account=0
#     #         break
#     time.sleep(1.5)

# pag.moveTo(790,random.randint(480+account*540,490+account*540))
# pag.mouseDown()
# time.sleep(0.2)
# pag.moveTo(790-10,random.randint(480+account*540,490+account*540),5)   # 153인데 20 더 여유줌
# time.sleep(0.5)
# pag.mouseUp()
# time.sleep(0.2)
# account = 1
# pag.moveTo(790,random.randint(480+account*540,490+account*540))
# pag.mouseDown()
# time.sleep(0.2)
# pag.moveTo(790-10,random.randint(480+account*540,490+account*540),5)   # 153인데 20 더 여유줌
# time.sleep(0.5)
# pag.mouseUp()
# time.sleep(0.2)

def Enter_Screenshot_mode(account, left_where):
    error_count = 0
    reboot = 0
    drag_times = 0
    while True:
        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        screen = ImageGrab.grab()
        pix_status_scr = screen.getpixel((910,55+account*540)) # = 미세 오른쪽
        pix_clicked = (28, 39, 51)      # 클릭해서 어두워짐
        
        screen_mode_clicked = pag.locateCenterOnScreen('screen_mode_clicked.png', confidence=0.95, region=(876,42+account*540,27,26))
        screen_mode_not_clicked = pag.locateCenterOnScreen('screen_mode_not_clicked.png', confidence=0.95, region=(876,43+account*540,27,25))
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
                            pag.hotkey('ctrl','alt','up')
                            time.sleep(0.2)
                            pag.click(284,15)
                        if account == 1:
                            pag.moveTo(400,1078)
                            time.sleep(0.3)
                            pag.dragTo(400,1028,1)
                            time.sleep(0.3)
                            pag.hotkey('ctrl','alt','up')
                            time.sleep(0.2)
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
        pag.keyDown('Ctrlleft')
        time.sleep(0.1)
        pag.scroll(-40)
        time.sleep(1)
        pag.scroll(-40)
        time.sleep(1)
        pag.scroll(-40)
        time.sleep(0.1)
        pag.keyUp('Ctrlleft')
        time.sleep(1)
        break
    
    while (left_where == 'left_up') and (drag_times < 4):
        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        pag.moveTo(264,255+account*540)     # 왼쪽 아래로 드래그
        time.sleep(0.1)
        pag.drag(200, 300, 0.3)
        time.sleep(0.7)
        drag_times = drag_times + 1

    while (left_where == 'left_down') and (drag_times < 4):
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
        # ++ 길드보상, 상점보상..
        
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
                pag.click(cond_guild)
                time.sleep(5)
            else:
                print('길드 보상 수령 완료!')
                return
            cond_guild_in = pag.locateCenterOnScreen('cond_guild_in.png', confidence=0.9, region=(626,477+account*540,19,19))
            if (cond_guild_in):
                time.sleep(2)
                print('cond_guild_in',cond_guild_in)
                pag.click(450,380+account*540)
                time.sleep(1)
                pag.click(450,380+account*540)
                time.sleep(2)
                pag.click(865,500+account*540)
                time.sleep(5)
                Kingdom_ready(account,'kkd_out')
                return
        elif whereto == 'shop':
            cond_shop = pag.locateCenterOnScreen('cond_shop.png', confidence=0.9, region=(45,111+account*540,23,21))
            if (cond_shop):
                pag.click(cond_shop)
                time.sleep(2)
                if Kingdom_ready(account,'sangjum_in'):
                    bShop = True
                    break
                else:
                    print('상점 진입 실패!')
                    return False
            else:
                print('[상점] 이벤트 없음')
                Kingdom_ready(account, 'kkd_out')
                return False
        
        else:
            # 왕국활동 창이 켜져 있으면
            if (act_popup_mark_x):
                if whereto == 'trade':
                    # 이미지 확인(무역센터 느낌표)
                    activity_trade1 = pag.locateCenterOnScreen('activity_trade1.png', confidence=0.95, region=(115,95+account*540,80,80))
                    if (activity_trade1):
                        print('[왕국활동] 무역센터 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 무역센터로 들어갑니다.')
                        pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540)
                        time.sleep(2)
                        bTradeEvent = True
                        break
                if whereto == 'research':
                    # 이미지 확인(연구소 느낌표)
                    if Kingdom_ready(account,'research_in'):
                        bResearchEvent = True
                        break
                    else:
                        activity_research = pag.locateCenterOnScreen('activity_research.png', confidence=0.95, region=(115,95+76*1+account*540,80,80))
                        if (activity_research):
                            print('[왕국활동] 연구소 이벤트가 없습니다.')
                            return False
                        else:
                            print('[왕국활동] 연구소 들어갑니다.')
                            pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76)
                            time.sleep(2)
                            bResearchEvent = True
                            break
                        
                if whereto == 'balloon':
                    # 이미지 확인(열기구 느낌표)
                    activity_balloon = pag.locateCenterOnScreen('activity_balloon.png', confidence=0.95, region=(115,95+76*2+account*540,80,80))
                    if (activity_balloon):
                        print('[왕국활동] 열기구 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 열기구 들어갑니다.')
                        pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*2)
                        time.sleep(2)
                        bBalloonEvent = True
                        break
                if whereto == 'train':
                    # 이미지 확인(열차 느낌표)
                    activity_train = pag.locateCenterOnScreen('activity_train.png', confidence=0.95, region=(115,95+76*3+account*540,80,80))
                    if (activity_train):
                        print('[왕국활동] 곰젤리 열차 이벤트가 없습니다.')
                        return False
                    else:
                        print('[왕국활동] 곰젤리 열차 들어갑니다.')
                        pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*3)
                        time.sleep(2)
                        bTrainEvent = True
                        break
                if whereto == 'sowon':
                    print('[왕국활동] 소원나무는 그냥 들어가 드립니다.')
                    pag.click(random.randint(155-10,155+10),random.randint(135-10,135+10)+account*540+76*4)
                    time.sleep(2)
                    bTradeEvent = True
                
                    
            else:
                if whereto == 'trade' and Kingdom_ready(account,'trade_in'):
                    bTradeEvent = True
                    break
                elif whereto == 'research' and Kingdom_ready(account,'research_in'):
                    bResearchEvent = True
                    break
                elif whereto == 'balloon' and Kingdom_ready(account,'balloon_in'):
                    bBalloonEvent = True
                    break
                elif whereto == 'train' and Kingdom_ready(account,'train_in'):
                    bTrainEvent = True
                    break
                else:
                    Kingdom_ready(account,'kkd_out')

                # 왕국활동 창 꺼져있는 상태에선
                act_check_mark = pag.locateCenterOnScreen('act_check_mark.png', confidence=0.9, region=(174,458+account*540,13,11))         # 체크 마크
                act_nukimpyo_mark = pag.locateCenterOnScreen('act_nukimpyo_mark.png', confidence=0.9, region=(174,458+account*540,13,11))   # 느낌표 마크
            
                if (act_check_mark) or (act_nukimpyo_mark): # 뭐라도 있으면
                    pag.click(155,490+account*540)          # 클릭해!
                    time.sleep(1)
                else:
                    print('[왕국활동]아무 이벤트도 없습니다.')
                    return False

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
            if not (cond_shop_jaehwa):
                pag.click(35,55+account*540)
                time.sleep(1)
                pag.moveTo(25,505+account*540)
                pag.dragTo(25,100+account*540,1)
                time.sleep(1)
            else:
                print('상점보상 끝!')
                pag.click(random.randint(880,880+24), random.randint(44,44+22)+account*540)
                time.sleep(2)
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
        cond_trade_perl = pag.locateCenterOnScreen('cond_trade_perl.png', confidence=0.85, region=(460,30+account*540,78,47))               # 해상무역센터 위치 확인
        cond_trade_angmu = pag.locateCenterOnScreen('cond_trade_angmu.png', confidence=0.85, region=(150,320+account*540,18,29))            # 해상무역센터 앵무 교역소 이벤트
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
                if error_count > 10:
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
        if (cond_kkd_train):
            return True
        time.sleep(1)

def Angmu_Action(prd_name, ctr, account):
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
                time.sleep(0.2)
                pag.click(random.randint(420,500),random.randint(370,400)+account*540)
                time.sleep(2)
            if block_numb > 0 and block_numb == max_numb:
                pag.click(trade_block)
                time.sleep(0.2)
                pag.click(random.randint(420,500),random.randint(370,400)+account*540)
                time.sleep(2)
            if nachimban_numb > 0 and nachimban_numb == max_numb:
                pag.click(trade_nachimban)
                time.sleep(0.2)
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
        time.sleep(0.2)
        pag.moveTo(random.randint(786,820)-157*4,random.randint(480+account*540,490+account*540),5)   # 153인데 20 더 여유줌
        time.sleep(0.5)
        pag.mouseUp()
        time.sleep(0.2)
        
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
                    time.sleep(0.2)
                    pag.moveTo(790+50,random.randint(480+account*540,490+account*540),2)   # 한 번 움직여보고
                    time.sleep(0.5)
                    trade_baseline_gray_new = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.95, region=(2,32+account*540,917,505))
                    if (trade_baseline_gray_new):
                        pag.moveTo(790+50-trade_baseline_gray_new[0]+73,random.randint(480+account*540,490+account*540),3)   # 153인데 20 더 여유줌
                    time.sleep(0.5)
                    pag.mouseUp()
                    time.sleep(0.2)
            
            trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.9, region=(2,32+account*540,917,505))
            if (trade_baseline):
                if (92 >= trade_baseline[0] > 70) or (92+157 >= trade_baseline[0] > 70+157):
                    print('오우예')
                    Scroll_count = Scroll_count + 1
                    break
                else:
                    pag.moveTo(790,random.randint(480+account*540,490+account*540))
                    pag.mouseDown()
                    time.sleep(0.2)
                    pag.moveTo(790+50,random.randint(480+account*540,490+account*540),2)   # 한 번 움직여보고
                    time.sleep(0.5)
                    trade_baseline_new = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.95, region=(2,32+account*540,917,505))
                    if (trade_baseline_new):
                        pag.moveTo(790+50-trade_baseline_new[0]+73,random.randint(480+account*540,490+account*540),3)   # 153인데 20 더 여유줌
                    time.sleep(0.5)
                    pag.mouseUp()
                    time.sleep(0.2)
    return print('Angmu_Aft_Refresh 완료!')
    


cond_check = False
while cond_check:
    if keyboard.is_pressed('end'):
        print('end 누름')
        break
    screen = ImageGrab.grab()
    pix_prod = screen.getpixel((610,140+account*540))   # 생산품 이미지 확인
    pix_status = screen.getpixel((605,55+account*540)) # 상단골드
    pix_status2 = screen.getpixel((540,510+account*540)) # 마침표
    cond_wanted_enter = pag.locateAllOnScreen('Cond_wanted_select1.png', confidence=0.9, region=(2,32+account*540,917,505))   # 입장 버튼.. 나중에 요일별로?
    cond_wanted_enter = list(cond_wanted_enter)
    if len(cond_wanted_enter) > 0: # 입장. 보이면 걍 클릭
        print('cond_wanted_enter',cond_wanted_enter)
    
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
    pix_status_in_dark = (97, 72, 5)    #건물 안이긴 한데 창이 떠있음
    pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
    pix_status_out_window = (0, 64, 90)   # 창이 떠서 어두워짐
    pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진.. status
    pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
    pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중 - status
    pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비 - status
    pix_status_bal_arrive = (170, 169, 168) # 열기구 탐사 완료 - status2
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
    pix_status_fountain = (84, 93, 134) # 분수.. status
    pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
    pix_status_trade = (255, 216, 2)    # 해상무역센터 로비 status
    pix_status_wanted = (29, 10, 12)    # 오늘의 현상수배 선택하는 곳
    pix_status_fight_comp = (168, 167, 167) # 모험 전투 후
    pix_status_fight_comp1 = (121, 98, 74)   # 모험 전투 후1

    
    print('pix_prod',pix_prod)
    print('pix_status',pix_status)
    print('pix_status2',pix_status2)
    time.sleep(1)

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


def Sowon_Prod_Check(pix_status):
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
        if Sowon_numb(account) > jelly_lev3*easy_prod:
            return True
        else:
            return False

    # elif pix_status == pix_jelly_lv4:
    #     print('석류 잼',jelly_lev4)
    #     if Sowon_numb(account) > jelly_lev4*normal_prod:
    #         return True
    #     else:
    #         return False

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
        if Sowon_numb(account) > rollc_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_rollc_lv3:
        print('뻐꾹뻐꾹 시계',rollc_lev3)
        if Sowon_numb(account) > rollc_lev3*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_rollc_lv4:
        print('백조깃털 드림캐쳐',rollc_lev4)
        if Sowon_numb(account) > rollc_lev4*hard_prod:
            return True
        else:
            return False

    
    elif pix_status == pix_bread_lv1:
        print('든든한 호밀빵',bread_lev1)
        if Sowon_numb(account) > bread_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_bread_lv2:
        print('달콤쫀득 잼파이',bread_lev2)
        if Sowon_numb(account) > bread_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_bread_lv3:
        print('은행 포카치아',bread_lev3)
        if Sowon_numb(account) > bread_lev3*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_bread_lv4:
        print('슈가코팅 도넛',bread_lev4)
        if Sowon_numb(account) > bread_lev4*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_bread_lv5:
        print('폭신 카스테라',bread_lev5)
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
        if Sowon_numb(account) > jampy_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_jampy_lv2:
        print('곰젤리 버거',jampy_lev2)
        if Sowon_numb(account) > jampy_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_jampy_lv3:
        print('캔디크림 파스타',jampy_lev3)
        if Sowon_numb(account) > jampy_lev3*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_jampy_lv4:
        print('폭신폭신 오므라이스',jampy_lev4)
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
        if Sowon_numb(account) > doye_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_doye_lv2:
        print('반짝반짝 유리판',doye_lev2)
        if Sowon_numb(account) > doye_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_doye_lv3:
        print('반짝이는 색동구슬',doye_lev3)
        if Sowon_numb(account) > doye_lev3*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_doye_lv4:
        print('무지갯빛 디저트 보울',doye_lev4)
        if Sowon_numb(account) > doye_lev4*hard_prod:
            return True
        else:
            return False

    
    elif pix_status == pix_flower_lv1:
        print('캔디꽃',flower_lev1)
        if Sowon_numb(account) > flower_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_flower_lv2:
        print('행복한 꽃화분',flower_lev2)
        if Sowon_numb(account) > flower_lev2*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_flower_lv3:
        print('캔디꽃다발',flower_lev3)
        if Sowon_numb(account) > flower_lev3*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_flower_lv4:
        print('롤리팝 꽃바구니',flower_lev4)
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
        if Sowon_numb(account) > latte_lev1*easy_prod:
            return True
        else:
            return False

    elif pix_status == pix_latte_lv2:
        print('몽글몽글 버블티',latte_lev2)
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
        if Sowon_numb(account) > dolls_lev1*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_dolls_lv2:
        print('곰젤리 솜인형',dolls_lev2)
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

    
    elif pix_status == pix_muffin_lv1:
        print('으스스 머핀',muffin_lev1)
        if Sowon_numb(account) > muffin_lev1*normal_prod:
            return True
        else:
            return False

    elif pix_status == pix_muffin_lv2:
        print('생딸기 케이크',muffin_lev2)
        return False
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


sowon_numcheck = False
while sowon_numcheck:
    if keyboard.is_pressed('end'):
        print('end 누름')
        break
    account = 1
    sowon_num_start_pos = pag.locateCenterOnScreen('sowon_num_start_pos.png', confidence=0.85, region = (430, 188+account*540, 24+11*2, 14+2))
    if (sowon_num_start_pos):
        print('sowon_num_start_pos',sowon_num_start_pos)
    sowon_num_slash_1 = pag.locateCenterOnScreen('sowon_num_slash_1.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
    if (sowon_num_slash_1):
        print('sowon_num_slash_1',sowon_num_slash_1)
    sowon_num_slash_2 = pag.locateCenterOnScreen('sowon_num_slash_2.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
    if (sowon_num_slash_2):
        print('sowon_num_slash_2',sowon_num_slash_2)
    time.sleep(1)
    
# Sowon_numb(1)
# account=1
# sowon_num_start_pos = pag.locateCenterOnScreen('sowon_num_start_pos.png', confidence=0.8, region = (2, 32 + account * 540, 917, 505))
# if (sowon_num_start_pos):
#     print('sowon_num_start_pos',sowon_num_start_pos)
#     pag.moveTo(sowon_num_start_pos)

def jjokji_check(pos,account):
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
        if Sowon_Prod_Check(pix_status):
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
            if Sowon_Prod_Check(pix_status):
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
            print('좌하 없고')
        else:
            if Sowon_Prod_Check(pix_status):
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
            print('좌하 없고')
        else:
            if Sowon_Prod_Check(pix_status):
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
            else:
                jokji1_ok = False
                pag.click(random.randint(680,680+14),random.randint(76,76+14)+account*540)
                time.sleep(0.5)
    
    if jokji1_ok:
        pag.click(random.randint(232,232+60)+(pos-1)*165,random.randint(427,427+20)+account*540)
        print('쪽지 보냅니다!')
        return True
    
    if not jokji1_ok:
        pag.click(random.randint(230,230+65)+(pos-1)*165,random.randint(140,140+10)+account*540)
        print('쪽지 짤라!!')
        return False

# 소원나무 내부 픽셀, 이미지 조건 확인
def Sowon_jjokji_action(jjokji_numb, account, jjokji_limit):
    how_many_jjokji = jjokji_numb
    jjokji_sended = 0
    bEvent_checked = False
    sowon_jjokji_start = time.time()
    # 소원나무 들어가기
    while True:
        sowon_jjokji_now = time.time()
        if sowon_jjokji_now - sowon_jjokji_start > 30:
            End_kkd(account)
            Check_Initiating(account)
            time.sleep(10)
            Kingdom_ready(account,'kkd_out')
            sowon_jjokji_start = time.time()
            
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

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
            
            
        else:
            cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430,45+account*540,31,35))    # 소원나무
            if (cond_kkd_sowon):
                print('소원나무 들어왔슴돠!')
                break
            else:
                print('왕국활동 눌러!')
                pag.click(random.randint(142,142+26),random.randint(489,489+26)+account*540)
    
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
            Check_Initiating(account)
            time.sleep(10)
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
            time.sleep(3)
            pag.click(85,385+account*540)
        else:
            print('뭐지!!!!!!!!!!!!!')
        
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

    

def Three_numb(lv,account):
    # lv는 1, 2, 3으로
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
    find_num('prod_0.png', 151+(lv-1)*153+account*540, list_num_0)
    find_num('prod_1.png', 151+(lv-1)*153+account*540, list_num_1)
    find_num('prod_1_1.png', 151+(lv-1)*153+account*540, list_num_1)
    find_num('prod_2.png', 151+(lv-1)*153+account*540, list_num_2)
    find_num('prod_3.png', 151+(lv-1)*153+account*540, list_num_3)
    find_num('prod_3_1.png', 151+(lv-1)*153+account*540, list_num_3)
    find_num('prod_4.png', 151+(lv-1)*153+account*540, list_num_4)
    find_num('prod_4_1.png', 151+(lv-1)*153+account*540, list_num_4)
    find_num('prod_4_2.png', 151+(lv-1)*153+account*540, list_num_4)
    find_num('prod_5.png', 151+(lv-1)*153+account*540, list_num_5)
    find_num('prod_6.png', 151+(lv-1)*153+account*540, list_num_6)
    find_num('prod_7.png', 151+(lv-1)*153+account*540, list_num_7)
    find_num('prod_8.png', 151+(lv-1)*153+account*540, list_num_8)
    find_num('prod_8_1.png', 151+(lv-1)*153+account*540, list_num_8)
    find_num('prod_9.png', 151+(lv-1)*153+account*540, list_num_9)
    find_num('prod_9_1.png', 151+(lv-1)*153+account*540, list_num_9)
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

# latte, dolls, beer, muffin, jewel 이거.. 3개 값 비교해서 젤 적은 제품 클릭
def Latte_action(account):
    print('[latte] Prod_action함수!', account)
    start_time = time.time()
    error_count = 0
    
    # if latte_lev1 > 0:
    #     Three_numb(1,account)
        
    #     if 
    
    while True:
        now_time = time.time()
        # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
        pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
        time.sleep(0.5)
        # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
        prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45,60+account*540,55,22))
        # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        if (prod_full_list3):
            print('리스트 full!')
            return True
        if now_time - start_time > 30:
            print('동작 최대시간 초과 입니다.')
            return False
        if keyboard.is_pressed('end'):
            return False
        # ctr = pag.locateCenterOnScreen(image, confidence=0.85, region=(560,75+account*540,105,460))
        prd_done = pag.locateCenterOnScreen('prod_done.png', confidence=0.85, region=(2,32+account*540,917,505))
        # prd_done1 = pag.locateCenterOnScreen('prod_done1.png', confidence=0.9, region=(2,32+account*540,917,505))
        # prd_done2 = pag.locateCenterOnScreen('prod_done2.png', confidence=0.9, region=(2,32+account*540,917,505))
        list_full = pag.locateCenterOnScreen('Cond_makinglist_full.png', confidence=0.97, region=(2,32+account*540,917,505))
        list_full1 = pag.locateCenterOnScreen('Cond_makinglist_full1.png', confidence=0.97, region=(2,32+account*540,917,505))
        lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
        not_opened = pag.locateCenterOnScreen('Cond_not_opened.png',confidence=0.95, region=(2,32+account*540,917,505))
        # ctr_list = pag.locateCenterOnScreen(list_image, confidence=0.9, region=(40,168+account*540,71,321))
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2,32+account*540,917,505))

        if (play_halted):
            pag.click(play_halted)

    
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
    return a, b, c

# account=0
# x=460
# y=90
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((x,y+account*540)) # 소원나무 확인 뽀인트
# print('pix_status',pix_status)
# pag.moveTo(x,y+account*540)
# account=0
# def sowon_jjokji_check(file,account):
#     image = pag.locateCenterOnScreen(file, confidence=0.85, region=(2,32+account*540,917,505))
#     if (image):
#         print(file,image)
#         pag.moveTo(image)
# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
    
#     sowon_jjokji_check('act_sowon_wood.png',0)
#     time.sleep(1)

# sowon_jjokji_check('act_sowon_doye_lv1.png',0)
# account=0
# pag.screenshot('bSowon_beer_lev3.png', region=(460-25, 90-25+account*540, 50, 50))

# Sowon_jjokji_action(5,1)
# account=1
# sowon_num_start_pos = pag.locateCenterOnScreen('sowon_num_start_pos.png', confidence=0.8, region = (439-12-11, 188+account*540, 24+11*2+5+3, 14+2))
# if (sowon_num_start_pos):
#     print('sowon_num_start_pos',sowon_num_start_pos)
#     x1 = sowon_num_start_pos[0] + 11
# else:
#     print('량 : 을 못찾아 437+11로 고정합니다.')
#     x1 = 437+11
# sowon_num_slash_1 = pag.locateCenterOnScreen('sowon_num_slash_1.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
# if (sowon_num_slash_1):
#     print('sowon_num_slash_1',sowon_num_slash_1)
#     x2 = sowon_num_slash_1[0]
#     slash_found = True
# sowon_num_slash_2 = pag.locateCenterOnScreen('sowon_num_slash_2.png', confidence=0.85, region = (480, 185+account*540, 30, 20))
# if not slash_found and (sowon_num_slash_2):
#     print('sowon_num_slash_2',sowon_num_slash_2)
#     x2 = sowon_num_slash_2[0]
#     slash_found = True

# if Angmu_Enter(0):
# Angmu_Aft_Refresh(0)
# if Angmu_Enter(1):
#     Angmu_Aft_Refresh(1)
# print('계정',account)
# trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2,350+account*540,917,45))
# trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2,350+account*540,917,45))
# trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2,350+account*540,917,45))
# if (trade_kidung):
#     print('trade_kidung',trade_kidung)
# if (trade_block):
#     print('trade_block',trade_block)
# if (trade_nachimban):
#     print('trade_nachimban',trade_nachimban)

# screen = ImageGrab.grab()
# pix_status = screen.getpixel((628,716+account*540)) # 상단골드
# pix_status2 = screen.getpixel((628,510+account*540)) # 마침표
# account=0
# prod_pin = pag.locateAllOnScreen('prod_pin.png', confidence=0.95, region=(602,32+account*540,20,508))
# prod_pin = list(prod_pin)
# if len(prod_pin)>0:
#     for p in prod_pin:
#         ctr = pag.center(p)
#         print('prod_pin',ctr)
# prod_pin = pag.locateAllOnScreen('prod_pin.png', confidence=0.95, region=(602,84+account*540,20,22))
# if (prod_pin):
#     screen = ImageGrab.grab()
#     pix_status = screen.getpixel((628,716+account*540)) # 상단골드
#     pix_status2 = screen.getpixel((628,510+account*540)) # 마침표
# account=1
# prod_pin = pag.locateCenterOnScreen('prod_pin.png', confidence=0.95, region=(602,84+account*540, 20, 68))
# if (prod_pin):
#     print('prod_pin',prod_pin)
# prod_pin = (612, 95)
def numb_new_recog(prod_pin, line):
    its_number = 0
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
        
    if pos_numb == 2:
        # print('두 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),10,14)
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
        # print('세 자릿 수 범위 확인',prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14)
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(622,prod_pin[1]+85-7+153*(line-1),12,14))
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

# start_time=time.time()
# account=1
# prod_pin = (612, 95+account*540)
# print(numb_new_recog(prod_pin, 1))
# print(numb_new_recog(prod_pin, 2))
# print(numb_new_recog(prod_pin, 3))
# end_time=time.time()
# print(end_time-start_time)
# 이걸로 0.7~3.65초?
# line = 1
# num_list = list()
# list_output = list()
# pos_numb = 2
# num_2 = pag.locateAllOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
# num_2 = list(set(num_2))
# print(num_2)
# if len(num_2) != 0:
#     for p in num_2:
#         print('p',p)
#         ctr = pag.center(p)
#         print('ctr',ctr)
#         list_output.append((ctr[0],2))
# print('리스트아웃풋',list_output)

# num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0]+24-pos_numb*5,prod_pin[1]+85-7+153*(line-1),pos_numb*5*2,14))
# if (num_2):
#     print(num_2)
#     pag.moveTo(num_2)
# start_time=time.time()
# print(prod_check('doye_lev1.png',0))
# print(prod_check('doye_lev2.png',0))
# print(prod_check('doye_lev3.png',0))
# end_time=time.time()
# print(end_time-start_time)
# 3.6~7초........
# account = 0


# Angmu_Enter(1,'research')
# account=1
# activity_trade1 = pag.locateCenterOnScreen('activity_trade1.png', confidence=0.95, region=(115,95+account*540,80,80))
# if (activity_trade1):
#     pag.moveTo(activity_trade1)

# ++ urgent 생산
# 선행조건 : 기본적으로 모든 생산품 시간 파악(연구소 텍스트/엑셀파일 import/export?) - 연구소 파악?
# 두 건물은 동일한 제품 찍기. 각 동작 후 카운트 돌리고 완료 예상시간은 건물 내 3/3~7/7 이미지 파악으로 결정
# 픽셀값 건물선택으로 해당 건물에만 생산 돌리기. 나-젤-각-(비/젤/우/솜)-대장-잼-롤케 이렇게 총 6건물.
# 건물 들어가 클릭 완료 시 각 시간 카운트. 나무 건물에서 나갔다가 각 동작 완료 10초 전 다시 나무 건물로 들어옴(랜드마크 등 변수있음)
# 다음 동작 완료 시간까지 10초 미만으로 남았으면 좌/우 움직여 클릭.
# 목표치 도달하면 나~각은 2렙 찍고 대장~롤케는 다음 생산품 파악해 클릭
# 중단시점 : 여섯 건물 끝나면 / 정해진 시간 지나면?(기차/열기구?)
# 중단방법 : 건물 나가 체크마크 확인 후 왕국 활동
# 쿠하/열차/열기구/분수 동작 시간도 체크해야....
# urgent 아니어도 위와 같이 해놓으면 생산 동작 시간을 생산 완료 건물/아닌 건물로 파악 가능..
# 생산 완료 건물 생산품 1~3렙(고렙은 1렙)은 소원나무 프리패스
# urgent 생산 중단 시점 : 6건물 

# ++ 연구소
# 각 생산품 레벨확인? 연구 목표는 어떻게?(왕국/쿠키)
# 튜플? 짜서 x, y 좌표로? 각 레벨까지 하면 예를 들어 (1,1,1)
# 왕국연구 x = 26, y = 4
# 쿠키연구 x = 28, y = 4
# 목표 : 쿠키 (28, 2, 10) 이런식으로. 연구 완료 뜨면 들어감.
# 연구중 아님 - 쿠키 연구 클릭 - 현재 x좌표 찾기(무조건 2~3개는 떠있으니 3의 배수로 이미지 찾기?)
# - 좌/우로 드래그 - 목표 28 찾으면 2번 위치 확인(결과값은 (28, 2, 7) 이런식으로?) - 클릭클릭
# 재료/노움이 없는 경우를 대비해 1순위, 2순위, 3순위 이런식으로 다음 할 것 정하기
# 다음 연구 완료 시 1순위부터 다시 연구 가능여부 판단
# 왕국 연구의 경우 순서대로 지나가면서 레벨 확인
# 좌표 확인은 연구 중 맨 윗줄 아이콘 가려질 수 있으니 글씨 이미지로
# 완료는 핀 모양+색깔로 확인. 완료 아닌 경우....... 개별 이미지를 다 따야나

# 생산 모드 - 싱크로(2개 건물은 동일 제품 생산), urgent, 역순생산(고렙 우선)


account=1
clock_tower_A = 10
material1_A = 5
wood_t_A = 2
jelbean_t_A = 2
rollc_t_A = 9
smith_t_A = 10
jelly_t_A = 4
bread_t_A = 10
sugar_t_A = 6
biscuit_t_A = 3
berry_t_A = 3
flower_t_A = 10
jampy_t_A = 10
doye_t_A = 10
product1_A = 5
milky_t_A = 2
latte_t_A = 2
milk_t_A = 10
material2_A = 5
product2_A = 5
doll_t_A = 3
cotton_t_A = 10
beer_t_A = 10
muffin_t_A = 10
jewel_t_A = 0

clock_tower_B = 10
material1_B = 5
wood_t_B = 4
jelbean_t_B = 4
rollc_t_B = 10
smith_t_B = 10
jelly_t_B = 10
bread_t_B = 10
sugar_t_B = 5
biscuit_t_B = 6
berry_t_B = 5
flower_t_B = 10
jampy_t_B = 10
doye_t_B = 10
product1_B = 5
milky_t_B = 2
latte_t_B = 3
milk_t_B = 10
material2_B = 5
product2_B = 5
doll_t_B = 3
cotton_t_B = 10
beer_t_B = 3
muffin_t_B = 2
jewel_t_B = 0

wood_actual_t = 30
wood_real_t = 30


account=0
# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
    # time.sleep(1)

cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
if (cond_network):
    pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
    time.sleep(0.3)

# urgent 생산 우선 만들어 볼까..
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

# 건물에 들어가기
def Enter_Building(account):
    error_position = 0
    while True:
        if keyboard.is_pressed('end'):
            print('end버튼 눌러 종료됨')
            return False
        bWod_r = False
        bWod_l = False
        pix_status_in = (194, 144, 10)    # 생산건물 내
        pix_status_out = (0, 181, 255)    # 바탕화면(왕국), 트로피컬도 동일
        print('건물 들어가기 전 왕국 위치 확인')
        if not Kingdom_ready(account, 'prod_in'):
            Check_Initiating(account)
        else:
            print('이미 건물 안이네요!')
            return True

        while True:
            if keyboard.is_pressed('end'):
                return False
            wod_r = pag.locateCenterOnScreen('wood_sign_r.png', confidence=0.85, region=(271,79+account*540,545,377))
            wod_l = pag.locateCenterOnScreen('wood_sign_l.png', confidence=0.85, region=(271,79+account*540,545,377))
            print(wod_r)
            print(wod_l)
            if (not (wod_r) and not (wod_l)):    # 왕국, 간판 없음
                print('간판이 없으니 스샷모드로 찾아볼까요')
                Enter_Screenshot_mode(account, 'left_down')
                # 중간에 풀렸다면?... 아몰랑

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
                wod_r = pag.locateCenterOnScreen('wood_sign_r.png', confidence=0.85, region=(271,79+account*540,545,377))
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
                wod_l = pag.locateCenterOnScreen('wood_sign_l.png', confidence=0.85, region=(271,79+account*540,545,377))
                if (wod_l):
                    pag.click(wod_l.x+10, wod_l.y-10)
                    time.sleep(2)
                    if Kingdom_ready(account, 'prod_in'):
                        print('우간판으로 건물 진입!')
                        return
                else:
                    print('어... 뭐야 왜 간판 사라짐...')
                    Kingdom_ready(account, 'kkd_out')


def Wood_to_Cotton(account, Min_number, Max_number, Making_Level):   # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
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
        print('리스트 full!')
        Skip_Next(account)
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
        Skip_Next(account)
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
                    time.sleep(0.2)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    break
                else:
                    print('1분 넘게 남아 삭제함돠')
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                    time.sleep(0.2)
                    pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
            else:
                break
        pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+account*540)
        pag.mouseDown()
        time.sleep(0.7)
        pag.mouseUp()
        time.sleep(0.3)
        Skip_Next(account)
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
        print('리스트 full!')
        if prod_direction_left:
            Skip_Next(account)
        else:
            Skip_Right(account)
        return True
    else:
        up_1 = pag.locateCenterOnScreen('up_1.png',confidence=0.8,region=(500,47+account*540,14,15))
        if (up_1):
            print('1천대!')
            its_number = 1000
        else:
            up_2 = pag.locateCenterOnScreen('up_2.png',confidence=0.8,region=(500,47+account*540,14,15))
            if (up_2):
                print('2천대!')
                its_number = 2000
            else:
                up_3 = pag.locateCenterOnScreen('up_3.png',confidence=0.8,region=(500,47+account*540,14,15))
                if (up_3):
                    print('3천대!')
                    its_number = 3000
                else:
                    up_4 = pag.locateCenterOnScreen('up_4.png',confidence=0.8,region=(500,47+account*540,14,15))
                    if (up_4):
                        print('4천대!')
                        its_number = 4000
                    else:
                        up_5 = pag.locateCenterOnScreen('up_5.png',confidence=0.8,region=(500,47+account*540,14,15))
                        if (up_5):
                            print('5천대!')
                            its_number = 5000
                        else:
                            up_6 = pag.locateCenterOnScreen('up_6.png',confidence=0.8,region=(500,47+account*540,14,15))
                            if (up_6):
                                print('6천대!')
                                its_number = 6000
                            else:
                                print('1000 미만...')
                                its_number = 999

        # 설정 수량보다 많아지면 걍 넘어가고
        if its_number >= Max_number:
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
            return False
        # 설정 수량보다 적으면 생산 렙으로 생산
        else:
            wood_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
            jelbean_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
            sugar_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
            if (wood_list_lv2):
                wood_clear = True
            if(jelbean_list_lv2):
                jelbean_clear = True
            if (sugar_list_lv2):
                sugar_clear = True
            while True:
                if wood_clear:
                    wood_list_lv2 = pag.locateCenterOnScreen('wood_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (wood_list_lv2):
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
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                break
                if jelbean_clear:
                    jelbean_list_lv2 = pag.locateCenterOnScreen('jelbean_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (jelbean_list_lv2):
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
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                break
                if sugar_clear:
                    sugar_list_lv2 = pag.locateCenterOnScreen('sugar_list_lv2.png', confidence = 0.9, region = (58,185+account*540,33,106))
                    if (sugar_list_lv2):
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
                                time.sleep(0.2)
                                print('1분 내에 끝날 거라 남겼슴돠')
                                break
                            else:
                                print('1분 넘게 남아 삭제함돠')
                                pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                                time.sleep(0.2)
                                pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                                time.sleep(0.2)
                                pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                                break
            pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+(Making_Level-1)*153+account*540) # 1렙이면 200. 2~3렙은 153씩 올라감
            pag.mouseDown()
            time.sleep(0.7)
            pag.mouseUp()
            time.sleep(0.3)
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
            return True


bWood_Quick = True
bJelbean_Quick = True
bSugar_Quick = True

def list_clear(account):
    while True:
        cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75-10,200-10+account*540,20,20))
        if (cond_2nd_clear):
            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
            if (prod_refresh):
                pag.click(prod_refresh) # >> 클릭(즉시생산)
                # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                time.sleep(0.5)
                remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence = 0.945, region = (570,239+account*540,49,25)) # 다이아 10 확인
                if (remain_time_less_minute):
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    return
                else:
                    print('1분 넘게 남아 삭제함돠')
                    pag.click(random.randint(651-5,651+5),random.randint(85-5,85+5)+account*540)    # 즉시생산 창닫기
                    time.sleep(0.2)
                    pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)-73+account*540) # 첫째 칸 클릭
                    time.sleep(0.2)
                    pag.click(random.randint(462-5,462+5),random.randint(378-5,378+5)+account*540)  # 확인
                    return
            else:
                # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
                pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
                time.sleep(0.2)
                return True
        else:
            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence = 0.945, region = (90,145+account*540,24,20))
            if not (prod_refresh):
                # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
                pag.click(x=random.randint(223,428),y=random.randint(190,410)+account*540)
                time.sleep(0.2)
            # 둘째 칸 취소
            pag.click(random.randint(75-5,75+5),random.randint(200-5,200+5)+account*540)
        
        # 그새 생산 완료돼서 둘 째 칸 생산중이면 뜨는 취소창은 빼기
        cond_cancel = pag.locateCenterOnScreen('cond_cancel.png', confidence=0.96, region=(469,221+account*540,36,19))
        if (cond_cancel):
            pag.click(random.randint(628-5,628+5),random.randint(166-5,166+5)+account*540)
            time.sleep(0.2)
        # 안넣으니 클릭하고 바로 빈칸 캐치해서 멈출때가 있군....
        time.sleep(0.2)
                
urgent_prod = False
urgent_start_t = time.time()
prod_direction_left = True
def Quick_Production(account,urgent_start_t):
    # 실행 체크
    Check_Initiating(account)
    #건물에 들어가기..
    Enter_Building(account)
    # 초기화
    cycle_check = 0
    
    while True:
        if keyboard.is_pressed('end'):
            return
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence = 0.96, region = (440,363+account*540,43,29))
        if (cond_network):
            pag.click(random.randint(462-5,462+5),random.randint(377-5,377+5)+account*540)
            time.sleep(0.3)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
        if (cond_halted):
            pag.click(740,310+account*540)
            End_kkd(account)
            Kingdom_ready(account,'kkd_out')            # 재부팅
            return

        urgent_now_t = time.time()
        # 설정 시간 지나면 나가기... 우선 1시간으로? 아님 시간 설정?
        if urgent_now_t - urgent_start_t > 3600:
            pag.click(891,54+account*540)
            return
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
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        if pix_prod == pix_wood:
            pix_error_count = 0
            print('wood!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        elif pix_prod == pix_jelbean:
            pix_error_count = 0
            print('jelbean!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        elif pix_prod == pix_sugar:
            pix_error_count = 0
            print('sugar!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)

        elif pix_prod == pix_smith:
            pix_error_count = 0
            print('smith!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)

        elif pix_prod == pix_biscuit:
            pix_error_count = 0
            print('biscuit!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)    

        elif pix_prod == pix_berry:
            pix_error_count = 0
            print('berry!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)    

        elif pix_prod == pix_milk:
            pix_error_count = 0
            print('milk!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        elif pix_prod == pix_cotton:
            pix_error_count = 0
            print('cotton!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        elif pix_prod == pix_jelly:
            pix_error_count = 0
            print('jelly!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)
        
        elif pix_prod == pix_rollc:
            pix_error_count = 0
            print('rollc!')
            if prod_direction_left:
                Skip_Next(account)
            else:
                Skip_Right(account)

        elif pix_prod == pix_bread:
            pix_error_count = 0
            print('bread!')
            prod_direction_left = True
            Skip_Next(account)

        elif pix_prod == pix_jampy:
            pix_error_count = 0
            print('jampy!')
            prod_direction_left = True
            Skip_Next(account)

        elif pix_prod == pix_doye:
            pix_error_count = 0
            print('doye!')
            prod_direction_left = True
            Skip_Next(account)

        elif pix_prod == pix_flower:
            pix_error_count = 0
            print('flower!')
            prod_direction_left = True
            Skip_Next(account)

        elif pix_prod == pix_milky:
            pix_error_count = 0
            print('milky!')
            prod_direction_left = True
            Skip_Next(account)

        elif pix_prod == pix_latte:
            pix_error_count = 0
            print('latte!')
            prod_direction_left = False
            Skip_Right(account)


        elif pix_prod == pix_dolls:
            pix_error_count = 0
            print('dolls!')
            prod_direction_left = False
            Skip_Right(account)
            
        
        elif pix_prod == pix_beer:
            pix_error_count = 0
            print('beer!')
            prod_direction_left = False
            Skip_Right(account)

        elif pix_prod == pix_muffin:
            pix_error_count = 0
            print('muffin!')
            prod_direction_left = False
            Skip_Right(account)
        
        elif pix_prod == pix_jewel:
            pix_error_count = 0
            print('jewel!')
            prod_direction_left = False
            Skip_Right(account)

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
            Skip_Next(account)
        
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
                Skip_Next(account)
    

# account=1
# pag.moveTo(random.randint(770-10,770+10),random.randint(197-10,197+10)+account*540)
# pag.mouseDown()
# time.sleep(0.7)
# pag.mouseUp()
# time.sleep(0.5)
# list_clear(1)

# position_now를 만들어볼까?
# 나:1 젤:2 각:3 비:4 베:5 우:6 솜:7..
# 어차피 픽셀로 읽을건데? -> 생산 3렙 이상의 경우...
# 대장간의 경우 81(도끼)~87(망치) = False(생산완료 조건)을 걸 수도 있고
# 8렙 건물 들어오면 4렙 생산하고 있었으면 84~ : True, 81~83 : False, 
# prod_action(prod_lv1~8, completed) 이런식으로? 그럼 그놈은 화면 내에서 4렙을 쭉 만드는...
# 재고가 줄었음을 어떻게 알 수 있지? 소원나무, 이후 생산품인 경우니깐..

# --> prod_action을 1~3(픽셀 읽었으니 맨 위), 4~6 읽고 진행(대장간은 7..)
# 어차피 건물 대기열 1개 남았을 때만 동작하니..
# 0 아닌 최고 생산품 prod_action이 false일 때 해당 건물 b~~~completed 살려서 아예 안돌게
# 다음 생산 때 고고씽
# 두 계정 동시 연동은 어케하지 흠... 1계정 한바꾸 2계정 한바꾸? 이런식으로 설정 시간 동안?
account = 0
# 연구소 연구 완료 입장 시
# screen = ImageGrab.grab()
# pix_research = screen.getpixel((547,510+account*540)) # 마침표
# pix_research_comp = (170, 171, 174)
# if (pix_research == pix_research_comp):
#     print(pix_research)
#     pag.click(random.randint(205,205+515), random.randint(95,95+400))
#     time.sleep(1)


# # 연구소 입장 완료 시
# cond_research = pag.locateCenterOnScreen('cond_research.png', confidence=0.9, region=(12,36+account*540,36,36))  # 연구소 노움 얼굴
# if (cond_research):
#         print('연구소 입니다!')

# # 연구소 연구 선택 시
# screen = ImageGrab.grab()
# pix_research_wangkook = screen.getpixel((330,515+account*540)) # 왕국 연구
# pix_research_cookie = screen.getpixel((500,515+account*540)) # 쿠키 연구
# pix_research_deselected = (37, 49, 72)
# pix_research_selected = (58, 73, 109)
# if pix_research_wangkook == pix_research_selected:
#     print('왕국 연구 선택됨!')
# if pix_research_cookie == pix_research_selected:
#     print('쿠키 연구 선택됨!')
# # 연구중?



# while True:
#     research_W_01 = pag.locateCenterOnScreen('research_W_01.png', confidence=0.9, region=(2,32+account*540,917,505))
#     if (research_W_01):
#         print('research_W_01',research_W_01)
#         break
#     research_W_021 = pag.locateCenterOnScreen('research_W_021.png', confidence=0.9, region=(2,32+account*540,917,505))
#     if (research_W_021):
#         print('research_W_021',research_W_021)
#         break
#     research_W_022 = pag.locateCenterOnScreen('research_W_022.png', confidence=0.9, region=(2,32+account*540,917,505))
#     if (research_W_022):
#         print('research_W_022',research_W_022)
#         break
#     research_W_03 = pag.locateCenterOnScreen('research_W_03.png', confidence=0.9, region=(2,32+account*540,917,505))
#     if (research_W_03):
#         print('research_W_03',research_W_03)
#         break
#     if (research_W_041):
#         print('research_W_041',research_W_041)
#         break
#     research_W_041 = pag.locateCenterOnScreen('research_W_041.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_042 = pag.locateCenterOnScreen('research_W_042.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_043 = pag.locateCenterOnScreen('research_W_043.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_05 = pag.locateCenterOnScreen('research_W_05.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_061 = pag.locateCenterOnScreen('research_W_061.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_062 = pag.locateCenterOnScreen('research_W_062.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_063 = pag.locateCenterOnScreen('research_W_063.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_07 = pag.locateCenterOnScreen('research_W_07.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_081 = pag.locateCenterOnScreen('research_W_081.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_082 = pag.locateCenterOnScreen('research_W_082.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_083 = pag.locateCenterOnScreen('research_W_083.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_09 = pag.locateCenterOnScreen('research_W_09.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_10 = pag.locateCenterOnScreen('research_W_10.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_111 = pag.locateCenterOnScreen('research_W_111.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_112 = pag.locateCenterOnScreen('research_W_112.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_113 = pag.locateCenterOnScreen('research_W_113.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_12 = pag.locateCenterOnScreen('research_W_12.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_131 = pag.locateCenterOnScreen('research_W_131.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_132 = pag.locateCenterOnScreen('research_W_132.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_133 = pag.locateCenterOnScreen('research_W_133.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_14 = pag.locateCenterOnScreen('research_W_14.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_151 = pag.locateCenterOnScreen('research_W_151.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_152 = pag.locateCenterOnScreen('research_W_152.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_153 = pag.locateCenterOnScreen('research_W_153.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_16 = pag.locateCenterOnScreen('research_W_16.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_171 = pag.locateCenterOnScreen('research_W_171.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_172 = pag.locateCenterOnScreen('research_W_172.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_18 = pag.locateCenterOnScreen('research_W_18.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_191 = pag.locateCenterOnScreen('research_W_191.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_192 = pag.locateCenterOnScreen('research_W_192.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_193 = pag.locateCenterOnScreen('research_W_193.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_20 = pag.locateCenterOnScreen('research_W_20.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_211 = pag.locateCenterOnScreen('research_W_211.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_212 = pag.locateCenterOnScreen('research_W_212.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_213 = pag.locateCenterOnScreen('research_W_213.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_22 = pag.locateCenterOnScreen('research_W_22.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_23 = pag.locateCenterOnScreen('research_W_23.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_24 = pag.locateCenterOnScreen('research_W_24.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_251 = pag.locateCenterOnScreen('research_W_251.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_252 = pag.locateCenterOnScreen('research_W_252.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_253 = pag.locateCenterOnScreen('research_W_253.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_W_26 = pag.locateCenterOnScreen('research_W_26.png', confidence=0.9, region=(2,32+account*540,917,505))

#     research_C_011 = pag.locateCenterOnScreen('research_C_011.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_012 = pag.locateCenterOnScreen('research_C_012.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_02 = pag.locateCenterOnScreen('research_C_02.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_031 = pag.locateCenterOnScreen('research_C_031.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_032 = pag.locateCenterOnScreen('research_C_032.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_033 = pag.locateCenterOnScreen('research_C_033.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_034 = pag.locateCenterOnScreen('research_C_034.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_041 = pag.locateCenterOnScreen('research_C_041.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_042 = pag.locateCenterOnScreen('research_C_042.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_043 = pag.locateCenterOnScreen('research_C_043.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_044 = pag.locateCenterOnScreen('research_C_044.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_05 = pag.locateCenterOnScreen('research_C_05.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_061 = pag.locateCenterOnScreen('research_C_061.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_062 = pag.locateCenterOnScreen('research_C_062.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_07 = pag.locateCenterOnScreen('research_C_07.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_081 = pag.locateCenterOnScreen('research_C_081.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_082 = pag.locateCenterOnScreen('research_C_082.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_083 = pag.locateCenterOnScreen('research_C_083.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_084 = pag.locateCenterOnScreen('research_C_084.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_091 = pag.locateCenterOnScreen('research_C_091.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_092 = pag.locateCenterOnScreen('research_C_092.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_093 = pag.locateCenterOnScreen('research_C_093.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_094 = pag.locateCenterOnScreen('research_C_094.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_10 = pag.locateCenterOnScreen('research_C_10.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_111 = pag.locateCenterOnScreen('research_C_111.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_112 = pag.locateCenterOnScreen('research_C_112.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_12 = pag.locateCenterOnScreen('research_C_12.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_131 = pag.locateCenterOnScreen('research_C_131.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_132 = pag.locateCenterOnScreen('research_C_132.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_133 = pag.locateCenterOnScreen('research_C_133.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_134 = pag.locateCenterOnScreen('research_C_134.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_141 = pag.locateCenterOnScreen('research_C_141.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_142 = pag.locateCenterOnScreen('research_C_142.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_143 = pag.locateCenterOnScreen('research_C_143.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_144 = pag.locateCenterOnScreen('research_C_144.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_15 = pag.locateCenterOnScreen('research_C_15.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_161 = pag.locateCenterOnScreen('research_C_161.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_162 = pag.locateCenterOnScreen('research_C_162.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_171 = pag.locateCenterOnScreen('research_C_171.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_172 = pag.locateCenterOnScreen('research_C_172.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_173 = pag.locateCenterOnScreen('research_C_173.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_174 = pag.locateCenterOnScreen('research_C_174.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_181 = pag.locateCenterOnScreen('research_C_181.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_182 = pag.locateCenterOnScreen('research_C_182.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_183 = pag.locateCenterOnScreen('research_C_183.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_184 = pag.locateCenterOnScreen('research_C_184.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_19 = pag.locateCenterOnScreen('research_C_19.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_201 = pag.locateCenterOnScreen('research_C_201.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_202 = pag.locateCenterOnScreen('research_C_202.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_211 = pag.locateCenterOnScreen('research_C_211.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_212 = pag.locateCenterOnScreen('research_C_212.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_213 = pag.locateCenterOnScreen('research_C_213.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_214 = pag.locateCenterOnScreen('research_C_214.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_221 = pag.locateCenterOnScreen('research_C_221.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_222 = pag.locateCenterOnScreen('research_C_222.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_223 = pag.locateCenterOnScreen('research_C_223.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_224 = pag.locateCenterOnScreen('research_C_224.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_23 = pag.locateCenterOnScreen('research_C_23.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_24 = pag.locateCenterOnScreen('research_C_24.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_251 = pag.locateCenterOnScreen('research_C_251.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_252 = pag.locateCenterOnScreen('research_C_252.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_253 = pag.locateCenterOnScreen('research_C_253.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_254 = pag.locateCenterOnScreen('research_C_254.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_261 = pag.locateCenterOnScreen('research_C_261.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_262 = pag.locateCenterOnScreen('research_C_262.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_263 = pag.locateCenterOnScreen('research_C_263.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_264 = pag.locateCenterOnScreen('research_C_264.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_27 = pag.locateCenterOnScreen('research_C_27.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_281 = pag.locateCenterOnScreen('research_C_281.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_282 = pag.locateCenterOnScreen('research_C_282.png', confidence=0.9, region=(2,32+account*540,917,505))
#     research_C_283 = pag.locateCenterOnScreen('research_C_283.png', confidence=0.9, region=(2,32+account*540,917,505))

# a = "'research_W_02"
# b = ".png'"
# print(a)
# print(len(a))
# print(b)
# print(a+b)

# # 연구 찾아서, 클릭하는 경우
# account=0

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
    its_image = pag.locateCenterOnScreen(its_name+its_format, confidence=0.925, region=(2,32+account*540,917,505))
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

# def research_movement(account,where_to,research_position):
#     if (research_position):
#         if where_to > research_position:
#             pag.moveTo(900,484+account*540)
#             pag.mouseDown()
#             time.sleep(0.3)
#             pag.moveTo(870,484+account*540,0.2)
#             if where_to - research_position > 2:
#                 pag.moveTo(50,484+account*540,0.5)
#             else:
#                 pag.moveTo(450,484+account*540,0.5)
#             time.sleep(0.3)
#             pag.mouseUp()
                
#         if research_position > where_to:
#             pag.moveTo(50,484+account*540)
#             pag.mouseDown()
#             time.sleep(0.3)
#             pag.moveTo(80,484+account*540,0.2)
#             if research_position - where_to > 2:
#                 pag.moveTo(900,484+account*540,0.5)
#             else:
#                 pag.moveTo(450,484+account*540,0.5)
#             time.sleep(0.3)
#             pag.mouseUp()
#         print('research_position',research_position)
#         print('where_to',where_to)
#         if abs(research_position - where_to) == 1:
#             print('목표 지점 도착!')
#             return True
#     else:
#         pag.moveTo(450,484+account*540)
#         pag.mouseDown()
#         time.sleep(0.3)
#         pag.moveTo(420,484+account*540,0.2)
#         pag.moveTo(300,484+account*540,0.5)
#         time.sleep(0.2)
#         pag.mouseUp()



# 현재 위치 찾는 것
# bResearchFind = True
# research_position = 0
# where_to = 4
# what_to = 'C'
# while bResearchFind:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     research_position = research_pos_now(account,what_to,0.925)
#     if (research_position):
#         research_movement(account,where_to,research_position)
#         if abs(where_to - research_position) < 3:
#             print('원하는 곳에 도달?')
#             break
#     else:
#         pag.moveTo(450,484+account*540)
#         pag.mouseDown()
#         time.sleep(0.3)
#         pag.moveTo(420,484+account*540,0.2)
#         pag.moveTo(300,484+account*540,0.5)
#         time.sleep(0.2)
#         pag.mouseUp()
#     time.sleep(1)



# while True:
#     if keyboard.is_pressed('end'):
#         print('end 누름')
#         break
#     print(research_pos_now(account,'C',0.925))
#     time.sleep(1)
# cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region = (2,32+account*540,917,505))
# research_C_092_in = pag.locateCenterOnScreen('research_C_092_in.png', confidence=0.925, region=(265,58+account*540,385,32))
# if (research_C_092_in):
#     print('research_C_092_in',research_C_092_in)
# research_C_05_in = pag.locateCenterOnScreen('research_C_05_in.png', confidence=0.96, region=(2,32+account*540,917,505))
# if (research_C_05_in):
#     print('research_C_05_in',research_C_05_in)
#     pag.moveTo(research_C_05_in)
#     time.sleep(1)
# account=1
# research_C_05_in = pag.locateCenterOnScreen('research_C_05_in.png', confidence=0.96, region=(2,32+account*540,917,505))
# if (research_C_05_in):
#     print('research_C_05_in',research_C_05_in)
#     pag.moveTo(research_C_05_in)
# 만일을 위해...

# cond_research_comp_in = pag.locateCenterOnScreen('cond_research_comp_in.png', confidence=0.96, region=(133,114+account*540,60,19))
# if (cond_research_comp_in):
#     print('cond_research_comp_in',cond_research_comp_in)
#     pag.moveTo(cond_research_comp_in)
#     time.sleep(2)
#     pag.click(cond_research_comp_in)

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
        print('bPosition_Checked',bPosition_Checked)
        print('num_where_to',num_where_to)
        print('position_now',position_now)
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

# 실제 생산하는 녀석.. 이렇게 보니 앞에 생산품도 함수로 만들수 있지 않을까
def prod_action(image, list_image, account, check_num):
    print('Prod_action함수!',image, list_image, account, check_num)
    start_time = time.time()
    error_count = 0

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
    
    cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75-10,200-10+account*540,20,20))
    if (cond_2nd_clear):
        ShowTime = True
    else:
        return True
    
    while ShowTime:
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

        now_time = time.time()
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
            print('리스트 full!')
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
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    return False
                elif (not_opened):                                  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284,15+account*540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    return False
                else:                                               # 그거 아니면 생산 클릭
                    print('생산품 클릭!')
                    pag.moveTo(ctr[0]+177,ctr[1]+48)
                    time.sleep(0.1)
                    pag.mouseDown()
                    time.sleep(0.7)
                    pag.mouseUp()
                    time.sleep(0.5)

                    lack_of_material = pag.locateCenterOnScreen('lack_material.png',confidence=0.95, region=(2,32+account*540,917,505))
                    if (lack_of_material):
                        print('재료가 부족해요')
                        pag.click(284,15+account*540)
                        time.sleep(0.1)
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
                time.sleep(0.2)
                pag.moveTo(610,295+account*540+15,2)   # 15 내리고 이미지 다시 찾음
                time.sleep(0.2)
                pag.mouseUp()
                time.sleep(2)
                error_count = error_count+1
            if error_count == 0:
                pag.moveTo(610,295+account*540)
                pag.mouseDown()
                time.sleep(0.2)
                pag.moveTo(610,295+account*540-10,2)   # 10 올리고 이미지 다시 찾음
                time.sleep(0.2)
                pag.mouseUp()
                time.sleep(2)
                error_count = 1


# if Angmu_Enter(account,'research'):
#     research_action(account,'C','research_C_283')
# up_1 = pag.locateCenterOnScreen('up_1.png',confidence=0.8,region=(500,47+account*540,14,15))
# if (up_1):
#     print('1천대!')
# else:
#     up_2 = pag.locateCenterOnScreen('up_2.png',confidence=0.8,region=(500,47+account*540,14,15))
#     if (up_2):
#         print('2천대!')
#     else:
#         up_3 = pag.locateCenterOnScreen('up_3.png',confidence=0.8,region=(500,47+account*540,14,15))
#         if (up_3):
#             print('3천대!')
#         else:
#             up_4 = pag.locateCenterOnScreen('up_4.png',confidence=0.8,region=(500,47+account*540,14,15))
#             if (up_4):
#                 print('4천대!')
#             else:
#                 up_5 = pag.locateCenterOnScreen('up_5.png',confidence=0.8,region=(500,47+account*540,14,15))
#                 if (up_5):
#                     print('5천대!')
#                 else:
#                     up_6 = pag.locateCenterOnScreen('up_6.png',confidence=0.8,region=(500,47+account*540,14,15))
#                     if (up_6):
#                         print('6천대!')
#                     else:
#                         print('1000 미만...')
# Making_Level = 1
# pag.moveTo(random.randint(773-5,773+5),random.randint(200-3,200+3)+(Making_Level-1)*153+account*540) # 1렙이면 200. 2~3렙은 153씩 올라감
# pag.mouseDown()
# time.sleep(0.7)
# pag.mouseUp()
# time.sleep(0.5)
# pag.click(222,777)
# Skip_Next(1)
# 드래그드래그
# account=1
# trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2,325+account*540,750,26))
# trade_baseline = list(trade_baseline)
# out_baseline = list()
# if len(trade_baseline) >0 :
#     for p in trade_baseline:
#         ctr = pag.center(p)
#         pag.moveTo(ctr)
#         print(ctr)
#         Angmu_check(ctr[0]+29, account)
#         out_baseline.append(ctr)
#         time.sleep(1)
#     print('out_baseline',out_baseline)
# account=0
# ctr = (701, 338)
# Angmu_Action('trade_sword_lv2.png', ctr, account)
# Angmu_check(74+29+157*4, 0)
# Angmu_check(550, 1)
# account=0
# cond_trade_refresh = pag.locateCenterOnScreen('cond_trade_refresh.png', confidence=0.85, region=(2,32+account*540,917,505))
# if (cond_trade_refresh):
#     print('cond_trade_refresh', cond_trade_refresh)
# research_C_23 = pag.locateCenterOnScreen('research_C_23.png', confidence=0.85, region=(2,32+account*540,917,505))
# if (research_C_23):
#     print('research_C_23', research_C_23)

# find_and_check(account,'research_C_23')
# if Angmu_Enter(account,'research'):
#     research_action(account,'C','research_C_283')   # 모든 쿠키 치명타..
# account=0
# cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.96, region=(2,32+account*540,917,505))
# if (cond_balloon_lack_heart):
#     print('cond_balloon_lack_heart',cond_balloon_lack_heart)
#     pag.moveTo(cond_balloon_lack_heart)
# if Angmu_Enter(account,'research'):
#     research_action(account,'C','research_C_112')   # 케이크 충전 가속
account = 0
def Event_action(account):
    how_many_gold = 0
    while True:
        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        
        event_empty = pag.locateCenterOnScreen('event_empty.png', confidence = 0.9, region=(745,427+account*540,59,16))
        # event_train_3 = pag.locateCenterOnScreen('event_train_3.png', confidence = 0.9, region=(696,341+account*540,157,59))
        if not (event_empty):
            pag.click(774,290+account*540)
            time.sleep(1)
        
        if (event_empty):
            event_topping_10 = pag.locateCenterOnScreen('event_topping_10.png', confidence = 0.9, region=(696,341+account*540,157,59))
            event_topping_20 = pag.locateCenterOnScreen('event_topping_20.png', confidence = 0.9, region=(696,341+account*540,157,59))
            if (event_topping_10) or (event_topping_20):
                print('오키!',how_many_gold*45644)
                return
            else:
                pag.click(717,264+account*540)
                time.sleep(2)
                pag.click(830,303+account*540)
                time.sleep(0.3)
                pag.click(600,250+account*540)
                time.sleep(0.3)
                pag.click(830,303+account*540)
                how_many_gold = how_many_gold + 1
        time.sleep(0.2)


# Event_action(0)
# Event_action(1)
account=0
# Heart_new_numb(0)
Heart_new_numb(1)