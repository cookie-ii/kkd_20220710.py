import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
from datetime import datetime
import random

# 제작 건물 첫번째 칸에 몇번째 제품이 있나?
def check_item_number(account, where):
    if(where == 'top'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))
    if (where == 'bot'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 153))

    if smith_lev7:
        # print('7번째 아이템')
        return 7
    elif smith_lev6 or bread_lev6 or jampy_lev6 or flower_lev6 or magic_lev6:
    # elif smith_lev6:
        # print('6번째 아이템')
        return 6
    elif smith_lev5 or jelly_lev5 or bread_lev5 or jampy_lev5 or flower_lev5 or icecream_lev5 or magic_lev5:
        # print('5번째 아이템')
        return 5
    elif smith_lev4 or jelly_lev4 or rollc_lev4 or bread_lev4 or jampy_lev4 or doye_lev4 or flower_lev4 or icecream_lev4  or magic_lev4:
        # print('4번째 아이템')
        return 4
    elif smith_lev3 or jelly_lev3 or rollc_lev3 or bread_lev3 or jampy_lev3 or doye_lev3 or flower_lev3 or icecream_lev3 or magic_lev3:
        # print('3번째 아이템')
        return 3
    elif smith_lev2 or jelly_lev2 or rollc_lev2 or bread_lev2 or jampy_lev2 or doye_lev2 or flower_lev2 or icecream_lev2 or magic_lev2:
        # print('2번째 아이템')
        return 2
    elif smith_lev1 or jelly_lev1 or rollc_lev1 or bread_lev1 or jampy_lev1 or doye_lev1 or flower_lev1 or icecream_lev1 or magic_lev1:
        print('smith', smith_lev1, 'jelly', jelly_lev1, 'rollc', rollc_lev1, 'bread', bread_lev1, 'jampy', jampy_lev1, 'doye', doye_lev1, 'flower', flower_lev1, 'icecream', icecream_lev1, 'magic', magic_lev1)
        # print('1번째 아이템')
        return 1
    else:
        print('?')

account = 0
# list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 일반 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
# print((list_numb2[0][0]-14, list_numb2[0][1]+52))
a = check_item_number(account, 'top')
print('a:', a)