import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
from datetime import datetime
import random

account = 0

scrshot_items3 = 0
scrshot_items6 = 1

scrshot_stby_items = False

# pag.screenshot('prod_check_point_magic.PNG', region=(607+(account//2)*960, 88+(account%2)*540, 5,5))   # 마법공방 체크포인트 따기

# prod_check_point = pag.locateCenterOnScreen('prod_check_point_magic.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 마법공방 이미지 따기 (분홍 별)
# prod_check_point = pag.locateCenterOnScreen('prod_check_point.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460))       # 나머지 건물 이미지 따기 (빨간 점)
# print(prod_check_point.x-960, prod_check_point.y)

# # # 안쓰는 거!!
# # # 1~3번째 제품 이미지 캡쳐
# # pag.screenshot('lev1.PNG', region=(593+(account//2)*960, 140+(account%2)*540, 20, 20))
# # pag.screenshot('lev2.PNG', region=(593+(account//2)*960, 293+(account%2)*540, 20, 20))
# # pag.screenshot('lev3.PNG', region=(593+(account//2)*960, 446+(account%2)*540, 20, 20))
# #
# # # 4~번째 제품 이미지 캡쳐
# # pag.screenshot('lev4.PNG', region=(593+(account//2)*960, 140+(account%2)*540, 20, 20))
# # pag.screenshot('lev5.PNG', region=(593+(account//2)*960, 293+(account%2)*540, 20, 20))
# # pag.screenshot('lev6.PNG', region=(593+(account//2)*960, 446+(account%2)*540, 20, 20))

while scrshot_items3:
    # 강제종료
    if keyboard.is_pressed('end'):
        break
    # 제작 제품(???_lev1~lev0) 스샷 찍기
    list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 일반 건물일때
    # list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 마법공방 건물일때
    list_numb2 = list(list_numb1)
    print(list_numb2)
    print(len(list_numb2))

    # # 1~3 번째 제품 이미지 캡쳐
    if (len(list_numb2) == 3):
        pag.screenshot('magic_lev1.PNG', region = (list_numb2[0][0]-14, list_numb2[0][1]+52, 20, 20))
        pag.screenshot('magic_lev2.PNG', region = (list_numb2[1][0]-14, list_numb2[1][1]+52, 20, 20))
        pag.screenshot('magic_lev3.PNG', region = (list_numb2[2][0]-14, list_numb2[2][1]+52, 20, 20))
        print('%d개 아이템 스샷'%(len(list_numb2)))
        break
    if (len(list_numb2) == 2):
        pag.screenshot('magic_lev1.PNG', region = (list_numb2[0][0]-14, list_numb2[0][1]+52, 20, 20))
        pag.screenshot('magic_lev2.PNG', region = (list_numb2[1][0]-14, list_numb2[1][1]+52, 20, 20))
        print('%d개 아이템 스샷'%(len(list_numb2)))
        break
    if (len(list_numb2) == 1):
        pag.screenshot('magic_lev1.PNG', region = (list_numb2[0][0]-14, list_numb2[0][1]+52, 20, 20))
        print('%d개 아이템 스샷'%(len(list_numb2)))
        break

# pag.screenshot('magic_lev6.PNG', region=(607 - 14, 394 + 52, 20, 20))

while scrshot_items6:
    # 강제종료
    if keyboard.is_pressed('end'):
        break
    # 제작 제품(???_lev1~lev0) 스샷 찍기
    list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.95, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))  # 일반 건물일때
    # list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.955, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 마법공방 건물일때
    list_numb2 = list(list_numb1)
    print(list_numb2)
    print(len(list_numb2))

    # # 4~6 번째 제품 이미지 캡쳐
    if (len(list_numb2) == 3):
        pag.screenshot('magic_lev4.PNG', region=(list_numb2[0][0] - 14, list_numb2[0][1] + 52, 20, 20))
        pag.screenshot('magic_lev5.PNG', region=(list_numb2[1][0] - 14, list_numb2[1][1] + 52, 20, 20))
        pag.screenshot('magic_lev6.PNG', region=(list_numb2[2][0] - 14, list_numb2[2][1] + 52, 20, 20))
        print('%d개 아이템 스샷' % (len(list_numb2)))
        break
    if (len(list_numb2) == 2):
        pag.screenshot('magic_lev4.PNG', region=(list_numb2[0][0] - 14, list_numb2[0][1] + 52, 20, 20))
        pag.screenshot('magic_lev5.PNG', region=(list_numb2[1][0] - 14, list_numb2[1][1] + 52, 20, 20))
        print('%d개 아이템 스샷' % (len(list_numb2)))
        break
    if (len(list_numb2) == 1):
        pag.screenshot('magic_lev4.PNG', region=(list_numb2[0][0] - 14, list_numb2[0][1] + 52, 20, 20))
        print('%d개 아이템 스샷' % (len(list_numb2)))
        break

# print(list_numb2)
# print(list_numb2[0][0]-(account//2)*960-16, ',', list_numb2[0][1]+50)
# print(list_numb2[1][0]-(account//2)*960-16, ',', list_numb2[1][1]+50)
# print(list_numb2[2][0]-(account//2)*960-16, ',', list_numb2[2][1]+50)

# # print(list_numb2[0][0]-(account//2)*960-16)
# # print(list_numb2[0][1]+50)
# # print(list_numb2[1][0]-(account//2)*960)
# # print(list_numb2[1][1])
# # print(list_numb2[2][0]-(account//2)*960)
# # print(list_numb2[2][1])


while scrshot_stby_items:
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    # 대기 제품(???_stby_lv1~lv0) 스샷 찍기
    # 대기 제품 위치 확인용
    # prod_check_stby_lv1 = pag.locateCenterOnScreen('prod_check_stby_lv1.PNG', confidence=0.92, region=(2+(account//2)*960, 2+(account%2)*540, 960, 540))
    # print(prod_check_stby_lv1)
    # prod_check_stby_lv2 = pag.locateCenterOnScreen('prod_check_stby_lv2.PNG', confidence=0.92, region=(2+(account//2)*960, 2+(account%2)*540, 960, 540))
    # print(prod_check_stby_lv2)

    # 대기 제품 진짜 스샷 찍자!
    pag.screenshot('prod_check_stby_lv11.PNG', region = (51+(account//2)*960, 179+(account%2)*540, 45, 45))  # 두번째 대기열
    pag.screenshot('prod_check_stby_lv22.PNG', region = (51+(account//2)*960, 250+(account%2)*540, 45, 45))  # 세번째 대기열
    pag.screenshot('prod_check_stby_lv33.PNG', region = (51+(account//2)*960, 321+(account%2)*540, 45, 45))  # 네번째 대기열
    pag.screenshot('prod_check_stby_lv44.PNG', region = (51+(account//2)*960, 392+(account%2)*540, 45, 45))  # 다섯번째 대기열
    print('4개 대기 아이템 스샷')
    break
