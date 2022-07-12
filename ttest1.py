import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
from datetime import datetime
import random


#
# def Skip_Next(account, prod_direction_left):
#     if prod_direction_left:  # 이레가 수정햇서
#         pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
#         time.sleep(0.5)
#         prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95, region=(339 + (account // 2) * 960, 253 + (account % 2) * 540, 175, 87))
#         time.sleep(1)
#         if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
#             print('욕심을 버리시오 중생이여..')
#             pag.click(455 + (account // 2) * 960, 379 + (account % 2) * 540)
#             time.sleep(0.3)
#             pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
#             time.sleep(0.3)
#     else:
#         pag.click(485 + (account // 2) * 960, 280 + (account % 2) * 540)
#         time.sleep(0.3)
#
#     cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#     if (cond_network):
#         pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#         time.sleep(0.3)
#     # 220201 흠.. 대충 범위 내 점점점의 점 하나를 찾아 클릭하는 것..
#     # 클릭 괜찮은 x좌표 223~427, 클릭 안되는 y좌표 777~862(237~322)
#     dotdotdot4 = pag.locateCenterOnScreen('dotdotdot4.png', confidence=0.814, region=(150 + (account // 2) * 960, 200 + (account % 2) * 540, 360, 160))
#
#     if (dotdotdot4):
#         # print('dotdotdot4:', dotdotdot4)
#         if (dotdotdot4.y+88 >= 468 + (account % 2) * 540):
#             dotdotdot4.y = dotdotdot4.y - (dotdotdot4.y + 88 - 468)
#             pag.click(dotdotdot4.x, dotdotdot4.y)
#         elif (dotdotdot4.x >= 415+(account//2)*960):
#             changed_dot = dotdotdot4.x + (424+(account//2)*960 - dotdotdot4.x)
#             pag.click(changed_dot, dotdotdot4.y+88)
#         elif (dotdotdot4.x <= 232 + (account // 2) * 960):
#             changed_dot = dotdotdot4.x + (227+(account//2)*960 - dotdotdot4.x)
#             pag.click(changed_dot, dotdotdot4.y + 88)
#         else:
#             pag.click(dotdotdot4.x, dotdotdot4.y+88)
#         time.sleep(0.3)
#
#     return
#
# def numb_new_recog(prod_pin, line, account):
#     its_number = 0
#     how_many_nums = 0
#     pos_numb = 0  # 0인 경우는 걍 0.. 1의자리 1, 십의자리2, 그외 3.. 만개 이상 재고는 없겠지
#     num_list = list()
#     # print('라인 %s번 진행합니다!' % (line))
#     screen = ImageGrab.grab()
#     # 3렙 건물인 경우 무조건 prod_pin = (612,95)
#     # print('?', prod_pin[0]+19,prod_pin[1]+81+153*(line-1))
#     pix_jaritsu1_1 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
#     # print((prod_pin[0] + 19 , prod_pin[1] + 81 + 153 * (line - 1)))
#     # print('pix_자릿수1_1:', pix_jaritsu1_1)
#     pix_jaritsu1_2 = screen.getpixel((prod_pin[0] + 19 , prod_pin[1] + 87 + 153 * (line - 1)))  # 하
#     # print((prod_pin[0] + 19 , prod_pin[1] + 87 + 153 * (line - 1)))
#     # print('pix_자릿수1_2:', pix_jaritsu1_2)
#
#
#     if ((pix_jaritsu1_1) == (255, 255, 255)) and ((pix_jaritsu1_2) == (255, 255, 255)):
#         pix_zero_1 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 82 + 153 * (line - 1)))  # 상
#         # print((prod_pin[0] + 24 , prod_pin[1] + 82 + 153 * (line - 1)))
#         # print('pix_zero_1:', pix_zero_1)
#         pix_zero_2 = screen.getpixel((prod_pin[0] + 24 , prod_pin[1] + 85 + 153 * (line - 1)))  # 하
#         # print((prod_pin[0] + 24 , prod_pin[1] + 85 + 153 * (line - 1)))
#         # print('pix_zero_2:', pix_zero_2)
#         # print('pos_numb', pos_numb)
#         for p in pix_zero_1:
#             if p < 252:
#                 pos_numb = 1
#         for p in pix_zero_2:
#             if p < 252:
#                 pos_numb = 1
#         if pos_numb == 0:
#             print('이 숫자는 0 입니다!')
#             its_number = 0
#             return 0
#         # if pos_numb == 1:
#         # print('이 숫자는 한 자릿 수 입니다!')
#     else:
#         pix_jaritsu2_1 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 상
#         # print((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))
#         # print('pix_자릿수2_1:', pix_jaritsu2_1)
#         pix_jaritsu2_2 = screen.getpixel((prod_pin[0] + 14 , prod_pin[1] + 81 + 153 * (line - 1)))  # 하
#         # print((prod_pin[0] + 14, prod_pin[1] + 81 + 153 * (line - 1)))
#         # print('pix_자릿수2_2:', pix_jaritsu2_2)
#         if ((pix_jaritsu2_1) == (255, 255, 255)) and ((pix_jaritsu2_2) == (255, 255, 255)):
#             # print('이 숫자는 두 자릿 수 입니다!')
#             pos_numb = 2
#         else:
#             # print('이 숫자는 세 자릿 수 입니다!')
#             pos_numb = 3
#     # print('자릿수 다시 확인', pos_numb)
#     if pos_numb == 1:
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         # print('한 자릿 수 범위 확인1', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1))
#         if (num_1):
#             return 1
#         num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_1_1):
#             return 1
#         num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_2):
#             return 2
#         num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_3):
#             return 3
#         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_3_1):
#             return 3
#         num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_4):
#             return 4
#         num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_4_2):
#             return 4
#         num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_5):
#             return 5
#         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_6):
#             return 6
#         num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_7):
#             return 7
#         num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_8):
#             return 8
#         num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_8_1):
#             return 8
#         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_9):
#             return 9
#         num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14))
#         if (num_9_1):
#             return 9
#         return 0
#
#     if pos_numb == 2:
#         # 10의자리 숫자 걍검색
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#         # print('두 자릿 수 10자리 범위', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1))
#         if (num_1):
#             its_number = its_number + 10
#         else:
#             num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#             if (num_1_1):
#                 its_number = its_number + 10
#             else:
#                 num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                 if (num_2):
#                     its_number = its_number + 20
#                 else:
#                     num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                     if (num_3):
#                         its_number = its_number + 30
#                     else:
#                         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                         if (num_3_1):
#                             its_number = its_number + 30
#                         else:
#                             num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                             if (num_4):
#                                 its_number = its_number + 40
#                             else:
#                                 num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                 if (num_4_2):
#                                     its_number = its_number + 40
#                                 else:
#                                     num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                     if (num_5):
#                                         its_number = its_number + 50
#                                     else:
#                                         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                         if (num_6):
#                                             its_number = its_number + 60
#                                         else:
#                                             num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                             if (num_7):
#                                                 its_number = its_number + 70
#                                             else:
#                                                 num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                                 if (num_8):
#                                                     its_number = its_number + 80
#                                                 else:
#                                                     num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                                     if (num_8_1):
#                                                         its_number = its_number + 80
#                                                     else:
#                                                         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                                         if (num_9):
#                                                             its_number = its_number + 90
#                                                         else:
#                                                             num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 11, 14))
#                                                             if (num_9_1):
#                                                                 its_number = its_number + 90
#                                                             else:
#                                                                 print('십의 자리 숫자 확인 에러!!')
#         # 1의자리 숫자 걍검색
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#         # print('두자릿수 1자리 범위:', prod_pin[0] + 24 - pos_numb * 5 + 10, prod_pin[1] + 85 - 7 + 153 * (line - 1))
#         if (num_1):
#             its_number = its_number + 1
#         else:
#             num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#             if (num_1_1):
#                 its_number = its_number + 1
#             else:
#                 num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                 if (num_2):
#                     its_number = its_number + 2
#                 else:
#                     num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                     if (num_3):
#                         its_number = its_number + 3
#                     else:
#                         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                         if (num_3_1):
#                             its_number = its_number + 3
#                         else:
#                             num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                             if (num_4):
#                                 its_number = its_number + 4
#                             else:
#                                 num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                 if (num_4_2):
#                                     its_number = its_number + 4
#                                 else:
#                                     num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                     if (num_5):
#                                         its_number = its_number + 5
#                                     else:
#                                         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                         if (num_6):
#                                             its_number = its_number + 6
#                                         else:
#                                             num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                             if (num_7):
#                                                 its_number = its_number + 7
#                                             else:
#                                                 num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                 if (num_8):
#                                                     its_number = its_number + 8
#                                                 else:
#                                                     num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                     if (num_8_1):
#                                                         its_number = its_number + 8
#                                                     else:
#                                                         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                         if (num_9):
#                                                             its_number = its_number + 9
#                                                         else:
#                                                             num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                             if (num_9_1):
#                                                                 its_number = its_number + 9
#                                                             else:
#                                                                 print('일의 자리 숫자 확인 에러!!')
#         # print('현재 재고는 =', its_number)
#         return its_number
#     if pos_numb == 3:
#         # print('세 자릿 수 범위 확인', prod_pin[0] + 24 - pos_numb * 5, prod_pin[1] + 85 - 7 + 153 * (line - 1), pos_numb * 5 * 2, 14)
#         # 100의 자리
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#         if (num_1):
#             its_number = its_number + 100
#         else:
#             num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#             if (num_1_1):
#                 its_number = its_number + 100
#             else:
#                 num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                 if (num_2):
#                     its_number = its_number + 200
#                 else:
#                     num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                     if (num_3):
#                         its_number = its_number + 300
#                     else:
#                         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                         if (num_3_1):
#                             its_number = its_number + 300
#                         else:
#                             num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                             if (num_4):
#                                 its_number = its_number + 400
#                             else:
#                                 num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                 if (num_4_2):
#                                     its_number = its_number + 400
#                                 else:
#                                     num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                     if (num_5):
#                                         its_number = its_number + 500
#                                     else:
#                                         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                         if (num_6):
#                                             its_number = its_number + 600
#                                         else:
#                                             num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                             if (num_7):
#                                                 its_number = its_number + 700
#                                             else:
#                                                 num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                 if (num_8):
#                                                     its_number = its_number + 800
#                                                 else:
#                                                     num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                     if (num_8_1):
#                                                         its_number = its_number + 800
#                                                     else:
#                                                         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                         if (num_9):
#                                                             its_number = its_number + 900
#                                                         else:
#                                                             num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(622+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                             if (num_9_1):
#                                                                 its_number = its_number + 900
#                                                             else:
#                                                                 print('백의 자리 숫자 확인 에러!!')
#         # 10의 자리 숫자 걍검색
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#         if (num_1):
#             its_number = its_number + 10
#         else:
#             num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#             if (num_1_1):
#                 its_number = its_number + 10
#             else:
#                 num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                 if (num_2):
#                     its_number = its_number + 20
#                 else:
#                     num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                     if (num_3):
#                         its_number = its_number + 30
#                     else:
#                         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                         if (num_3_1):
#                             its_number = its_number + 30
#                         else:
#                             num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                             if (num_4):
#                                 its_number = its_number + 40
#                             else:
#                                 num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                 if (num_4_2):
#                                     its_number = its_number + 40
#                                 else:
#                                     num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                     if (num_5):
#                                         its_number = its_number + 50
#                                     else:
#                                         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                         if (num_6):
#                                             its_number = its_number + 60
#                                         else:
#                                             num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                             if (num_7):
#                                                 its_number = its_number + 70
#                                             else:
#                                                 num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                 if (num_8):
#                                                     its_number = its_number + 80
#                                                 else:
#                                                     num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                     if (num_8_1):
#                                                         its_number = its_number + 80
#                                                     else:
#                                                         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                         if (num_9):
#                                                             its_number = its_number + 90
#                                                         else:
#                                                             num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                             if (num_9_1):
#                                                                 its_number = its_number + 90
#                                                             else:
#                                                                 num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(631+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                                 if (num_0):
#                                                                     print('십의 자리 0!!')
#                                                                 else:
#                                                                     print('10의 자리 못읽음..')
#         # 1의 자리 숫자 걍검색
#         num_1 = pag.locateCenterOnScreen('prod_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#         if (num_1):
#             its_number = its_number + 1
#         else:
#             num_1_1 = pag.locateCenterOnScreen('prod_1_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#             if (num_1_1):
#                 its_number = its_number + 1
#             else:
#                 num_2 = pag.locateCenterOnScreen('prod_2.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                 if (num_2):
#                     its_number = its_number + 2
#                 else:
#                     num_3 = pag.locateCenterOnScreen('prod_3.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                     if (num_3):
#                         its_number = its_number + 3
#                     else:
#                         num_3_1 = pag.locateCenterOnScreen('prod_3_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                         if (num_3_1):
#                             its_number = its_number + 3
#                         else:
#                             num_4 = pag.locateCenterOnScreen('prod_4.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                             if (num_4):
#                                 its_number = its_number + 4
#                             else:
#                                 num_4_2 = pag.locateCenterOnScreen('prod_4_2.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                 if (num_4_2):
#                                     its_number = its_number + 4
#                                 else:
#                                     num_5 = pag.locateCenterOnScreen('prod_5.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                     if (num_5):
#                                         its_number = its_number + 5
#                                     else:
#                                         num_6 = pag.locateCenterOnScreen('prod_6.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                         if (num_6):
#                                             its_number = its_number + 6
#                                         else:
#                                             num_7 = pag.locateCenterOnScreen('prod_7.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                             if (num_7):
#                                                 its_number = its_number + 7
#                                             else:
#                                                 num_8 = pag.locateCenterOnScreen('prod_8.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                 if (num_8):
#                                                     its_number = its_number + 8
#                                                 else:
#                                                     num_8_1 = pag.locateCenterOnScreen('prod_8_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                     if (num_8_1):
#                                                         its_number = its_number + 8
#                                                     else:
#                                                         num_9 = pag.locateCenterOnScreen('prod_9.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                         if (num_9):
#                                                             its_number = its_number + 9
#                                                         else:
#                                                             num_9_1 = pag.locateCenterOnScreen('prod_9_1.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                             if (num_9_1):
#                                                                 its_number = its_number + 9
#                                                             else:
#                                                                 num_0 = pag.locateCenterOnScreen('prod_0.png', confidence=0.8, region=(640+((account // 2)*960) , prod_pin[1] + 85 - 7 + 153 * (line - 1), 10, 14))
#                                                                 if (num_0):
#                                                                     print('1의 자리 0!!')
#                                                                 else:
#                                                                     print('1의 자리 못읽음..')
#         print('현재 재고는 =', its_number)
#         return its_number
#
# def three_prod_action(account, check_list_img1, check_list_img2, check_list_img3, check_num1, check_num2, check_num3, prod_direction_left):
#     start_time = time.time()
#
#     cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#     if (cond_network):
#         pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#         time.sleep(0.3)
#
#     prod_refresh = pag.locateCenterOnScreen('prod_refresh.png', confidence=0.955, region=(90 + (account // 2) * 960, 145 + (account % 2) * 540, 24, 20))
#     if not (prod_refresh):
#         # 생산품 완료 + 혹시 운좋아 점점점을 클릭할 수도..
#         pag.click(x=random.randint(223, 428) + (account // 2) * 960, y=random.randint(336, 398) + (account % 2) * 540)
#         time.sleep(0.5)
#
#     # cond_2nd_clear = pag.locateCenterOnScreen('cond_2nd_clear.png', confidence=0.96, region=(75 - 10 + (account//2)*960, 200 - 10 + (account%2) * 540, 20, 20))
#     # cond_2nd_clear1 = pag.locateCenterOnScreen('cond_2nd_clear1.png', confidence=0.94, region=(75 - 10 + (account // 2) * 960, 200 - 10 + (account % 2) * 540, 20, 20))
#     cond_3rd_clear1 = pag.locateCenterOnScreen('cond_3rd_clear1.png', confidence=0.94, region=(75 - 10 + (account // 2) * 960, 200 - 10 + 70+(account % 2) * 540, 20, 20))
#     if not (cond_3rd_clear1):
#         Skip_Next(account, prod_direction_left)
#         return True
#
#     # 풀리스트인 경우 넘어감
#     prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#     prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#     prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#     prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#     prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#     if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
#         print('리스트 full!4')
#         return True
#
#     # 3렙건물이니 고정
#     prod_pin = (612+(account//2)*960, 95 + (account % 2) * 540)
#     # prod_pin = (612 + (account // 2) * 960, 95 + (account % 2) * 540)             # 이렇게 안고쳐도 되나?
#     # print('prod_pin:', prod_pin)
#     target_numb1 = check_num1 - numb_new_recog(prod_pin, 1, account)
#     # print('1st ok', target_numb1)
#     # print('')
#     # print('prod_pin:', prod_pin)
#     target_numb2 = check_num2 - numb_new_recog(prod_pin, 2, account)
#     # print('2nd ok', target_numb2)
#     # print('')
#     # print('prod_pin:', prod_pin)
#     target_numb3 = check_num3 - numb_new_recog(prod_pin, 3, account)
#     # print('3rd ok', target_numb3)
#     # print('')
#     # 기타 조건 초기화
#     line1_clicked = 0
#     line2_clicked = 0
#     line3_clicked = 0
#     prod_line1_completed = False
#     prod_line2_completed = False
#     prod_line3_completed = False
#     list_numbb1 = 0
#     list_numbb2 = 0
#     list_numbb3 = 0
#
#     # 리스트를 한번만 읽자!
#     if check_num1 != 0:  # 목표값이 있고(열었고)
#         if target_numb1 > 0:  # 목표 수량보다 부족한 경우
#             list_numb1 = pag.locateAllOnScreen(check_list_img1, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
#             list_numb1 = list(list_numb1)
#             # print('list_numb1:', list_numb1)
#             # print('len(...):', len(list_numb1))
#             if len(list_numb1) > 0:
#                 list_numbb1 = len(list_numb1)  # 현재 리스트에 몇 개 있냐
#             else:
#                 list_numbb1 = 0
#     else:
#         prod_line1_completed = True
#         compare_numb1 = -1
#         list_numbb1 = 0
#
#     if check_num2 != 0:  # 목표값이 있고(열었고)
#         if target_numb2 > 0:  # 목표 수량보다 부족한 경우
#             list_numb2 = pag.locateAllOnScreen(check_list_img2, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
#             list_numb2 = list(list_numb2)
#             # print('list_numb2:', list_numb2)
#             # print('len(...):', len(list_numb2))
#             if len(list_numb2) > 0:
#                 list_numbb2 = len(list_numb2)  # 현재 리스트에 몇 개 있냐
#             else:
#                 list_numbb2 = 0
#     else:
#         prod_line2_completed = True
#         compare_numb2 = -1
#         list_numbb2 = 0
#
#     if check_num3 != 0:  # 목표값이 있고(열었고)
#         if target_numb3 > 0:  # 목표 수량보다 부족한 경우
#             list_numb3 = pag.locateAllOnScreen(check_list_img3, confidence=0.95, region=(42 + (account // 2) * 960, 169 + (account % 2) * 540, 66, 318))
#             list_numb3 = list(list_numb3)
#             # print('list_numb3:', list_numb3)
#             # print('len(...):', len(list_numb3))
#             if len(list_numb3) > 0:
#                 list_numbb3 = len(list_numb3)  # 현재 리스트에 몇 개 있냐
#             else:
#                 list_numbb3 = 0
#     else:
#         prod_line3_completed = True
#         compare_numb3 = -1
#         list_numbb3 = 0
#
#     print('현재 리스트에는 = 1:%s, 2:%s, 3:%s개 있습니다.' % (target_numb1, target_numb2, target_numb3))
#     while True:
#         now_time = time.time()
#         cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
#         if (cond_network):
#             pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
#             time.sleep(0.3)
#
#         # 풀리스트인 경우 넘어감
#         prod_full_list3 = pag.locateCenterOnScreen('prod_full_list3.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#         prod_full_list4 = pag.locateCenterOnScreen('prod_full_list4.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#         prod_full_list5 = pag.locateCenterOnScreen('prod_full_list5.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#         prod_full_list6 = pag.locateCenterOnScreen('prod_full_list6.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#         prod_full_list7 = pag.locateCenterOnScreen('prod_full_list7.png', confidence=0.95, region=(45 + (account // 2) * 960, 60 + (account % 2) * 540, 55, 22))
#         if (prod_full_list3) or (prod_full_list4) or (prod_full_list5) or (prod_full_list6) or (prod_full_list7):
#             print('리스트 full!5')
#             prod_warehousefull = pag.locateCenterOnScreen('prod_warehousefull.PNG', confidence=0.95, region=(339 + (account // 2) * 960, 253 + (account % 2) * 540, 175, 87))
#             time.sleep(1)
#             if (prod_warehousefull):  # 이레가 추가 ㅠ.ㅠ
#                 print('욕심을 버리시오 중생이여..')
#                 pag.click(455 + (account // 2) * 960, 379 + (account % 2) * 540)
#                 time.sleep(0.3)
#                 pag.click(164 + (account // 2) * 960, 280 + (account % 2) * 540)
#                 time.sleep(0.3)
#             else:
#                 Skip_Next(account, prod_direction_left)
#             return True
#         # 동작시간 확인
#         if now_time - start_time > 30:
#             print('동작 최대시간 초과 입니다.')
#             Skip_Next(account, prod_direction_left)
#             return False
#
#         # 강제종료
#         if keyboard.is_pressed('end'):
#             return False
#
#         # 조건 확인
#         play_halted = pag.locateCenterOnScreen('cond_g_play.png', region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#         # 구글 플레이 종료 뭐시기
#         if (play_halted):
#             pag.click(play_halted)
#
#         # 리스트 수량 파악
#         if (target_numb1 - list_numbb1 - line1_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
#             # print('target_numb1 - list_numbb1 - line1_clicked:', target_numb1 - list_numbb1 - line1_clicked)
#             compare_numb1 = (target_numb1 - list_numbb1 - line1_clicked) / check_num1  # 비율(1을 안넘음)
#             # print('compare_numb1:', compare_numb1)
#         else:
#             compare_numb1 = -1
#             prod_line1_completed = True
#
#         if (target_numb2 - list_numbb2 - line2_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
#             # print('target_numb2 - list_numbb2 - line2_clicked:', target_numb2 - list_numbb2 - line2_clicked)
#             compare_numb2 = (target_numb2 - list_numbb2 - line2_clicked) / check_num2  # 비율(1을 안넘음)
#             # print('compare_numb2:', compare_numb1)
#         else:
#             compare_numb2 = -1
#             prod_line2_completed = True
#
#         if (target_numb3 - list_numbb3 - line3_clicked) > 0:  # 부족분-리스트 > 0 이면 더 만들어야지
#             # print('target_numb3 - list_numbb3 - line3_clicked:', target_numb3 - list_numbb3 - line3_clicked)
#             compare_numb3 = (target_numb3 - list_numbb3 - line3_clicked) / check_num3  # 비율(1을 안넘음)
#             # print('compare_numb3:', compare_numb1)
#         else:
#             compare_numb3 = -1
#             prod_line3_completed = True
#
#         if (prod_line1_completed and prod_line2_completed and prod_line3_completed):
#             Skip_Next(account, prod_direction_left)
#             return False
#         else:
#             max_numb = max(compare_numb1, compare_numb2, compare_numb3)
#             if max_numb == compare_numb1 and not prod_line1_completed:
#                 pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + (account % 2) * 540)
#                 lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
#                     print('재료가 부족해요')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line1_clicked = 999  # 나락으로 보내버력!
#                 elif (not_opened):  # 안 연거
#                     print('열지 않은 제품이라서 넘어가겠어요~!')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line1_clicked = 999  # 나락으로 보내버력!
#                 else:
#                     line1_clicked = line1_clicked + 1
#             if max_numb == compare_numb2 and not prod_line2_completed:
#                 pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + 153 + (account % 2) * 540)
#                 lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
#                     print('재료가 부족해요')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line2_clicked = 999  # 나락으로 보내버력!
#                 elif (not_opened):  # 안 연거
#                     print('열지 않은 제품이라서 넘어가겠어요~!')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line2_clicked = 999  # 나락으로 보내버력!
#                 else:
#                     line2_clicked = line2_clicked + 1
#             if max_numb == compare_numb3 and not prod_line3_completed:
#                 pag.click(random.randint(745, 745 + 10) + (account // 2) * 960, random.randint(190, 190 + 15) + 153 * 2 + (account % 2) * 540)
#                 lack_of_material = pag.locateCenterOnScreen('lack_material.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 not_opened = pag.locateCenterOnScreen('Cond_not_opened.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
#                 if (lack_of_material):  # 어디 라인 재료가 부족한 지 모르겠네.. 1렙거 부족하면 다 생산 못하겠는데
#                     print('재료가 부족해요')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line3_clicked = 999  # 나락으로 보내버력!
#                 elif (not_opened):  # 안 연거
#                     print('열지 않은 제품이라서 넘어가겠어요~!')
#                     pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
#                     time.sleep(0.1)
#                     pag.hotkey('esc')
#                     time.sleep(0.5)
#                     line3_clicked = 999  # 나락으로 보내버력!
#                 else:
#                     line3_clicked = line3_clicked + 1
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
#                 pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 153 + 13) + (account % 2) * 540, 2, 0.3)
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
#                 pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 153 + 13) + (account % 2) * 540, 2, 0.3)
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



# account=0
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((901 + (account // 2) * 960, 138 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단
# # pix_pass_reward_exist = (254, 0, 0)# print(pix_reward)
# pix_pass_reward_exist = (254, 1, 1)
# print(pix_pass_reward)
#
# account=1
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((901 + (account // 2) * 960, 138 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단
# # pix_pass_reward_exist = (254, 0, 0)# print(pix_reward)
# pix_pass_reward_exist = (254, 1, 1)
# print(pix_pass_reward)
#
# account=2
# screen = ImageGrab.grab()
# pix_pass_reward = screen.getpixel((901 + (account // 2) * 960, 138 + (account % 2) * 540))  # 패스 보상# pix_reward = screen.getpixel((39 + (account // 2) * 960, 340 + (account % 2) * 540))  # 소원나무 일일보상 칸 좌상단
# # pix_pass_reward_exist = (254, 0, 0)# print(pix_reward)
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

# account =0
# screen = ImageGrab.grab()
# pix_status = screen.getpixel((605 + (account // 2) * 960, 55 + (account % 2) * 540))  # 상단골드
# print(pix_status)

# pix_prod = screen.getpixel((610 + (account // 2) * 960, 140 + (account % 2) * 540))
# print(pix_prod)

# pix_lackof = screen.getpixel((545 + (account // 2) * 960, 745 - 540 + (account % 2) * 540))  # 재료부족창?
# print(pix_lackof)

# pix_status = screen.getpixel((460 + (account // 2) * 960, 90 + (account % 2) * 540))  # 소원나무 확인 뽀인트
# print(pix_status)

account = 0
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
                    pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 153 + 13) + (account % 2) * 540, 2, 0.3)
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
                    pag.click(random.randint(629, 629 + 13) + (account // 2) * 960, random.randint(153, 153 + 13) + (account % 2) * 540, 2, 0.3)
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
Scroll_count = 0
start_time = time.time()
while True:
    if Scroll_count == 0:
        print('기둥동네예요!')
        trade_kidung = pag.locateCenterOnScreen('trade_kidung.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
        trade_block = pag.locateCenterOnScreen('trade_block.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
        trade_nachimban = pag.locateCenterOnScreen('trade_nachimban.png', confidence=0.85, region=(2 + (account // 2) * 960, 350 + (account % 2) * 540, 917, 45))
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
            pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
            time.sleep(2)
        if block_numb > 0 and block_numb == max_numb:
            pag.click(trade_block)
            time.sleep(0.5)
            pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
            time.sleep(2)
        if nachimban_numb > 0 and nachimban_numb == max_numb:
            pag.click(trade_nachimban)
            time.sleep(0.5)
            pag.click(random.randint(420, 500) + (account // 2) * 960, random.randint(370, 400) + (account % 2) * 540)
            time.sleep(2)
        # Angmu_Action('trade_tro_1', trade_tro_1)
        # Angmu_Action('trade_tro_2', trade_tro_2)

    if 2 >= Scroll_count >= 1:
        print('스크롤 ==', Scroll_count)
        trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26)) # 0.943하면 잘 못읽나?
        trade_baseline_list = list(trade_baseline)
        if len(trade_baseline_list) != 0:
            for p in trade_baseline_list:
                ctr = pag.center(p)
                # 범위 내 조건 확인
                if Angmu_Action('crystal_pure.png', ctr, account):
                    print('판별 완료',ctr)
                elif Angmu_Action('crystal_magic.png', ctr, account):
                    print('판별 완료',ctr)
                elif Angmu_Action('crystal_power.png', ctr, account):
                    print('판별 완료',ctr)
                elif Angmu_Action('crystal_quick.png', ctr, account):
                    print('판별 완료',ctr)
                elif Angmu_Action('trade_assist_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_assist_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_bomb_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_bomb_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_fist_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_fist_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_recovery_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_recovery_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_shield_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_shield_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_shooting_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_shooting_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_staff_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_staff_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_sword_lv1.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_sword_lv2.png', ctr, account):
                    print('판별 완료', ctr)
                elif Angmu_Action('trade_star.png', ctr, account):
                    print('별조각 판별 완료1', ctr)
                elif Angmu_Action('trade_swift_sugar.png', ctr, account):
                    print('신속의 설탕결정 판별 완료1', ctr)
                elif Angmu_Action('trade_pure_sugar.png', ctr, account):
                    print('순수의 설탕결정 판별 완료1', ctr)
                else:
                    print('여긴 어디 나는 누구?')

    if 5 > Scroll_count >= 1:
        print('스크롤 ==', Scroll_count)
        trade_baseline = pag.locateAllOnScreen('trade_baseline.png', confidence=0.943, region=(2 + (account // 2) * 960, 325 + (account % 2) * 540, 750, 26))
        trade_baseline_list = list(trade_baseline)
        print('trade_baseline_list:', trade_baseline_list)
        if len(trade_baseline_list) != 0:
            for p in trade_baseline_list:
                ctr = pag.center(p)
                # print('생산품까지 확인')
                print('생산품까지 확인, ctr:', ctr)
                if (account) == 0:
                    # if Angmu_Action('trade_cotton.png', ctr, account):
                    #     print('솜 판별 완료', ctr)
                    # elif Angmu_Action('trade_berry.png', ctr, account):
                    #     print('베리 판별 완료', ctr)
                    # elif Angmu_Action('trade_biscuit.png', ctr, account):
                    #     print('판별 완료',ctr)
                    if Angmu_Action('trade_milk.png', ctr, account):
                        print('우유 판별 완료',ctr)
                    elif Angmu_Action('trade_star.png', ctr, account):
                        print('별조각 판별 완료', ctr)
                    elif Angmu_Action('trade_swift_sugar.png', ctr, account):
                        print('신속의 설탕결정 판별 완료', ctr)
                    elif Angmu_Action('trade_pure_sugar.png', ctr, account):
                        print('순수의 설탕결정 판별 완료', ctr)
                    else:
                        print('여긴 어디 나는 누구 계정0')
                if (account) == 1:
                    # if Angmu_Action('trade_berry.png', ctr, account):
                    #     print('베리 판별 완료', ctr)
                    if Angmu_Action('trade_cotton.png', ctr, account):
                        print('솜 판별 완료',ctr)
                    # elif Angmu_Action('trade_biscuit.png', ctr, account):
                    #     print('판별 완료',ctr)
                    # elif Angmu_Action('trade_milk.png', ctr, account):
                    #     print('판별 완료',ctr)
                    elif Angmu_Action('trade_star.png', ctr, account):
                        print('별조각 판별 완료', ctr)
                    elif Angmu_Action('trade_swift_sugar.png', ctr, account):
                        print('신속의 설탕결정 판별 완료', ctr)
                    elif Angmu_Action('trade_pure_sugar.png', ctr, account):
                        print('순수의 설탕결정 판별 완료', ctr)

                    else:
                        print('여긴 어디 나는 누구 계정1')
                if (account) == 2:
                    # if Angmu_Action('trade_berry.png', ctr, account):
                    #     print('베리 판별 완료', ctr)
                    if Angmu_Action('trade_cotton.png', ctr, account):
                        print('솜 판별 완료',ctr)
                    # elif Angmu_Action('trade_biscuit.png', ctr, account):
                    #     print('판별 완료',ctr)
                    # elif Angmu_Action('trade_milk.png', ctr, account):
                    #     print('판별 완료',ctr)
                    elif Angmu_Action('trade_star.png', ctr, account):
                        print('별조각 판별 완료', ctr)
                    elif Angmu_Action('trade_swift_sugar.png', ctr, account):
                        print('신속의 설탕결정 판별 완료', ctr)
                    elif Angmu_Action('trade_pure_sugar.png', ctr, account):
                        print('순수의 설탕결정 판별 완료', ctr)

                    else:
                        print('여긴 어디 나는 누구 계정2')

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
    print('드래그')
    pag.moveTo(random.randint(786, 820) + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
    pag.mouseDown()
    time.sleep(0.5)
    pag.moveTo(random.randint(786, 820) - 150 * 3 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 5)  # 153인데 20 더 여유줌
    time.sleep(0.5)
    pag.mouseUp()
    time.sleep(0.5)

    # ++ 작업 후 >= 3으로변경
    if Scroll_count >= 4:
        print('완료')
        pag.click(284 + (account // 2) * 960, 15 + (account % 2) * 540)
        time.sleep(0.1)
        pag.hotkey('esc')
        time.sleep(2)
        pag.hotkey('esc')
        time.sleep(6)


    start_lineup = time.time()
    while True:
        if keyboard.is_pressed('end'):
            print('end 누름')
            break
        now_lineup = time.time()
        if now_lineup - start_lineup > 20:
            print('뭐얏...', '현재시간:', datetime.now().strftime('%H:%M:%S'))
            Scroll_count = Scroll_count + 1
            break
        if now_lineup - start_lineup > 60:
            print('뭐얏...111', '현재시간:', datetime.now().strftime('%H:%M:%S'))

        cond_network = pag.locateCenterOnScreen('cond_network.png', confidence=0.96, region=(440 + (account // 2) * 960, 363 + (account % 2) * 540, 43, 29))
        if (cond_network):
            pag.click(random.randint(462 - 5, 462 + 5) + (account // 2) * 960, random.randint(377 - 5, 377 + 5) + (account % 2) * 540)
            time.sleep(0.3)

        cond_trade_angmu_confirm = pag.locateCenterOnScreen('cond_trade_angmu_confirm.png', confidence=0.85, region=(420 + (account // 2) * 960, 80 + (account % 2) * 540, 58, 33))  # 해상무역센터 앵무 교역소 위치 확인
        if not (cond_trade_angmu_confirm):
            print('튕기거나 빠져나갔나봐요...')


        trade_baseline_gray = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (trade_baseline_gray):
            if (92 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline_gray[0] > 70 + 157 + (account // 2) * 960):
                Scroll_count = Scroll_count + 1
                break
            else:                 # 아니면 살짝 왼쪽으로 돌려서 영점조정
                pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
                time.sleep(0.5)
                trade_baseline_gray_new = pag.locateCenterOnScreen('trade_baseline_gray.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (trade_baseline_gray_new):
                    pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_gray_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(0.5)

        trade_baseline = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.9, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
        if (trade_baseline):
            print(92 + 157 + (account // 2) * 960, '>=', trade_baseline[0], '>', 70 + 157 + (account // 2) * 960)
            if (92 + (account // 2) * 960 >= trade_baseline[0] > 70 + (account // 2) * 960) or (92 + 157 + (account // 2) * 960 >= trade_baseline[0] > 70 + 157 + (account // 2) * 960):
                print(92 + 157 + (account // 2) * 960*2 ,'>=', trade_baseline[0] ,'>', 70 + 157 + (account // 2) * 960)
                Scroll_count = Scroll_count + 1
                break
            else:            # 약간 왼쪽으로(trade baseline 뉴 찾을때까지) 돌려
                pag.moveTo(790 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540))
                pag.mouseDown()
                time.sleep(0.5)
                pag.moveTo(790 + 50 + (account // 2) * 960, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 2)  # 한 번 움직여보고
                time.sleep(0.5)
                trade_baseline_new = pag.locateCenterOnScreen('trade_baseline.png', confidence=0.95, region=(2 + (account // 2) * 960, 32 + (account % 2) * 540, 917, 505))
                if (trade_baseline_new):
                    pag.moveTo(790+(account//2)*960*2 + 50 - trade_baseline_new[0] + 73, random.randint(474 + (account % 2) * 540, 481 + (account % 2) * 540), 3)  # 153인데 20 더 여유줌
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(0.5)
