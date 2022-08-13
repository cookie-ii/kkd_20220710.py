import pyautogui as pag
import time
import keyboard

# 초코칩 토핑 - 쿨타임, 피감, (공격력)
cool_to_6 = False
cool_to_12 = False

# 라즈베리 토핑 - 공격력, (쿨타임, 피감)
attack_to_6 = False
attack_to_12 = False

# 아몬드 토핑 - 피감 올리기
defense_to_6 = True
defense_to_12 = False

account = 0


error_count_topping = 0
while cool_to_12:      # 쿨 토핑 6~9렙 -> 12렙으로
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_cool6 = pag.locateCenterOnScreen('topping_cool6.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    topping_cool9 = pag.locateCenterOnScreen('topping_cool9.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_cool6 or topping_cool9:
        # 토핑 선택
        if (topping_cool9):
            pag.click(topping_cool9)
        elif(topping_cool6):
            pag.click(topping_cool6)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)
        # 12강 선택
        pag.click(525 + (account // 2) * 960, 261 + (account % 2) * 540)
        time.sleep(0.8)
        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(9)
        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647+(account//2)*960, 78+(account%2)*540, 49, 46))
            if(research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)

        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)

while cool_to_6:      # 쿨토핑 1렙->6렙까지
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_cool = pag.locateCenterOnScreen('topping_cool.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_cool:
        # 토핑 선택
        pag.click(topping_cool)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)

        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(5)

        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
            if (research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)

        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)


while attack_to_12:      # 쿨 토핑 6~9렙 -> 12렙으로
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_attack6 = pag.locateCenterOnScreen('topping_attack6.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    topping_attack9 = pag.locateCenterOnScreen('topping_attack9.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_attack6 or topping_attack9:
        # 토핑 선택
        if (topping_attack9):
            pag.click(topping_attack9)
        elif(topping_attack6):
            pag.click(topping_attack6)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)
        # 12강 선택
        pag.click(525 + (account // 2) * 960, 261 + (account % 2) * 540)
        time.sleep(0.8)
        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(9)
        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647+(account//2)*960, 78+(account%2)*540, 49, 46))
            if(research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)

        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)

while attack_to_6:      # 쿨토핑 1렙->6렙까지
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_attack = pag.locateCenterOnScreen('topping_attack.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_attack:
        # 토핑 선택
        pag.click(topping_attack)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)

        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(5)

        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
            if (research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)

        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)


while defense_to_12:      # 쿨 토핑 6~9렙 -> 12렙으로
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_defense6 = pag.locateCenterOnScreen('topping_defense6.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    topping_defense9 = pag.locateCenterOnScreen('topping_defense9.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_defense6 or topping_defense9:
        # 토핑 선택
        if (topping_defense9):
            pag.click(topping_defense9)
        elif(topping_defense6):
            pag.click(topping_defense6)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)
        # 12강 선택
        pag.click(525 + (account // 2) * 960, 261 + (account % 2) * 540)
        time.sleep(0.8)
        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(9)
        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647+(account//2)*960, 78+(account%2)*540, 49, 46))
            if(research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)

        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)

while defense_to_6:      # 쿨토핑 1렙->6렙까지
    # 강제종료
    if keyboard.is_pressed('end'):
        break

    topping_defense = pag.locateCenterOnScreen('topping_defense.PNG', confidence=0.9, region=(483 + (account // 2) * 960, 125 + (account % 2) * 540, 396, 359))
    research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
    if topping_defense:
        # 토핑 선택
        pag.click(topping_defense)
        time.sleep(0.8)
        # '강화'버튼 클릭
        pag.click(350+(account//2)*960, 500+(account%2)*540)
        time.sleep(0.8)
        #  '연속 강화' 버튼 클릭
        pag.click(620+(account//2)*960, 492+(account%2)*540)
        time.sleep(0.8)

        # 또 들어가서 '연속 강화' 버튼 클릭
        pag.click(456+(account//2)*960, 374+(account%2)*540)
        time.sleep(5)

        while True:
            research_window = pag.locateCenterOnScreen('research_window.png', confidence=0.96, region=(647 + (account // 2) * 960, 78 + (account % 2) * 540, 49, 46))
            if (research_window):
                print('강화 끝')
                pag.click(research_window)
                time.sleep(0.8)
                break
            else:
                print('기다려요')
                time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875+(account//2)*960, 101+(account%2)*540)
        time.sleep(1.5)
    elif (research_window):
        print('강화 끝')
        pag.click(research_window)
        time.sleep(0.8)
        # 강화 창 나가기
        pag.click(875 + (account // 2) * 960, 101 + (account % 2) * 540)
        time.sleep(1.5)
    else: # 강화안된 토핑이 안보여!
        if(error_count_topping>=3):
            print('매크로 종료')
            break
        print('화면 올림')
        error_count_topping = error_count_topping+1
        # 화면 올렷
        Updown(account, 'up')
        time.sleep(0.8)