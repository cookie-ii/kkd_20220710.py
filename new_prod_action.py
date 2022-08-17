import random
import time
from datetime import datetime
import keyboard
import pyautogui as pag
from PIL import ImageGrab
import sys
import math

def Skip_Next(account, prod_direction_left):
    if prod_direction_left:  # 이레가 수정햇서
        pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
        time.sleep(0.4)
        pag.click(x=random.randint(243, 422) + (account // 2) * 960, y=random.randint(336, 398) + (account % 2) * 540)
        time.sleep(0.4)
        # prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95, region=(339 + (account // 2) * 960, 253 + (account % 2) * 540, 175, 87))
        # time.sleep(1)
        # if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
        #     print('욕심을 버리시오 중생이여..')
        #     pag.click(455 + (account // 2) * 960, 379 + (account % 2) * 540)
        #     time.sleep(0.3)
        #     pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
        #     time.sleep(0.3)
    else:
        pag.click(485 + (account // 2) * 960, 280 + (account % 2) * 540)
        time.sleep(0.4)
        pag.click(x=random.randint(243, 422) + (account // 2) * 960, y=random.randint(336, 398) + (account % 2) * 540)
        time.sleep(0.7)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)
    # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
    # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
    dotdotdot4 = pag.locateCenterOnScreen('dotdotdot4.png', confidence=0.814, region=(150 + (account // 2) * 960, 200 + (account % 2) * 540, 360, 160))
    dotdotdot5 = pag.locateCenterOnScreen('dotdotdot5.png', confidence=0.814, region=(150 + (account // 2) * 960, 200 + (account % 2) * 540, 360, 160))

    if (dotdotdot4):
        # print('dotdotdot4:', dotdotdot4)
        if (dotdotdot4.y+88 >= 468 + (account % 2) * 540):
            dotdotdot4.y = dotdotdot4.y - (dotdotdot4.y + 88 - 468)
            pag.click(dotdotdot4.x, dotdotdot4.y)
        elif (dotdotdot4.x >= 415+(account//2)*960):
            changed_dot = dotdotdot4.x + (424+(account//2)*960 - dotdotdot4.x)
            pag.click(changed_dot, dotdotdot4.y+88)
        elif (dotdotdot4.x <= 232 + (account // 2) * 960):
            changed_dot = dotdotdot4.x + (227+(account//2)*960 - dotdotdot4.x)
            pag.click(changed_dot, dotdotdot4.y + 88)
        else:
            pag.click(dotdotdot4.x, dotdotdot4.y+88)
        time.sleep(0.3)
        if (dotdotdot5):
            if (dotdotdot5.y + 88 >= 468 + (account % 2) * 540):
                dotdotdot5.y = dotdotdot5.y - (dotdotdot5.y + 88 - 468)
                pag.click(dotdotdot5.x, dotdotdot5.y)
            elif (dotdotdot5.x >= 415 + (account // 2) * 960):
                changed_dot = dotdotdot5.x + (424 + (account // 2) * 960 - dotdotdot5.x)
                pag.click(changed_dot, dotdotdot5.y + 88)
            elif (dotdotdot5.x <= 232 + (account // 2) * 960):
                changed_dot = dotdotdot5.x + (227 + (account // 2) * 960 - dotdotdot5.x)
                pag.click(changed_dot, dotdotdot5.y + 88)
            else:
                pag.click(dotdotdot5.x, dotdotdot5.y + 88)
            time.sleep(0.3)
    return



def numb_new_recog_new(prod_pin, account):
    its_number = 0
    how_many_nums = 0
    pos_numb = 0  # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
    num_list = list()
    # print('라인 %s번 진행합니다!' % (line))
    screen = ImageGrab.grab()
    # 3렙 건물인 경우 무조건 prod_pin = (612,95)
    # pix_jaritsu1_1 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
    pix_jaritsu1_1 = screen.getpixel((prod_pin[0] + 19, prod_pin[1] + 81))  # 상
    # print('pix_자릿수1_1:', pix_jaritsu1_1)
    # pix_jaritsu1_2 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 87 + 153 * (line - 1)))  # 하
    pix_jaritsu1_2 = screen.getpixel((prod_pin[0] + 19, prod_pin[1] + 87))  # 하
    # print('pix_자릿수1_2:', pix_jaritsu1_2)


    if ((pix_jaritsu1_1) == (255, 255, 255)) and ((pix_jaritsu1_2) == (255, 255, 255)):
        pix_zero_1 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 82 ))  # 상
        # print((prod_pin[0] + 24 , prod_pin[1] + 82 ))
        # print('pix_zero_1:', pix_zero_1)
        pix_zero_2 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 85 ))  # 하
        # print((prod_pin[0] + 24 , prod_pin[1] + 85 ))
        # print('pix_zero_2:', pix_zero_2)
        # print('pos_numb', pos_numb)
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
        pix_jaritsu2_1 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 ))  # 상
        pix_jaritsu2_2 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 ))  # 하
        if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
            # print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            # print('이 숫자는 세 자릿 수 입니다!')
            pos_numb = 3
    # print('자릿수 다시 확인', pos_numb)
    if pos_numb == 1:
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        # print('한 자릿 수 범위 확인1', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7)
        if (num_1):
            return 1
        num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_1_1):
            return 1
        num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_2):
            return 2
        num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_3):
            return 3
        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_3_1):
            return 3
        num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_4):
            return 4
        num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_4_2):
            return 4
        num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_5):
            return 5
        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_6):
            return 6
        num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_7):
            return 7
        num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_8):
            return 8
        num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_8_1):
            return 8
        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_9):
            return 9
        num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_9_1):
            return 9
        return 0

    if pos_numb == 2:
        # 10의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
        # print('두 자릿 수 10자리 범위', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7)
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                print('십의 자리 숫자 확인 에러!!')
        # 1의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
        # print('두자릿수 1자리 범위:', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7)
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                print('일의 자리 숫자 확인 에러!!')
        print('현재 재고는 =', its_number)
        return its_number
    if pos_numb == 3:
        # print('세 자릿 수 범위 확인', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14)
        # pag.screenshot('ire_number_check100.PNG', region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 900
                                                            else:
                                                                print('백의 자리 숫자 확인 에러!!')
        # 10의 자리 숫자 걍검색
        # pag.screenshot('ire_number_check10.PNG', region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                                if (num_0):
                                                                    print('십의 자리 0!!')
                                                                else:
                                                                    print('10의 자리 못읽음..')
        # 1의 자리 숫자 걍검색
        # pag.screenshot('ire_number_check1.PNG', region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                                if (num_0):
                                                                    print('1의 자리 0!!')
                                                                else:
                                                                    print('1의 자리 못읽음..')
        print('현재 재고는 =', its_number)
        return its_number


def Updown_new(account, updown, updown_number):
    try:
        if updown == 'up_little':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 - updown_number, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'down_little':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + updown_number, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)

    except:
        print('에러가 났어요! Updown_new')
        # send_telegram_message('Updown에서 에러가 났어요!')
        # Kingdom_ready(account, 'kkd_out')  # 재부팅



def Updown(account, updown):
    try:
        if updown == 'up':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 - 173, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'up1':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 - 173 +18, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'down1':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 173-18, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'up_little':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 - 35, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'down_little':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 35, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'down':
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 173-5, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.5)
            pag.click(262 + (account // 2) * 960, 328 + (account % 2) * 540)
            time.sleep(1.5)
        if updown == 'leftup':
            pag.moveTo(94 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(94 + (account // 2) * 960, 295 + (account % 2) * 540 - 173, 2)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            # time.sleep(0.5)
            # pag.click(262 + (account//2)*960, 328 + (account%2) * 540)
            time.sleep(1.5)
    except:
        print('에러가 났어요! Updown')
        # send_telegram_message('Updown에서 에러가 났어요!')
        # Kingdom_ready(account, 'kkd_out')  # 재부팅

# 제작 건물 첫번째 칸에 몇번째 제품이 있나?
def check_item_number(account, where):
    if(where == 'top'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
    if (where == 'bot'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 145))

    if smith_lev1 or jelly_lev1 or rollc_lev1 or bread_lev1 or jampy_lev1 or doye_lev1 or flower_lev1 or icecream_lev1 or magic_lev1:
        # print('1번째 아이템')
        return 1
    elif smith_lev2 or jelly_lev2 or rollc_lev2 or bread_lev2 or jampy_lev2 or doye_lev2 or flower_lev2 or icecream_lev2 or magic_lev2:
        # print('2번째 아이템')
        return 2
    elif smith_lev3 or jelly_lev3 or rollc_lev3 or bread_lev3 or jampy_lev3 or doye_lev3 or flower_lev3 or icecream_lev3 or magic_lev3:
        # print('3번째 아이템')
        return 3
    elif smith_lev4 or jelly_lev4 or rollc_lev4 or bread_lev4 or jampy_lev4 or doye_lev4 or flower_lev4 or icecream_lev4  or magic_lev4:
        # print('4번째 아이템')
        return 4
    elif smith_lev5 or jelly_lev5 or bread_lev5 or jampy_lev5 or flower_lev5 or icecream_lev5 or magic_lev5:
        # print('5번째 아이템')
        return 5
    elif smith_lev6 or bread_lev6 or jampy_lev6 or flower_lev6 or magic_lev6:
    # elif smith_lev6:
        # print('6번째 아이템')
        return 6
    elif smith_lev7:
        # print('7번째 아이템')
        return 7
    else:
        print('몇번째 아이템인지 못읽었어, 화면 올립니다')
        Updown(account, 'down1')
        return False

# 생산건물 안에서 화면 조정
def prod_default_screen(account, building):
    while True:
        if keyboard.is_pressed('end'):
            break
        # time.sleep(1)
        if building == 'normal':
            list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.85, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
        elif building == 'magic':
            list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 마법공방 건물일때

        # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
        list_numb2 = list(list_numb1)
        # print(list_numb2)

        if not list_numb2:
            print('안보여!')
            continue
            # Updown(account, 'down_little')
            #
            # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
            # list_numb2 = list(list_numb1)
            # print(list_numb2)
        if 75 <= list_numb2[0][1] - (account % 2) * 540 <= 75 + 20:
            # print('첫 y값이 75+20 ~ 75사이', list_numb2[0][1] - (account % 2) * 540)
            break
        elif 75 >= list_numb2[0][1] - (account % 2) * 540:
            # print('조금.. 올리나?')
            a = int(list_numb2[0][1]) - 88
            print(a)
            Updown_new(account, 'down_little', a)
        elif list_numb2[0][1] - (account % 2) * 540 >= 75 + 20:
            # print('조금.. 내리나?')
            a = int(list_numb2[0][1]) - 88
            print(a)
            Updown_new(account, 'up_little', a)
        else:
            print('prod_default_screen 오류예요!')
            print(list_numb2)
            break

def Check_available_slots(account):
    try:
        pag.click(x=random.randint(243, 422) + (account // 2) * 960, y=random.randint(336, 398) + (account % 2) * 540)
        time.sleep(0.5)

        prod_full_1 = pag.locateCenterOnScreen('prod_full_1.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_2 = pag.locateCenterOnScreen('prod_full_2.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_3 = pag.locateCenterOnScreen('prod_full_3.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_4 = pag.locateCenterOnScreen('prod_full_4.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_5 = pag.locateCenterOnScreen('prod_full_5.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_6 = pag.locateCenterOnScreen('prod_full_6.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_7 = pag.locateCenterOnScreen('prod_full_7.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_8 = pag.locateCenterOnScreen('prod_full_8.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_9 = pag.locateCenterOnScreen('prod_full_9.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))
        prod_full_10 = pag.locateCenterOnScreen('prod_full_10.PNG', grayscale=True, confidence=0.9, region=(65 + (account // 2) * 960, 60 + (account % 2) * 540, 20, 22))

        prod_full_n3 = pag.locateCenterOnScreen('prod_full_n3.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n4 = pag.locateCenterOnScreen('prod_full_n4.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n5 = pag.locateCenterOnScreen('prod_full_n5.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n6 = pag.locateCenterOnScreen('prod_full_n6.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n7 = pag.locateCenterOnScreen('prod_full_n7.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n8 = pag.locateCenterOnScreen('prod_full_n8.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n9 = pag.locateCenterOnScreen('prod_full_n9.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        prod_full_n10 = pag.locateCenterOnScreen('prod_full_n10.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 25))
        if (prod_full_1):
            a = 1
        elif (prod_full_2):
            a = 2
        elif (prod_full_3):
            a = 3
        elif (prod_full_4):
            a = 4
        elif (prod_full_5):
            a = 5
        elif (prod_full_6):
            a = 6
        elif (prod_full_7):
            a = 7
        elif (prod_full_8):
            a = 8
        elif (prod_full_9):
            a = 9
        elif (prod_full_10):
            a = 10
        else:
            a = 0

        if (prod_full_n3):
            b = 3
        elif (prod_full_n4):
            b = 4
        elif (prod_full_n5):
            b = 5
        elif (prod_full_n6):
            b = 6
        elif (prod_full_n7):
            b = 7
        elif (prod_full_n8):
            b = 8
        elif (prod_full_n9):
            b = 9
        elif (prod_full_n10):
            b = 10
        else:
            b = 0

        print('a:', a, 'b:', b, 'available_slot:', b - a)
        return b - a
    except:
        print('Check_available_slots 오류!')

# 화면에 보이는 아이템 3개 모두 확인하는 함수
def three_prod_action_new(account, building, check_num1, check_num2, check_num3, prod_direction_left):
    start_time = time.time()
    time.sleep(0.5)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # 제작 아이템 화면 잘 보이는지 확인
    prod_default_screen(account, building)

    if building == 'normal':
        list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))  # 일반 건물일때
    elif building == 'magic':
        list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))  # 마법공방 건물일때

    list_numb2 = list(list_numb1)
    print(list_numb2)

    for i in range(len(list_numb2)):
        if i == 0:
            prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
            aa = check_item_number(account, 'top')
            a = check_num1 - numb_new_recog_new(prod_pin, account)
            target_numb[aa-1] = a
            # print(target_numb)
        if i == 1:
            prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
            bb = check_item_number(account, 'top')+1
            a = check_num2 - numb_new_recog_new(prod_pin, account)
            target_numb[bb-1] = a
            # print(target_numb)
        if i == 2:
            prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
            cc = check_item_number(account, 'bot')
            a = check_num3 - numb_new_recog_new(prod_pin, account)
            target_numb[cc-1] = a
            # print(target_numb)

# 화면에 보이는 아이템 3개 중 마지막(3번째) 아이템 확인하는 함수
def three_prod_action_last_one(account, building, check_num1, prod_direction_left):
    start_time = time.time()
    time.sleep(0.5)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # 제작 아이템 화면 잘 보이는지 확인
    prod_default_screen(account, building)

    if building == 'normal':
        list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 460))  # 일반 건물일때
    elif building == 'magic':
        list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 460))  # 마법공방 건물일때

    list_numb2 = list(list_numb1)
    print('list_numb = %s'%list_numb2)

    prod_pin = (list_numb2[0][0] + 5, list_numb2[0][1] + 7)
    aa = check_item_number(account, 'bot')
    a = check_num1 - numb_new_recog_new(prod_pin, account)
    target_numb[aa-1] = a
    # print(target_numb)
    
            
# 생산 제일 많이 해야하는 아이템 클릭하는 함수
def click_item(account,index):

    index = (index) % 4
    print('함수 안의 index:', index)

    click_al = pag.locateCenterOnScreen('prod_click_al.PNG', confidence=0.9, region=(690 + (account//2)*960, 160 + 153*(index) + (account%2)*540, 175, 153))

    if not (click_al):    # 초록바탕의 제작 버튼이 보이는가?
        print('click_al이 없어요. y값:', 160 + 153*(index) + (account%2)*540)
        return False
    if (index) == 0: # 첫번째 줄 클릭
        print('현재 화면의 1번째 아이템 클릭')
    elif (index) == 1: # 두번째 줄 클릭
        print('현재 화면의 2번째 아이템 클릭')
    elif (index) == 2: # 세번째 줄 클릭
        print('현재 화면의 3번째 아이템 클릭')
    else:
        print('화면에 아이템이 안보여요!')
        return False
    click_al = (click_al.x + 112, click_al.y)
    pag.moveTo(click_al)
    time.sleep(0.4)
    pag.mouseDown()
    time.sleep(0.5)
    pag.mouseUp()
    time.sleep(0.8)



# ======================================================================================================================================================================

wood_min_C = 1800
wood_max_C = 2200
wood_prod_C = 2

jelbean_min_C = 2000
jelbean_max_C = 2200
jelbean_prod_C = 2

sugar_min_C = 2000
sugar_max_C = 2200
sugar_prod_C = 2

biscuit_min_C = -1
biscuit_max_C = 2200
biscuit_prod_C = 2

berry_min_C = -1
berry_max_C = 2500
berry_prod_C = 2

milk_min_C = -1
milk_max_C = 2500
milk_prod_C = 1

cotton_min_C = -1
cotton_max_C = 2500
cotton_prod_C = 1

smith_num_C = 2  # 대장간 건물 수
smith_lev1_C = 250  # 도끼
smith_lev2_C = 250  # 곡괭이
smith_lev3_C = 250  # 톱
smith_lev4_C = 250  # 삽
smith_lev5_C = 200  # 말뚝
smith_lev6_C = 200  # 집게
smith_lev7_C = 200  # 망치

jelly_num_C = 2  # 젤리쨈 건물 수
jelly_lev1_C = 220  # 젤리빈
jelly_lev2_C = 220  # 스윗젤리 잼
jelly_lev3_C = 220  # 달고나 잼
jelly_lev4_C = 220  # 석류 잼
jelly_lev5_C = 0  # 톡톡베리 잼

rollc_num_C = 2  # 롤케이크 건물 수
rollc_lev1_C = 220  # 솔방울새 인형
rollc_lev2_C = 220  # 도토리 램프
rollc_lev3_C = 220  # 뻐꾹뻐꾹 시계
rollc_lev4_C = 350  # 백조깃털 드림캐처

bread_num_C = 2  # 빵집 건물 수
bread_lev1_C = 220  # 든든한 호밀빵
bread_lev2_C = 220  # 달콤쫀득 잼파이
bread_lev3_C = 220  # 은행 포카치아
bread_lev4_C = 250  # 슈가코팅 도넛
bread_lev5_C = 250  # 폭신 카스테라
bread_lev6_C = 0  # 골드리치 크로와상

jampy_num_C = 2  # 잼파이 건물 수
jampy_lev1_C = 90  # 따끈따끈 젤리스튜
jampy_lev2_C = 100  # 곰젤리 버거
jampy_lev3_C = 100  # 캔디크림 파스타
jampy_lev4_C = 100  # 폭신폭신 오므라이스
jampy_lev5_C = 200  # 콤비네이션 피자젤리
jampy_lev6_C = 0  # 고급스러운 젤리빈 정식

doye_num_C = 2  # 토닥토닥 도예공방 건물 수
doye_lev1_C = 250  # 비스킷 화분
doye_lev2_C = 250  # 반짝반짝 유리판
doye_lev3_C = 250  # 반짝이는 색동구슬
doye_lev4_C = 300  # 무지갯빛 디저트 보울

flower_num_C = 2  # 꽃가게 건물 수
flower_lev1_C = 90  # 캔디꽃
flower_lev2_C = 60  # 행복한 꽃화분
flower_lev3_C = 50  # 캔디꽃다발
flower_lev4_C = 50  # 롤리팝 꽃바구니
flower_lev5_C = 20  # 유리꽃 부케
flower_lev6_C = 20  # 찬란한 요거트 화환

milky_num_C = 2  # 우유 가공소 건물 수
milky_lev1_C = 90  # 크림
milky_lev2_C = 90  # 버터
milky_lev3_C = 90  # 수제 치즈

latte_num_C = 2  # 라떼 건물 수
latte_lev1_C = 70  # 젤리빈 라떼
latte_lev2_C = 70  # 몽글몽글 버블티
latte_lev3_C = 70  # 스윗베리 에이드

dolls_num_C = 2  # 러블리 인형공방 건물 수
dolls_lev1_C = 120  # 구름사탕 쿠션
dolls_lev2_C = 120  # 곰젤리 솜인형
dolls_lev3_C = 120  # 용과 드래곤 솜인형

beer_num_C = 2  # 오크통 쉼터 건물 수
beer_lev1_C = 140  # 크림 루트비어
beer_lev2_C = 140  # 레드베리 주스
beer_lev3_C = 140  # 빈티지 와일드 보틀

muffin_num_C = 2  # 퐁 드 파티세리 건물 수
muffin_lev1_C = 110  # 으스스 머핀
muffin_lev2_C = 100  # 생딸기 케이크
muffin_lev3_C = 120  # 파티파티 쉬폰케이크

jewel_num_C = 2  # 살롱 드 쥬얼리 건물 수
jewel_lev1_C = 120  # 글레이즈드 링
jewel_lev2_C = 110  # 루비베리 브로치
jewel_lev3_C = 110  # 로얄 곰젤리 크라운

magic_num_C = 1  # 마법공방
magic_lev1_C = 90  # 고농축 에스프레소
magic_lev2_C = 90  # 울퉁불퉁 뿔고구마
magic_lev3_C = 90  # 향기로운 포도주스
magic_lev4_C = 90  # 칼슘 튼튼 우유
magic_lev5_C = 90  # 까끌까끌 생호밀
magic_lev6_C = 0  # 빨리감기 태엽장치
magic_lev7_C = 0  # 수수께끼의 파우더 주머니
magic_lev8_C = 0  # 수수께끼의 빛나는 파우더 주머니
magic_lev9_C = 0  # 수수께끼의 신비한 파우더 주머니
magic_lev10_C = 0  # 힘의 설탕결정
magic_lev11_C = 0  # 신속의 설탕결정
magic_lev12_C = 0  # 마력의 설탕결정
magic_lev13_C = 0  # 토핑 조각
magic_lev14_C = 0  # 찬란한 빛조각

icecream_num_C = 2  # 아이스크림 트럭 건물 수
icecream_lev1_C = 20  # 낮의 별가루 스프링클 아이스크림
icecream_lev2_C = 30  # 밤의 별가루 스프링클 아이스크림
icecream_lev3_C = 30  # 꿈꾸는 성의 아이스크림 바닐라 샌드
icecream_lev4_C = 30  # 꿈꾸는 성의 아이스크림 초코 샌드
icecream_lev5_C = 30  # 밀키웨이 아이스바

# 기본 생산품
wood_min = wood_min_C
wood_max = wood_max_C
wood_prod = wood_prod_C
jelbean_min = jelbean_min_C
jelbean_max = jelbean_max_C
jelbean_prod = jelbean_prod_C
sugar_min = sugar_min_C
sugar_max = sugar_max_C
sugar_prod = sugar_prod_C
biscuit_min = biscuit_min_C
biscuit_max = biscuit_max_C
biscuit_prod = biscuit_prod_C
berry_min = berry_min_C
berry_max = berry_max_C
berry_prod = berry_prod_C
milk_min = milk_min_C
milk_max = milk_max_C
milk_prod = milk_prod_C
cotton_min = cotton_min_C
cotton_max = cotton_max_C
cotton_prod = cotton_prod_C

smith_lev1 = smith_lev1_C  # 도끼
smith_lev2 = smith_lev2_C  # 곡괭이
smith_lev3 = smith_lev3_C  # 톱
smith_lev4 = smith_lev4_C  # 삽
smith_lev5 = smith_lev5_C  # 말뚝
smith_lev6 = smith_lev6_C  # 집게
smith_lev7 = smith_lev7_C  # 망치
jelly_lev1 = jelly_lev1_C  # 젤리빈
jelly_lev2 = jelly_lev2_C  # 스윗젤리 잼
jelly_lev3 = jelly_lev3_C  # 달고나 잼
jelly_lev4 = jelly_lev4_C  # 석류 잼
jelly_lev5 = jelly_lev5_C  # 톡톡베리 잼
rollc_lev1 = rollc_lev1_C  # 솔방울새 인형
rollc_lev2 = rollc_lev2_C  # 도토리 램프
rollc_lev3 = rollc_lev3_C  # 뻐꾹뻐꾹 시계
rollc_lev4 = rollc_lev4_C  # 백조깃털 드림캐처
bread_lev1 = bread_lev1_C  # 든든한 호밀빵
bread_lev2 = bread_lev2_C  # 달콤쫀득 잼파이
bread_lev3 = bread_lev3_C  # 은행 포카치아
bread_lev4 = bread_lev4_C  # 슈가코팅 도넛
bread_lev5 = bread_lev5_C  # 폭신 카스테라
bread_lev6 = bread_lev6_C  # 골드리치 크로와상
jampy_lev1 = jampy_lev1_C  # 따끈따끈 젤리스튜
jampy_lev2 = jampy_lev2_C  # 곰젤리 버거
jampy_lev3 = jampy_lev3_C  # 캔디크림 파스타
jampy_lev4 = jampy_lev4_C  # 폭신폭신 오므라이스
jampy_lev5 = jampy_lev5_C  # 콤비네이션 피자젤리
jampy_lev6 = jampy_lev6_C  # 고급스러운 젤리빈 정식
doye_lev1 = doye_lev1_C  # 비스킷 화분
doye_lev2 = doye_lev2_C  # 반짝반짝 유리판
doye_lev3 = doye_lev3_C  # 반짝이는 색동구슬
doye_lev4 = doye_lev4_C  # 무지갯빛 디저트 보울
flower_lev1 = flower_lev1_C  # 캔디꽃
flower_lev2 = flower_lev2_C  # 행복한 꽃화분
flower_lev3 = flower_lev3_C  # 캔디꽃다발
flower_lev4 = flower_lev4_C  # 롤리팝 꽃바구니
flower_lev5 = flower_lev5_C  # 유리꽃 부케
flower_lev6 = flower_lev6_C  # 찬란한 요거트 화환
milky_lev1 = milky_lev1_C  # 크림
milky_lev2 = milky_lev2_C  # 버터
milky_lev3 = milky_lev3_C  # 수제 치즈
latte_lev1 = latte_lev1_C  # 젤리빈 라떼
latte_lev2 = latte_lev2_C  # 몽글몽글 버블티
latte_lev3 = latte_lev3_C  # 스윗베리 에이드
dolls_lev1 = dolls_lev1_C  # 구름사탕 쿠션
dolls_lev2 = dolls_lev2_C  # 곰젤리 솜인형
dolls_lev3 = dolls_lev3_C  # 용과 드래곤 솜인형
beer_lev1 = beer_lev1_C  # 크림 루트비어
beer_lev2 = beer_lev2_C  # 레드베리 주스
beer_lev3 = beer_lev3_C  # 빈티지 와일드 보틀
muffin_lev1 = muffin_lev1_C  # 으스스 머핀
muffin_lev2 = muffin_lev2_C  # 생딸기 케이크
muffin_lev3 = muffin_lev3_C  # 파티파티 쉬폰케이크
jewel_lev1 = jewel_lev1_C  # 글레이즈드 링
jewel_lev2 = jewel_lev2_C  # 루비베리 브로치
jewel_lev3 = jewel_lev3_C  # 로얄 곰젤리 크라운
magic_lev1 = magic_lev1_C  # 고농축 에스프레소
magic_lev2 = magic_lev2_C  # 울퉁불퉁 뿔고구마
magic_lev3 = magic_lev3_C  # 향기로운 포도주스
magic_lev4 = magic_lev4_C  # 빨리감기 태엽장치
magic_lev5 = magic_lev5_C  # 수수께끼의 파우더 주머니
magic_lev6 = magic_lev6_C  # 수수께끼의 빛나는 파우더 주머니
magic_lev7 = magic_lev7_C  # 수수께끼의 신비한 파우더 주머니

icecream_lev1 = icecream_lev1_C
icecream_lev2 = icecream_lev2_C
icecream_lev3 = icecream_lev3_C
icecream_lev4 = icecream_lev4_C
icecream_lev5 = icecream_lev5_C
icecream_num = icecream_num_C

smith_num = smith_num_C  # 대장간 건물 수
jelly_num = jelly_num_C  # 젤리쨈 건물 수
rollc_num = rollc_num_C  # 롤케이크 건물 수
bread_num = bread_num_C  # 빵집 건물 수
jampy_num = jampy_num_C  # 잼파이 건물 수
doye_num = doye_num_C  # 토닥토닥 도예공방 건물 수
flower_num = flower_num_C  # 꽃가게 건물 수
milky_num = milky_num_C  # 우유 가공소 건물 수
latte_num = latte_num_C  # 라떼 건물 수
dolls_num = dolls_num_C  # 러블리 인형공방 건물 수
beer_num = beer_num_C  # 오크통 쉼터 건물 수
muffin_num = muffin_num_C  # 퐁 드 파티세리 건물 수
jewel_num = jewel_num_C  # 살롱 드 쥬얼리 건물 수
magic_num = magic_num_C  # 마법공방



bjellycompleted = False
bsmithcompleted = False
bProdHigh = True  # 동일 건물 2개인 경우 2번째 건물에서 높은 생산품 우선 생산
bSecond = False  # 두 번째 건물 작업이냐?
prod_direction_left = True
prod_pix_confirm = 2  # 픽셀 못읽는거 n번(스크롤업 n*2 번) 해도 안되면 좌로 넘김



# 여기부터 아이템 확인 시작!
account = 0

# z = check_item_number(account)
# print(z)

# screen = ImageGrab.grab()
# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# pix_smith = (163, 118, 85)  # 도끼 스미스
# pix_jelly = (15, 174, 202)  # 젤리빈 잼 젤리
# cycle_check = 0
cycle_check = 0
pix_error_count = 0

# try:
while True:
    target_numb = [0, 0, 0, 0, 0, 0, 0]
    
    screen = ImageGrab.grab()
    pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
    pix_wood = (117, 59, 40)  # 나무
    pix_jelbean = (4, 239, 237)  # 젤리빈
    pix_sugar = (255, 255, 255)  # 설탕
    pix_biscuit = (205, 132, 63)  # 비스킷
    pix_berry = (187, 40, 44)  # 젤리베리
    pix_milk = (236, 241, 241)  # 우유
    pix_cotton = (255, 247, 255)  # 솜
    pix_smith = (163, 118, 85)  # 도끼 스미스
    pix_jelly = (15, 174, 202)  # 젤리빈 잼 젤리
    pix_rollc = (214, 146, 105)  # 솔새 롤케
    pix_bread = (142, 66, 8)  # 호밀빵 브레드
    pix_jampy = (168, 29, 42)  # 젤리스튜 잼파이
    pix_doye = (157, 84, 43)  # 비스킷 화분 - 도예
    pix_flower = (255, 30, 130)  # 캔디꽃 - flower
    pix_milky = (213, 229, 234)  # 크림 - milky
    pix_latte = (255, 251, 238)  # 젤리빈 라떼 - latte
    pix_dolls = (109, 235, 249)  # 쿠션 - dolls
    pix_beer = (153, 103, 67)  # 크림루트비어 - beer
    pix_muffin = (190, 92, 59)  # 머핀 - muffin
    pix_jewel = (143, 99, 63)  # 글레이즈드링 - jewel
    pix_magic = (93, 55, 48)  # 마법공방 - magic
    pix_icecream = (254, 253, 229)  # 디즈니 아이스크림 트럭

#smith 잠시 비활성화
    # if pix_prod == pix_smith:
    #     print('smith!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or smith_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (smith_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', smith_lev1, smith_lev2, smith_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', smith_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', smith_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', smith_lev6, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 elif (item_number == 5):
    #                     three_prod_action_last_one(account, 'normal', smith_lev7, prod_direction_left)
    #
    #                     if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
    #                         print('7렙까지 만들어요')
    #                         to_make = 7
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp)+1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp)+1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and smith_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (smith_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', smith_lev1, smith_lev2, smith_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', smith_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', smith_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', smith_lev6, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 elif (item_number == 5):
    #                     three_prod_action_last_one(account, 'normal', smith_lev7, prod_direction_left)
    #
    #                     if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
    #                         print('7렙까지 만들어요')
    #                         to_make = 7
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    # elif pix_prod == pix_jelly:
    #     print('jelly!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or jelly_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (jelly_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', jelly_lev1, jelly_lev2, jelly_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', jelly_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', jelly_lev4, prod_direction_left)
    #
    #                     if jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('jelly, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and jelly_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (jelly_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', jelly_lev1, jelly_lev2, jelly_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', jelly_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', jelly_lev4, prod_direction_left)
    #
    #                     if jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('jelly, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    # elif pix_prod == pix_rollc:
    #     print('rollc!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or rollc_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (rollc_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', rollc_lev1, rollc_lev2, rollc_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', rollc_lev4, prod_direction_left)
    #
    #                     if rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         print('3렙까지 만들어요')
    #                         to_make = 3
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('rollc, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and rollc_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (rollc_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', rollc_lev1, rollc_lev2, rollc_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', rollc_lev4, prod_direction_left)
    #
    #                     if rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         print('3렙까지 만들어요')
    #                         to_make = 3
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp)+1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('rollc, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    #
    # elif pix_prod == pix_magic:
    #     print('magic!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or magic_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (magic_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', magic_lev1, magic_lev2, magic_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', magic_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', magic_lev4, prod_direction_left)
    #
    #                     if magic_lev5 and magic_lev4 and magic_lev3 and magic_lev2 and magic_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not magic_lev5 and magic_lev4 and magic_lev3 and magic_lev2 and magic_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('magic, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and magic_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (magic_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', magic_lev1, magic_lev2, magic_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', magic_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', magic_lev4, prod_direction_left)
    #
    #                     if magic_lev5 and magic_lev4 and magic_lev3 and magic_lev2 and magic_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not magic_lev5 and magic_lev4 and magic_lev3 and magic_lev2 and magic_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('magic, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break


    if pix_prod == pix_icecream:
        print('icecream!')
        pix_error_count = 0
        z = Check_available_slots(account)
        if z <= 1:
            # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            print('리스트 full!3')
            time.sleep(0.5)
            Skip_Next(account, prod_direction_left)
            continue

        # while True:
        #     if keyboard.is_pressed('end'):
        #         break

        if not bProdHigh or icecream_num == 1:
            # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
            if not (icecream_lev1 == 0):
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    item_number = check_item_number(account, 'top')
                    print('item_number = %d' % item_number, ', target_numb = ', target_numb)
                    if (item_number == 1):
                        three_prod_action_new(account, 'normal', icecream_lev1, icecream_lev2, icecream_lev3, prod_direction_left)
                        Updown(account, 'up1')
                        time.sleep(0.5)
                    if (item_number == 2):
                        three_prod_action_last_one(account, 'normal', icecream_lev4, prod_direction_left)
                        Updown(account, 'up1')
                        time.sleep(0.5)
                    if (item_number == 3):
                        three_prod_action_last_one(account, 'normal', icecream_lev4, prod_direction_left)

                        if icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
                            print('5렙까지 만들어요')
                            to_make = 5
                            print(target_numb[0:to_make])
                            tmp = max(target_numb[0:to_make])
                            index = target_numb[0:to_make].index(tmp) + 1
                            print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))

                            if item_number + 2 >= index >= item_number:
                                click_item(account, index - item_number)
                            elif index < item_number:
                                print(item_number - index, '칸 올려요')
                                for i in range(item_number - index):
                                    Updown(account, 'down1')
                                    time.sleep(0.5)
                                item_number = item_number - (item_number - index)
                                click_item(account, index - item_number)
                            else:
                                print('조건이 이상해요1')
                        elif not icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
                            print('4렙까지 만들어요')
                            to_make = 4
                            print(target_numb[0:to_make])
                            tmp = max(target_numb[0:to_make])
                            index = target_numb[0:to_make].index(tmp) + 1
                            print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))

                            if item_number + 2 >= index >= item_number:
                                click_item(account, index - item_number)
                            elif index < item_number:
                                print(item_number - index, '칸 올려요')
                                for i in range(item_number - index):
                                    Updown(account, 'down1')
                                    time.sleep(0.5)
                                item_number = item_number - (item_number - index)
                                click_item(account, index - item_number)
                            else:
                                print('조건이 이상해요2')
                        else:
                            print('icecream, 5렙까지도 아니고 4렙까지도 아니다!')

                        Skip_Next(account, prod_direction_left)
                        break
            break
        if bProdHigh and icecream_num == 2:  # 첫 번째 건물 작업
            # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
            if not (icecream_lev1 == 0):
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    item_number = check_item_number(account, 'top')
                    print('item_number = %d'%item_number, ', target_numb = ', target_numb)
                    if (item_number == 1):
                        three_prod_action_new(account, 'normal', icecream_lev1, icecream_lev2, icecream_lev3, prod_direction_left)
                        Updown(account, 'up1')
                        time.sleep(0.5)
                    if (item_number == 2):
                        three_prod_action_last_one(account, 'normal', icecream_lev4, prod_direction_left)
                        Updown(account, 'up1')
                        time.sleep(0.5)
                    if (item_number == 3):
                        three_prod_action_last_one(account, 'normal', icecream_lev4, prod_direction_left)

                        if icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
                            print('5렙까지 만들어요')
                            to_make = 5
                            print(target_numb[0:to_make])
                            tmp = max(target_numb[0:to_make])
                            index = target_numb[0:to_make].index(tmp) + 1
                            print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))

                            if item_number + 2 >= index >= item_number:
                                click_item(account, index - item_number)
                            elif index < item_number:
                                print(item_number - index, '칸 올려요')
                                for i in range(item_number - index):
                                    Updown(account, 'down1')
                                    time.sleep(0.5)
                                item_number = item_number - (item_number - index)
                                click_item(account, index - item_number)
                            else:
                                print('조건이 이상해요1')
                        elif not icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
                            print('4렙까지 만들어요')
                            to_make = 4
                            print(target_numb[0:to_make])
                            tmp = max(target_numb[0:to_make])
                            index = target_numb[0:to_make].index(tmp) + 1
                            print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))

                            if item_number + 2 >= index >= item_number:
                                click_item(account, index - item_number)
                            elif index < item_number:
                                print(item_number - index, '칸 올려요')
                                for i in range(item_number - index):
                                    Updown(account, 'down1')
                                    time.sleep(0.5)
                                item_number = item_number - (item_number - index)
                                click_item(account, index - item_number)
                            else:
                                print('조건이 이상해요2')
                        else:
                            print('icecream, 5렙까지도 아니고 4렙까지도 아니다!')

                        Skip_Next(account, prod_direction_left)
                        break


    # elif pix_prod == pix_doye:
    #     print('doye!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or doye_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (doye_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', doye_lev1, doye_lev2, doye_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', doye_lev4, prod_direction_left)
    #
    #                     if doye_lev4 and doye_lev3 and doye_lev2 and doye_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not doye_lev4 and doye_lev3 and doye_lev2 and doye_lev1:
    #                         print('3렙까지 만들어요')
    #                         to_make = 3
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('doye, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and doye_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (doye_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', doye_lev1, doye_lev2, doye_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', doye_lev4, prod_direction_left)
    #
    #                     if doye_lev4 and doye_lev3 and doye_lev2 and doye_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not doye_lev4 and doye_lev3 and doye_lev2 and doye_lev1:
    #                         print('3렙까지 만들어요')
    #                         to_make = 3
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp)+1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('doye, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
                        
    # elif pix_prod == pix_bread:
    #     print('bread!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or bread_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (bread_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', bread_lev1, bread_lev2, bread_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', bread_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', bread_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', bread_lev6, prod_direction_left)
    #
    #                     if bread_lev6 and bread_lev5 and bread_lev4 and bread_lev3 and bread_lev2 and bread_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number+2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not bread_lev6 and bread_lev5 and bread_lev4 and bread_lev3 and bread_lev2 and bread_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('bread, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and bread_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (bread_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', bread_lev1, bread_lev2, bread_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', bread_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', bread_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', bread_lev6, prod_direction_left)
    #                     if bread_lev6 and bread_lev5 and bread_lev4 and bread_lev3 and bread_lev2 and bread_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요3')
    #                     elif not bread_lev6 and bread_lev5 and bread_lev4 and bread_lev3 and bread_lev2 and bread_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('bread, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    # elif pix_prod == pix_jampy:
    #     print('jampy!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or jampy_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (jampy_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', jampy_lev1, jampy_lev2, jampy_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev6, prod_direction_left)
    #
    #                     if jampy_lev6 and jampy_lev5 and jampy_lev4 and jampy_lev3 and jampy_lev2 and jampy_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number+2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not jampy_lev6 and jampy_lev5 and jampy_lev4 and jampy_lev3 and jampy_lev2 and jampy_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('jampy, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and jampy_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (jampy_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', jampy_lev1, jampy_lev2, jampy_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', jampy_lev6, prod_direction_left)
    #                     if jampy_lev6 and jampy_lev5 and jampy_lev4 and jampy_lev3 and jampy_lev2 and jampy_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요3')
    #                     elif not jampy_lev6 and jampy_lev5 and jampy_lev4 and jampy_lev3 and jampy_lev2 and jampy_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('jampy, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    # elif pix_prod == pix_flower:
    #     print('flower!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     # while True:
    #     #     if keyboard.is_pressed('end'):
    #     #         break
    #
    #     if not bProdHigh or flower_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (flower_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', flower_lev1, flower_lev2, flower_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', flower_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', flower_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', flower_lev6, prod_direction_left)
    #
    #                     if flower_lev6 and flower_lev5 and flower_lev4 and flower_lev3 and flower_lev2 and flower_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number+2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not flower_lev6 and flower_lev5 and flower_lev4 and flower_lev3 and flower_lev2 and flower_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('flower, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #         break
    #     if bProdHigh and flower_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (flower_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', flower_lev1, flower_lev2, flower_lev3, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', flower_lev4, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', flower_lev5, prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', flower_lev6, prod_direction_left)
    #                     if flower_lev6 and flower_lev5 and flower_lev4 and flower_lev3 and flower_lev2 and flower_lev1:
    #                         print('6렙까지 만들어요')
    #                         to_make = 6
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요3')
    #                     elif not flower_lev6 and flower_lev5 and flower_lev4 and flower_lev3 and flower_lev2 and flower_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index-item_number)
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('flower, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
                        
    else:
        print('건물 안에서... 이게 아니라면... 내려!')
        pix_error_count = pix_error_count + 1
        if prod_pix_confirm >= pix_error_count:
            print('건물 안에서... 픽셀값 찾게 위로 올림')
            pag.moveTo(610 + (account // 2) * 960, random.randint(140, 160) + (account % 2) * 540)
            time.sleep(0.1)
            pag.mouseDown()
            time.sleep(0.1)
            pag.moveTo(610 + (account // 2) * 960, 160 + 350 + (account % 2) * 540, 0.3)
            pag.mouseUp()
            time.sleep(2)
        else:
            print('건물 안에서... 이게 아니라면... 끝내!')
            break
            Skip_Next(account, prod_direction_left)
# except:
#     print('eeeeerror!')