import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
from datetime import datetime
import random



def Skip_Next(account, prod_direction_left):
    if prod_direction_left:  # 이레가 수정햇서
        pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
        time.sleep(0.5)
        prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95, region=(339 + (account // 2) * 960, 253 + (account % 2) * 540, 175, 87))
        time.sleep(1)
        if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
            print('욕심을 버리시오 중생이여..')
            pag.click(455 + (account // 2) * 960, 379 + (account % 2) * 540)
            time.sleep(0.3)
            pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
            time.sleep(0.3)
    else:
        pag.click(485 + (account // 2) * 960, 280 + (account % 2) * 540)
        time.sleep(0.3)

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)
    # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
    # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
    dotdotdot4 = pag.locateCenterOnScreen('dotdotdot4.png', confidence=0.814, region=(150 + (account // 2) * 960, 200 + (account % 2) * 540, 360, 160))

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
        print('이 숫자는 한 자릿 수 입니다!')
    else:
        pix_jaritsu2_1 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
        # print((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))
        # print('pix_자릿수2_1:', pix_jaritsu2_1)
        pix_jaritsu2_2 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 하
        # print((prod_pin[0] + 14, prod_pin[1] + 81 + 153 * (line - 1)))
        # print('pix_자릿수2_2:', pix_jaritsu2_2)
        if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
            print('이 숫자는 두 자릿 수 입니다!')
            pos_numb = 2
        else:
            print('이 숫자는 세 자릿 수 입니다!')
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
        print('두 자릿 수 10자리 범위', pos_numb)
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
        print('두자릿수 1자리 범위:', pos_numb)
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
        print('현재 재고는 =', its_number)
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
        print('현재 재고는 =', its_number)
        return its_number

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
        if building == 'normal':
            list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.85, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
        elif building == 'magic':
            list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 마법공방 건물일때

        # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
        list_numb2 = list(list_numb1)
        # print(list_numb2)

        if not list_numb2:
            print('안보여!')
            Updown(account, 'down1')
            break
        if 75 <= list_numb2[0][1] <= 102:
            print('적당한 위치구먼!')
            return
        elif 103 <= list_numb2[0][1] <= 235:
            print('윗쪽으로 올립시다')
            a = 153 + 90 - int(list_numb2[0][1])
            print(a)
            Updown_new(account, 'down_little', a)


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
        list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 150))  # 일반 건물일때
    elif building == 'magic':
        list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 385 + (account % 2) * 540, 105, 150))  # 마법공방 건물일때

    list_numb2 = list(list_numb1)
    # print('list_numb = %s'%list_numb2)
    if (list_numb2):
        prod_pin = (list_numb2[0][0] + 5, list_numb2[0][1] + 7)
        aa = check_item_number(account, 'bot')
        a = check_num1 - numb_new_recog_new(prod_pin, account)
        target_numb[aa - 1] = a
        # print(target_numb)


# 생산 제일 많이 해야하는 아이템 클릭하는 함수
def click_item(account, index1):
    global index
    index1 = (index1) % 4
    print('함수 안의 index1:', index1)

    click_al = pag.locateCenterOnScreen('prod_click_al.PNG', confidence=0.9, region=(690 + (account // 2) * 960, 160 + 153 * (index1) + (account % 2) * 540, 175, 153))
    if not (click_al):  # 초록바탕의 제작 버튼이 보이는가?
        print('click_al이 없어요. y값:', 160 + 153 * (index1) + (account % 2) * 540)
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

    if (index1) == 0:  # 첫번째 줄 클릭
        print('현재 화면의 1번째 아이템 클릭')
    elif (index1) == 1:  # 두번째 줄 클릭
        print('현재 화면의 2번째 아이템 클릭')
    elif (index1) == 2:  # 세번째 줄 클릭
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

# 화면에 보이는 아이템 3개 모두 확인하는 함수
# def three_prod_action_new(account, building, check_num1, check_num2, check_num3, prod_direction_left):
#     start_time = time.time()
#     time.sleep(0.5)
#
#     cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#     if (cond_network):
#         pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#         time.sleep(0.3)
#
#     # 제작 아이템 화면 잘 보이는지 확인
#     prod_default_screen(account, building)
#
#     if building == 'normal':
#         list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))  # 일반 건물일때
#     elif building == 'magic':
#         list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))  # 마법공방 건물일때
#
#     list_numb2 = list(list_numb1)
#     # print(list_numb2)
#
#     for i in range(len(list_numb2)):
#         if i == 0:
#             prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
#             aa = check_item_number(account, 'top')
#             a = check_num1 - numb_new_recog_new(prod_pin, account)
#             target_numb[aa-1] = a
#             # print(target_numb)
#         if i == 1:
#             prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
#             bb = check_item_number(account, 'top')+1
#             a = check_num2 - numb_new_recog_new(prod_pin, account)
#             target_numb[bb-1] = a
#             # print(target_numb)
#         if i == 2:
#             prod_pin = (list_numb2[i][0] + 5, list_numb2[i][1] + 7)
#             cc = check_item_number(account, 'bot')
#             a = check_num3 - numb_new_recog_new(prod_pin, account)
#             target_numb[cc-1] = a
#             # print(target_numb)
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
        print('현재 재고는 =', its_number)
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
def three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left):
    start_time = time.time()

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # # 풀리스트인 경우 넘어감
    z0 = pag.locateCenterOnScreen('z0.png', confidence=0.95, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
    z1 = pag.locateCenterOnScreen('z1.png', confidence=0.95, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
    if z0 or z1:
        # if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7) or (prod_full_list8):
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
        z0 = pag.locateCenterOnScreen('z0.png', confidence=0.95, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
        z1 = pag.locateCenterOnScreen('z1.png', confidence=0.95, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
        if z0 or z1:
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


#
# milky_num_C = 2  # 우유 가공소 건물 수
# milky_lev1_C = 100  # 크림
# milky_lev2_C = 100  # 버터
# milky_lev3_C = 100  # 수제 치즈
# milky_lev1 = milky_lev1_C  # 크림
# milky_lev2 = milky_lev2_C  # 버터
# milky_lev3 = milky_lev3_C  # 수제 치즈
#
# muffin_num_A = 1  # 퐁 드 파티세리 건물 수
# muffin_lev1_A = 25  # 으스스 머핀
# muffin_lev2_A = 25  # 생딸기 케이크
# muffin_lev3_A = 25  # 파티파티 쉬폰케이크
# muffin_lev1 = muffin_lev1_A  # 크림
# muffin_lev2 = muffin_lev2_A  # 버터
# muffin_lev3 = muffin_lev3_A  # 수제 치즈
#
# prod_direction_left = True
# # three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left)
# account = 2
# if not three_prod_action(account, 'milky_stby_lv1.png', 'milky_stby_lv2.png', 'milky_stby_lv3.png', milky_lev1, milky_lev2, milky_lev3, prod_direction_left):
#     bmilkycompleted = True
# # if not three_prod_action(account, 'muffin_stby_lv1.png', 'muffin_stby_lv2.png', 'muffin_stby_lv3.png', muffin_lev1, muffin_lev2, muffin_lev3, prod_direction_left):
# #     bmuffincompleted = True



# def find_num_x(image, x1, x2, list_output, account):
#     prod_num = pag.locateAllOnScreen(image, confidence=0.85, region=(x1, 440 + (account % 2) * 540, x2 - x1, 26))
#     num_list = list(prod_num)
#     if len(num_list) != 0:
#         for p in num_list:
#             ctr = pag.center(p)
#             list_output.append(ctr)
#     # print(image,list_output)
#     return
#
#
#
# def find_num(image, yPosition, list_output):
#     prod_num = pag.locateAllOnScreen(image, confidence=0.85, grayscale=True, region=(620 + (account // 2) * 960, yPosition + 20, 33, 18))
#     num_list = list(prod_num)
#     if len(num_list) != 0:
#         for p in num_list:
#             ctr = pag.center(p)
#             list_output.append(ctr)
#     return
#
#
# def del_duplication(dif, list_origin):
#     list_origin.sort()
#     list_origin = list(set(list_origin))
#     del_list = list()
#     if len(list_origin) > 1:  # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
#         for i in range(len(list_origin) - 1):
#             for j in range(len(list_origin) - 1 - i):
#                 # if abs(int(list_origin[i][0])-int(list_origin[i+1+j][0])) < dif and abs(int(list_origin[i][1])-int(list_origin[i+1+j][1])) < dif:
#                 if abs(int(list_origin[i][0]) - int(list_origin[i + 1 + j][0])) < dif:
#                     del_list.append(list_origin[i])
#                 if list_origin[i][0] == list_origin[i + 1 + j][0]:
#                     del_list.append(list_origin[i])
#     list_origin = [x for x in list_origin if x not in del_list]
#     list_origin.sort()
#     return list_origin
#
# def prod_check(image, account):
#     error_count = 0
#     while True:
#         if keyboard.is_pressed('end'):
#             break
#         its_location = pag.locateCenterOnScreen(image, region=(590 + (account // 2) * 960, 83 + (account % 2) * 540, 30, 455), confidence=0.95)
#         if not (its_location):
#             error_count = error_count + 1
#             time.sleep(0.5)
#             pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
#             pag.mouseDown()
#             time.sleep(0.5)
#             pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 5, 1)  # 153인데 20 더 여유줌
#             time.sleep(1)
#             pag.mouseUp()
#             time.sleep(1)
#             if error_count > 2:
#                 print('두 번 읽었지만 읽지 못했습니다. 999로 가정합니다.')
#                 return 9999
#         else:
#             break
#     if (its_location):  # 해당 이미지를 찾은 경우
#         its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
#         list_real_num = list()  # 실제값 계산을 위한 리스트 생성
#         list_num_0 = list()
#         list_num_1 = list()
#         list_num_2 = list()
#         list_num_3 = list()
#         list_num_4 = list()
#         list_num_5 = list()
#         list_num_6 = list()
#         list_num_7 = list()
#         list_num_8 = list()
#         list_num_9 = list()
#         # 으아아아아 숫자 가져와아아아아
#         find_num('prod_0.png', its_location[1], list_num_0)
#         find_num('prod_1.png', its_location[1], list_num_1)
#         # find_num('prod_1_1.png', its_location[1], list_num_1)   # 이레가 삭제햇서요...
#         find_num('prod_2.png', its_location[1], list_num_2)
#         find_num('prod_3.png', its_location[1], list_num_3)
#         find_num('prod_3_1.png', its_location[1], list_num_3)
#         find_num('prod_4.png', its_location[1], list_num_4)
#         find_num('prod_4_1.png', its_location[1], list_num_4)
#         find_num('prod_4_2.png', its_location[1], list_num_4)
#         find_num('prod_5.png', its_location[1], list_num_5)
#         find_num('prod_6.png', its_location[1], list_num_6)
#         find_num('prod_7.png', its_location[1], list_num_7)
#         find_num('prod_8.png', its_location[1], list_num_8)
#         find_num('prod_8_1.png', its_location[1], list_num_8)
#         find_num('prod_9.png', its_location[1], list_num_9)
#         find_num('prod_9_1.png', its_location[1], list_num_9)
#         list_num_0 = del_duplication(3, list_num_0)
#         list_num_1 = del_duplication(3, list_num_1)
#         list_num_2 = del_duplication(3, list_num_2)
#         list_num_3 = del_duplication(3, list_num_3)
#         list_num_4 = del_duplication(3, list_num_4)
#         list_num_5 = del_duplication(3, list_num_5)
#         list_num_6 = del_duplication(3, list_num_6)
#         list_num_7 = del_duplication(3, list_num_7)
#         list_num_8 = del_duplication(3, list_num_8)
#         list_num_9 = del_duplication(3, list_num_9)
#         if (list_num_0):  # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
#             for p in list_num_0:
#                 list_real_num.append((p[0], 0))
#
#         if (list_num_1):
#             for p in list_num_1:
#                 list_real_num.append((p[0], 1))
#
#         if (list_num_2):
#             for p in list_num_2:
#                 list_real_num.append((p[0], 2))
#
#         if (list_num_3):
#             for p in list_num_3:
#                 list_real_num.append((p[0], 3))
#
#         if (list_num_4):
#             for p in list_num_4:
#                 list_real_num.append((p[0], 4))
#
#         if (list_num_5):
#             for p in list_num_5:
#                 list_real_num.append((p[0], 5))
#
#         if (list_num_6):
#             for p in list_num_6:
#                 list_real_num.append((p[0], 6))
#
#         if (list_num_7):
#             for p in list_num_7:
#                 list_real_num.append((p[0], 7))
#
#         if (list_num_8):
#             for p in list_num_8:
#                 list_real_num.append((p[0], 8))
#
#         if (list_num_9):
#             for p in list_num_9:
#                 list_real_num.append((p[0], 9))
#
#         # 지겨운 실제값 리스트를 받았으니
#         list_real_num.sort()  # 추려서
#
#         for i in range(len(list_real_num)):  # 실제 int값으로 변환
#             its_number = its_number + list_real_num[i][1] * 10 ** (len(list_real_num) - i - 1)
#
#         print('현재 재고는 =', its_number)
#         return its_number
#
#
# def Angmu_check(x1, account):
#     print('앵무체크의 x1은?:', x1)
#     trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     trade_slash_real_mini = pag.locateCenterOnScreen('trade_slash_real_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     if (trade_slash):
#         x2 = trade_slash[0]
#         # print('trade_slash:', trade_slash, 'x2:', x2)
#     if (trade_slash_mini):
#         x2 = trade_slash_mini[0]
#         # print('trade_slash_mini:', trade_slash_mini, 'x2:', x2)
#     if (trade_slash_real_mini):
#         x2 = trade_slash_real_mini[0]
#         # print('trade_slash_real_mini:', trade_slash_real_mini, 'x2:', x2)
#     if (not (trade_slash)) and (not (trade_slash_mini)) and (not (trade_slash_real_mini)):
#         # print('/없음')
#         return 0
#     # trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     # trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     # trade_slash_real_mini = pag.locateCenterOnScreen('trade_slash_real_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
#     # if (trade_slash):
#     #     x2 = trade_slash[0]
#     # if (trade_slash_mini):
#     #     x2 = trade_slash_mini[0]
#     # if (trade_slash_real_mini):
#     #     x2 = trade_slash_real_mini[0]
#     # if (not (trade_slash)) and (not (trade_slash_mini)) and (not (trade_slash_real_mini)):
#     #     print('/없음')
#     #     return 0
#
#     its_number = 0  # 숫자 초기화(없는 경우 그대로 유지되겠지?)
#     list_real_num = list()  # 실제값 계산을 위한 리스트 생성
#     list_num_0 = list()
#     list_num_1 = list()
#     list_num_2 = list()
#     list_num_3 = list()
#     list_num_4 = list()
#     list_num_5 = list()
#     list_num_6 = list()
#     list_num_7 = list()
#     list_num_8 = list()
#     list_num_9 = list()
#     # 으아아아아 숫자 가져와아아아아
#     find_num_x('up_th0.png', x1, x2, list_num_0, account)
#     find_num_x('up_th1.png', x1, x2, list_num_1, account)
#     find_num_x('up_th1_1.png', x1, x2, list_num_1, account)
#     find_num_x('up_th2.png', x1, x2, list_num_2, account)
#     find_num_x('up_th3.png', x1, x2, list_num_3, account)
#     find_num_x('up_th3_1.png', x1, x2, list_num_3, account)
#     find_num_x('up_th4.png', x1, x2, list_num_4, account)
#     find_num_x('up_th5.png', x1, x2, list_num_5, account)
#     find_num_x('up_th6.png', x1, x2, list_num_6, account)
#     find_num_x('up_th7.png', x1, x2, list_num_7, account)
#     find_num_x('up_th8.png', x1, x2, list_num_8, account)
#     find_num_x('up_th9.png', x1, x2, list_num_9, account)
#     find_num_x('up_ths_0.png', x1, x2, list_num_0, account)
#     find_num_x('up_thm_0.png', x1, x2, list_num_0, account)
#     find_num_x('up_ths_0_1.png', x1, x2, list_num_0, account)
#     find_num_x('up_ths_0_2.png', x1, x2, list_num_0, account)
#     find_num_x('up_ths_1.png', x1, x2, list_num_1, account)
#     find_num_x('up_thm_1.png', x1, x2, list_num_1, account)
#     find_num_x('up_ths_2.png', x1, x2, list_num_2, account)
#     find_num_x('up_ths_2_1.png', x1, x2, list_num_2, account)
#     find_num_x('up_ths_3.png', x1, x2, list_num_3, account)
#     find_num_x('up_thm_3.png', x1, x2, list_num_3, account)
#     find_num_x('up_ths_4.png', x1, x2, list_num_4, account)
#     find_num_x('up_thm_4.png', x1, x2, list_num_4, account)
#     find_num_x('up_ths_5.png', x1, x2, list_num_5, account)
#     find_num_x('up_ths_5_1.png', x1, x2, list_num_5, account)
#     find_num_x('up_ths_6.png', x1, x2, list_num_6, account)
#     find_num_x('up_ths_6_1.png', x1, x2, list_num_6, account)
#     find_num_x('up_ths_7.png', x1, x2, list_num_7, account)
#     find_num_x('up_ths_7_1.png', x1, x2, list_num_7, account)
#     find_num_x('up_ths_8.png', x1, x2, list_num_8, account)
#     find_num_x('up_ths_8_1.png', x1, x2, list_num_8, account)
#     find_num_x('up_ths_8_2.png', x1, x2, list_num_8, account)
#     find_num_x('up_ths_9.png', x1, x2, list_num_9, account)
#     find_num_x('up_thm_9.png', x1, x2, list_num_9, account)
#     find_num_x('up_ths_9_1.png', x1, x2, list_num_9, account)
#     list_num_0 = del_duplication(2, list_num_0)
#     list_num_1 = del_duplication(2, list_num_1)
#     list_num_2 = del_duplication(2, list_num_2)
#     list_num_3 = del_duplication(2, list_num_3)
#     list_num_4 = del_duplication(2, list_num_4)
#     list_num_5 = del_duplication(2, list_num_5)
#     list_num_6 = del_duplication(2, list_num_6)
#     list_num_7 = del_duplication(2, list_num_7)
#     list_num_8 = del_duplication(2, list_num_8)
#     list_num_9 = del_duplication(2, list_num_9)
#     if (list_num_0):  # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
#         for p in list_num_0:
#             list_real_num.append((p[0], 0))
#
#     if (list_num_1):
#         for p in list_num_1:
#             list_real_num.append((p[0], 1))
#         print('append 후 list_1', list_num_1)
#     if (list_num_2):
#         for p in list_num_2:
#             list_real_num.append((p[0], 2))
#
#     if (list_num_3):
#         for p in list_num_3:
#             list_real_num.append((p[0], 3))
#
#     if (list_num_4):
#         for p in list_num_4:
#             list_real_num.append((p[0], 4))
#
#     if (list_num_5):
#         for p in list_num_5:
#             list_real_num.append((p[0], 5))
#
#     if (list_num_6):
#         for p in list_num_6:
#             list_real_num.append((p[0], 6))
#
#     if (list_num_7):
#         for p in list_num_7:
#             list_real_num.append((p[0], 7))
#
#     if (list_num_8):
#         for p in list_num_8:
#             list_real_num.append((p[0], 8))
#
#     if (list_num_9):
#         for p in list_num_9:
#             list_real_num.append((p[0], 9))
#
#     # 지겨운 실제값 리스트를 받았으니
#     list_real_num.sort()  # 추려서
#
#     # print('sort 이후',list_real_num)
#
#     # del_list = list()
#     # if len(list_real_num) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
#     #     for i in range(len(list_real_num)-1):
#     #         for j in range(len(list_real_num)-1-i):
#     #             if abs(int(list_real_num[i][0])-int(list_real_num[i+1+j][0])) < 2 and abs(int(list_real_num[i][1])-int(list_real_num[i+1+j][1])) < 2:
#     #                 del_list.append(list_real_num[i])
#     # list_real_num = [x for x in list_real_num if x not in del_list]
#
#     # print('set 이전', list_real_num)
#
#     # list_real_num1 = set(list_real_num)
#
#     # print('set 이후',list_real_num1)
#
#     for i in range(len(list_real_num)):  # 실제 int값으로 변환
#         its_number = its_number + list_real_num[i][1] * 10 ** (len(list_real_num) - i - 1)
#
#     print('현재 재고는 =', its_number)
#     return its_number
#
# def Angmu_Action(prd_name, ctr, account):
#     cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#     if (cond_network):
#         pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#         time.sleep(0.3)
#     # print('ctr[0]:', ctr[0])
#     if (prd_name == 'trade_star.png'):
#         # print('별조각은 무조건 삽니다')
#         itssoyo = pag.locateCenterOnScreen('trade_star.png', confidence=0.85)
#         if itssoyo:
#             pag.click(itssoyo)
#             time.sleep(1)
#             pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#             time.sleep(2)
#             trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472 + (account // 2) * 960, 221 + (account % 2) * 540, 25, 17))
#             if (trade_not_enough):
#                 print('앗 부족..')
#                 pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 145 + 13) + (account % 2) * 540, 2, 0.3)
#             return True
#         else:
#             # print('사지 않고 넘어갑니다!')
#             return True
#     item_check = pag.locateCenterOnScreen(prd_name, confidence=0.82, region=(ctr[0] + 35, 345 + (account % 2) * 540, 60, 50))
#     if (item_check):
#         if Angmu_check(ctr[0] + 9, account) > 324:
#             # print('어머 이건 사야해!')
#             print('어머 이건 사야해! item_check', item_check)
#             pag.click(item_check)
#             time.sleep(1)
#             pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#             time.sleep(2)
#             trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472 + (account // 2) * 960, 221 + (account % 2) * 540, 25, 17))
#             if (trade_not_enough):
#                 print('앗 부족..')
#                 pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 145 + 13) + (account % 2) * 540, 2, 0.3)
#             return True
#
#         else:
#             print('사지 않고 넘어갑니다!')
#             return True
#
#     else:
#         return False
#
#
# def Angmu_Aft_Refresh(account):
#     Scroll_count = 0
#     start_time = time.time()
#     while True:
#         cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#         if (cond_network):
#             pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#             time.sleep(0.3)
#
#         now_time = time.time()
#         if keyboard.is_pressed('end'):
#             print('end 누름')
#             break
#
#         # if now_time - start_time > 300:
#         #     End_kkd(account)
#         #     Kingdom_ready(account, 'kkd_out')
#
#         if Scroll_count == 0:
#             print('기둥동네예요!')
#             trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#             trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#             trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#             # trade_tro_1 = pag.locateCenterOnScreen('trade_tro_1.png', confidence=0.85, region=(2,350+account*540,917,40))
#             # trade_tro_2 = pag.locateCenterOnScreen('trade_tro_2.png', confidence=0.85, region=(2,350+account*540,917,40))
#
#             if (trade_kidung):
#                 kidung_numb = Angmu_check(trade_kidung[0] - 26, account)
#             else:
#                 kidung_numb = 0
#             if (trade_block):
#                 block_numb = Angmu_check(trade_block[0] - 26, account)
#             else:
#                 block_numb = 0
#             if (trade_nachimban):
#                 nachimban_numb = Angmu_check(trade_nachimban[0] - 26, account)
#             else:
#                 nachimban_numb = 0
#             max_numb = max(kidung_numb, block_numb, nachimban_numb)
#             if kidung_numb > 0 and kidung_numb == max_numb:
#                 pag.click(trade_kidung)
#                 time.sleep(0.5)
#                 pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#                 time.sleep(2)
#             if block_numb > 0 and block_numb == max_numb:
#                 pag.click(trade_block)
#                 time.sleep(0.5)
#                 pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#                 time.sleep(2)
#             if nachimban_numb > 0 and nachimban_numb == max_numb:
#                 pag.click(trade_nachimban)
#                 time.sleep(0.5)
#                 pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#                 time.sleep(2)
#             # Angmu_Action('trade_tro_1', trade_tro_1)
#             # Angmu_Action('trade_tro_2', trade_tro_2)
#
#         if Scroll_count == 1:
#             print('스크롤 ==', Scroll_count)
#             # trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26))
#             trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26)) # 0.943하면 잘 못읽나?
#             trade_baseline_list = list(trade_baseline)
#             # print('스크롤 1의 trade_baseline_list:', trade_baseline_list)
#             if len(trade_baseline_list) != 0:
#                 for p in trade_baseline_list:
#                     ctr = pag.center(p)
#                     # 범위 내 조건 확인
#                     if Angmu_Action('trade_assist_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_assist_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_bomb_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_bomb_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_fist_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_fist_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_recovery_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_recovery_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_shield_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_shield_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_shooting_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_shooting_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_staff_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_staff_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_sword_lv1.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_sword_lv2.png', ctr, account):
#                         print('판별 완료', ctr)
#                     elif Angmu_Action('trade_star.png', ctr, account):
#                         print('별조각 판별 완료1', ctr)
#                     else:
#                         print('여긴 어디 나는 누구?')
#
#         if 5 > Scroll_count >= 1:
#             print('스크롤 ==', Scroll_count)
#             trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26))
#             trade_baseline_list = list(trade_baseline)
#             print('trade_baseline_list:', trade_baseline_list)
#             if len(trade_baseline_list) != 0:
#                 for p in trade_baseline_list:
#                     ctr = pag.center(p)
#                     # print('생산품까지 확인')
#                     print('생산품까지 확인, ctr:', ctr)
#                     if (account) == 0:
#                         if Angmu_Action('trade_cotton.png', ctr, account):
#                             print('솜 판별 완료', ctr)
#                         elif Angmu_Action('trade_berry.png', ctr, account):
#                             print('베리 판별 완료', ctr)
#                         # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                         #     print('판별 완료',ctr)
#                         elif Angmu_Action('trade_milk.png', ctr, account):
#                             print('우유 판별 완료',ctr)
#                         elif Angmu_Action('trade_star.png', ctr, account):
#                             print('별조각 판별 완료', ctr)
#                         else:
#                             print('여긴 어디 나는 누구 계정0')
#                     if (account) == 1:
#                         if Angmu_Action('trade_berry.png', ctr, account):
#                             print('베리 판별 완료', ctr)
#                         elif Angmu_Action('trade_cotton.png', ctr, account):
#                             print('솜 판별 완료',ctr)
#                         # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                         #     print('판별 완료',ctr)
#                         # elif Angmu_Action('trade_milk.png', ctr, account):
#                         #     print('판별 완료',ctr)
#                         elif Angmu_Action('trade_star.png', ctr, account):
#                             print('별조각 판별 완료', ctr)
#                         else:
#                             print('여긴 어디 나는 누구 계정1')
#                     if (account) == 2:
#                         if Angmu_Action('trade_berry.png', ctr, account):
#                             print('베리 판별 완료', ctr)
#                         elif Angmu_Action('trade_cotton.png', ctr, account):
#                             print('솜 판별 완료',ctr)
#                         # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                         #     print('판별 완료',ctr)
#                         # elif Angmu_Action('trade_milk.png', ctr, account):
#                         #     print('판별 완료',ctr)
#                         elif Angmu_Action('trade_star.png', ctr, account):
#                             print('별조각 판별 완료', ctr)
#                         else:
#                             print('여긴 어디 나는 누구 계정2')
#
#         # if Scroll_count >= 2:
#         #     print('아이고 힘들다 2~')
#         #     trade_assist_lv3 = pag.locateCenterOnScreen('trade_assist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_bomb_lv3 = pag.locateCenterOnScreen('trade_bomb_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_fist_lv3 = pag.locateCenterOnScreen('trade_fist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_recovery_lv3 = pag.locateCenterOnScreen('trade_recovery_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_shield_lv3 = pag.locateCenterOnScreen('trade_shield_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_shooting_lv3 = pag.locateCenterOnScreen('trade_shooting_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_staff_lv3 = pag.locateCenterOnScreen('trade_staff_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#         #     trade_sword_lv3 = pag.locateCenterOnScreen('trade_sword_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#
#         # 드래그드래그
#         print('드래그')
#         pag.moveTo(random.randint(786, 820) + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#         # print('drag1', random.randint(786, 820) + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#         pag.mouseDown()
#         time.sleep(0.5)
#         pag.moveTo(random.randint(786, 820) - 150 * 4 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 5)  # 153인데 20 더 여유줌
#         # print('drag2', random.randint(786, 820) - 157 * 4 + (account // 2) * 960, random.randint(474 + (account % 2) * 540 , 481 + (account % 2) * 540))
#         time.sleep(0.5)
#         pag.mouseUp()
#         time.sleep(0.5)
#
#         # ++ 작업 후 >= 3으로변경
#         if Scroll_count >= 4:
#             print('완료')
#             pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#             time.sleep(0.1)
#             pag.hotkey('esc')
#             time.sleep(2)
#             pag.hotkey('esc')
#             time.sleep(6)
#             return
#
#         start_lineup = time.time()
#         while True:
#             if keyboard.is_pressed('end'):
#                 print('end 누름')
#                 break
#             now_lineup = time.time()
#             if now_lineup - start_lineup > 20:
#                 print('뭐얏...', '현재시간:', datetime.now().strftime('%H:%M:%S'))
#                 Scroll_count = Scroll_count + 1
#                 break
#             if now_lineup - start_lineup > 60:
#                 print('뭐얏...111', '현재시간:', datetime.now().strftime('%H:%M:%S'))
#                 # Kingdom_ready(account, 'kkd_out')
#                 return
#
#             cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#             if (cond_network):
#                 pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#                 time.sleep(0.3)
#
#             cond_trade_angmu_confirm = pag.locateCenterOnScreen('cond_trade_angmu_confirm.png', confidence=0.85, region=(420 + (account // 2) * 960, 80 + (account % 2) * 540, 58, 33))  # 해상무역센터 앵무 교역소 위치 확인
#             if not (cond_trade_angmu_confirm):
#                 print('튕기거나 빠져나갔나봐요...')
#                 # Kingdom_ready(account, 'kkd_out')
#                 return
#
#
#             trade_baseline_gray = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#             if (trade_baseline_gray):
#                 if (92 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + 157 + (account // 2) * 960):
#                     Scroll_count = Scroll_count + 1
#                     break
#                 else:                 # 아니면 살짝 왼쪽으로 돌려서 영점조정
#                     pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#                     pag.mouseDown()
#                     time.sleep(0.5)
#                     pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
#                     time.sleep(0.5)
#                     trade_baseline_gray_new = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                     if (trade_baseline_gray_new):
#                         print('trade_baseline_gray_new:', trade_baseline_gray_new)
#                         pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_gray_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
#                     time.sleep(0.5)
#                     pag.mouseUp()
#                     time.sleep(0.5)
#
#             trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#             if (trade_baseline):
#                 if (92 + (account // 2) * 960 >= trade_baseline[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline[0] > 70 + 157 + (account // 2) * 960):
#                     Scroll_count = Scroll_count + 1
#                     break
#                 else:            # 약간 왼쪽으로(trade baseline 뉴 찾을때까지) 돌려
#                     pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#                     pag.mouseDown()
#                     time.sleep(0.5)
#                     pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
#                     time.sleep(0.5)
#                     trade_baseline_new = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                     if (trade_baseline_new):
#                         pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
#                     time.sleep(0.5)
#                     pag.mouseUp()
#                     time.sleep(0.5)
#     return print('Angmu_Aft_Refresh 완료!')

# account = 1
# Angmu_Aft_Refresh(account)

# account = 0
# print((account//2)*960)
# print((account%2)*540)
# account = 1
# print((account//2)*960)
# print((account%2)*540)
# account = 2
# print((account//2)*960)
# print((account%2)*540)


#
# wood = 1000
# jelbean = 1500
# sugar = 1200
# a = wood, jelbean, sugar
# print(a)


# # 소원나무
# account=0
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((460 + (account // 2) * 960, 90 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단
# pix_pass_reward_exist = (254, 1, 1)
# print(pix_pass_reward)
#
# account=1
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((460 + (account // 2) * 960, 90 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단# pix_pass_reward_exist = (254, 0, 0)# print(pix_reward)
# pix_pass_reward_exist = (254, 1, 1)
# print(pix_pass_reward)
#
# account=2
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((460 + (account // 2) * 960, 90 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단# pix_pass_reward_exist = (254, 0, 0)# print(pix_reward)
# pix_pass_reward_exist = (254, 1, 1)
# print(pix_pass_reward)










# pix_jokji1_waiting = pag.locateCenterOnScreen('pix_jjokji_waiting.png', confidence=0.8, region=(283+165*0 + (account // 2) * 960, 205 + (account % 2) * 540, 48, 39))
# pix_jokji2_waiting = pag.locateCenterOnScreen('pix_jjokji_waiting.png', confidence=0.8, region=(283+165*1 + (account // 2) * 960, 205 + (account % 2) * 540, 48, 39))
# pix_jokji3_waiting = pag.locateCenterOnScreen('pix_jjokji_waiting.png', confidence=0.8, region=(283+165*2 + (account // 2) * 960, 205 + (account % 2) * 540, 48, 39))
# pix_jokji4_waiting = pag.locateCenterOnScreen('pix_jjokji_waiting.png', confidence=0.8, region=(283+165*3 + (account // 2) * 960, 205 + (account % 2) * 540, 48, 39))
# pix_jokji1 = screen.getpixel((255 + 165*0 + (account // 2) * 960, 182 + (account % 2) * 540))  # 쪽지1
# pix_jokji2 = screen.getpixel((255 + 165*1 + (account // 2) * 960, 181 + (account % 2) * 540))  # 쪽지2
# pix_jokji3 = screen.getpixel((255 + 165*2 + (account // 2) * 960, 181 + (account % 2) * 540))  # 쪽지3
# pix_jokji4 = screen.getpixel((255 + 165*3 + (account // 2) * 960, 181 + (account % 2) * 540))  # 쪽지4
# # pix_jokji1_wait = screen.getpixel((790 - 165 * 3 + (account // 2) * 960, 224 + (account % 2) * 540))  # 쪽지1
# # pix_jokji2_wait = screen.getpixel((790 - 165 * 2 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지2
# # pix_jokji3_wait = screen.getpixel((790 - 165 * 1 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지3
# # pix_jokji4_wait = screen.getpixel((790 - 165 * 0 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지4
# pix_jokji1_wait = screen.getpixel((705 + 85 - 165 * 3 + (account // 2) * 960, 224 + (account % 2) * 540))  # 쪽지1
# pix_jokji2_wait = screen.getpixel((705 + 85 - 165 * 2 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지2
# pix_jokji3_wait = screen.getpixel((705 + 85 - 165 * 1 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지3
# pix_jokji4_wait = screen.getpixel((705 + 85 + (account // 2) * 960, 225 + (account % 2) * 540))  # 쪽지4




# print('pix_jokji1', pix_jokji1)
# print('pix_jokji2', pix_jokji3)
# print('pix_jokji3', pix_jokji3)
# print('pix_jokji4', pix_jokji4)
# print('pix_jokji1_wait', pix_jokji1_wait)
# print('pix_jokji2_wait', pix_jokji2_wait)
# print('pix_jokji3_wait', pix_jokji3_wait)
# print('pix_jokji4_wait', pix_jokji4_wait)

account =1
screen = ImageGrab.grab()
pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
print(pix_status)

# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# print(pix_prod)

# pix_lackof = screen.getpixel((545 + (account // 2) * 960, 745 - 540 + (account % 2) * 540))  # 재료부족창?
# print(pix_lackof)

# pix_status = screen.getpixel((460 + (account // 2) * 960, 90 + (account % 2) * 540))  # 소원나무 확인 뽀인트
# print(pix_status)


def Angmu_Action(prd_name, ctr, account):
    try:
        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
        if (cond_network):
            pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
            time.sleep(0.3)
        # print('ctr[0]:', ctr[0])
        if (prd_name == 'trade_star.png'):
            itssoyo = pag.locateCenterOnScreen('trade_star.png', confidence=0.85)
            if itssoyo:
                pag.click(itssoyo)
                time.sleep(1)
                pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
                time.sleep(2)
                trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472 + (account // 2) * 960, 221 + (account % 2) * 540, 25, 17))
                if (trade_not_enough):
                    print('앗 부족..')
                    pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 145 + 13) + (account % 2) * 540, 2, 0.3)
                return True
            else:
                return True
        item_check = pag.locateCenterOnScreen(prd_name, confidence=0.82, region=(ctr[0] + 35, 345 + (account % 2) * 540, 60, 50))
        if (item_check):
            # if Angmu_check(ctr[0] + 9, account) > 324:
                # print('어머 이건 사야해!')
            if (prd_name == 'trade_star.png') or (prd_name == 'crystal_magic.png') or (prd_name == 'crystal_quick.png') or (prd_name == 'crystal_quick.png') or (prd_name == 'crystal_power.png') or (Angmu_check(ctr[0]+9,account) > 324):
            #     print('어머 이건 사야해!')
                print('어머 이건 사야해! item_check', item_check)
                pag.click(item_check)
                time.sleep(1)
                pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
                time.sleep(2)
                trade_not_enough = pag.locateCenterOnScreen('trade_not_enough.png', confidence=0.85, region=(472 + (account // 2) * 960, 221 + (account % 2) * 540, 25, 17))
                if (trade_not_enough):
                    print('앗 부족..')
                    pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 145 + 13) + (account % 2) * 540, 2, 0.3)
                return True

            else:
                print('사지 않고 넘어갑니다!')
                return True

        else:
            return False
    except:
        print('에러가 났어요! angmu_action')
        # Kingdom_ready(account, 'kkd_out')  # 재부팅

def find_num_x(image, x1, x2, list_output, account):
    prod_num = pag.locateAllOnScreen(image, confidence=0.85, region=(x1, 440 + (account % 2) * 540, x2 - x1, 26))
    num_list = list(prod_num)
    if len(num_list) != 0:
        for p in num_list:
            ctr = pag.center(p)
            list_output.append(ctr)
    # print(image,list_output)
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

def Angmu_check(x1, account):
    print('앵무체크의 x1은?:', x1)
    trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    trade_slash_real_mini = pag.locateCenterOnScreen('trade_slash_real_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    if (trade_slash):
        x2 = trade_slash[0]
        # print('trade_slash:', trade_slash, 'x2:', x2)
    if (trade_slash_mini):
        x2 = trade_slash_mini[0]
        # print('trade_slash_mini:', trade_slash_mini, 'x2:', x2)
    if (trade_slash_real_mini):
        x2 = trade_slash_real_mini[0]
        # print('trade_slash_real_mini:', trade_slash_real_mini, 'x2:', x2)
    if (not (trade_slash)) and (not (trade_slash_mini)) and (not (trade_slash_real_mini)):
        # print('/없음')
        return 0
    # trade_slash = pag.locateCenterOnScreen('trade_slash.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    # trade_slash_mini = pag.locateCenterOnScreen('trade_slash_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    # trade_slash_real_mini = pag.locateCenterOnScreen('trade_slash_real_mini.png', confidence=0.85, region=(x1, 439 + (account % 2) * 540, 90, 28))
    # if (trade_slash):
    #     x2 = trade_slash[0]
    # if (trade_slash_mini):
    #     x2 = trade_slash_mini[0]
    # if (trade_slash_real_mini):
    #     x2 = trade_slash_real_mini[0]
    # if (not (trade_slash)) and (not (trade_slash_mini)) and (not (trade_slash_real_mini)):
    #     print('/없음')
    #     return 0

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
    if (list_num_0):  # Y좌표에 따른 숫자 배치. X좌표에 따라 배치돼야 하므로 X좌표는 살리고 Y좌표는 숫자 계산을 위해 리스트 값으로 대체
        for p in list_num_0:
            list_real_num.append((p[0], 0))

    if (list_num_1):
        for p in list_num_1:
            list_real_num.append((p[0], 1))
        print('append 후 list_1', list_num_1)
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

    # print('sort 이후',list_real_num)

    # del_list = list()
    # if len(list_real_num) > 1: # 중복 확인. 0,1,2,3,4 이런식이면 0과 1~4, 1과 2~4, 3과 4 이런식으로 중복 비교
    #     for i in range(len(list_real_num)-1):
    #         for j in range(len(list_real_num)-1-i):
    #             if abs(int(list_real_num[i][0])-int(list_real_num[i+1+j][0])) < 2 and abs(int(list_real_num[i][1])-int(list_real_num[i+1+j][1])) < 2:
    #                 del_list.append(list_real_num[i])
    # list_real_num = [x for x in list_real_num if x not in del_list]

    # print('set 이전', list_real_num)

    # list_real_num1 = set(list_real_num)

    # print('set 이후',list_real_num1)

    for i in range(len(list_real_num)):  # 실제 int값으로 변환
        its_number = its_number + list_real_num[i][1] * 10 ** (len(list_real_num) - i - 1)

    print('현재 재고는 =', its_number)
    return its_number
# Scroll_count = 0
# start_time = time.time()
# while True:
#     if Scroll_count == 0:
#         print('기둥동네예요!')
#         trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#         trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#         trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
#         # trade_tro_1 = pag.locateCenterOnScreen('trade_tro_1.png', confidence=0.85, region=(2,350+account*540,917,40))
#         # trade_tro_2 = pag.locateCenterOnScreen('trade_tro_2.png', confidence=0.85, region=(2,350+account*540,917,40))
#
#         if (trade_kidung):
#             kidung_numb = Angmu_check(trade_kidung[0] - 26, account)
#         else:
#             kidung_numb = 0
#         if (trade_block):
#             block_numb = Angmu_check(trade_block[0] - 26, account)
#         else:
#             block_numb = 0
#         if (trade_nachimban):
#             nachimban_numb = Angmu_check(trade_nachimban[0] - 26, account)
#         else:
#             nachimban_numb = 0
#         max_numb = max(kidung_numb, block_numb, nachimban_numb)
#         if kidung_numb > 0 and kidung_numb == max_numb:
#             pag.click(trade_kidung)
#             time.sleep(0.5)
#             pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#             time.sleep(2)
#         if block_numb > 0 and block_numb == max_numb:
#             pag.click(trade_block)
#             time.sleep(0.5)
#             pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#             time.sleep(2)
#         if nachimban_numb > 0 and nachimban_numb == max_numb:
#             pag.click(trade_nachimban)
#             time.sleep(0.5)
#             pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
#             time.sleep(2)
#         # Angmu_Action('trade_tro_1', trade_tro_1)
#         # Angmu_Action('trade_tro_2', trade_tro_2)
#
#     if 2 >= Scroll_count >= 1:
#         print('스크롤 ==', Scroll_count)
#         trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26)) # 0.943하면 잘 못읽나?
#         trade_baseline_list = list(trade_baseline)
#         if len(trade_baseline_list) != 0:
#             for p in trade_baseline_list:
#                 ctr = pag.center(p)
#                 # 범위 내 조건 확인
#                 if Angmu_Action('crystal_pure.png', ctr, account):
#                     print('판별 완료',ctr)
#                 elif Angmu_Action('crystal_magic.png', ctr, account):
#                     print('판별 완료',ctr)
#                 elif Angmu_Action('crystal_power.png', ctr, account):
#                     print('판별 완료',ctr)
#                 elif Angmu_Action('crystal_quick.png', ctr, account):
#                     print('판별 완료',ctr)
#                 elif Angmu_Action('trade_assist_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_assist_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_bomb_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_bomb_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_fist_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_fist_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_recovery_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_recovery_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_shield_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_shield_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_shooting_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_shooting_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_staff_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_staff_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_sword_lv1.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_sword_lv2.png', ctr, account):
#                     print('판별 완료', ctr)
#                 elif Angmu_Action('trade_star.png', ctr, account):
#                     print('별조각 판별 완료1', ctr)
#                 elif Angmu_Action('trade_swift_sugar.png', ctr, account):
#                     print('신속의 설탕결정 판별 완료1', ctr)
#                 elif Angmu_Action('trade_pure_sugar.png', ctr, account):
#                     print('순수의 설탕결정 판별 완료1', ctr)
#                 else:
#                     print('여긴 어디 나는 누구?')
#
#     if 5 > Scroll_count >= 1:
#         print('스크롤 ==', Scroll_count)
#         trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26))
#         trade_baseline_list = list(trade_baseline)
#         print('trade_baseline_list:', trade_baseline_list)
#         if len(trade_baseline_list) != 0:
#             for p in trade_baseline_list:
#                 ctr = pag.center(p)
#                 # print('생산품까지 확인')
#                 print('생산품까지 확인, ctr:', ctr)
#                 if (account) == 0:
#                     # if Angmu_Action('trade_cotton.png', ctr, account):
#                     #     print('솜 판별 완료', ctr)
#                     # elif Angmu_Action('trade_berry.png', ctr, account):
#                     #     print('베리 판별 완료', ctr)
#                     # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                     #     print('판별 완료',ctr)
#                     if Angmu_Action('trade_milk.png', ctr, account):
#                         print('우유 판별 완료',ctr)
#                     elif Angmu_Action('trade_star.png', ctr, account):
#                         print('별조각 판별 완료', ctr)
#                     elif Angmu_Action('trade_swift_sugar.png', ctr, account):
#                         print('신속의 설탕결정 판별 완료', ctr)
#                     elif Angmu_Action('trade_pure_sugar.png', ctr, account):
#                         print('순수의 설탕결정 판별 완료', ctr)
#                     else:
#                         print('여긴 어디 나는 누구 계정0')
#                 if (account) == 1:
#                     # if Angmu_Action('trade_berry.png', ctr, account):
#                     #     print('베리 판별 완료', ctr)
#                     if Angmu_Action('trade_cotton.png', ctr, account):
#                         print('솜 판별 완료',ctr)
#                     # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                     #     print('판별 완료',ctr)
#                     # elif Angmu_Action('trade_milk.png', ctr, account):
#                     #     print('판별 완료',ctr)
#                     elif Angmu_Action('trade_star.png', ctr, account):
#                         print('별조각 판별 완료', ctr)
#                     elif Angmu_Action('trade_swift_sugar.png', ctr, account):
#                         print('신속의 설탕결정 판별 완료', ctr)
#                     elif Angmu_Action('trade_pure_sugar.png', ctr, account):
#                         print('순수의 설탕결정 판별 완료', ctr)
#
#                     else:
#                         print('여긴 어디 나는 누구 계정1')
#                 if (account) == 2:
#                     # if Angmu_Action('trade_berry.png', ctr, account):
#                     #     print('베리 판별 완료', ctr)
#                     if Angmu_Action('trade_cotton.png', ctr, account):
#                         print('솜 판별 완료',ctr)
#                     # elif Angmu_Action('trade_biscuit.png', ctr, account):
#                     #     print('판별 완료',ctr)
#                     # elif Angmu_Action('trade_milk.png', ctr, account):
#                     #     print('판별 완료',ctr)
#                     elif Angmu_Action('trade_star.png', ctr, account):
#                         print('별조각 판별 완료', ctr)
#                     elif Angmu_Action('trade_swift_sugar.png', ctr, account):
#                         print('신속의 설탕결정 판별 완료', ctr)
#                     elif Angmu_Action('trade_pure_sugar.png', ctr, account):
#                         print('순수의 설탕결정 판별 완료', ctr)
#
#                     else:
#                         print('여긴 어디 나는 누구 계정2')
#
#     # if Scroll_count >= 2:
#     #     print('아이고 힘들다 2~')
#     #     trade_assist_lv3 = pag.locateCenterOnScreen('trade_assist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_bomb_lv3 = pag.locateCenterOnScreen('trade_bomb_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_fist_lv3 = pag.locateCenterOnScreen('trade_fist_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_recovery_lv3 = pag.locateCenterOnScreen('trade_recovery_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_shield_lv3 = pag.locateCenterOnScreen('trade_shield_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_shooting_lv3 = pag.locateCenterOnScreen('trade_shooting_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_staff_lv3 = pag.locateCenterOnScreen('trade_staff_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#     #     trade_sword_lv3 = pag.locateCenterOnScreen('trade_sword_lv3.png', confidence=0.85, region=(2,350+account*540,917,40))
#
#     # 드래그드래그
#     print('드래그')
#     pag.moveTo(random.randint(786, 820) + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#     pag.mouseDown()
#     time.sleep(0.5)
#     pag.moveTo(random.randint(786, 820) - 150 * 3 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 5)  # 153인데 20 더 여유줌
#     time.sleep(0.5)
#     pag.mouseUp()
#     time.sleep(0.5)
#
#     # ++ 작업 후 >= 3으로변경
#     if Scroll_count >= 4:
#         print('완료')
#         pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#         time.sleep(0.1)
#         pag.hotkey('esc')
#         time.sleep(2)
#         pag.hotkey('esc')
#         time.sleep(6)
#
#
#     start_lineup = time.time()
#     while True:
#         if keyboard.is_pressed('end'):
#             print('end 누름')
#             break
#         now_lineup = time.time()
#         if now_lineup - start_lineup > 20:
#             print('뭐얏...', '현재시간:', datetime.now().strftime('%H:%M:%S'))
#             Scroll_count = Scroll_count + 1
#             break
#         if now_lineup - start_lineup > 60:
#             print('뭐얏...111', '현재시간:', datetime.now().strftime('%H:%M:%S'))
#
#         cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#         if (cond_network):
#             pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#             time.sleep(0.3)
#
#         cond_trade_angmu_confirm = pag.locateCenterOnScreen('cond_trade_angmu_confirm.png', confidence=0.85, region=(420 + (account // 2) * 960, 80 + (account % 2) * 540, 58, 33))  # 해상무역센터 앵무 교역소 위치 확인
#         if not (cond_trade_angmu_confirm):
#             print('튕기거나 빠져나갔나봐요...')
#
#
#         trade_baseline_gray = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#         if (trade_baseline_gray):
#             if (92 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + 157 + (account // 2) * 960):
#                 Scroll_count = Scroll_count + 1
#                 break
#             else:                 # 아니면 살짝 왼쪽으로 돌려서 영점조정
#                 pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#                 pag.mouseDown()
#                 time.sleep(0.5)
#                 pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
#                 time.sleep(0.5)
#                 trade_baseline_gray_new = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 if (trade_baseline_gray_new):
#                     pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_gray_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
#                 time.sleep(0.5)
#                 pag.mouseUp()
#                 time.sleep(0.5)
#
#         trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#         if (trade_baseline):
#             print(92 + 157 + (account // 2) * 960, '>=', trade_baseline[0], '>', 70 + 157 + (account // 2) * 960)
#             if (92 + (account // 2) * 960 >= trade_baseline[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline[0] > 70 + 157 + (account // 2) * 960):
#                 print(92 + 157 + (account // 2) * 960*2 ,'>=', trade_baseline[0] ,'>', 70 + 157 + (account // 2) * 960)
#                 Scroll_count = Scroll_count + 1
#                 break
#             else:            # 약간 왼쪽으로(trade baseline 뉴 찾을때까지) 돌려
#                 pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
#                 pag.mouseDown()
#                 time.sleep(0.5)
#                 pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
#                 time.sleep(0.5)
#                 trade_baseline_new = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 if (trade_baseline_new):
#                     pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
#                 time.sleep(0.5)
#                 pag.mouseUp()
#                 time.sleep(0.5)


def prod_check(image, account):
    error_count = 0
    while True:
        if keyboard.is_pressed('end'):
            break
        its_location = pag.locateCenterOnScreen(image, region=(590 + (account // 2) * 960, 83 + (account % 2) * 540, 30, 455), confidence=0.95)
        if not (its_location):
            error_count = error_count + 1
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
            pag.mouseDown()
            time.sleep(0.5)
            pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 5, 1)  # 153인데 20 더 여유줌
            time.sleep(0.5)
            pag.mouseUp()
            time.sleep(0.8)
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
        find_num('prod_0_1.png', its_location[1], list_num_0)
        find_num('prod_1.png', its_location[1], list_num_1)
        # find_num('prod_1_1.png', its_location[1], list_num_1)   # 이레가 삭제햇서요...
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

        print('현재 재고는 =', its_number)
        return its_number

def find_num(image, yPosition, list_output):
    prod_num = pag.locateAllOnScreen(image, confidence=0.87, grayscale=True, region=(620 + (account // 2) * 960, yPosition + 20, 33, 18))
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
        print('에러가 났어요! Updown')
        # send_telegram_message('Updown에서 에러가 났어요!')
        # Kingdom_ready(account, 'kkd_out')  # 재부팅


def prod_action(image, list_image, account, check_num):
    # print('Prod_action함수!', image, list_image, account, check_num)
    start_time = time.time()
    error_count = 0

    cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
    if (cond_network):
        pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        time.sleep(0.3)

    # cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    # if (cond_halted):
    #     # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
    #     pag.click(cond_halted)
    #     End_kkd(account)
    #     Kingdom_ready(account, 'kkd_out')  # 재부팅
    #     return False

    # cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    # cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    # if (cond_halted1):
    #     pag.click(cond_halted_close)
    #     time.sleep(7)
    #     Kingdom_ready(account, 'kkd_out')  # 재부팅

    prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence=0.945, region=(90 + (account // 2) * 960, 145 + (account % 2) * 540, 24, 20))
    if not (prod_refresh) or (prod_refresh.y):

        time.sleep(0.3)
        ShowTime = True
    else:
        return True

    # cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75 - 10 + (account//2)*960, 200 - 10 + (account%2) * 540, 20, 20))
    # cond_2nd_clear1 = pag.locateCenterOnScreen('cond_2nd_clear1.png', confidence=0.94, region=(75 - 10 + (account // 2) * 960, 200 - 10 + (account % 2) * 540, 20, 20))
    # cond_3rd_clear1 = pag.locateCenterOnScreen('cond_3rd_clear1.png', confidence=0.94, region=(75 - 10 +(account // 2) * 960, 200 - 10 +  70+(account % 2) * 540, 20, 20))  # 세번째 3번째 칸 비었으면 생산시작!
    # if (cond_3rd_clear1):
    #     ShowTime = True
    # else:
    #     return True

    print('Prod_action함수!', image, list_image, account, check_num)

    while ShowTime:
        # cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
        # if (cond_network):
        #     pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
        #     time.sleep(0.6)
        #
        # cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        # if (cond_halted):
        #     # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
        #     pag.click(cond_halted)
        #     End_kkd(account)
        #     Kingdom_ready(account, 'kkd_out')  # 재부팅
        #     return False
        #
        # cond_halted1 = pag.locateCenterOnScreen('cond_halted1.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        # cond_halted_close = pag.locateCenterOnScreen('cond_halted_close.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        # if (cond_halted1):
        #     pag.click(cond_halted_close)
        #     time.sleep(7)
        #     Kingdom_ready(account, 'kkd_out')  # 재부팅

        now_time = time.time()
        prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence=0.945, region=(90 + (account // 2) * 960, 145 + (account % 2) * 540, 24, 20))
        if not (prod_refresh):
            # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
            pag.click(x=random.randint(223, 428) + (account // 2) * 960, y=random.randint(190, 410) + (account % 2) * 540)
            time.sleep(0.3)
        # 클릭했는데도 리스트가 가득 차있다? 어찔까... 그냥 넘어가면 최고렙을 계속 찍을..지도?
        prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
        prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
        prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
        prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
        prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
        # 3~7렙 Full list인 경우 다음 건물로 넘어감. 하지만 고렙 생산..중이면 그거 취소 못하고 저렙 생산이 안될텐데...
        if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
            print('리스트 full!1')
            return True
        if now_time - start_time > 10:
            print('동작 최대시간 초과 입니다.')
            return False
        if keyboard.is_pressed('end'):
            return True

        ctr = pag.locateCenterOnScreen(image, confidence=0.87, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 460))    # 생산품 이미지 큰거, 오른쪽에 핀으로 꽂혀있는거
        prd_done = pag.locateCenterOnScreen('prod_done.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 마지막 칸 바닥이 보임 = 생산 다 누름
        list_full = pag.locateCenterOnScreen('Cond_makinglist_full.png', confidence=0.97, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))   # 생산시 생기는 흰화살표 윗부분 /
        list_full1 = pag.locateCenterOnScreen('Cond_makinglist_full1.png', confidence=0.97, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 생산시 생기는 흰화살표 세모꼴 <
        lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))      # '확인'버튼
        ctr_list = pag.locateCenterOnScreen(list_image, confidence=0.9, region=(40 + (account // 2) * 960, 168 + (account % 2) * 540, 71, 321))    #  생산 대기중인 제품? 나무+원배경
        play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))

        # if (play_halted):
        #     pag.click(play_halted)

        if (ctr):  # 이미지 찾음
            print('이미지 검색!', image)
            while True:
                if ctr.y < 465 + (account % 2) * 540:  # 최대 밑으로 스크롤 한 경우 464+540*account 이하여야 함. 넘어가면 불안쓰
                    print('이미지 범위 내에요!')
                    break
                else:
                    print('이미지가 너무 밑에 있어 올립니다.')
                    Updown(account, 'up')  # 순방향 위로 드래그
                    ctr = pag.locateCenterOnScreen(image, confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            now_time = time.time()
            if now_time - start_time > 30:
                print('동작 최대시간 초과 입니다.')
                return False
            number_bef_action = prod_check(image, account)
            target_numb = check_num - number_bef_action

            # 목표 수량 미만
            if target_numb > 0:
                print('목표 수량 미달!', target_numb)
                if (list_full) or (list_full1) or (prd_done):  # 생산 완료
                    print('목표 생산물 클릭 완료!!')
                    return True
                elif (lack_of_material):  # 재료 부족
                    print('재료가 부족해요')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)
                    return False
                elif (not_opened):  # 안 연거
                    print('열지 않은 제품이라서 넘어가겠어요~!')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)
                    return False
                else:  # 그거 아니면 생산 클릭           실제 생산!
                    print('생산품 클릭!')
                    pag.moveTo(ctr[0] + 235, ctr[1] + 48)
                    # pag.moveTo(ctr[0] + 177, ctr[1] + 48)
                    # time.sleep(0.2)
                    pag.mouseDown()
                    time.sleep(0.3)
                    pag.mouseUp()
                    time.sleep(0.5)

                    lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                    if (lack_of_material):
                        print('재료가 부족해요')
                        pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                        time.sleep(0.3)
                        pag.hotkey('esc')
                        time.sleep(0.3)
                        return False

            # 목표 수량 초과
            if target_numb <= 0:
                print('목표 수량 초과!')
                if (ctr_list):     # 생산 대기중인 제품 삭제!
                    if 111 + (account // 2) * 960 >= ctr_list.x + (account // 2) * 960 >= 40 + (account // 2) * 960:
                        print('이 제품은 충분히 생산했으니 삭제하겠써요!')
                        pag.click(ctr_list)
                        time.sleep(0.7)
                else:
                    return False
        else:  # 이미지 못찾음
            print('이미지를 찾지 못했습니다.')
            if error_count > 2:  # 그래도 못찾으면 에러
                return False
            if error_count == 1:
                pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 + 15, 2)  # 15 내리고 이미지 다시 찾음
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(2)
                error_count = error_count + 1
            if error_count == 0:
                pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540)
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(610 + (account // 2) * 960, 295 + (account % 2) * 540 - 10, 2)  # 10 올리고 이미지 다시 찾음
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(2)
                error_count = error_count + 1
# account = 2
# # prod_action()
# # prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence=0.945, region=(90 + (account // 2) * 960, 145 + (account % 2) * 540, 24, 20))
# # if not (prod_refresh) or 140<= (prod_refresh.y) <= 140+175:
# #     print(prod_refresh)
# account = 2
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
# print(pix_status)


def Check_Initiating(account):
    print('부팅여부 확인합니다.')
    bStart = False
    bTouchto = False
    kkd_start = pag.locateCenterOnScreen('init_kkm.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_touch = pag.locateCenterOnScreen('init_touch.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_down = pag.locateCenterOnScreen('init_Touch1.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
    kkd_start_bg = pag.locateCenterOnScreen('init_kkm_recent.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 최근 항목이 없습니다.
    kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))

    while True:
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
            # End_kkd(account)
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
                # End_kkd(account)
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
            if (kkd_down):
                time.sleep(3)
                print('[부팅중] 다운로드 터치!')
                pag.click(kkd_down)
                bTouchto = True
            if (not (kkd_touch) and not (kkd_down)) and bTouchto:
                time.sleep(3)
                print('[부팅중] Touch to Start 터치 완료!', '현재시간:', datetime.now().strftime('%H:%M:%S'))
                break
        if bTouchto:
            print('부팅 실행 했습니다.')
            time.sleep(17)
            # for i in range(0, 19, 1):
            #     mark_x = pag.locateCenterOnScreen('mark_x.png', confidence=0.92, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505)) # 화면에 파란x버튼 보임
            #     if(mark_x):
            #         print('부팅 되었나봄!')
            #         return True
            #     print('부팅 중...', i)
            #     time.sleep(1)
            return
    else:
        print('튕긴건 아니네요')
        return

def Kingdom_ready(account, whereto):  # 특정 위치 확인
    try:
        error_position = 0
        start_time = time.time()

        while True:
            time.sleep(2)
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
            pix_status_in = (194, 143, 10)  # 생산건물 내
            pix_status_in_dark = (97, 72, 5)  # 건물 안이긴 한데 창이 떠있음
            pix_status_in_magic_dark = (109, 81, 9) # 마법공방이고 생산품 보상이 떠있음
            # pix_status_out = (0, 181,   255)    # 바탕화면(왕국), 트로피컬도 동일
            pix_status_out = (11, 194, 250)  # 바탕화면(왕국), 트로피컬도 동일  ㅁㅁㅁ수정
            # pix_status_out_window = (0, 64, 91)   # 창이 떠서 어두워짐
            pix_status_out_window = (6, 95, 125)  # 창이 떠서 어두워짐
            # pix_status_out_esc = (0, 90, 127)   # 왕국.. ESC나 트로피컬 썬배드로 어두워진..
            # pix_status_out_esc = (6, 97, 124)  # 왕국.. ESC나 트로피컬 썬배드로 어두워진..ㅁㅁㅁ수정
            pix_status_out_esc = (6, 97, 126)
            # pix_status_sowon = (239, 171, 2)  # 소원나무, 곰젤리열차, 상점 동일
            pix_status_sowon = (255, 208, 3)  # 소원나무, 곰젤리열차, 상점 동일 헷갈려 ㅁㅁㅁ수정
            pix_status_ballon = (29, 36, 46)  # 열기구 날아다니는 중
            # pix_status_bal_lobby = (170, 126, 1)  # 열기구 로비
            pix_status_bal_lobby = (175, 131, 0)  # 열기구 로비
            pix_status_bal_window = (127, 95, 4)  # 열기구 창 떠서 어두워짐
            pix_status_adv = (14, 167, 251)  # 모험하기
            pix_status_kdpass = (42, 27, 19)  # 킹덤패스
            pix_status_warehouse = (55, 64, 105)  # 창고 뜸
            pix_status_mail = (60, 70, 105)  # 우편함
            pix_lackof1 = (243, 233, 223)  # 베이지색
            # pix_status_not_prod = (0, 124, 176) # 건물 클릭했지만 생산 건물은 아님
            pix_status_not_prod = (8, 133, 172)  # 건물 클릭했지만 생산 건물은 아님
            # pix_status_cookiehouse = (0, 129, 182)  # 엥 이게 다 달라?
            pix_status_cookiehouse = (84, 93, 134)  # 엥 이게 다 달라?
            # pix_status_lotto = (255, 189, 8)    # 뽑기, 해변교역소
            pix_status_lotto = (255, 208, 2)  # 뽑기, 해변교역소
            pix_status_mycookie = (0, 0, 0)  # 내 쿠키...으... 움직이면 틀어질텐데
            pix_status_fountain = (84, 93, 134)  # 분수..
            # pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
            pix_stats_kkd_start = (11, 10, 42)  # 바탕화면 나갔네
            pix_status_trade = (255, 216, 2)  # 해상무역센터 로비
            pix_status_wanted = (29, 10, 12)  # 오늘의 현상수배 선택하는 곳
            pix_status_fight_comp = (168, 167, 167)  # 모험 전투 후
            pix_status_temple = (177, 123, 145) # 찬란한 영웅들의 신전 대기화면, 석상화면 같음
            pix_status_temple_dark = (88, 61, 76) # 찬란한 영웅들의 신전 화면 어두워졌을 때(슬롯 확장 잘못누름)

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
            cond_kkd_arena = pag.locateCenterOnScreen('cond_kkd_arena.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 킹덤아레나
            cond_reward = pag.locateCenterOnScreen('cond_reward.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 미션 보상받기
            mark_x_mission = pag.locateCenterOnScreen('mark_x_mission.png', confidence=0.8, region=(778 + (account // 2) * 960, 124 + (account % 2) * 540, 50, 50))  # 미션 취소
            cond_error_page = pag.locateCenterOnScreen('cond_error_page.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 검은 바탕... 렉 등에 의한 오류?
            kkd_start_ire = pag.locateCenterOnScreen('cond_g_play1.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            kkd_ad = pag.locateCenterOnScreen('cond_error_ad.png', confidence=0.95, region=(1, 1 , 960*2, 540*2))
            kkd_ad1 = pag.locateCenterOnScreen('cond_error_ad1.png', confidence=0.95, region=(1, 1, 960 * 2, 540 * 2))
            kkd_ad2 = pag.locateCenterOnScreen('cond_error_ad2.png', confidence=0.95, region=(1, 1, 960 * 2, 540 * 2))
            kkd_ad3 = pag.locateCenterOnScreen('cond_error_ad3.png', grayscale=True, confidence=0.8, region=(1, 1, 960 * 2, 540 * 2))
            kkd_winupdate = pag.locateCenterOnScreen('cond_error_winupdate.png', confidence=0.95, region=(1, 1, 960 * 2, 540 * 2))
            print('[Kingdom_ready] 현재 픽셀값 : ', pix_status, '실행 %s초 지났습니다.' % int(now_time - start_time), account, '계정, 현재시간:', datetime.now().strftime('%H:%M:%S'))
            # print('[Kingdom_ready] 실행 %s초 지났습니다.' % int(now_time - start_time), '현재시간:', datetime.now().strftime('%H:%M:%S'))
            if now_time - start_time >= 300:
                print('너무 오래 돌리고 있는데?')
                # End_kkd(account)  # 쿠킹덤 종료. 15분 안엔 끝나겠지.
                Kingdom_ready(account, 'kkd_out')  # 재부팅
                start_time = 0

            #현재 계정 매크로 종료...흠....
            man_macroA = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (account // 2) * 960, 1 + (account % 2) * 540, 422, 29))
            man_macroB = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (account // 2) * 960, 1 + (account % 2) * 540, 422, 29))
            man_macroC = pag.locateCenterOnScreen('cond_manual_macro.png', confidence=0.9, region=(500 + (account // 2) * 960, 1 + (account % 2) * 540, 422, 29))
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
                # End_kkd_line(account)
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

            # 상하단 픽셀 위치 모두 (0, 0, 0)이고 esc 누른 경우
            if pix_status == (0, 0, 0) and pix_status == (0, 0, 0) and (cond_error_page):
                # End_kkd(account)  # 쿠킹덤 종료. 15분 안엔 끝나겠지.
                Kingdom_ready(account, 'kkd_out')  # 재부팅

            cond_halted = pag.locateCenterOnScreen('cond_halted.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            if (cond_halted):
                # pag.click(740 + (account // 2) * 960, 310 + (account % 2) * 540)
                pag.click(cond_halted)
                # End_kkd(account)
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

            elif pix_status == pix_status_adv:  # 모험하기
                if (pix_status == whereto) or (whereto == 'mohum'):
                    print('모험하기?')
                    return True
                else:
                    if whereto == 'mohum':
                        return False
                    print('모험은 아...직?')
                    pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
                    time.sleep(0.3)
                    pag.hotkey('esc')
                    time.sleep(0.3)

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

            # elif (cond_kkd_out):
            #     if (cond_gold):
            #         if (cond_kkd_arena):
            #             print('킹덤아레나인가요?')
            #             pag.click(605 + (account // 2) * 960, 55 + (account % 2) * 540)
            #             time.sleep(1)
            #         else:
            #             print('왕국이네요!')
            #             if (whereto == 'kkd_out'):
            #                 return True
            #             elif (whereto == 'tropical_in'):
            #                 print('왕국인데 트로피칼 볼래요')
            #                 if Tropical_Event(account):  # 트로피칼에 이벤트 없으면
            #                     print('트로피칼 입장!')
            #                     return True
            #                 else:
            #                     print('트로피칼 이벤트 없어서 들어가지 않습니다.')
            #                     return False
            #             else:
            #                 return False
            #
            #     else:
            #         print('왕국이긴 한데 이상한 건물인가 봅니다.')
            #         pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
            #         time.sleep(0.3)
            #         pag.hotkey('esc')
            #         time.sleep(0.7)

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
                    # Ballon_send(account)
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
                        # pag.click(284 + (account//2)*960, 45 + (account%2) * 540)
                        time.sleep(3)
                        pag.hotkey('esc')
                        time.sleep(3)
                        pag.hotkey('esc')
                        time.sleep(3)
                    if error_position == 3:
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.click(605 + (account // 2) * 960, 55 + (account % 2) * 540)
                        time.sleep(5)
                    if error_position == 6:
                        pag.click(175 + (account // 2) * 960, 17 + (account % 2) * 540)  # 우선 해당 창 클릭하고 esc부터 갈겨보자!
                        time.sleep(2)
                        pag.click(284 + (account // 2) * 960, 45 + (account % 2) * 540)
                        time.sleep(2)
                        pag.hotkey('alt', 'up')
                        time.sleep(2)
                        # End_kkd(account)  # 우선 모든 창 꺼보고
                        time.sleep(2)
                        Kingdom_ready(account, 'kkd_out')  # 바탕화면으로 튕겼는지, 아니면 뭔지 확인
                        time.sleep(2)
                    # if error_position == 7:
                    #     time.sleep(2)
                    #     Kingdom_ready(account, 'kkd_out')   # 바탕화면으로 튕겼는지, 아니면 뭔지 확인
                    #     time.sleep(20)
                    if error_position > 6:
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
        # End_kkd(account)
        Kingdom_ready(account, 'kkd_out')  # 재부팅

def End_kkd_quit(account):
    pag.hotkey('alt', 'up')
    time.sleep(3)
    pag.click(2 + (account // 2) * 960, 15 + (account % 2) * 540)  # 메뉴바 한번 클릭해주고
    pag.hotkey('pgup')   # 실행중인 모든 창 띄우기
    time.sleep(5)
    while True:
        if keyboard.is_pressed('end'):
            return False
        init_kkm = pag.locateCenterOnScreen('init_kkm.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (init_kkm):
            print('쿠키런:킹덤 아이콘 보입니다!')
            return True
        init_kkm_recent = pag.locateCenterOnScreen('init_kkm_recent.PNG', confidence=0.9, grayscale=True, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (init_kkm_recent):
            pag.click(init_kkm_recent)
            pag.hotkey('esc')
            time.sleep(2)
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

def Arena_Event(account):
    try:
        bStep1_play = False  # 플레이 버튼을 눌렀는가?
        error_count = 0
        start_time = time.time()
        while True:
            cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
            if (cond_network):
                pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
                time.sleep(0.3)

            if keyboard.is_pressed('end'):
                return False
            now_time = time.time()
            if now_time - start_time > 900:
                # End_kkd(account)  # 쿠킹덤 종료. 15분 안엔 끝나겠지.
                Kingdom_ready(account, 'kkd_arena')  # 재부팅
                return False
            screen = ImageGrab.grab()
            pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
            pix_status2 = screen.getpixel((540 + (account // 2) * 960, 510 + (account % 2) * 540))  # 마침표
            pix_status_out = (0, 181, 255)  # 바탕화면(왕국), 트로피컬도 동일
            cond_adv_mode_select = pag.locateCenterOnScreen('cond_adv_mode_select.png', confidence=0.85, region=(12 + (account // 2) * 960, 38 + (account % 2) * 540, 37, 36))  # Play버튼 누른 후 모험하기 창
            cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825 + (account // 2) * 960, 490 + (account % 2) * 540, 45, 40))  # 쿠키왕국
            cond_adv_tro_mode = pag.locateCenterOnScreen('cond_adv_tro_mode.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))  # 트로피컬 소다제도의 '도'
            cond_adv_arena = pag.locateCenterOnScreen('cond_adv_arena.png', confidence=0.8, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
            cond_adv_arena_no_ticket = pag.locateCenterOnScreen('cond_adv_arena_no_ticket.png', confidence=0.90, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))

            # 바탕화면도 모험하기도 아니면 우선 바탕화면으로
            if not (cond_kkd_out) and not (cond_adv_mode_select):
                print('왕국도 모험하기 화면도 아니네요!')
                Kingdom_ready(account, 'kkd_out')

            # 모험하기 화면
            if not bStep1_play and (cond_adv_mode_select):
                bStep1_play = True  # 플레이 버튼만 눌렸지..

            # 바탕화면이면 플레이 버튼 누르기(복귀와 확인이 같이 있으니 굳이 조건 필요없을듯)
            if (pix_status == pix_status_out or (cond_kkd_out)) and not bStep1_play:
                print('Play 버튼 클릭~!')
                pag.click(random.randint(730, 785) + (account // 2) * 960, random.randint(470, 525) + (account % 2) * 540)
                time.sleep(3)

            if bStep1_play:
                if (cond_adv_arena):
                    print('킹덤 아레나 입장모드 보임', cond_adv_arena)
                    if (cond_adv_arena_no_ticket):
                        print('근데 티켓이 없네?', cond_adv_arena_no_ticket)
                        pag.click(892 + (account // 2) * 960, 54 + (account % 2) * 540)
                        time.sleep(6)
                        return False
                    else:
                        print('아레나 입장합니다!')
                        pag.click(cond_adv_arena)
                        time.sleep(6)
                        return True

                if not (cond_adv_arena):
                    print('드래그드래그')
                    pag.moveTo(random.randint(730, 785) + (account // 2) * 960, random.randint(470, 525) + (account % 2) * 540)
                    pag.drag(-300, 0, 2)  # 현상수배와 반대로.. 왼쪽으로 가야 하니깐 300으로 바꿔주고
                    time.sleep(3)
                    error_count = error_count + 1
                    if error_count > 5:
                        print('없는 걸 보니... 에러인가봐요! 없을리가 없는데...')
                        pag.click(892 + (account // 2) * 960, 54 + (account % 2) * 540)
                        time.sleep(8)
                        return False
            time.sleep(0.3)
    except:
        print('에러가 났어요! arena_event')
        # send_telegram_message('arena_event에서 에러가 났어요!')
        Kingdom_ready(account, 'kkd_out')  # 재부팅

account = 0
# End_kkd_quit(account)
# Kingdom_ready(account, 'kkd_out')
# cond_kkd_out = pag.locateCenterOnScreen('cond_kkd_out.png', confidence=0.85, region=(825 + (account // 2) * 960, 490 + (account % 2) * 540, 45, 40))  # 쿠키왕국
# if(cond_kkd_out):
#     print('ok')
# else:
#     print('???')
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
# print(pix_status)
# Arena_Event(account)
# pix_magic = (93, 55, 48)  # 마법공방 - magic
magic_num_A = 1    # 마법공방
magic_lev1_A = 20    # 고농축 에스프레소
magic_lev2_A = 20    # 울퉁불퉁 뿔고구마
magic_lev3_A = 190    # 향기로운 포도주스
magic_lev4_A = 0    # 빨리감기 태엽장치
magic_lev5_A = 0    # 수수께끼의 파우더 주머니
magic_lev6_A = 0    # 수수께끼의 빛나는 파우더 주머니
magic_lev7_A = 0    # 수수께끼의 신비한 파우더 주머니
magic_lev8_A = 0    # 힘의 설탕결정
magic_lev9_A = 0    # 신속의 설탕결정
magic_lev10_A = 0    # 마력의 설탕결정
magic_lev11_A = 0    # 토핑 조각
magic_lev12_A = 0    # 찬란한 빛조각
# magic_lev1 = magic_lev1_A  # 고농축 에스프레소
# magic_lev2 = magic_lev2_A  # 울퉁불퉁 뿔고구마
# magic_lev3 = magic_lev3_A  # 향기로운 포도주스
# magic_lev4 = magic_lev4_A  # 빨리감기 태엽장치
# magic_lev5 = magic_lev5_A  # 수수께끼의 파우더 주머니
# magic_lev6 = magic_lev6_A  # 수수께끼의 빛나는 파우더 주머니
# magic_lev7 = magic_lev7_A  # 수수께끼의 신비한 파우더 주머니
# prod_direction_left = True
# # screen = ImageGrab.grab()
# # pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# bmagiccompleted = False
# if pix_prod == pix_magic:
# # pix_error_count = 0
#     print('magic!')
#     if not bmagiccompleted:
#         # print('생산 확인...')
#         if not three_prod_action(account, 'magic_stby_lv1.png', 'magic_stby_lv2.png', 'magic_stby_lv3.png', magic_lev1, magic_lev2, magic_lev3, prod_direction_left):
#             bmagiccompleted = True
#     else:
#         print('ddddd')
#         # Skip_Next(account, prod_direction_left)

# screen = ImageGrab.grab()
# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# print(pix_prod)
#
# 스샷찍기
# account = 1
# pag.screenshot('prod_full_2-8.PNG', region=(87+(account//2)*960, 65+(account%2)*540, 9, 13))


# account = 2
# z0 = pag.locateCenterOnScreen('z0.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z1 = pag.locateCenterOnScreen('z1.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z2 = pag.locateCenterOnScreen('z2.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z3 = pag.locateCenterOnScreen('z3.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z4 = pag.locateCenterOnScreen('z4.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z5 = pag.locateCenterOnScreen('z5.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z6 = pag.locateCenterOnScreen('z6.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z7 = pag.locateCenterOnScreen('z7.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z8 = pag.locateCenterOnScreen('z8.png', confidence=0.9, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
#
#
# if z8:
#     print('8')
# elif z7:
#     print('7')
# elif z6:
#     print('6')
# elif z5:
#     print('5')
# elif z4:
#     print('4')
# elif z3:
#     print('3')
# elif z2:
#     print('2')
# elif z1:
#     print('1')
# # elif z0:
# #     print('0')
# account = 2
# z0 = pag.locateCenterOnScreen('z0.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z1 = pag.locateCenterOnScreen('z1.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z2 = pag.locateCenterOnScreen('z2.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z3 = pag.locateCenterOnScreen('z3.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z4 = pag.locateCenterOnScreen('z4.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z5 = pag.locateCenterOnScreen('z5.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z6 = pag.locateCenterOnScreen('z6.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z7 = pag.locateCenterOnScreen('z7.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# z8 = pag.locateCenterOnScreen('z8.png', confidence=0.85, region=(814 + (account // 2) * 960, 86 + (account % 2) * 540, 50, 446))
# if not (z8 or z7 or z6 or z5 or z4 or z3 or z2 or z1):
#     print('리스트 full!4')
# else:
#     print('0')





# def research_action1(account, what_research):
#     print('연구소 들어왔어요!')
#     research_ing = pag.locateCenterOnScreen('research_ing.png', confidence=0.945, region=(230 + (account // 2) * 960, 115 + (account % 2) * 540, 24, 18))
#     if (research_ing):
#         print('엇.. 뭔가 연구중입니다.')
#         Kingdom_ready(account, 'kkd_out')
#         return False
#
#     # 왕국이냐 쿠키냐 선택
#     while True:
#         if keyboard.is_pressed('end'):
#             print('end 누름')
#             return False
#         # 연구소이고, 연구소 안에서 창이 떠있어서 화면 중간에 x버튼 있다? 없애!
#         research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(600 + (account // 2) * 960, 35 + (account % 2) * 540, 245, 130))
#         if (research_window):
#             pag.click(research_window)
#             time.sleep(0.3)
#
#         if what_research == 'W':
#             screen = ImageGrab.grab()
#             pix_research_wangkook = screen.getpixel((330 + (account // 2) * 960, 515 + (account % 2) * 540))  # 왕국 연구
#             pix_research_selected = (58, 73, 109)
#             if pix_research_wangkook == pix_research_selected:
#                 print('왕국 연구 선택됨!')
#                 break
#             else:
#                 pag.click(330 + (account // 2) * 960, 515 + (account % 2) * 540)
#                 time.sleep(0.3)
#
#         if what_research == 'C':
#             screen = ImageGrab.grab()
#             pix_research_cookie = screen.getpixel((500 + (account // 2) * 960, 515 + (account % 2) * 540))  # 쿠키 연구
#             pix_research_selected = (58, 73, 109)
#             if pix_research_cookie == pix_research_selected:
#                 print('쿠키 연구 선택됨!')
#                 break
#             else:
#                 pag.click(500 + (account // 2) * 960, 515 + (account % 2) * 540)
#                 time.sleep(0.3)
#
#     # 연구 돌립시다
#     while True:
#         if keyboard.is_pressed('end'):
#             print('end 누름')
#             return False
#         # time.sleep(2)
#
#         research_green_light = pag.locateCenterOnScreen('research_green_light.png', confidence=0.96, region=(8 + (account // 2) * 960, 80 + (account % 2) * 540, 868, 401))
#         if (research_green_light):
#             print('실행 가능한 연구가 보여요!')
#             print('green_light', research_green_light)
#             pag.click(research_green_light.x + 43, research_green_light.y + 43)
#             time.sleep(1)
#             print('연구 시작합니다')
#             pag.click(467 + (account // 2) * 960,471 + (account % 2) * 540)   # 연구하기 버튼 클릭
#             time.sleep(1)
#             research_ing = pag.locateCenterOnScreen('research_ing.png', confidence=0.945, region=(230 + (account // 2) * 960, 115 + (account % 2) * 540, 24, 18))
#             if (research_ing):
#                 print('연구 시작했습니다!')
#                 Kingdom_ready(account, 'kkd_out')
#                 return True
#         else:
#             print('실행 가능한 연구가 안 보여요!')
#             pag.click(37+(account//2)*960, 59+(account%2)*540)   # 수염할아버지 얼굴 한번 클릭하고
#             time.sleep(1)
#
#             # # 실행 가능한 연구 찾아 화면 왼쪽으로 드래그
#             # pag.moveTo(random.randint(730 + (account // 2) * 960, 785 + (account // 2) * 960), random.randint(470 + (account % 2) * 540, 525 + (account % 2) * 540))
#             # pag.drag(700, 0, 3)  # 왼 손으로 비비고
#
#             # 실행 가능한 연구 찾아 화면 오른쪽으로 드래그
#             pag.moveTo(random.randint(730 + (account // 2) * 960, 785 + (account // 2) * 960), random.randint(470 + (account % 2) * 540, 480 + (account % 2) * 540))
#             pag.drag(-350, 0, 3)  # 오른손으로 비비고
#             continue



# account = 2
# research_action1(account, 'W')

#
# account = 0
# check_check = pag.locateCenterOnScreen('check.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
# if (check_check):  # 있으면 클릭하긴 하는데..
#     # pag.click(check_check)
#     print(check_check)
#     time.sleep(1)  # 2초쯤 기다리면 되려나..
# else:
#     print('check 없어요')
# account = 0
# screen = ImageGrab.grab()
# pix_status_scr1 = screen.getpixel((65 + (account // 2) * 960, 505 + (account % 2) * 540))  # = 왼쪽아래 건설하기 아이콘쪽
# pix_status1_tropical = (255, 98, 170)  # 트로피칼이다
# pix_status1_tropical_windowopen = (127, 49, 85)  # 트로피칼에 메뉴창 떠있다
# tropical_start_time = time.time()
# while pix_status1_tropical or pix_status1_tropical_windowopen:
#     tropical_now_time = time.time()
#     if tropical_now_time - tropical_start_time >= 300:
#         print('너무 오래 돌리는데? 300초 이상')
#         break
#     if (pix_status1_tropical):
#         print('트로피칼!')

# account = 0
# print('1', account)
# def Next_account():
#     global account
#     account = (account+1)%3
#     print('2', account)
# Next_account()
# print('3', account)
#

account = 0
# 생산건물 대기열 몇개나 비었는지 확인
def Check_available_slots(account):
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
    
    prod_full_n3 = pag.locateCenterOnScreen('prod_full_n3.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n4 = pag.locateCenterOnScreen('prod_full_n4.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n5 = pag.locateCenterOnScreen('prod_full_n5.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n6 = pag.locateCenterOnScreen('prod_full_n6.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n7 = pag.locateCenterOnScreen('prod_full_n7.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n8 = pag.locateCenterOnScreen('prod_full_n8.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n9 = pag.locateCenterOnScreen('prod_full_n9.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    prod_full_n10 = pag.locateCenterOnScreen('prod_full_n10.PNG', grayscale=True, confidence=0.9, region=(84 + (account // 2) * 960, 60 + (account % 2) * 540, 22, 22))
    if(prod_full_1):
        a = 1
    elif(prod_full_2):
        a = 2
    elif(prod_full_3):
        a = 3
    elif(prod_full_4):
        a = 4
    elif(prod_full_5):
        a = 5
    elif(prod_full_6):
        a = 6
    elif(prod_full_7):
        a = 7
    elif(prod_full_8):
        a = 8
    elif(prod_full_9):
        a = 9
    elif (prod_full_10):
        a = 10
    else:
        a = 0

    if(prod_full_n3):
        b = 3
    elif(prod_full_n4):
        b = 4
    elif(prod_full_n5):
        b = 5
    elif(prod_full_n6):
        b = 6
    elif(prod_full_n7):
        b = 7
    elif(prod_full_n8):
        b = 8
    elif(prod_full_n9):
        a = 9
    elif(prod_full_n10):
        b = 10
    else:
        b = 0
#
#     print('a:', a)
#     print('b:', b)
#     print('available_slot:', b-a)
#     return b-a
# slots = Check_available_slots(account)
# print(slots)
# account = 0
# trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.85, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
# print(trade_baseline)
# if (trade_baseline):
#     print(92 + 0 + (account // 2) * 960, '>=', trade_baseline[0], '>', 70 + 0 + (account // 2) * 960)
#     if (92 + (account // 2) * 960 >= trade_baseline[0] > 70 + (account // 2) * 960) or (92 + 0 + (account // 2) * 960 >= trade_baseline[0] > 70 + 0 + (account // 2) * 960):
#         print(92 + 0 + (account // 2) * 960*2 ,'>=', trade_baseline[0] ,'>', 70 + 0 + (account // 2) * 960)

# account = 1
# screen = ImageGrab.grab()
# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# print(pix_prod)

# account = 2
# prod_check_point = pag.locateCenterOnScreen('prod_check_point_magic.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460))
# print(prod_check_point.x-960, prod_check_point.y)
# pag.screenshot('prod_check_point_magic.PNG', region=(607+(account//2)*960, 88+(account%2)*540, 5,5))

# pag.screenshot('lev3.PNG', region=(593+(account//2)*960, 446+(account%2)*540, 20, 20))
# pag.screenshot('lev2.PNG', region=(593+(account//2)*960, 293+(account%2)*540, 20, 20))
# pag.screenshot('lev1.PNG', region=(593+(account//2)*960, 140+(account%2)*540, 20, 20))

# 제작 제품(???_lev1~lev0) 스샷 찍기
# list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460))
# list_numb2 = list(list_numb1)
# pag.screenshot('magic_lev44.PNG', region = (list_numb2[0][0]-14, list_numb2[0][1]+52, 20, 20))
# pag.screenshot('magic_lev55.PNG', region = (list_numb2[1][0]-14, list_numb2[1][1]+52, 20, 20))
# pag.screenshot('magic_lev66.PNG', region = (list_numb2[2][0]-14, list_numb2[2][1]+52, 20, 20))
#
# print(list_numb2)
# print(list_numb2[0][0]-960-16)
# print(list_numb2[0][1]+50)
# print(list_numb2[1][0]-960)
# print(list_numb2[1][1])
# print(list_numb2[2][0]-960)
# print(list_numb2[2][1])


# 대기 제품(???_stby_lv1~lv0) 스샷 찍기
# 대기 제품 위치 확인용
# magic_stby_lv1 = pag.locateCenterOnScreen('magic_stby_lv1.PNG', confidence=0.92, region=(2+(account//2)*960, 2+(account%2)*540, 960, 540))
# print(magic_stby_lv1)
# magic_stby_lv2 = pag.locateCenterOnScreen('magic_stby_lv2.PNG', confidence=0.92, region=(2+(account//2)*960, 2+(account%2)*540, 960, 540))
# print(magic_stby_lv2)

# 대기 제품 진짜 스샷 찍자!
# pag.screenshot('magic_stby_lv44.PNG', region = (51+(account//2)*960, 179+(account%2)*540, 45, 45))
# pag.screenshot('magic_stby_lv55.PNG', region = (51+(account//2)*960, 250+(account%2)*540, 45, 45))
# pag.screenshot('magic_stby_lv66.PNG', region = (51+(account//2)*960, 321+(account%2)*540, 45, 45))
# pag.screenshot('magic_stby_lv77.PNG', region = (51+(account//2)*960, 392+(account%2)*540, 45, 45))



account = 2

jelly_lev1 = 60
jelly_lev2 = 60
jelly_lev3 = 60
jelly_lev4 = 60
jelly_lev5 = 0
jelly_lev6 = 0




a = 36
b = 25
c = 59
d = -119
e = 259

# aa = [a, b, c, d, e]
# print(aa)
# tmp = max(aa)
# index = aa.index(tmp)
# print(index)
# print(aa(index))

# aa = []
# aa.append(a)
# print(aa)
# aa.append(b)
# print(aa)
# aa.append(c)
# print(aa)
# aa.append(d)
# print(aa)
# aa.append(e)
# print(aa)
# aa.append(a)
# print(aa)

# tmp = max(aa)
# index = aa.index(tmp)
# print(index)

def test():
    global aa
    print(aa)
#
# test()
# tmp = max(list(aa))
# index = aa.index(tmp)
# print('index:', aa(index))


# if not jelly_lev6 and jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
#     print('6렙부터 없어')
#     print(aa[0:5])
#     tmp = max(aa[0:5])
#     index = aa[0:5].index(tmp)
#     print(index)
# if not jelly_lev6 and not jelly_lev5 and jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
#     print('5렙부터 없어')
#     print(aa[0:4])
#     tmp = max(aa[0:4])
#     index = aa[0:4].index(tmp)
#     print(index)
# if not jelly_lev6 and not jelly_lev5 and not jelly_lev4 and jelly_lev3 and jelly_lev2 and jelly_lev1:
#     print('4렙부터 없어')
#     print(aa[0:3])
#     tmp = max(aa[0:3])
#     index = aa[0:3].index(tmp)
#     print(index)

# index = 3
# print((index-1)%3)
# account = 2
# index = 0
# print('클릭하러 갑시다!')
# click_all = pag.locateCenterOnScreen('prod_click_all.PNG', confidence=0.9, region=(800 + (account//2)*960, 160 + index * 153 + (account%2)*540, 25, 145))
# if (index) % 3 == 0: # 첫번째 줄 클릭
#     print('현재 화면의 0번째 아이템 클릭')
# if (index) % 3 == 1: # 두번째 줄 클릭
#     print('현재 화면의 1번째 아이템 클릭')
# if (index) % 3 == 2: # 세번째 줄 클릭
#     print('현재 화면의 2번째 아이템 클릭')
# pag.click(click_all, duration = 1.5)
# print(click_all)


# list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 82 + (account % 2) * 540, 105, 145))  # 일반 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
#
# while True:
#     if keyboard.is_pressed('end'):
#         break
#     list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 82 + (account % 2) * 540, 105, 145))  # 일반 건물일때
#     list_numb2 = list(list_numb1)
#     print(list_numb2)
#
#     if not list_numb2:
#         print('안보여!')
#         Updown(account, 'down_little')
#         list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 82 + (account % 2) * 540, 105, 145))  # 일반 건물일때
#         list_numb2 = list(list_numb1)
#         print(list_numb2)
#     if 82 <= list_numb2[0][1] - (account % 2) * 540 <= 82 + 20:
#         print('첫 y값이 82+20 ~ 82사이', list_numb2[0][1] - (account % 2) * 540)
#         break
#     elif 82 >= list_numb2[0][1] - (account % 2) * 540:
#         print('조금.. 올리나?')
#         a = int(list_numb2[0][1])-88
#         print(a)
#         Updown_new(account, 'down_little', a)
#     elif list_numb2[0][1] - (account % 2) * 540 >= 82 + 20:
#         print('조금.. 내리나?')
#         a = int(list_numb2[0][1])-88
#         print(a)
#         Updown_new(account, 'up_little', a)
#     else:
#         print('dldlksadjfl;askdjf')
#         print(list_numb2)
#         a = int(list_numb2[0][1])-88
#         print(a, (a//30))
#         for i in range(abs(a//30)):
#             Updown_new(account, 'down_little', a)
#
#         break
#

# target_numb = [5, -5, 0, -51, -70, -176, -183]
# print(target_numb)
#
# tmp = max(target_numb)
# index = target_numb.index(tmp)+1
# print(index)

#
# account = 2
# index = 0
# # click_all = pag.locateCenterOnScreen('prod_click_all.PNG', confidence=0.8, region=(800 + (account//2)*960, 160 + (account%2)*540, 75, 145))
# # print(click_all)
#
#
# index = (index) % 3
# print('함수 안의 index:', index)
# click_all = pag.locateCenterOnScreen('prod_click_all.PNG', confidence=0.8, region=(800 + (account//2)*960, 160 + 153*index + (account%2)*540, 75, 145))
# if not (click_all):    # 초록바탕의 x(여러개제작) 버튼이 보이는가?
#     print('click_all이 없어요')
# if (index) == 0: # 첫번째 줄 클릭
#     print('현재 화면의 0번째 아이템 클릭')
# elif (index) == 1: # 두번째 줄 클릭
#     print('현재 화면의 1번째 아이템 클릭')
# elif (index) == 2: # 세번째 줄 클릭
#     print('현재 화면의 2번째 아이템 클릭')
# else:
#     print('화면에 아이템이 안보여요!')
# pag.moveTo(click_all)
# time.sleep(0.4)
# pag.mouseDown()
# time.sleep(0.5)
# pag.mouseUp()
# time.sleep(0.7)



# index = 5
# index = (index) % 4
# print(index)



# index = 2
# index = (index) % 4
# print('함수 안의 index:', index)
#
# click_all = pag.locateCenterOnScreen('prod_click_all.PNG', confidence=0.85, region=(800 + (account//2)*960, 160 + 153*(index) + (account%2)*540, 75, 145))
# if not (click_all):    # 초록바탕의 x(여러개제작) 버튼이 보이는가?
#     print('click_all이 없어요')
#
# if (index) == 0: # 첫번째 줄 클릭
#     print('현재 화면의 1번째 아이템 클릭')
# elif (index) == 1: # 두번째 줄 클릭
#     print('현재 화면의 2번째 아이템 클릭')
# elif (index) == 2: # 세번째 줄 클릭
#     print('현재 화면의 3번째 아이템 클릭')
# else:
#     print('화면에 아이템이 안보여요!')


def check_item_number(account, where):
    if(where == 'top'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.95, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.95, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.95, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.95, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.95, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 75 + (account % 2) * 540, 50, 50))
    if (where == 'bot'):
        smith_lev1 = pag.locateCenterOnScreen('smith_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev2 = pag.locateCenterOnScreen('smith_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev3 = pag.locateCenterOnScreen('smith_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev4 = pag.locateCenterOnScreen('smith_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev5 = pag.locateCenterOnScreen('smith_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev6 = pag.locateCenterOnScreen('smith_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        smith_lev7 = pag.locateCenterOnScreen('smith_lev7.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        jelly_lev1 = pag.locateCenterOnScreen('jelly_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jelly_lev2 = pag.locateCenterOnScreen('jelly_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jelly_lev3 = pag.locateCenterOnScreen('jelly_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jelly_lev4 = pag.locateCenterOnScreen('jelly_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jelly_lev5 = pag.locateCenterOnScreen('jelly_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        rollc_lev1 = pag.locateCenterOnScreen('rollc_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        rollc_lev2 = pag.locateCenterOnScreen('rollc_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        rollc_lev3 = pag.locateCenterOnScreen('rollc_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        rollc_lev4 = pag.locateCenterOnScreen('rollc_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        bread_lev1 = pag.locateCenterOnScreen('bread_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        bread_lev2 = pag.locateCenterOnScreen('bread_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        bread_lev3 = pag.locateCenterOnScreen('bread_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        bread_lev4 = pag.locateCenterOnScreen('bread_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        bread_lev5 = pag.locateCenterOnScreen('bread_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        bread_lev6 = pag.locateCenterOnScreen('bread_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        jampy_lev1 = pag.locateCenterOnScreen('jampy_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jampy_lev2 = pag.locateCenterOnScreen('jampy_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jampy_lev3 = pag.locateCenterOnScreen('jampy_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jampy_lev4 = pag.locateCenterOnScreen('jampy_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jampy_lev5 = pag.locateCenterOnScreen('jampy_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        jampy_lev6 = pag.locateCenterOnScreen('jampy_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        doye_lev1 = pag.locateCenterOnScreen('doye_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        doye_lev2 = pag.locateCenterOnScreen('doye_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        doye_lev3 = pag.locateCenterOnScreen('doye_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        doye_lev4 = pag.locateCenterOnScreen('doye_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        flower_lev1 = pag.locateCenterOnScreen('flower_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        flower_lev2 = pag.locateCenterOnScreen('flower_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        flower_lev3 = pag.locateCenterOnScreen('flower_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        flower_lev4 = pag.locateCenterOnScreen('flower_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        flower_lev5 = pag.locateCenterOnScreen('flower_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        flower_lev6 = pag.locateCenterOnScreen('flower_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

        magic_lev1 = pag.locateCenterOnScreen('magic_lev1.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        magic_lev2 = pag.locateCenterOnScreen('magic_lev2.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        magic_lev3 = pag.locateCenterOnScreen('magic_lev3.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        magic_lev4 = pag.locateCenterOnScreen('magic_lev4.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        magic_lev5 = pag.locateCenterOnScreen('magic_lev5.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))
        magic_lev6 = pag.locateCenterOnScreen('magic_lev6.PNG', confidence=0.92, region=(580 + (account // 2) * 960, 385 + (account % 2) * 540, 50, 50))

    if smith_lev1 or jelly_lev1 or rollc_lev1 or bread_lev1 or jampy_lev1 or doye_lev1 or flower_lev1 or icecream_lev1 or magic_lev1:
        print(smith_lev1, jelly_lev1, rollc_lev1, bread_lev1, jampy_lev1, doye_lev1, flower_lev1, icecream_lev1, magic_lev1)
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
        print('?')
#
# account = 0
# list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.95, region=(560+(account//2)*960, 75+(account%2)*540, 105, 460)) # 일반 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
# print((list_numb2[0][0]-14, list_numb2[0][1]+52))
#
#
# a = check_item_number(account, 'bot')
# print('a:', a)
# icecream_lev1 = pag.locateCenterOnScreen('icecream_lev1.PNG', confidence=0.92, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
# icecream_lev2 = pag.locateCenterOnScreen('icecream_lev2.PNG', confidence=0.92, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
# icecream_lev3 = pag.locateCenterOnScreen('icecream_lev3.PNG', confidence=0.92, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
# icecream_lev4 = pag.locateCenterOnScreen('icecream_lev4.PNG', confidence=0.92, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
# icecream_lev5 = pag.locateCenterOnScreen('icecream_lev5.PNG', confidence=0.92, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 145))
#
# # print(560 + (account // 2) * 960, 75 + (account % 2) * 540)
# if(icecream_lev1):
#     print('1', icecream_lev1)
# elif(icecream_lev2):
#     print('2', icecream_lev2)
# elif(icecream_lev3):
#     print('3', icecream_lev3)
# elif(icecream_lev4):
#     print('4', icecream_lev4)
# elif(icecream_lev5):
#     print('5', icecream_lev5)
# else:
#     print('??????????')

def click_item(account,index1):

    global index

    
    new_index1 = (index1) % 4
    print('함수 안의 index1 = %s, new_index1:'% (index1),  index1)

    click_al = pag.locateCenterOnScreen('prod_click_al.PNG', confidence=0.9, region=(690 + (account//2)*960, 160 + 153*(new_index1) + (account%2)*540, 175, 153))
    if not (click_al):    # 초록바탕의 제작 버튼이 보이는가?
        print('click_al이 없어요. y값:', 160 + 153*(index1) + (account%2)*540)
        return False
    x0 = pag.locateCenterOnScreen('prod_x0.PNG', confidence=0.89, region=(814 + (account // 2) * 960, 177 + ((new_index1) % 3) * 153 + (account % 2) * 540, 44, 37))
    if (x0):
        print('목표 아이템 제작 불가!')
        print('1', target_numb)
        target_numb[index - 1] = -999
        print('2', target_numb)
        time.sleep(20)
    else:
        print('x0 안보영')
        click_item(account, index1 - item_number)

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

# while True:
#     if keyboard.is_pressed('end'):
#         break
    # time.sleep(1)
    # if building == 'normal':
    # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.8, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
    # list_numb1 = pag.locateAllOnScreen('prod_check_point1.PNG', confidence=0.87, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
    # elif building == 'magic':
    #     list_numb1 = pag.locateAllOnScreen('prod_check_point_magic.PNG', confidence=0.96, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 마법공방 건물일때

    # list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 153))  # 일반 건물일때
    # list_numb2 = list(list_numb1)
    # print(list_numb2)
    #
    # if not list_numb2:
    #     print('안보여!')
    #     Updown(account, 'down1')
    #     break
    #
    # if 75 <= list_numb2[0][1] - (account % 2) * 540 <= 75 + 20:
    #     print('첫 y값이 75+20 ~ 75사이', list_numb2[0][1] - (account % 2) * 540)
    #     break
    # # elif 75 >= list_numb2[0][1] - (account % 2) * 540:
    # #     print('조금.. 올리나?', int(list_numb2[0][1]))
    # #     a = int(list_numb2[0][1]) - 88
    # #     # print(a)
    # #     Updown_new(account, 'down_little', a)
    # elif list_numb2[0][1] - (account % 2) * 540 >= 75 + 20:
    #     print('조금.. 내리나?', int(list_numb2[0][1]))
    #     a = int(list_numb2[0][1]) - 88      # 위에가 살짝 가렸을 때가 문제구먼... 어케하지?
    #     print(a)
    #     Updown_new(account, 'down_little', a)
    # else:
    #     print('prod_default_screen 오류예요!')
    #     print(list_numb2)
    #     break







# account = 0
# list_numb1 = pag.locateAllOnScreen('prod_check_point1.PNG', confidence=0.8, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
# print(list_numb2[0][1])
# if 75<= list_numb2[0][1] <= 102:
#     print('적당한 위치구먼!')
# if 103<= list_numb2[0][1] <= 235:
#     print('윗쪽으로 올립시다')
#     a = 153+90 - int(list_numb2[0][1])
#     print(a)
#     Updown_new(account, 'down_little', a)









# b = abs(int(list_numb2[0][1]) - 88)
# print(b)
# if(0<b<=10):
#     print('알맞군')
# if(b<=74):
#     print('조금.. 올리나?')
#     Updown_new(account, 'up_little', b)
# elif (b > 74):
#     print('조금.. 내리나?')
#     Updown_new(account, 'down_little', b)
# if (239>=list_numb2[0][1]>=88+20):
#     a = int(list_numb2[0][1])-88+153
#     print('조금.. 내리나?', int(list_numb2[0][1]))
#     print(a)
#     # Updown_new(account, 'down_little', a)
# account = 0
# index = 0
# item_number = 2
# target_numb = [-161, -145, -21, 240]
# while True:
#     if keyboard.is_pressed('end'):
#         break
#     time.sleep(5)
#     to_make = 4
#     print('%s렙까지 만들어요 : ' % to_make, target_numb[0:to_make])
#     tmp = max(target_numb[0:to_make])
#     index = target_numb[0:to_make].index(tmp) + 1
#     print('index: %s 번째 아이템이 제일 모자라요, 현재 화면 %s' % (index, item_number))
#
#     if item_number + 2 >= index >= item_number:
#         click_item(account, index - item_number)
#         break
#     elif index < item_number:
#         print(item_number - index, '칸 올려요')
#         for i in range(item_number - index):
#             Updown(account, 'down1')
#             time.sleep(0.5)
#
#         item_number = item_number - (item_number - index)
#         print('item_number = %s, index = %s'%(item_number, index%3))
#         x0 = pag.locateCenterOnScreen('prod_x0.PNG', confidence=0.89, region=(814 + (account // 2) * 960, 177 + ((index) % 3) * 153 + (account % 2) * 540, 44, 37))
#         if (x0):
#             print('목표 아이템 제작 불가!')
#             print(target_numb)
#             target_numb[index-1] = -999
#             print(target_numb)
#             time.sleep(20)
#             continue
#     else:
#         print('x0 안보영')
#         click_item(account, index - item_number)
#     break

# index = 4
# x0 = pag.locateCenterOnScreen('prod_x0.PNG', confidence=0.89, region=(814 + (account // 2) * 960, 177 + ((index) % 3) * 153 + (account % 2) * 540, 44, 37))
# if (x0):
#     print('목표 아이템 제작 불가!')
#     # print(target_numb)
#     # target_numb[index - 1] = -999
#     # print(target_numb)
#     # time.sleep(20)
#     # continue
# else:
#     print('x0 안보영')
#     # click_item(account, index - item_number)
#
# current_hour = datetime.now().strftime('%H')
# print('current_hour = ', current_hour)
# print(type(current_hour))
# if (current_hour == '23'):
#     print('23시예요!')











# account = 2
# check_num1 = 100
# check_num2 = 100
# check_num3 = 100
#
# prod_pin = (612+(account//2)*960, 95 + (account % 2) * 540)
#
# target_numb1 = check_num1 - numb_new_recog(prod_pin, 1, account)
#
# target_numb2 = check_num2 - numb_new_recog(prod_pin, 2, account)
#
# target_numb3 = check_num3 - numb_new_recog(prod_pin, 3, account)
#
# print('1:', target_numb1)
# print('2:', target_numb2)
# print('3:', target_numb3)

#
# a = 100
# b = 0
# if(a):
#     print(a)
#
# if not (b):
#     print(b)













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
smith_lev6_C = 0  # 집게
smith_lev7_C = 0  # 망치

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


def three_prod_action_new(account, building, building_name, prod_direction_left):
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
    file_type_text = '.png'
    check_num1 = eval(start_text + mid_text + str(1))
    check_num2 = eval(start_text + mid_text + str(2))
    check_num3 = eval(start_text + mid_text + str(3))
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
#
# target_numb = [-33, 15, 46, ]
# building_name = 'smith'
# start_text = building_name+'_'
# mid_text = 'lev'
# file_type_text = '.png'
#
#
#
# for i in range(0, 10, 1):
#     print(eval(start_text+mid_text+str(i+1)))
#     if(eval(start_text+mid_text+str(i+1))==0):
#         print('이 레벨은 값이 0이구만요!')
#         a = i+1
#         break
# print(a)
# check_numb1 = start_text+mid_text+str(1)
# print(check_numb1)
#







# start_text+mid_text+str(1)+end_text
# aa = 6
# check_num1 = eval(start_text + mid_text + str(aa))
# print(check_num1)






def check_var(var_name):
    if var_name in globals():
        print('ok')
        return True
    else:
        print('none')
        return False

# z = check_var('smith_lev8')
# print(z)

# def to_make_number(building_name):
#     for i in range(10):
#         start_text = building_name+'_'
#         mid_text = 'lev'
#         if (eval(start_text + mid_text + str(i + 1)) == 0):
#             print('이 레벨은 값이 0이구만요!')
#             a = i+1
#             return a
#
# # account = 0
# z = to_make_number('smith')
# print(z)
#

#
#
#
#
#
# if not bProdHigh or smith_num == 1:
#     bSecond = False
#     # 작업 순방향 시작
#     if not (smith_lev1 == 0) and not bsmithcompleted:
#         if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
#             if (smith_lev2 == 0):
#                 bsmithcompleted = True
#             if not (smith_lev2 == 0) and not bsmithcompleted:
#                 if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
#                     if (smith_lev3 == 0):
#                         bsmithcompleted = True
#                     if not (smith_lev3 == 0) and not bsmithcompleted:
#                         if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
#                             if (smith_lev4 == 0):
#                                 bsmithcompleted = True
#                             if not (smith_lev4 == 0) and not bsmithcompleted:
#                                 Updown(account, 'up')
#                                 if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
#                                     if (smith_lev5 == 0):
#                                         bsmithcompleted = True
#                                     if not (smith_lev5 == 0) and not bsmithcompleted:
#                                         Updown(account, 'up')
#                                         if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
#                                             if (smith_lev6 == 0):
#                                                 bsmithcompleted = True
#                                             if not (smith_lev6 == 0) and not bsmithcompleted:
#                                                 Updown(account, 'up')
#                                                 if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
#                                                     if (smith_lev7 == 0):
#                                                         bsmithcompleted = True
#                                                     if not (smith_lev7 == 0) and not bsmithcompleted:
#                                                         Updown(account, 'up')
#                                                         if not prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7):
#                                                             bsmithcompleted = True
#                                                         Skip_Next(account, prod_direction_left)
#                                                     else:
#                                                         Skip_Next(account, prod_direction_left)
#                                                 else:
#                                                     Skip_Next(account, prod_direction_left)
#                                             else:
#                                                 Skip_Next(account, prod_direction_left)
#                                         else:
#                                             Skip_Next(account, prod_direction_left)
#                                     else:
#                                         Skip_Next(account, prod_direction_left)
#                                 else:
#                                     Skip_Next(account, prod_direction_left)
#                             else:
#                                 Skip_Next(account, prod_direction_left)
#                         else:
#                             Skip_Next(account, prod_direction_left)
#                     else:
#                         Skip_Next(account, prod_direction_left)
#                 else:
#                     Skip_Next(account, prod_direction_left)
#             else:
#                 Skip_Next(account, prod_direction_left)
#         else:
#             Skip_Next(account, prod_direction_left)
#     else:
#         Skip_Next(account, prod_direction_left)
#     # 작업 순방향 끝
# while True:
#     if keyboard.is_pressed('end'):
#         break
#     if not bProdHigh or smith_num == 1:
#         break
#     if bProdHigh and not bSecond and smith_num == 2:  # 첫 번째 건물 작업
#         # 작업 순방향 시작
#         if not (smith_lev1 == 0):
#             if not prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1):
#                 if not (smith_lev2 == 0):
#                     if not prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2):
#                         if not (smith_lev3 == 0):
#                             if not prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3):
#                                 if not (smith_lev4 == 0):
#                                     Updown(account, 'up')
#                                     if not prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4):
#                                         if not (smith_lev5 == 0):
#                                             Updown(account, 'up')
#                                             if not prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5):
#                                                 if not (smith_lev6 == 0):
#                                                     Updown(account, 'up')
#                                                     if not prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6):
#                                                         if not (smith_lev7 == 0):
#                                                             Updown(account, 'up')
#                                                             prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7)
#                                                             Skip_Next(account, prod_direction_left)
#                                                             bSecond = True
#                                                             break
#                                                         else:
#                                                             Skip_Next(account, prod_direction_left)
#                                                             bSecond = True
#                                                             break
#                                                     else:
#                                                         Skip_Next(account, prod_direction_left)
#                                                         bSecond = True
#                                                         break
#                                                 else:
#                                                     Skip_Next(account, prod_direction_left)
#                                                     bSecond = True
#                                                     break
#                                             else:
#                                                 Skip_Next(account, prod_direction_left)
#                                                 bSecond = True
#                                                 break
#                                         else:
#                                             Skip_Next(account, prod_direction_left)
#                                             bSecond = True
#                                             break
#                                     else:
#                                         Skip_Next(account, prod_direction_left)
#                                         bSecond = True
#                                         break
#                                 else:
#                                     Skip_Next(account, prod_direction_left)
#                                     bSecond = True
#                                     break
#                             else:
#                                 Skip_Next(account, prod_direction_left)
#                                 bSecond = True
#                                 break
#                         else:
#                             Skip_Next(account, prod_direction_left)
#                             bSecond = True
#                             break
#                     else:
#                         Skip_Next(account, prod_direction_left)
#                         bSecond = True
#                         break
#                 else:
#                     Skip_Next(account, prod_direction_left)
#                     bSecond = True
#                     break
#             else:
#                 Skip_Next(account, prod_direction_left)
#                 bSecond = True
#                 break
#         else:
#             Skip_Next(account, prod_direction_left)
#             bSecond = True
#             break
#         # 작업 순방향 끝
#     if bProdHigh and bSecond and smith_num == 2:  # 두 번째 건물 작업
#         # 작업 역방향 시작
#         if (smith_lev7 == 0):
#             if (smith_lev6 == 0):
#                 if (smith_lev5 == 0):
#                     if (smith_lev4 == 0):
#                         if (smith_lev3 == 0):
#                             if (smith_lev2 == 0):
#                                 prod_action('smith_lev1.png', 'smith_stby_lv1.png', account, smith_lev1)
#                                 Skip_Next(account, prod_direction_left)
#                                 bSecond = False
#                                 break
#                             else:
#                                 prod_action('smith_lev2.png', 'smith_stby_lv2.png', account, smith_lev2)
#                                 Skip_Next(account, prod_direction_left)
#                                 bSecond = False
#                                 break
#                         else:
#                             prod_action('smith_lev3.png', 'smith_stby_lv3.png', account, smith_lev3)
#                             Skip_Next(account, prod_direction_left)
#                             bSecond = False
#                             break
#                     else:
#                         Updown(account, 'up')
#                         prod_action('smith_lev4.png', 'smith_stby_lv4.png', account, smith_lev4)
#                         Skip_Next(account, prod_direction_left)
#                         bSecond = False
#                         break
#                 else:
#                     Updown(account, 'up')
#                     Updown(account, 'up')
#                     prod_action('smith_lev5.png', 'smith_stby_lv5.png', account, smith_lev5)
#                     Skip_Next(account, prod_direction_left)
#                     bSecond = False
#                     break
#             else:
#                 Updown(account, 'up')
#                 Updown(account, 'up')
#                 Updown(account, 'up')
#                 prod_action('smith_lev6.png', 'smith_stby_lv6.png', account, smith_lev6)
#                 Skip_Next(account, prod_direction_left)
#                 bSecond = False
#                 break
#         else:
#             Updown(account, 'up')
#             Updown(account, 'up')
#             Updown(account, 'up')
#             Updown(account, 'up')
#             prod_action('smith_lev7.png', 'smith_stby_lv7.png', account, smith_lev7)
#             Skip_Next(account, prod_direction_left)
#             bSecond = False
#             break
#         # 작업 역방향 끝




# if building == 'normal':
# list_numb1 = pag.locateAllOnScreen('prod_check_point.PNG', confidence=0.9, region=(560 + (account // 2) * 960, 75 + (account % 2) * 540, 105, 185))  # 일반 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
# # elif building == 'magic':
# list_numb1 = pag.locateAllOnScreen('prod_clock.PNG', confidence=0.9, region=(552 + (account // 2) * 960, 75 + (account % 2) * 540, 25, 460))  # 마법공방 건물일때
# list_numb2 = list(list_numb1)
# print(list_numb2)
# a = list_numb2[0][0] + 52
# b = list_numb2[0][1] -111
# # c = (a, b)
# # print(list_numb2[0][0], list_numb2[0][1])
# print(a, b)
# # print(c)
# # print(c[0][0], c[0][1])
#
#
#
