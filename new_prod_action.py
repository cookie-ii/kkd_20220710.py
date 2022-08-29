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

def numb_new_recog(prod_pin, line, account):
    its_number = 0
    how_many_nums = 0
    pos_numb = 0  # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
    num_list = list()
    # print('라인 %s번 진행합니다!' % (line))
    screen = ImageGrab.grab()
    # 3렙 건물인 경우 무조건 prod_pin = (612,95)
    # print('?', prod_pin[0]+19,prod_pin[1]+81+153*(line-1))
    pix_jaritsu1_1 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
    # print((prod_pin[0] + 19 , prod_pin[1] + 81 + 153 * (line - 1)))
    # print('pix_자릿수1_1:', pix_jaritsu1_1)
    pix_jaritsu1_2 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 87 + 153 * (line - 1)))  # 하
    # print((prod_pin[0] + 19 , prod_pin[1] + 87 + 153 * (line - 1)))
    # print('pix_자릿수1_2:', pix_jaritsu1_2)


    if ((pix_jaritsu1_1) == (255, 255, 255)) and ((pix_jaritsu1_2) == (255, 255, 255)):
        pix_zero_1 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 82 + 153 * (line - 1)))  # 상
        # print((prod_pin[0] + 24 , prod_pin[1] + 82 + 153 * (line - 1)))
        # print('pix_zero_1:', pix_zero_1)
        pix_zero_2 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 85 + 153 * (line - 1)))  # 하
        # print((prod_pin[0] + 24 , prod_pin[1] + 85 + 153 * (line - 1)))
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
        pix_jaritsu2_1 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
        # print((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))
        # print('pix_자릿수2_1:', pix_jaritsu2_1)
        pix_jaritsu2_2 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 하
        # print((prod_pin[0] + 14, prod_pin[1] + 81 + 153 * (line - 1)))
        # print('pix_자릿수2_2:', pix_jaritsu2_2)
        if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
            # print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            # print('이 숫자는 세 자릿 수 입니다!')
            pos_numb = 3
    # print('자릿수 다시 확인', pos_numb)
    if pos_numb == 1:
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        # print('한 자릿 수 범위 확인1', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1))
        if (num_1):
            return 1
        num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_1_1):
            return 1
        num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_2):
            return 2
        num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_3):
            return 3
        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_3_1):
            return 3
        num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_4):
            return 4
        num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_4_2):
            return 4
        num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_5):
            return 5
        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_6):
            return 6
        num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_7):
            return 7
        num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_8):
            return 8
        num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_8_1):
            return 8
        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_9):
            return 9
        num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
        if (num_9_1):
            return 9
        return 0

    if pos_numb == 2:
        # 10의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
        # print('두 자릿 수 10자리 범위', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                print('십의 자리 숫자 확인 에러!!')
        # 1의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
        # print('두자릿수 1자리 범위:', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                print('일의 자리 숫자 확인 에러!!')
        # print('현재 재고는 =', its_number)
        return its_number
    if pos_numb == 3:
        # print('세 자릿 수 범위 확인', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14)
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 900
                                                            else:
                                                                print('백의 자리 숫자 확인 에러!!')
        # 10의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                                if (num_0):
                                                                    print('십의 자리 0!!')
                                                                else:
                                                                    print('10의 자리 못읽음..')
        # 1의 자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
                                                                if (num_0):
                                                                    print('1의 자리 0!!')
                                                                else:
                                                                    print('1의 자리 못읽음..')
        # print('현재 재고는 =', its_number)
        return its_number

# prod_pin 기준으로 1자리, 2자리, 3자리 숫자 읽어오는 함수
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
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        # print('한 자릿 수 범위 확인1', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7)
        if (num_1):
            return 1
        num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_1_1):
            return 1
        num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_2):
            return 2
        num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_3):
            return 3
        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_3_1):
            return 3
        num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_4):
            return 4
        num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_4_2):
            return 4
        num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_5):
            return 5
        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_6):
            return 6
        num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_7):
            return 7
        num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_8):
            return 8
        num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_8_1):
            return 8
        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_9):
            return 9
        num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14))
        if (num_9_1):
            return 9
        return 0

    if pos_numb == 2:
        # 10의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
        # print('두 자릿 수 10자리 범위', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7)
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 11, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                print('십의 자리 숫자 확인 에러!!')
        # 1의자리 숫자 걍검색
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
        # print('두자릿수 1자리 범위:', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7)
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                print('일의 자리 숫자 확인 에러!!')
        # print('현재 재고는 =', its_number)
        return its_number
    if pos_numb == 3:
        # print('세 자릿 수 범위 확인', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7, pos_numb * 5 * 2, 14)
        # pag.screenshot('ire_number_check100.PNG', region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        # 100의 자리
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 100
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 100
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 200
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 300
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 300
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 400
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 400
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 500
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 600
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 700
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 800
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 800
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 900
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 900
                                                            else:
                                                                print('백의 자리 숫자 확인 에러!!')
        # 10의 자리 숫자 걍검색
        # pag.screenshot('ire_number_check10.PNG', region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 10
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 10
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 20
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 30
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 30
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 40
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 40
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 50
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 60
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 70
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 80
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 80
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 90
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 90
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.85, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                                if (num_0):
                                                                    print('십의 자리 0!!')
                                                                else:
                                                                    print('10의 자리 못읽음..')
        # 1의 자리 숫자 걍검색
        # pag.screenshot('ire_number_check1.PNG', region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
        if (num_1):
            its_number = its_number + 1
        else:
            num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
            if (num_1_1):
                its_number = its_number + 1
            else:
                num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                if (num_2):
                    its_number = its_number + 2
                else:
                    num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                    if (num_3):
                        its_number = its_number + 3
                    else:
                        num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                        if (num_3_1):
                            its_number = its_number + 3
                        else:
                            num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                            if (num_4):
                                its_number = its_number + 4
                            else:
                                num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                if (num_4_2):
                                    its_number = its_number + 4
                                else:
                                    num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                    if (num_5):
                                        its_number = its_number + 5
                                    else:
                                        num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                        if (num_6):
                                            its_number = its_number + 6
                                        else:
                                            num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                            if (num_7):
                                                its_number = its_number + 7
                                            else:
                                                num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                if (num_8):
                                                    its_number = its_number + 8
                                                else:
                                                    num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                    if (num_8_1):
                                                        its_number = its_number + 8
                                                    else:
                                                        num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                        if (num_9):
                                                            its_number = its_number + 9
                                                        else:
                                                            num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                            if (num_9_1):
                                                                its_number = its_number + 9
                                                            else:
                                                                num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.85, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7, 10, 14))
                                                                if (num_0):
                                                                    print('1의 자리 0!!')
                                                                else:
                                                                    print('1의 자리 못읽음..')
        # print('현재 재고는 =', its_number)
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
        # # send_telegram_message('Updown에서 에러가 났어요!')
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
        # # send_telegram_message('Updown에서 에러가 났어요!')
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
    elif smith_lev4 or jelly_lev4 or rollc_lev4 or bread_lev4 or jampy_lev4 or doye_lev4 or flower_lev4 or icecream_lev4 or magic_lev4:
        # print('4번째 아이템')
        return 4
    elif smith_lev3 or jelly_lev3 or rollc_lev3 or bread_lev3 or jampy_lev3 or doye_lev3 or flower_lev3 or icecream_lev3 or magic_lev3:
        # print('3번째 아이템')
        return 3
    elif smith_lev2 or jelly_lev2 or rollc_lev2 or bread_lev2 or jampy_lev2 or doye_lev2 or flower_lev2 or icecream_lev2 or magic_lev2:
        # print('2번째 아이템')
        return 2
    elif smith_lev1 or jelly_lev1 or rollc_lev1 or bread_lev1 or jampy_lev1 or doye_lev1 or flower_lev1 or icecream_lev1 or magic_lev1:
        # print('smith', smith_lev1, 'jelly', jelly_lev1, 'rollc', rollc_lev1, 'bread', bread_lev1, 'jampy', jampy_lev1, 'doye', doye_lev1, 'flower', flower_lev1, 'icecream', icecream_lev1, 'magic', magic_lev1)
        # print('1번째 아이템')
        return 1
    else:
        print('몇번째 아이템인지 못읽었어, 화면 올립니다')
        Updown(account, 'down1')
        return False

# 생산건물 안에서 화면 조정
def prod_default_screen(account, building):
    start_time = time.time()
    while True:
        if keyboard.is_pressed('end'):
            break
        now_time = time.time()
        # time.sleep(1)
        # if building == 'normal':
        #     list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
        # elif building == 'magic':
        #     list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 마법공방 건물일때

        # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
        list_numb2 = list(list_numb1)
        # print(list_numb2)

        if not list_numb2:
            print('안보여!')
            Updown(account, 'down1')
            break
        if 75 <= list_numb2[0][1] - (account % 2) * 540 <= 100:
            # print('적당한 위치구먼!')
            break
        elif 101 <= list_numb2[0][1] - (account % 2) * 540 <= 235:

            a = int(list_numb2[0][1]) + (account % 2) * 540 - 88
            print('화면 미세 조정!: %s'%(a))
            Updown_new(account, 'up_little', a)
        # elif 103 <= list_numb2[0][1] - (account % 2) * 540 <= 235:
        #     print('윗쪽으로 올립시다')
        #     a = 153 + 90 - int(list_numb2[0][1]) + (account % 2) * 540
        #     print(a)
        #     Updown_new(account, 'down_little', a)


            #
            # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
            # list_numb2 = list(list_numb1)
            # print(list_numb2)
        # if 75 <= list_numb2[0][1] - (account % 2) * 540 <= 75 + 20:
        #     # print('첫 y값이 75+20 ~ 75사이', list_numb2[0][1] - (account % 2) * 540)
        #     break
        # elif 75 >= list_numb2[0][1] - (account % 2) * 540:
        #     print('조금.. 올리나?', int(list_numb2[0][1]))
        #     a = int(list_numb2[0][1]) - 88
        #     # print(a)
        #     Updown_new(account, 'down_little', a)
        # elif list_numb2[0][1] - (account % 2) * 540 >= 75 + 20:
        #     print('조금.. 내리나?', int(list_numb2[0][1]))
        #     a = int(list_numb2[0][1]) - 88      # 위에가 살짝 가렸을 때가 문제구먼... 어케하지?
        #     # print(a)
        #     Updown_new(account, 'down_little', a)
        # else:
        #     print('prod_default_screen 오류예요!')
        #     print(list_numb2)
        #     break

def Check_available_slots(account):
    try:
        pag.click(x=random.randint(243, 422) + (account // 2) * 960, y=random.randint(336, 398) + (account % 2) * 540)
        time.sleep(0.5)

        prod_full_1 = pag.locateCenterOnScreen('prod_full_1.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_2 = pag.locateCenterOnScreen('prod_full_2.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_3 = pag.locateCenterOnScreen('prod_full_3.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_4 = pag.locateCenterOnScreen('prod_full_4.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_5 = pag.locateCenterOnScreen('prod_full_5.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_6 = pag.locateCenterOnScreen('prod_full_6.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_7 = pag.locateCenterOnScreen('prod_full_7.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_8 = pag.locateCenterOnScreen('prod_full_8.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_9 = pag.locateCenterOnScreen('prod_full_9.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))
        prod_full_10 = pag.locateCenterOnScreen('prod_full_10.PNG', grayscale=True, confidence=0.9, region=(60 + (account // 2) * 960, 60 + (account % 2) * 540, 25, 22))

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


def three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left):
    start_time = time.time()
    time.sleep(0.5)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # # 풀리스트인 경우 넘어감
    z = Check_available_slots(account)
    if z == 0:
        print('리스트 full!4')
        Skip_Next(account, prod_direction_left)
        return True

    # 3렙건물이니 고정
    prod_pin = (612+(account//2)*960, 95 + (account % 2) * 540)

    target_numb1 = check_num1 - numb_new_recog(prod_pin, 1, account)

    target_numb2 = check_num2 - numb_new_recog(prod_pin, 2, account)

    target_numb3 = check_num3 - numb_new_recog(prod_pin, 3, account)

    # 기타 조건 초기화
    line1_clicked = 0
    line2_clicked = 0
    line3_clicked = 0
    prod_line1_completed = False
    prod_line2_completed = False
    prod_line3_completed = False
    list_numbb1 = 0
    list_numbb2 = 0
    list_numbb3 = 0

    # 리스트를 한번만 읽자!
    if check_num1 != 0:  # 목표값이 있고(열었고)
        if target_numb1 > 0:  # 목표 수량보다 부족한 경우
            list_numb1 = pag.locateAllOnScreen(check_list_img1, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
            list_numb1 = list(list_numb1)
            # print('list_numb1:', list_numb1)
            # print('len(...):', len(list_numb1))
            if len(list_numb1) > 0:
                list_numbb1 = len(list_numb1)  # 현재 리스트에 몇 개 있냐
            else:
                list_numbb1 = 0
    else:
        prod_line1_completed = True
        compare_numb1 = -1
        list_numbb1 = 0

    if check_num2 != 0:  # 목표값이 있고(열었고)
        if target_numb2 > 0:  # 목표 수량보다 부족한 경우
            list_numb2 = pag.locateAllOnScreen(check_list_img2, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
            list_numb2 = list(list_numb2)
            # print('list_numb2:', list_numb2)
            # print('len(...):', len(list_numb2))
            if len(list_numb2) > 0:
                list_numbb2 = len(list_numb2)  # 현재 리스트에 몇 개 있냐
            else:
                list_numbb2 = 0
    else:
        prod_line2_completed = True
        compare_numb2 = -1
        list_numbb2 = 0

    if check_num3 != 0:  # 목표값이 있고(열었고)
        if target_numb3 > 0:  # 목표 수량보다 부족한 경우
            list_numb3 = pag.locateAllOnScreen(check_list_img3, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
            list_numb3 = list(list_numb3)
            # print('list_numb3:', list_numb3)
            # print('len(...):', len(list_numb3))
            if len(list_numb3) > 0:
                list_numbb3 = len(list_numb3)  # 현재 리스트에 몇 개 있냐
            else:
                list_numbb3 = 0
    else:
        prod_line3_completed = True
        compare_numb3 = -1
        list_numbb3 = 0

    print('현재 리스트에는 = 1:%s, 2:%s, 3:%s개 있습니다.' % (target_numb1, target_numb2, target_numb3))
    while True:
        now_time = time.time()
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
        if (cond_network):
            pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
            time.sleep(0.3)

        # # 풀리스트인 경우 넘어감
        z = Check_available_slots(account)
        if z == 0:
            print('리스트 full!5')
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

        # 조건 확인
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        # 구글 플레이 종료 뭐시기
        if (play_halted):
            pag.click(play_halted)

        # 리스트 수량 파악
        if (target_numb1 - list_numbb1 - line1_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
            # print('target_numb1 - list_numbb1 - line1_clicked:', target_numb1 - list_numbb1 - line1_clicked)
            compare_numb1 = (target_numb1 - list_numbb1 - line1_clicked) / check_num1  # 비율(1을 안넘음)
            # print('compare_numb1:', compare_numb1)
        else:
            compare_numb1 = -1
            prod_line1_completed = True

        if (target_numb2 - list_numbb2 - line2_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
            # print('target_numb2 - list_numbb2 - line2_clicked:', target_numb2 - list_numbb2 - line2_clicked)
            compare_numb2 = (target_numb2 - list_numbb2 - line2_clicked) / check_num2  # 비율(1을 안넘음)
            # print('compare_numb2:', compare_numb1)
        else:
            compare_numb2 = -1
            prod_line2_completed = True

        if (target_numb3 - list_numbb3 - line3_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
            # print('target_numb3 - list_numbb3 - line3_clicked:', target_numb3 - list_numbb3 - line3_clicked)
            compare_numb3 = (target_numb3 - list_numbb3 - line3_clicked) / check_num3  # 비율(1을 안넘음)
            # print('compare_numb3:', compare_numb1)
        else:
            compare_numb3 = -1
            prod_line3_completed = True

        if (prod_line1_completed and prod_line2_completed and prod_line3_completed):
            Skip_Next(account, prod_direction_left)
            return False
        else:
            max_numb = max(compare_numb1, compare_numb2, compare_numb3)
            if max_numb == compare_numb1 and not prod_line1_completed:
                pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + (account % 2) * 540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line1_clicked = 999  # 나락으로 보내버력!
                elif (not_opened):  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line1_clicked = 999  # 나락으로 보내버력!
                else:
                    line1_clicked = line1_clicked + 1
            if max_numb == compare_numb2 and not prod_line2_completed:
                pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + 153 + (account % 2) * 540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line2_clicked = 999  # 나락으로 보내버력!
                elif (not_opened):  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line2_clicked = 999  # 나락으로 보내버력!
                else:
                    line2_clicked = line2_clicked + 1
            if max_numb == compare_numb3 and not prod_line3_completed:
                pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + 153 * 2 + (account % 2) * 540)
                lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
                    print('재료가 부족해요')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line3_clicked = 999  # 나락으로 보내버력!
                elif (not_opened):  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.5)
                    line3_clicked = 999  # 나락으로 보내버력!
                else:
                    line3_clicked = line3_clicked + 1

# 화면에 보이는 아이템 3개 모두 확인하는 함수
def three_prod_action_new(account, building, building_name, prod_direction_left):
    try:
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
        # print(list_numb2)

        start_text = building_name + '_'
        mid_text = 'lev'
        # file_type_text = '.png'
        check_num1 = eval(start_text + mid_text + str(1)) #  smith_lev1의 생산량(목표) 가져오기
        check_num2 = eval(start_text + mid_text + str(2)) #  smith_lev2의 생산량(목표) 가져오기
        check_num3 = eval(start_text + mid_text + str(3)) #  smith_lev2의 생산량(목표) 가져오기

        for i in range(len(list_numb2)):
            if i == 0:
                prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
                aa = check_item_number(account, 'top')
                a = check_num1 - numb_new_recog_new(prod_pin, account)  # 생산량(목표)에서 실제 재고 뺀 숫자 a에 저장
                target_numb[aa-1] = a                                   # 타겟넘버(리스트형)에 생산목표숫자 저장! 1렙->0번, 2렙->1번에 저장됨
                # print(target_numb)
            if i == 1:
                prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
                bb = check_item_number(account, 'top')+1
                a = check_num2 - numb_new_recog_new(prod_pin, account)  # 생산량(목표)에서 실제 재고 뺀 숫자 a에 저장
                target_numb[bb-1] = a                                   # 타겟넘버(리스트형)에 생산목표숫자 저장! 1렙->0번, 2렙->1번에 저장됨
                # print(target_numb)
            if i == 2:
                prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
                cc = check_item_number(account, 'bot')
                a = check_num3 - numb_new_recog_new(prod_pin, account)  # 생산량(목표)에서 실제 재고 뺀 숫자 a에 저장
                target_numb[cc-1] = a                                   # 타겟넘버(리스트형)에 생산목표숫자 저장! 1렙->0번, 2렙->1번에 저장됨
                # print(target_numb)
    except:
        print('three_prod_action_new 에러예요!')

# 화면에 보이는 아이템 3개 중 마지막(3번째) 아이템 확인하는 함수
def three_prod_action_last_one(account, building, building_name, prod_direction_left):
    start_time = time.time()
    time.sleep(0.5)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # 제작 아이템 화면 잘 보이는지 확인
    prod_default_screen(account, building)

    if building == 'normal':
        list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 150))  # 일반 건물일때
    elif building == 'magic':
        list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 150))  # 마법공방 건물일때

    list_numb2 = list(list_numb1)
    # print('list_numb = %s'%list_numb2)

    aa = check_item_number(account, 'bot')
    start_text = building_name + '_'
    mid_text = 'lev'
    # file_type_text = '.png'
    check_num1 = eval(start_text + mid_text + str(aa))

    if (list_numb2):
        prod_pin = (list_numb2[0][0] + 5, list_numb2[0][1] + 7)
        a = check_num1 - numb_new_recog_new(prod_pin, account)
        target_numb[aa-1] = a
        # print(target_numb)
    
            
# 생산 제일 많이 해야하는 아이템 클릭하는 함수
def click_item(account,index1):
    global index
    index1 = (index1) % 4
    print('함수 안의 index1:', index1)

    click_al = pag.locateCenterOnScreen('prod_click_al.PNG', confidence=0.9, region=(690 + (account//2)*960, 88 + 153*(index1) + (account%2)*540, 175, 153))
    if not (click_al):    # 초록바탕의 제작 버튼이 보이는가?
        print('click_al이 없어요. y값:', 88 + 153*(index1) + (account%2)*540)
        print('아직 안 연 제품인가봐요')
        target_numb[index - 1] = -999
        print(target_numb)
        return False
    x0 = pag.locateCenterOnScreen('prod_x0.PNG', confidence=0.89, region=(814 + (account // 2) * 960, 177 + ((index1) % 3) * 153 + (account % 2) * 540, 44, 37))
    if (x0):
        print('목표 아이템 제작 불가!')
        target_numb[index - 1] = -999
        print(target_numb)
        return False


    if (index1) == 0: # 첫번째 줄 클릭
        print('현재 화면의 1번째 아이템 클릭')
    elif (index1) == 1: # 두번째 줄 클릭
        print('현재 화면의 2번째 아이템 클릭')
    elif (index1) == 2: # 세번째 줄 클릭
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
    return True

def End_kkd_line(account):
    pag.click(871+(account//2)*960, 18+(account%2)*540)                 # 전체화면으로 바꿔!
    time.sleep(1.5)
    pag.click(1833, 17)          # 다시 원래 크기로 돌려놓고
    time.sleep(1.5)
    pag.hotkey('alt', 'up')      # 크기, 위치 맞춰놓자!
    time.sleep(1.5)
    pag.click(942+(account//2)*960, 522+(account%2)*540)     # 켜진 창 다 띄워서?
    time.sleep(1.5)
    pag.click(680+(account//2)*960, 82+(account%2)*540)     # 모두 지우기(큰글씨)
    time.sleep(1.5)
    pag.click(577+(account//2)*960, 62+(account%2)*540)     # 모두 지우기(작은글씨)
    time.sleep(1.5)
    pag.hotkey('alt', 'up')  # 크기, 위치 맞춰놓자!
    # pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
    # time.sleep(0.3)
    # pag.click(940 + (account // 2) * 960, 520 + (account % 2) * 540)
    # time.sleep(3)
    # pag.click(677 + (account // 2) * 960, 137 + (account % 2) * 540)
    # time.sleep(5)
    return

# 왠지 모르게 오류가 났다! 재부팅시켜!
def End_kkd(account):
    pag.click(2 + (account // 2) * 960, 15 + (account % 2) * 540)  # 메뉴바 한번 클릭해주고
    time.sleep(1)
    pag.hotkey('alt', 'up')
    time.sleep(3)
    pag.click(2 + (account // 2) * 960, 15 + (account % 2) * 540)  # 메뉴바 한번 클릭해주고
    pag.hotkey('pgup')   # 실행중인 모든 창 띄우기
    time.sleep(5)
    start_time_end_kkd = time.time()
    while True:
        now_time_end_kkd = time.time()
        if(now_time_end_kkd - start_time_end_kkd >= 30):
            print('end_kkd 너무 오래 걸리는걸? 30초 이상')
            pag.click(2 + (account // 2) * 960, 15 + (account % 2) * 540)  # 메뉴바 한번 클릭해주고
            pag.hotkey('home')  # 홈으로 가욧
            time.sleep(6)
            return True
        # print('End_kkd의 while true 들어왔다!')
        if keyboard.is_pressed('end'):
            return False
        init_kkm_recent = pag.locateCenterOnScreen('init_kkm_recent.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (init_kkm_recent):
            pag.click(init_kkm_recent)
            pag.hotkey('esc')
            return True
        cond_error_ad2 = pag.locateCenterOnScreen('cond_error_ad2.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (cond_error_ad2):
            pag.click(cond_error_ad2)
        cond_error1 = pag.locateCenterOnScreen('err_x1.PNG', confidence=0.9, grayscale = True, region = (2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (cond_error1):
            pag.click(cond_error1)
        cond_error2 = pag.locateCenterOnScreen('err_x1.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (cond_error2):
            pag.click(cond_error2)
        delete_all_1 = pag.locateCenterOnScreen('delete_all_1.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (delete_all_1):
            pag.click(delete_all_1)
        delete_all_2 = pag.locateCenterOnScreen('delete_all_2.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (delete_all_2):
            pag.click(delete_all_2)

def Check_if_error(account):
    # print('original', account)
    account = (account + 1) % 3
    kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    man_macro = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (account // 2) * 960, 1 + (account % 2) * 540, 422, 29))
    if (kkd_start_ire) and (man_macro):
        print('%d계정 매크로 돌리는 다른 계정 겜 튕겼네!'%(account))
        pag.click(man_macro)
    account = (account + 1) % 3
    kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    man_macro = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (account // 2) * 960, 1 + (account % 2) * 540, 422, 29))
    if (kkd_start_ire) and (man_macro):
        print('%d계정 매크로 돌리는 다른 계정 겜 튕겼네!'%(account))
        pag.click(man_macro)
    else:
        print('매크로 동작+튕김 현상 없음!')

def Kingdom_ready(account, whereto):  # 특정 위치 확인
    try:
        error_position = 0
        start_time = time.time()

        while True:
            time.sleep(1)
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
            if (cond_network):
                pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
                time.sleep(0.3)

            now_time = time.time()
            if keyboard.is_pressed('end'):
                print('end버튼 눌러 종료됨')
                return

            screen = ImageGrab.grab()
            pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
            pix_status_scr = screen.getpixel((910 + (account // 2) * 960, 55 + (account % 2) * 540))  # = 미세 오른쪽
            pix_status2 = screen.getpixel((540 + (account // 2) * 960, 510 + (account % 2) * 540))  # 마침표
            pix_status_boldline1 =screen.getpixel((10 + (account // 2) * 960, 40 + (account % 2) * 540))  # 테두리가 두꺼워졌어요!1
            pix_status_boldline2 = screen.getpixel((10 + (account // 2) * 960, 538 + (account % 2) * 540))  # 테두리가 두꺼워졌어요!2
            pix_status_boldline_yes = (13, 16, 48)

            pix_status_in = (227, 163, 2)  # 생산건물 내 07.31. 수정
            pix_status_in_dark = (114,81,1)  # 건물 안이긴 한데 창이 떠있음
            pix_status_in_magic_dark = (110, 81, 9)  # 건물 안이긴 한데 창이 떠있음
            pix_status_out = (11, 194, 252)  # 바탕화면(왕국), 트로피컬도 동일
            pix_status_out_window = (6, 95, 125)  # 창이 떠서 어두워짐
            pix_status_out_esc = (6, 97, 126)  # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
            pix_status_sowon = (255, 206, 1)  # 소원나무, 곰젤리열차, 상점 동일
            pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
            pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
            pix_status_bal_window = (127, 95, 4)  # 열기구 창 떠서 어두워짐
            # pix_status_adv = (11, 194, 252)  # 모험하기
            pix_status_kdpass = (253, 253, 253)  # 킹덤패스
            pix_status_warehouse = (55, 64, 105)  # 창고 뜸
            pix_status_mail = (60, 70, 105)  # 우편함
            pix_lackof1 = (243, 233, 223)  # 베이지색
            pix_status_not_prod = (8, 134, 174)  # 건물 클릭했지만 생산 건물은 아님
            pix_status_cookiehouse = (8, 138, 179)  # 엥 이게 다 달라?
            pix_status_lotto = (255, 206, 1)  # 뽑기, 해변교역소
            pix_status_mycookie = (0, 0, 0)  # 내 쿠키...으... 움직이면 틀어질텐데
            pix_status_fountain = (84, 93, 134)  # 분수..
            pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
            pix_status_trade = (255, 206, 2)  # 해상무역센터 로비
            pix_status_wanted = (29, 10, 12)  # 오늘의 현상수배 선택하는 곳
            pix_status_fight_comp = (168, 167, 167)  # 모험 전투 후
            pix_status_fight_comp1 = (121, 98, 74)  # 모험 전투 후1
            pix_status_temple = (177, 123, 153) # 찬란한 영웅들의 신전 대기화면, 석상화면 같음
            pix_status_temple_dark = (88, 61, 76) # 찬란한 영웅들의 신전 화면 어두워졌을 때(슬롯 확장 잘못누름)
            pix_status_arena_lobby = (197, 196, 194)  # 아레나 로비화면!

            pix_status_scr1 = screen.getpixel((65 + (account // 2) * 960, 505 + (account % 2) * 540))  # = 왼쪽아래 건설하기 아이콘쪽
            pix_status1_tropical = (255, 98, 170)  # 트로피칼이다
            pix_status1_tropical_windowopen = (127, 49, 85)  # 트로피칼에 메뉴창 떠있다

            # 220203 추가 - 이미지 확인방식 추가(업뎃 후 픽셀값 변경...)
            cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825 + (account // 2) * 960, 490 + (account % 2) * 540, 45, 40))  # 쿠키왕국
            cond_kkd_train = pag.locateCenterOnScreen('cond_kkd_train.png', confidence=0.85, region=(30 + (account // 2) * 960, 42 + (account % 2) * 540, 25, 33))  # 곰젤리열차
            cond_kkd_temple = pag.locateCenterOnScreen('cond_kkd_temple.png', confidence=0.85, region=(170 + (account // 2) * 960, 35 + (account % 2) * 540, 55, 35))  # 찬란한 영웅들의 신전(신전)
            cond_kkd_tro = pag.locateCenterOnScreen('cond_kkd_tro.png', confidence=0.85, region=(18 + (account // 2) * 960, 448 + (account % 2) * 540, 45, 40))  # 트로피칼(좌하단 파라솔 꽃)
            cond_kkd_sowon = pag.locateCenterOnScreen('cond_kkd_sowon.png', confidence=0.85, region=(430 + (account // 2) * 960, 45 + (account % 2) * 540, 31, 35))  # 소원나무
            cond_kkd_sangjum = pag.locateCenterOnScreen('cond_kkd_sangjum1.png', confidence=0.85, region=(14 + (account // 2) * 960, 40 + (account % 2) * 540, 46, 29))  # 상점
            cond_kkd_balloon = pag.locateCenterOnScreen('cond_kkd_balloon.png', confidence=0.85, region=(9 + (account // 2) * 960, 36 + (account % 2) * 540, 25, 35))  # 열기구(대기)
            cond_kkd_balloon_ing = pag.locateCenterOnScreen('cond_kkd_balloon_ing.png', confidence=0.85, region=(364 + (account // 2) * 960, 85 + (account % 2) * 540, 28, 37))  # 열기구(대기)
            adv_worldmap = pag.locateCenterOnScreen('adv_worldmap.png', confidence=0.85, region=(33 + (account // 2) * 960, 467 + (account % 2) * 540, 52, 43))  # 좌하단 월드맵 아이콘(트로피칼과 차이점)
            cond_gold = pag.locateCenterOnScreen('cond_gold.png', confidence=0.8, region=(310 + (account // 2) * 960, 35 + (account % 2) * 540, 555, 50))  # 골드 위치
            cond_gnome = pag.locateCenterOnScreen('cond_gnome.png', confidence=0.8, region=(310 + (account // 2) * 960, 35 + (account % 2) * 540, 555, 50))  # 노움 위치
            cond_diamond = pag.locateCenterOnScreen('cond_diamond.png', confidence=0.8, region=(310 + (account // 2) * 960, 35 + (account % 2) * 540, 555, 50))  # 다이아 위치
            cond_meatjelly = pag.locateCenterOnScreen('cond_meatjelly.png', confidence=0.8, region=(310 + (account // 2) * 960, 35 + (account % 2) * 540, 555, 50))  # 고기젤리 위치
            in_pos = pag.locateCenterOnScreen('bInPosition.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 건물 안
            cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12 + (account // 2) * 960, 38 + (account % 2) * 540, 37, 36))  # Play버튼 누른 후 모험하기 창
            cond_adv_arena_robby = pag.locateCenterOnScreen('cond_adv_arena_robby.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 킹덤아레나
            cond_reward = pag.locateCenterOnScreen('cond_reward.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 미션 보상받기
            mark_x_mission = pag.locateCenterOnScreen('mark_x_mission.png', confidence=0.8, region=(778 + (account // 2) * 960, 124 + (account % 2) * 540, 50, 50))  # 미션 취소
            cond_error_page = pag.locateCenterOnScreen('cond_error_page.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 검은 바탕... 렉 등에 의한 오류?
            kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            kkd_ad = pag.locateCenterOnScreen('cond_error_ad.png',  grayscale=True, confidence=0.8, region=(1471, 745 , 443, 335))
            kkd_ad1 = pag.locateCenterOnScreen('cond_error_ad1.png',  grayscale=True, confidence=0.8, region=(1471, 745 , 443, 335))
            kkd_ad2 = pag.locateCenterOnScreen('cond_error_ad2.png',  grayscale=True, confidence=0.8, region=(1471, 745 , 443, 335))
            kkd_ad3 = pag.locateCenterOnScreen('cond_error_ad3.png',  grayscale=True, confidence=0.8, region=(1471, 745 , 443, 335))
            kkd_winupdate = pag.locateCenterOnScreen('cond_error_winupdate.png', confidence=0.95, region=(1, 1, 960 * 2, 540 * 2))
            cond_kkd_arena = pag.locateCenterOnScreen('cond_kkd_arena.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            cond_kkd_arena_continue = pag.locateCenterOnScreen('cond_kkd_arena_continue.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 전투 재개(겜 튕겼다 들어와서 아레나 전투!)

            print('[Kingdom_ready] 현재 픽셀값 : ', pix_status, '실행 %s초 지났습니다.' % int(now_time - start_time), account, '계정, 현재시간:', datetime.now().strftime('%H:%M:%S'))
            # print('[Kingdom_ready] 실행 %s초 지났습니다.' % int(now_time - start_time), '현재시간:', datetime.now().strftime('%H:%M:%S'))
            if now_time - start_time >= 300:
                print('너무 오래 돌리고 있는데?')
                End_kkd(account)  # 쿠킹덤 종료. 15분 안엔 끝나겠지.
                Kingdom_ready(account, 'kkd_out')  # 재부팅
                start_time = 0

            #현재 계정 매크로 종료...흠....
            man_macroA = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (0 // 2) * 960, 1 + (0 % 2) * 540, 422, 29))
            man_macroB = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (1 // 2) * 960, 1 + (1 % 2) * 540, 422, 29))
            man_macroC = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (2 // 2) * 960, 1 + (2 % 2) * 540, 422, 29))
            if account == 0 and man_macroA:
                print('A계정 수동 매크로 동작중... 종료한다!')
                pag.click(man_macroA)
                time.sleep(2)
                man_macro_working = pag.locateCenterOnScreen('man_macro_working.png', confidence=0.9, region=(960, 540, 513, 523))
                pag.click(man_macro_working)
                time.sleep(2)
                man_macro_stop = pag.locateCenterOnScreen('macro_stop.png', confidence=0.9, region=(960, 540, 513, 523))
                pag.click(man_macro_stop)
                time.sleep(2)
            elif account == 1 and man_macroB:
                print('B계정 수동 매크로 동작중... 종료한다!')
                pag.click(man_macroB)
                time.sleep(2)
                man_macro_working = pag.locateCenterOnScreen('man_macro_working.png', confidence=0.9, region=(1156, 540, 513, 523))
                pag.click(man_macro_working)
                time.sleep(2)
                man_macro_stop = pag.locateCenterOnScreen('macro_stop.png', confidence=0.9, region=(1156, 540, 513, 523))
                pag.click(man_macro_stop)
                time.sleep(2)
            elif account == 2 and man_macroC:
                print('C계정 수동 매크로 동작중... 종료한다!')
                pag.click(man_macroC)
                time.sleep(2)
                man_macro_working = pag.locateCenterOnScreen('man_macro_working.png', confidence=0.9, region=(1398, 540, 513, 523))
                pag.click(man_macro_working)
                time.sleep(2)
                man_macro_stop = pag.locateCenterOnScreen('macro_stop.png', confidence=0.9, region=(1398, 540, 513, 523))
                pag.click(man_macro_stop)
                time.sleep(2)
            elif account == 0 and (man_macroB or man_macroC):
                Check_if_error(account)
            elif account == 1 and (man_macroC or man_macroA):
                Check_if_error(account)
            elif account == 2 and (man_macroA or man_macroB):
                Check_if_error(account)

            if (kkd_ad):
                print('광고 없애!')
                pag.click(kkd_ad)

            if (kkd_ad1):
                print('광고 없애!1')
                pag.click(kkd_ad1)

            if (kkd_ad2):
                print('광고 없애!2')
                pag.click(kkd_ad2)

            if (kkd_ad3):
                print('광고 없애!3')
                pag.click(kkd_ad3)

            if (kkd_winupdate):
                print('윈도우 업데이트 없애!')
                pag.click(kkd_winupdate)


            if (pix_status_boldline1 == pix_status_boldline_yes) and (pix_status_boldline2 == pix_status_boldline_yes): # 테두리가 두꺼워졌다면!
                print('테두리가 두꺼워졋서!!!', '계정:', account)
                End_kkd_line(account)
                # pag.click(871+(account//2)*960, 18+(account%2)*540)                 # 전체화면으로 바꿔!
                # time.sleep(1.5)
                # pag.click(1833, 17)          # 다시 원래 크기로 돌려놓고
                # time.sleep(1.5)
                # pag.hotkey('alt', 'up')      # 크기, 위치 맞춰놓자!
                # time.sleep(1.5)
                # pag.click(942+(account//2)*960, 522+(account%2)*540)     # 켜진 창 다 띄워서?
                # time.sleep(1.5)
                # pag.click(680+(account//2)*960, 82+(account%2)*540)     # 모두 지우기(큰글씨)
                # time.sleep(1.5)
                # pag.click(577+(account//2)*960, 62+(account%2)*540)     # 모두 지우기(작은글씨)
                # time.sleep(1.5)
                # pag.hotkey('alt', 'up')  # 크기, 위치 맞춰놓자!
                time.sleep(2)

            if (kkd_start_ire): # 바탕화면으로 나가서 쿠킹덤 아이콘이 보이나!?
                Check_Initiating(account)
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            if (cond_gold):
                # 혹시 또 1픽셀씩 오갈 수 있..으니?
                if 593 >= cond_gold.x >= 591:
                    # 소원,열차,상점,쿠키성 중 하나!
                    if not (cond_kkd_sowon) and not (cond_kkd_train) and not (cond_kkd_sangjum):
                        print('쿠키성이네요!')
                        pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
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

            if (cond_kkd_arena_continue):  # 아레나 돌리다가 튕겨서 에러났어요, 전투재개!
                pag.click(cond_kkd_arena_continue)
                time.sleep(80)
                return True

            # 상하단 픽셀 위치 모두 (0, 0, 0)이고 esc 누른 경우
            if pix_status == (0, 0, 0) and pix_status == (0, 0, 0) and (cond_error_page):
                End_kkd(account)  # 쿠킹덤 종료. 15분 안엔 끝나겠지.
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            if (cond_halted):
                # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
                pag.click(cond_halted)
                End_kkd(account)
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            if (cond_halted1):
                pag.click(cond_halted_close)
                time.sleep(7)
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            if pix_status == pix_status_in or (in_pos):  # 건물 안 ok
                print('건물 안이네요!')
                if (pix_status == whereto) or (whereto == 'prod_in'):
                    return True
                else:
                    if whereto == 'prod_in':
                        return False
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.1)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            elif whereto == 'kkd_arena':
                Kingdom_ready(account, 'kkd_out')
                time.sleep(1)
                Arena_Event(account)
                return True

            elif pix_status == pix_status_in_dark:  # 건물 안에서 창이 떠있으면 esc
                print('건물 내부 : 창은 닫자.')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

            elif pix_status == pix_status_in_magic_dark:  # 건물 안에서 창이 떠있으면 esc
                print('마법공방 내부 : 창은 닫자.')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.5)

            elif pix_status == pix_status_trade:  # 무역센터
                print('무역센터 내부!')
                if (pix_status == whereto) or (whereto == 'trade_in'):
                    print('무역센터야!')
                    return True
                else:
                    if whereto == 'trade_in':
                        return False
                    print('무역센터 아니야!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            elif pix_status == pix_status_temple:  # 신전
                print('신전 내부!')
                if (pix_status == whereto) or (whereto == 'temple_in'):
                    print('신전이야!')
                    return True
                else:
                    if whereto == 'temple_in':
                        return False
                    print('신전 아니야!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            elif (cond_gnome):
                if whereto == 'research_in':
                    print('연구소 옥희')
                    return True
                else:
                    print('연구소 안희야')
                    pag.click(891 + (account // 2) * 960, 54 + (account % 2) * 540)
                    time.sleep(3)

            elif pix_status == pix_status_fountain:  # 분수 내부
                print('분수 내부!')
                if (pix_status == whereto) or (whereto == 'fountain_in'):
                    print('분수?')
                    return True
                else:
                    if whereto == 'fountain_in':
                        return False
                    print('분수 아니야!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            # elif pix_status == pix_status_adv:  # 모험하기
            #     if (pix_status == whereto) or (whereto == 'mohum'):
            #         print('모험하기?')
            #         return True
            #     else:
            #         if whereto == 'mohum':
            #             return False
            #         print('모험은 아...직?')
            #         pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
            #         time.sleep(0.3)
            #         pag.hotkey('esc')
            #         time.sleep(0.3)

            elif pix_status == pix_status_wanted:  # 현상수배 하기
                if (pix_status == whereto) or (whereto == 'wanted'):
                    print('현상수배하기?')
                    return True
                else:
                    if whereto == 'wanted':
                        return False
                    print('현상수배 선택 창이네?')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            elif pix_status2 == pix_status_wanted:  # 현상수배 전투 종료
                if (pix_status == whereto) or (whereto == 'wanted_end'):
                    print('현상수배 전투 완료!!')
                    pag.click(540 + (account // 2) * 960, 510 + (account % 2) * 540)
                    time.sleep(2)
                    return True
                else:
                    if whereto == 'wanted_end':
                        print('현상수배 전투중!')
                        return False
                    print('현상수배 전투중!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

            elif pix_status == pix_status_kdpass:  # 킹덤패스
                print('킹덤패스! 아냐!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

            elif pix_status == pix_status_warehouse:  # 창고
                print('창고! 아냐!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

            elif pix_status == pix_status_lotto:  # 뽑기
                print('뽑기 아냐!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

            elif pix_status == pix_status_mycookie:  # 내 쿠키..
                print('내쿠키 아냐!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(0.3)

            elif pix_status == pix_status_not_prod:  # 건물 클릭했지만 쿠하나 일반건물
                print('이상한 건물!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)

            elif pix_status == pix_status_arena_lobby:
                print('아레나 로비 들어왔습니다!')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)

            elif (cond_kkd_train):
                if (whereto == 'train_in'):
                    print('곰젤리 열차입니다!')
                    return True
                else:
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(1)

            elif (cond_kkd_sowon):
                if (whereto == 'sowon_in'):
                    print('소원나무 입니다!')
                    return True
                else:
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(1)

            elif (cond_kkd_temple):
                if (whereto == 'temple_in'):
                    print('신전 입니다!')
                    return True
                else:
                    print('신전으로 가려던 게 아니니 나갑니다.')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(1)
            # elif pix_status == pix_status_arena_lobby:

            elif (cond_kkd_sangjum):
                if (whereto == 'sangjum_in'):
                    print('상점 입니다!')
                    return True
                else:
                    print('상점으로 가려던 게 아니니 나갑니다.')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(1)

            elif pix_status == pix_status_cookiehouse:
                print('쿠키하우스 안이에요')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)

            elif pix_status == pix_status_out_window:
                print('창을 닫아요~')
                pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                time.sleep(0.3)
                pag.hotkey('esc')
                time.sleep(1)

            elif pix_status == pix_status_out_esc:
                if (pix_status_scr1 == pix_status1_tropical):  # 트로피컬 메인화면
                    pag.click(869 + (account // 2) * 960, 494 + (account % 2) * 540)  # 왕국가기 버튼 클릭
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(1)

                if (pix_status_scr1 == pix_status1_tropical_windowopen):  # 트로피컬 메뉴화면
                    pag.hotkey('esc')
                    pag.click(869 + (account // 2) * 960, 494 + (account % 2) * 540)  # 왕국가기 버튼 클릭
                    time.sleep(0.5)
                    pag.hotkey('esc')
                    time.sleep(1)

                else:
                    print('esc 취소')
                    cond_balloon_lack_heart = pag.locateCenterOnScreen('cond_balloon_lack_heart.png', confidence=0.96, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                    if (cond_balloon_lack_heart):
                        # print('cond_balloon_lack_heart', cond_balloon_lack_heart)
                        pag.click(cond_balloon_lack_heart)

            elif (cond_kkd_out):
                if (cond_gold):
                    if (cond_kkd_arena):
                        print('킹덤아레나인가요?')
                        pag.click(605 + (account // 2) * 960, 55 + (account % 2) * 540)
                        time.sleep(1)
                    else:
                        print('왕국이네요!')
                        if (whereto == 'kkd_out'):
                            return True
                        elif (whereto == 'tropical_in'):
                            print('왕국인데 트로피칼 볼래요')
                            if Tropical_Event(account):  # 트로피칼에 이벤트 없으면
                                print('트로피칼 입장!')
                                return True
                            else:
                                print('트로피칼 이벤트 없어서 들어가지 않습니다.')
                                return False
                        else:
                            return False

                else:
                    print('왕국이긴 한데 이상한 건물인가 봅니다.')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.7)

            elif pix_status == pix_stats_kkd_start:
                print('꺼졌네요... 재실행')
                Check_Initiating(account)
                Kingdom_ready(account, 'kkd_out')

            elif pix_status == pix_status_ballon or (cond_kkd_balloon_ing):  # 열기구
                print('열기구 날아다니는 중!')
                if (pix_status == whereto) or (whereto == 'balloon_in'):
                    return True
                else:
                    if whereto == 'balloon_in':
                        return False
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
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
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(2)
                    pag.hotkey('esc')
                    time.sleep(2)

            # cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            # if (cond_halted):
            #     pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
            #     End_kkd(account)
            #     Kingdom_ready(account, 'kkd_out')  # 재부팅
            #     return False
            else:
                # 여기를 수정할거야 이레
                if not (pix_status2 == 'wanted_end'):
                    print('그 모든 게 아니라면....', '현재시간:', datetime.now().strftime('%H:%M:%S'))
                    time.sleep(1)
                    if error_position == 0:
                        pag.hotkey('alt', 'up')  # 창 정렬하고
                        time.sleep(2)
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)    # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.hotkey('esc')
                        time.sleep(2)
                    if error_position == 1:
                        pag.hotkey('alt', 'up')  # 창 정렬하고
                        time.sleep(2)
                        time.sleep(2)
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)   # 혹시 '쿠킹덤이 중지되었습니다' 떳나?
                        time.sleep(2)
                        pag.hotkey('esc')
                        time.sleep(2)
                        # pag.hotkey('alt', 'up')
                    if error_position == 2:
                        pag.hotkey('alt', 'up')  # 창 정렬하고
                        time.sleep(2)
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        time.sleep(2)
                        # pag.click(284 + (account//2)*960, 45 + (account%2) * 540)
                        time.sleep(3)
                        pag.hotkey('esc')
                        time.sleep(3)
                        pag.hotkey('esc')
                        time.sleep(3)
                    if error_position == 3:
                        time.sleep(2)
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.click(605 + (account // 2) * 960, 55 + (account % 2) * 540)
                        time.sleep(5)
                    if error_position == 6:
                        pag.click(284 + (account // 2) * 960, 45 + (account % 2) * 540)
                        time.sleep(2)
                        pag.hotkey('alt', 'up')
                        time.sleep(2)
                        End_kkd(account)  # 우선 모든 창 꺼보고
                        time.sleep(2)
                        Kingdom_ready(account, 'kkd_out')  # 바탕화면으로 튕겼는지, 아니면 뭔지 확인
                        time.sleep(2)
                    # if error_position == 7:
                    #     time.sleep(2)
                    #     Kingdom_ready(account, 'kkd_out')   # 바탕화면으로 튕겼는지, 아니면 뭔지 확인
                    #     time.sleep(20)
                    if error_position > 6:
                        time.sleep(2)
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.click(944 + (account // 2) * 960, 520 + (account % 2) * 540)
                        time.sleep(7)
                        pag.click(687 + (account // 2) * 960, 84 + (account % 2) * 540)
                        time.sleep(7)
                        Check_Initiating(account)
                        time.sleep(20)
                        error_position = 0
                    print('Error count =', error_position)
                    error_position = error_position + 1
                else:
                    print('여긴 안도니')
                    time.sleep(5)
                    return False
    except:
        print('에러가 났어요! Kingdom_ready')
        # send_telegram_message('Kingdom_ready에서 에러가 났어요!')
        End_kkd(account)
        time.sleep(3)
        Kingdom_ready(account, 'kkd_out')  # 재부팅

def Check_Initiating(account):
    print('부팅여부 확인합니다.')
    bStart = False
    bTouchto = False
    kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_start_bg = pag.locateCenterOnScreen('init_kkm_recent.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 최근 항목이 없습니다.
    kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    start_time = time.time()
    while True:
        now_time = time.time()
        if (now_time - start_time) >= 180:
            print('너무 오래 돌려요! 3분')
            return False
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.94, region=(376 + (account // 2) * 960, 354 + (account % 2) * 540, 159, 45))
        if (cond_network):  # 네트워크오류인듯?
            pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
            time.sleep(0.8)
        kkd_start_bg = pag.locateCenterOnScreen('init_kkm_recent.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 최근 항목이 없습니다.
        if (kkd_start_bg):  # 최근 항목이 없습니다.
            print('[부팅중] 계정 튕김! 창목록클릭중!')
            pag.hotkey('esc')
            time.sleep(1)

        cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (cond_halted):  # 쿠킹덤이 중지됨!
            # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
            pag.click(cond_halted)
            End_kkd(account)
            Kingdom_ready(account, 'kkd_out')  # 재부팅
            return False

        cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (cond_halted1):
            pag.click(cond_halted_close)
            time.sleep(7)
            Kingdom_ready(account, 'kkd_out')  # 재부팅

        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (play_halted):  # 구글플레이 확인버튼... 난 쓸일이 없는걸
            pag.click(play_halted)
        else:
            break

    if (kkd_start) or (kkd_touch) or (kkd_down) or (kkd_start_ire):
        while True:
            if (kkd_start_ire):
                pag.click(kkd_start_ire)
                time.sleep(1)
                break

            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440, 363 + (account % 2) * 540, 43, 29))
            if (cond_network):
                pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
                time.sleep(0.8)

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            if (cond_halted):  # 쿠킹덤이 중지됨!
                # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
                pag.click(cond_halted)
                End_kkd(account)
                Kingdom_ready(account, 'kkd_out')  # 재부팅
                return False

            cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            if (cond_halted1):
                pag.click(cond_halted_close)
                time.sleep(7)
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            if keyboard.is_pressed('end'):
                return

            while True:
                play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (play_halted):  # 쿠킹덤이 중지됨!
                    pag.click(play_halted)
                else:
                    break

            kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
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
            kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            kkd_Touch11 = pag.locateCenterOnScreen('init_Touch11.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            while True:
                play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (play_halted):
                    pag.click(play_halted)
                else:
                    break

            if (kkd_touch):
                time.sleep(3)
                print('[부팅중] Touch to Start 터치!', '현재시간:', datetime.now().strftime('%H:%M:%S'))
                pag.click(random.randint(410, 410 + 101) + (account // 2) * 960, random.randint(380, 380 + 23) + (account % 2) * 540)
                bTouchto = True
            if (kkd_Touch11):
                time.sleep(3)
                print('[부팅중] Touch to Start 터치!', '현재시간:', datetime.now().strftime('%H:%M:%S'))
                pag.click(random.randint(410, 410 + 101) + (account // 2) * 960, random.randint(380, 380 + 23) + (account % 2) * 540)
                bTouchto = True
            if (kkd_down):
                time.sleep(3)
                print('[부팅중] 다운로드 터치!')
                pag.click(kkd_down)
                bTouchto = True
            if (not kkd_Touch11 and not (kkd_touch) and not (kkd_down)) and bTouchto:
                time.sleep(3)
                print('[부팅중] Touch to Start 터치 완료!', '현재시간:', datetime.now().strftime('%H:%M:%S'))
                break
        if bTouchto:
            print('부팅 실행 했습니다.')
            time.sleep(17)
            return
    else:
        print('튕긴건 아니네요')
        return


def del_duplication(dif, list_origin):
    list_origin.sort()
    list_origin = list(set(list_origin))
    del_list = list()
    if len(list_origin) > 1:  # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
        for i in range(len(list_origin) - 1):
            for j in range(len(list_origin) - 1 - i):
                # if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif and abs(int(list_origin[i][1])-int(list_origin[i+1+j][1])) < dif:
                if abs(int(list_origin[i][0]) - int(list_origin[i + 1 + j][0])) < dif:
                    del_list.append(list_origin[i])
                if list_origin[i][0] == list_origin[i + 1 + j][0]:
                    del_list.append(list_origin[i])
    list_origin = [x for x in list_origin if x not in del_list]
    list_origin.sort()
    return list_origin


def find_upper_num(image, account, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.8, grayscale=True, region=(515 + (account // 2) * 960, 46 + (account % 2) * 540, 48, 19))
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

    if (list_num_0):  # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0], 0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0], 1))

    if (list_num_2):
        for p in list_num_2:
            list_real_num.append((p[0], 2))

    if (list_num_3):
        for p in list_num_3:
            list_real_num.append((p[0], 3))

    if (list_num_4):
        for p in list_num_4:
            list_real_num.append((p[0], 4))

    if (list_num_5):
        for p in list_num_5:
            list_real_num.append((p[0], 5))

    if (list_num_6):
        for p in list_num_6:
            list_real_num.append((p[0], 6))

    if (list_num_7):
        for p in list_num_7:
            list_real_num.append((p[0], 7))

    if (list_num_8):
        for p in list_num_8:
            list_real_num.append((p[0], 8))

    if (list_num_9):
        for p in list_num_9:
            list_real_num.append((p[0], 9))

    # 지겨운 실제값 리스트를 받았으니
    list_real_num.sort()  # 추려서

    for i in range(len(list_real_num)):  # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1] * 10 ** (len(list_real_num) - i - 1)

    print('이 제품의 수량은 =', its_number)
    return its_number

            
def Wood_to_Cotton(account, Min_number, Max_number, Making_Level, prod_direction_left):  # Min 넘버 미만일 때 1렙, Min-Max사이일 땐 2렙
    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    if (cond_halted):
        # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
        pag.click(cond_halted)
        End_kkd(account)
        Kingdom_ready(account, 'kkd_out')  # 재부팅
        return False

    cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    if (cond_halted1):
        pag.click(cond_halted_close)
        time.sleep(7)
        Kingdom_ready(account, 'kkd_out')  # 재부팅

    z = Check_available_slots(account)
    if z == 0:
        print('리스트 full!2')
        Skip_Next(account, prod_direction_left)
        return False

    its_number = Upper_numb(account)

    # print('확인한 상단 숫자 =', its_number)
    if Max_number * 0.8 > its_number:  # 최대 수량의 80% 이하이면
        bujockhaeyo = True
    else:
        bujockhaeyo = False
    start_time = time.time()

    if Min_number < its_number < Max_number:
        print('중간수량 : 설정 레벨로 진행합니다.')  # 773 -> 850
        pag.moveTo(random.randint(850 - 5, 850 + 5) + (account // 2) * 960, random.randint(200 - 3, 200 + 3) + (Making_Level - 1) * 153 + (account % 2) * 540)  # 1렙이면 200. 2~3렙은 153씩 올라감
        pag.mouseDown()
        time.sleep(0.3)
        pag.mouseUp()
        time.sleep(0.8)
        Skip_Next(account, prod_direction_left)
        return bujockhaeyo

    if Min_number >= its_number:  # 최소수량 이하이면 1렙 고정.
        print('위험수량 : 1레벨로 생산합니다.')

        while True:
            if keyboard.is_pressed('end'):
                print('end 누름')
                break

            now_time = time.time()
            if now_time - start_time > 30:
                return
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
            if (cond_network):
                pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
                time.sleep(0.3)

            prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence=0.945, region=(90 + (account // 2) * 960, 145 + (account % 2) * 540, 24, 20))
            if (prod_refresh):
                pag.click(prod_refresh)  # >> 클릭(즉시생산)
                # remain_time_dia = pag.locateCenterOnScreen('remain_time_dia.png', confidence = 0.945, region = (90,145+account*540,24,20))
                time.sleep(0.5)
                remain_time_less_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence=0.945, region=(570 + (account // 2) * 960, 239 + (account % 2) * 540, 49, 25))  # 다이아 10 확인
                remain_time_about_minute = pag.locateCenterOnScreen('remain_time_less_minute.png', confidence=0.945, region=(570 + (account // 2) * 960, 239 + (account % 2) * 540, 49, 25))  # 다이아 10 확인
                if (remain_time_less_minute) or (remain_time_about_minute):
                    pag.click(random.randint(651 - 5, 651 + 5) + (account // 2) * 960, random.randint(85 - 5, 85 + 5) + (account % 2) * 540)  # 즉시생산 창닫기
                    time.sleep(0.8)
                    print('1분 내에 끝날 거라 남겼슴돠')
                    break
                else:
                    print('1분 넘게 남아 삭제함돠2')
                    pag.click(random.randint(651 - 5, 651 + 5) + (account // 2) * 960, random.randint(85 - 5, 85 + 5) + (account % 2) * 540)  # 즉시생산 창닫기
                    time.sleep(0.2)
                    pag.click(random.randint(75 - 5, 75 + 5) + (account // 2) * 960, random.randint(200 - 5, 200 + 5) - 73 + (account % 2) * 540)  # 첫째 칸 클릭
                    time.sleep(0.2)
                    pag.click(random.randint(462 - 5, 462 + 5)+72 + (account // 2) * 960, random.randint(378 - 5, 378 + 5) + (account % 2) * 540)  # 확인
                    time.sleep(0.5)
            else:
                break
        pag.moveTo(random.randint(850 - 5, 850 + 5) + (account // 2) * 960, random.randint(200 - 3, 200 + 3) + (account % 2) * 540)      # 여기가 실제 생산 인가????
        pag.mouseDown()
        time.sleep(0.3)
        pag.mouseUp()
        time.sleep(0.5)
        Skip_Next(account, prod_direction_left)
        return bujockhaeyo

    if its_number >= Max_number:
        print('최대수량 : 생산하지 않고 넘어갑니다.')
        screen = ImageGrab.grab()
        pix_lackof = screen.getpixel((545 + (account // 2) * 960, 745 - 540 + (account % 2) * 540))  # 재료부족창?
        pix_lackof1 = (243, 233, 223)  # 베이지색
        if pix_lackof != pix_lackof1:
            pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
            time.sleep(0.5)
        return bujockhaeyo

def to_make_number(building_name):
    for i in range(8):
        start_text = building_name+'_'
        mid_text = 'lev'
        if (eval(start_text + mid_text + str(i + 1)) == 0):
            print('이 레벨은 값이 0이구만요!')
            a = i+1
            return a

def check_var(var_name):
    if var_name in globals():
        # print('ok')
        return True
    else:
        # print('none')
        return False

# 1~to_make 확인 후 재고 확인, 클릭까지 하고 나감
def prod_action_ire(account, building, building_name, prod_direction_left):
    while True:
        if pix_prod == eval('pix_'+building_name):
            print(building_name+' 건물 돌립니다')
            pix_error_count = 0
            z = Check_available_slots(account)
            if z <= 1:
                # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
                print('리스트 full!3')
                time.sleep(0.5)
                Skip_Next(account, prod_direction_left)
                return

            for i in range(8):
                start_text = building_name + '_'
                mid_text = 'lev'
                check_var1 = check_var(start_text + mid_text + str(i + 1))
                if not check_var1:
                    z = i
                    break
                if (eval(start_text + mid_text + str(i + 1)) == 0):
                    # print('이 레벨은 값이 0이구만요!')
                    z = i + 1
                    break

            # z = to_make_number(building_name)
            print(z)

            for i in range(z-1):
                item_number = check_item_number(account, 'top')
                # print('i:',i)
                print('item_number = ', item_number)
                if(item_number==1):
                    three_prod_action_new(account, building, building_name, prod_direction_left)
                if (item_number == 2):
                    three_prod_action_last_one(account, building, building_name, prod_direction_left)
                if (item_number == 3):
                    three_prod_action_last_one(account, building, building_name, prod_direction_left)
                if (item_number == 4):
                    three_prod_action_last_one(account, building, building_name, prod_direction_left)
                if (item_number == 5):
                    three_prod_action_last_one(account, building, building_name, prod_direction_left)

                if i < z-3:
                    Updown(account, 'up1')

                print(target_numb)

                if i == z-3:
                    break





            # if (z==7): # 7렙까지 읽고 생산
            #     if (item_number == 1):
            #         three_prod_action_new(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         item_number = check_item_number(account, 'bot')
            #         print(target_numb)
            #         time.sleep(0.5)
            #     if (item_number == 2):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         item_number = check_item_number(account, 'bot')
            #         print(target_numb)
            #         time.sleep(0.5)
            #     if (item_number == 3):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         item_number = check_item_number(account, 'bot')
            #         print(target_numb)
            #         time.sleep(0.5)
            #     if (item_number == 4):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         item_number = check_item_number(account, 'bot')
            #         print(target_numb)
            #         time.sleep(0.5)
            #     if (item_number == 5):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         print(target_numb)
            #         time.sleep(0.5)
            # if (z==6): # 6렙까지 읽고 생산
            #     if (item_number == 1):
            #         three_prod_action_new(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 2):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 3):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 4):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            # if (z==5):  # 5렙까지 읽고 생산
            #     if (item_number == 1):
            #         three_prod_action_new(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 2):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 3):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)
            # if (z==4):  # 4렙까지 읽고 생산
            #     if (item_number == 1):
            #         three_prod_action_new(account, building, building_name, prod_direction_left)
            #         Updown(account, 'up1')
            #         time.sleep(0.5)
            #     if (item_number == 2):
            #         three_prod_action_last_one(account, building, building_name, prod_direction_left)

            print('target_numb(list):', target_numb)
            while True:
                to_make = z
                print('%s렙까지 만들어요 : ' % to_make, target_numb[0:to_make])
                tmp = max(target_numb[0:to_make])
                index = target_numb[0:to_make].index(tmp) + 1
                print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))

                if item_number + 2 >= index >= item_number:
                    click_item1 = click_item(account, index - item_number)
                    if not (click_item1):
                        # 이게 맞나.... 어케해야 다음거 돌리지?
                        Skip_Next(account, prod_direction_left)
                        return
                    z = Check_available_slots(account)
                    if z <= 1:
                        print('리스트 full!')
                        time.sleep(0.5)
                        Skip_Next(account, prod_direction_left)
                        return
                elif index < item_number:
                    print(item_number - index, '칸 올려요')
                    for i in range(item_number - index):
                        Updown(account, 'down1')
                        time.sleep(0.5)

                    item_number = item_number - (item_number - index)

                    click_item2 = click_item(account, index - item_number)
                    if not (click_item2):
                        #이게 맞나.... 어케해야 다음거 돌리지?
                        Skip_Next(account, prod_direction_left)
                        return
                    z = Check_available_slots(account)
                    if z <= 1:
                        print('리스트 full!')
                        time.sleep(0.5)
                        Skip_Next(account, prod_direction_left)
                        return
                else:
                    print('조건이 이상해요.')
                    return

            # if not bProdHigh or eval(building_name+'_num') == 1:
            #     # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
            #     if not (eval(building_name+'lev1') == 0):
            #         while True:
            #             if keyboard.is_pressed('end'):
            #                 break
            #             item_number = check_item_number(account, 'top') # 현재화면 맨 윗 제품 번호 확인(1~7)
            #             print('item_number = %d'%item_number, ', target_numb = ', target_numb)
            #
            #             if (item_number == 1):
            #                 three_prod_action_new(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 2):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 3):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 4):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             elif (item_number == 5):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #
            #                 if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
            #                     while True:
            #                         to_make = 7
            #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
            #                         tmp = max(target_numb[0:to_make])
            #                         index = target_numb[0:to_make].index(tmp)+1
            #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
            #
            #                         if item_number + 2 >= index >= item_number:
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         elif index < item_number:
            #                             print(item_number - index, '칸 올려요')
            #                             for i in range(item_number - index):
            #                                 Updown(account, 'down1')
            #                                 time.sleep(0.5)
            #
            #                             item_number = item_number - (item_number - index)
            #
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         else:
            #                             print('조건이 이상해요1')
            #                 elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
            #                     while True:
            #                         to_make = 6
            #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
            #                         tmp = max(target_numb[0:to_make])
            #                         index = target_numb[0:to_make].index(tmp) + 1
            #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
            #
            #                         if item_number + 2 >= index >= item_number:
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         elif index < item_number:
            #                             print(item_number - index, '칸 올려요')
            #                             for i in range(item_number - index):
            #                                 Updown(account, 'down1')
            #                                 time.sleep(0.5)
            #
            #                             item_number = item_number - (item_number - index)
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         else:
            #                             print('조건이 이상해요2')
            #                 else:
            #                     print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
            #
            #                 Skip_Next(account, prod_direction_left)
            #                 break
            #             if (item_number >= 6):
            #                 Updown(account, 'down1')
            #                 time.sleep(0.5)
            #     break
            # if bProdHigh and smith_num == 2:  # 첫 번째 건물 작업
            #     # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
            #     if not (smith_lev1 == 0):
            #         while True:
            #             if keyboard.is_pressed('end'):
            #                 break
            #             item_number = check_item_number(account, 'top')
            #             print('item_number = %d'%item_number, ', target_numb = ', target_numb)
            #             if (item_number == 1):
            #                 three_prod_action_new(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 2):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 3):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             if (item_number == 4):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #                 Updown(account, 'up1')
            #                 time.sleep(0.5)
            #             elif (item_number == 5):
            #                 three_prod_action_last_one(account, building, building_name, prod_direction_left)
            #
            #                 if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
            #                     while True:
            #                         to_make = 7
            #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
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
            #
            #                             item_number = item_number - (item_number - index)
            #
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         else:
            #                             print('조건이 이상해요3')
            #                 elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
            #                     while True:
            #                         to_make = 6
            #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
            #                         tmp = max(target_numb[0:to_make])
            #                         index = target_numb[0:to_make].index(tmp) + 1
            #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
            #
            #                         if item_number + 2 >= index >= item_number:
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         elif index < item_number:
            #                             print(item_number - index, '칸 올려요')
            #                             for i in range(item_number - index):
            #                                 Updown(account, 'down1')
            #                                 time.sleep(0.5)
            #
            #                             item_number = item_number - (item_number - index)
            #
            #                             click_item(account, index - item_number)
            #                             z = Check_available_slots(account)
            #                             if z <= 1:
            #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
            #                                 print('리스트 full!3')
            #                                 time.sleep(0.5)
            #                                 Skip_Next(account, prod_direction_left)
            #                                 break
            #                         else:
            #                             print('조건이 이상해요4')
            #                 else:
            #                     print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
            #
            #                 Skip_Next(account, prod_direction_left)
            #                 break
            #             if (item_number >= 6):
            #                 Updown(account, 'down1')
            #                 time.sleep(0.5)

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
rollc_lev1_C = 120  # 솔방울새 인형
rollc_lev2_C = 120  # 도토리 램프
rollc_lev3_C = 120  # 뻐꾹뻐꾹 시계
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
flower_lev6_C = 0  # 찬란한 요거트 화환

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
account = 2

# z = check_item_number(account)
# print(z)

# screen = ImageGrab.grab()
# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# pix_smith = (163, 118, 85)  # 도끼 스미스
# pix_jelly = (15, 174, 202)  # 젤리빈 잼 젤리
# cycle_check = 0
cycle_check = 0
pix_error_count = 0
index = 0
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
bicecreamcompleted = False

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


# try:
while True:
    if keyboard.is_pressed('end'):
        break

    target_numb = [0, 0, 0, 0, 0, 0, 0]

    kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))


    pix_lackof1 = (243, 233, 223)  # 베이지색

    screen = ImageGrab.grab()
    pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
    pix_lackof = screen.getpixel((545 + (account // 2) * 960, 745 - 540 + (account % 2) * 540))  # 재료부족창?

    # 이상한 창이 떠있나?
    if pix_lackof == pix_lackof1:
        print('꺼져!(off!)')
        pag.click(545 + (account // 2) * 960, 205 + (account % 2) * 540)
        pag.keyDown('ESC')
        time.sleep(0.1)
        pag.keyUp('ESC')
        time.sleep(0.3)
        pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
        time.sleep(0.5)
    # 건물 내부 색상 파악
    elif pix_prod == pix_wood:
        pix_error_count = 0
        print('wood!')
        wood_bef_action = Wood_to_Cotton(account, wood_min, wood_max, wood_prod, prod_direction_left)
        cycle_check = cycle_check + 1
        time.sleep(0.5)

    elif pix_prod == pix_jelbean:
        pix_error_count = 0
        print('jelbean!')
        jelbean_bef_action = Wood_to_Cotton(account, jelbean_min, jelbean_max, jelbean_prod, prod_direction_left)
        time.sleep(0.5)

    elif pix_prod == pix_sugar:
        pix_error_count = 0
        print('sugar!')
        sugar_bef_action = Wood_to_Cotton(account, sugar_min, sugar_max, sugar_prod, prod_direction_left)
        time.sleep(0.5)

    elif pix_prod == pix_biscuit:
        pix_error_count = 0
        print('biscuit!')
        jjokji_biscuit = Wood_to_Cotton(account, biscuit_min, biscuit_max, biscuit_prod, prod_direction_left)
        time.sleep(0.5)

    elif pix_prod == pix_berry:
        pix_error_count = 0
        print('berry!')
        jjokji_berry = Wood_to_Cotton(account, berry_min, berry_max, berry_prod, prod_direction_left)
        time.sleep(0.5)

    elif pix_prod == pix_milk:
        pix_error_count = 0
        print('milk!')
        jjokji_milk = Wood_to_Cotton(account, milk_min, milk_max, milk_prod, prod_direction_left)
        time.sleep(0.5)

    elif pix_prod == pix_cotton:
        pix_error_count = 0
        print('cotton!')
        jjokji_cotton = Wood_to_Cotton(account, cotton_min, cotton_max, cotton_prod, prod_direction_left)
        time.sleep(0.5)

    #smith 잠시 비활성화
    elif pix_prod == pix_smith:
        print('smith!')
        prod_action_ire(account, 'normal', 'smith', prod_direction_left)
    elif pix_prod == pix_jelly:
        print('jelly!')
        prod_action_ire(account, 'normal', 'jelly', prod_direction_left)
    elif pix_prod == pix_rollc:
        print('rollc!')
        prod_action_ire(account, 'normal', 'rollc', prod_direction_left)
    elif pix_prod == pix_bread:
        print('bread!')
        prod_action_ire(account, 'normal', 'bread', prod_direction_left)
    elif pix_prod == pix_jampy:
        print('jampy!')
        prod_action_ire(account, 'normal', 'jampy', prod_direction_left)
    elif pix_prod == pix_doye:
        print('doye!')
        prod_action_ire(account, 'normal', 'doye', prod_direction_left)
    elif pix_prod == pix_flower:
        print('flower!')
        prod_action_ire(account, 'normal', 'flower', prod_direction_left)
    elif pix_prod == pix_magic:
        print('magic!')
        prod_action_ire(account, 'magic', 'magic', prod_direction_left)
    elif pix_prod == pix_icecream:
        print('icecream!')
        prod_action_ire(account, 'normal', 'icecream', prod_direction_left)
        # pix_error_count = 0
        # z = Check_available_slots(account)
        # if z <= 1:
        #     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #     print('리스트 full!3')
        #     time.sleep(0.5)
        #     Skip_Next(account, prod_direction_left)
        #     continue
        # if not bProdHigh or smith_num == 1:
        #     # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
        #     if not (smith_lev1 == 0):
        #         while True:
        #             if keyboard.is_pressed('end'):
        #                 break
        #             item_number = check_item_number(account, 'top')
        #             print('item_number = %d'%item_number, ', target_numb = ', target_numb)
        #             if (item_number == 1):
        #                 three_prod_action_new(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 2):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 3):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 4):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             elif (item_number == 5):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #
        #                 if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
        #                     while True:
        #                         to_make = 7
        #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
        #                         tmp = max(target_numb[0:to_make])
        #                         index = target_numb[0:to_make].index(tmp)+1
        #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
        #
        #                         if item_number + 2 >= index >= item_number:
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         elif index < item_number:
        #                             print(item_number - index, '칸 올려요')
        #                             for i in range(item_number - index):
        #                                 Updown(account, 'down1')
        #                                 time.sleep(0.5)
        #
        #                             item_number = item_number - (item_number - index)
        #
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         else:
        #                             print('조건이 이상해요1')
        #                 elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
        #                     while True:
        #                         to_make = 6
        #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
        #                         tmp = max(target_numb[0:to_make])
        #                         index = target_numb[0:to_make].index(tmp) + 1
        #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
        #
        #                         if item_number + 2 >= index >= item_number:
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         elif index < item_number:
        #                             print(item_number - index, '칸 올려요')
        #                             for i in range(item_number - index):
        #                                 Updown(account, 'down1')
        #                                 time.sleep(0.5)
        #
        #                             item_number = item_number - (item_number - index)
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         else:
        #                             print('조건이 이상해요2')
        #                 else:
        #                     print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
        #
        #                 Skip_Next(account, prod_direction_left)
        #                 break
        #             if (item_number >= 6):
        #                 Updown(account, 'down1')
        #                 time.sleep(0.5)
        #     break
        # if bProdHigh and smith_num == 2:  # 첫 번째 건물 작업
        #     # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
        #     if not (smith_lev1 == 0):
        #         while True:
        #             if keyboard.is_pressed('end'):
        #                 break
        #             item_number = check_item_number(account, 'top')
        #             print('item_number = %d'%item_number, ', target_numb = ', target_numb)
        #             if (item_number == 1):
        #                 three_prod_action_new(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 2):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 3):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             if (item_number == 4):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #                 Updown(account, 'up1')
        #                 time.sleep(0.5)
        #             elif (item_number == 5):
        #                 three_prod_action_last_one(account, 'normal', 'smith', prod_direction_left)
        #
        #                 if smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
        #                     while True:
        #                         to_make = 7
        #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
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
        #
        #                             item_number = item_number - (item_number - index)
        #
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         else:
        #                             print('조건이 이상해요3')
        #                 elif not smith_lev7 and smith_lev6 and smith_lev5 and smith_lev4 and smith_lev3 and smith_lev2 and smith_lev1:
        #                     while True:
        #                         to_make = 6
        #                         print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
        #                         tmp = max(target_numb[0:to_make])
        #                         index = target_numb[0:to_make].index(tmp) + 1
        #                         print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
        #
        #                         if item_number + 2 >= index >= item_number:
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         elif index < item_number:
        #                             print(item_number - index, '칸 올려요')
        #                             for i in range(item_number - index):
        #                                 Updown(account, 'down1')
        #                                 time.sleep(0.5)
        #
        #                             item_number = item_number - (item_number - index)
        #
        #                             click_item(account, index - item_number)
        #                             z = Check_available_slots(account)
        #                             if z <= 1:
        #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        #                                 print('리스트 full!3')
        #                                 time.sleep(0.5)
        #                                 Skip_Next(account, prod_direction_left)
        #                                 break
        #                         else:
        #                             print('조건이 이상해요4')
        #                 else:
        #                     print('smith, 7렙까지도 아니고 6렙까지도 아니다!')
        #
        #                 Skip_Next(account, prod_direction_left)
        #                 break
        #             if (item_number >= 6):
        #                 Updown(account, 'down1')
        #                 time.sleep(0.5)

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
    #     if not bProdHigh or jelly_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (jelly_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'jelly', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'jelly', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'jelly', prod_direction_left)
    #
    #                     if jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         while True:
    #                             to_make = 5
    #                             print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             else:
    #                                 print('조건이 이상해요1')
    #                     elif not jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         while True:
    #                             to_make = 4
    #                             print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             else:
    #                                 print('조건이 이상해요2')
    #                     else:
    #                         print('jelly, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'jelly', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'jelly', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'jelly', prod_direction_left)
    #
    #                     if jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         while True:
    #                             to_make = 5
    #                             print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                                 break
    #                             else:
    #                                 print('조건이 이상해요3')
    #                     elif not jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
    #                         while True:
    #                             to_make = 4
    #                             print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             else:
    #                                 print('조건이 이상해요4')
    #                     else:
    #                         print('jelly, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #
    # elif pix_prod == pix_rollc:
    # # if pix_prod == pix_rollc:
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
    #     if not bProdHigh or rollc_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (rollc_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'rollc', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'rollc', prod_direction_left)
    #
    #                     if rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         while True:
    #                             if keyboard.is_pressed('end'):
    #                                 break
    #                             to_make = 4
    #                             print('%s렙까지 만들어요 : '% to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                                 break
    #                             else:
    #                                 print('조건이 이상해요1')
    #                     elif not rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         while True:
    #                             if keyboard.is_pressed('end'):
    #                                 break
    #                             to_make = 3
    #                             print('%s렙까지 만들어요 : ' % to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                                 break
    #                             else:
    #                                 print('조건이 이상해요2')
    #                     else:
    #                         print('rollc, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    #                 if (item_number >= 3):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'rollc', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'rollc', prod_direction_left)
    #
    #                     if rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         while True:
    #                             if keyboard.is_pressed('end'):
    #                                 break
    #                             to_make = 4
    #                             print('%s렙까지 만들어요 : ' % to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                                 break
    #                             else:
    #                                 print('조건이 이상해요3')
    #                     elif not rollc_lev4 and rollc_lev3 and rollc_lev2 and rollc_lev1:
    #                         while True:
    #                             if keyboard.is_pressed('end'):
    #                                 break
    #                             to_make = 3
    #                             print('%s렙까지 만들어요 : ' % to_make, target_numb[0:to_make])
    #                             tmp = max(target_numb[0:to_make])
    #                             index = target_numb[0:to_make].index(tmp) + 1
    #                             print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                             if item_number + 2 >= index >= item_number:
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                             elif index < item_number:
    #                                 print(item_number - index, '칸 올려요')
    #                                 for i in range(item_number - index):
    #                                     Updown(account, 'down1')
    #                                     time.sleep(0.5)
    #
    #                                 item_number = item_number - (item_number - index)
    #                                 click_item(account, index - item_number)
    #                                 z = Check_available_slots(account)
    #                                 if z <= 1:
    #                                     # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                     print('리스트 full!3')
    #                                     time.sleep(0.5)
    #                                     Skip_Next(account, prod_direction_left)
    #                                     break
    #                                 break
    #                             else:
    #                                 print('조건이 이상해요4')
    #                     else:
    #                         print('rollc, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #
    #                 if (item_number >= 3):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #
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
    #     if not bProdHigh or doye_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (doye_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'doye', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'doye', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('doye, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 3):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'doye', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'doye', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('doye, 4렙까지도 아니고 3렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 3):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #
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
    #     if not bProdHigh or bread_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (bread_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('bread, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'bread', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('bread, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #     if not bProdHigh or jampy_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (jampy_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('jampy, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'jampy', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                             continue
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('jampy, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #     if not bProdHigh or flower_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (flower_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('flower, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 4):
    #                     three_prod_action_last_one(account, 'normal', 'flower', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요4')
    #                     else:
    #                         print('flower, 6렙까지도 아니고 5렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 5):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #
    #
    elif pix_prod == pix_milky:
        pix_error_count = 0
        print('milky!')
        if not bmilkycompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'milky_stby_lv1.png', 'milky_stby_lv2.png', 'milky_stby_lv3.png', milky_lev1, milky_lev2, milky_lev3, prod_direction_left):
                bmilkycompleted = True
        else:
            Skip_Next(account, prod_direction_left)

    elif pix_prod == pix_latte:
        pix_error_count = 0
        print('latte!')
        if not blattecompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'latte_stby_lv1.png', 'latte_stby_lv2.png', 'latte_stby_lv3.png', latte_lev1, latte_lev2, latte_lev3, prod_direction_left):
                blattecompleted = True
        else:
            Skip_Next(account, prod_direction_left)

    elif pix_prod == pix_dolls:
        pix_error_count = 0
        print('dolls!')
        if not bdollcompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'dolls_stby_lv1.png', 'dolls_stby_lv2.png', 'dolls_stby_lv3.png', dolls_lev1, dolls_lev2, dolls_lev3, prod_direction_left):
                bdollcompleted = True
        else:
            Skip_Next(account, prod_direction_left)

    elif pix_prod == pix_beer:
        pix_error_count = 0
        print('beer!')
        if not bbeercompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'beer_stby_lv1.png', 'beer_stby_lv2.png', 'beer_stby_lv3.png', beer_lev1, beer_lev2, beer_lev3, prod_direction_left):
                bbeercompleted = True
        else:
            Skip_Next(account, prod_direction_left)

    elif pix_prod == pix_muffin:
        pix_error_count = 0
        print('muffin!')
        if not bmuffincompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'muffin_stby_lv1.png', 'muffin_stby_lv2.png', 'muffin_stby_lv3.png', muffin_lev1, muffin_lev2, muffin_lev3, prod_direction_left):
                bmuffincompleted = True
        else:
            Skip_Next(account, prod_direction_left)

    elif pix_prod == pix_jewel:
        pix_error_count = 0
        print('jewel!')
        if not bjewelcompleted:
            # print('생산 확인...')
            if not three_prod_action(account, 'jewel_stby_lv1.png', 'jewel_stby_lv2.png', 'jewel_stby_lv3.png', jewel_lev1, jewel_lev2, jewel_lev3, prod_direction_left):
                bjewelcompleted = True
        else:
            Skip_Next(account, prod_direction_left)
    #
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
    #     if not bProdHigh or magic_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (magic_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'magic', 'magic',prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'magic', 'magic', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'magic', 'magic', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('magic, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
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
    #                     three_prod_action_new(account, 'magic', 'magic', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'magic', 'magic', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'magic', 'magic', prod_direction_left)
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
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
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('magic, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #
    # elif pix_prod == pix_icecream:
    #     print('icecream!')
    #     pix_error_count = 0
    #     z = Check_available_slots(account)
    #     if z <= 1:
    #         # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #         print('리스트 full!3')
    #         time.sleep(0.5)
    #         Skip_Next(account, prod_direction_left)
    #         continue
    #
    #     if not bProdHigh or icecream_num == 1:
    #         # 작업 순방향 시작 ------------------ 이건 잘 안도는듯?
    #         if not (icecream_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d' % item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'icecream', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'icecream', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'icecream', prod_direction_left)
    #
    #                     if icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('icecream, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)
    #         break
    #     if bProdHigh and icecream_num == 2:  # 첫 번째 건물 작업
    #         # 작업 순방향 시작  ---------------------------- 이게 진짜 건물 사이클인듯(건물이 2개니까!)
    #         if not (icecream_lev1 == 0):
    #             while True:
    #                 if keyboard.is_pressed('end'):
    #                     break
    #                 item_number = check_item_number(account, 'top')
    #                 print('item_number = %d'%item_number, ', target_numb = ', target_numb)
    #                 if (item_number == 1):
    #                     three_prod_action_new(account, 'normal', 'icecream', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 2):
    #                     three_prod_action_last_one(account, 'normal', 'icecream', prod_direction_left)
    #                     Updown(account, 'up1')
    #                     time.sleep(0.5)
    #                 if (item_number == 3):
    #                     three_prod_action_last_one(account, 'normal', 'icecream', prod_direction_left)
    #
    #                     if icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
    #                         print('5렙까지 만들어요')
    #                         to_make = 5
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요1')
    #                     elif not icecream_lev5 and icecream_lev4 and icecream_lev3 and icecream_lev2 and icecream_lev1:
    #                         print('4렙까지 만들어요')
    #                         to_make = 4
    #                         print(target_numb[0:to_make])
    #                         tmp = max(target_numb[0:to_make])
    #                         index = target_numb[0:to_make].index(tmp) + 1
    #                         print('%s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
    #
    #                         if item_number + 2 >= index >= item_number:
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         elif index < item_number:
    #                             print(item_number - index, '칸 올려요')
    #                             for i in range(item_number - index):
    #                                 Updown(account, 'down1')
    #                                 time.sleep(0.5)
    #                             item_number = item_number - (item_number - index)
    #                             click_item(account, index - item_number)
    #                             z = Check_available_slots(account)
    #                             if z <= 1:
    #                                 # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
    #                                 print('리스트 full!3')
    #                                 time.sleep(0.5)
    #                                 Skip_Next(account, prod_direction_left)
    #                                 break
    #                         else:
    #                             print('조건이 이상해요2')
    #                     else:
    #                         print('icecream, 5렙까지도 아니고 4렙까지도 아니다!')
    #
    #                     Skip_Next(account, prod_direction_left)
    #                     break
    #                 if (item_number >= 4):
    #                     Updown(account, 'down1')
    #                     time.sleep(0.5)

    else:
        print('건물 안에서... 이게 아니라면... 내려! pix_prod:',pix_prod)
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