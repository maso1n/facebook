import random
import pyautogui
import time
import random
import inform

def translete_ru():
    # перевод на ру
    pyautogui.click(1225, 740, duration=0.40)
    time.sleep(2)
    pyautogui.click(1225, 650, duration=0.40)
    time.sleep(2)

def translate_en():
    # перевод на англ
    pyautogui.click(1225, 740, duration=0.40)
    time.sleep(2)
    pyautogui.click(1225, 600, duration=0.40)
    time.sleep(2)
def random_x_y(start, end):
    return random.randrange(start, end, 1)

def random_time_duration():
    number = random.randrange(25, 32, 1)  # значение в диапазоне
    return number/100
def random_time_interval():
    number = random.randrange(11, 15, 1)  # значение в диапазоне
    return number/100
def random_scroll():
    if random.randrange(1, 11, 1) >= 8:
        pyautogui.scroll(random.randrange(-500, -300, 1))
    else:
        pass


time.sleep(5)
#translate_en()
selected_style = int(pyautogui.prompt('Пожалуйста введите стиль поста\n1 - текст\n2 - текст с фоном\n3 - картинку'))
print(selected_style)
for (index, group) in enumerate(inform.groups_links_list):
    time.sleep(4)
    #250 1000 45
    pyautogui.moveTo(random_x_y(250, 1000), random_x_y(45, 55), duration=random_time_duration())
    time.sleep(1.5)
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.typewrite(group, interval=random_time_interval())
    pyautogui.hotkey("enter")
    time.sleep(4)
    pyautogui.moveTo(random_x_y(500, 700), random_x_y(400, 600), 1.5, pyautogui.easeInQuad)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(2)
    pyautogui.click(random_x_y(1000, 1300), random_x_y(250, 350), duration=random_time_duration())
    time.sleep(5)
    pyautogui.scroll(random_x_y(-800, -600))
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(2)
    #pyautoguihotkey('ctrl', 'v')
    pyautogui.typewrite('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]')
    time.sleep(2)
    pyautogui.click(random_x_y(900, 1200), random_x_y(169, 172), duration=random_time_duration())
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(2)
    pyautogui.hotkey("f12")
    time.sleep(2)

    if selected_style == 1:
        pyautogui.click(random_x_y(550, 800), random_x_y(240, 250), duration=random_time_duration())
        time.sleep(1)
        time.sleep(2)
        pyautogui.hotkey('shift', 'alt')
        pyautogui.click(random_x_y(470, 850), random_x_y(370, 450), duration=random_time_duration())
        time.sleep(1)
        pyautogui.typewrite(inform.text, interval=random_time_interval())
        time.sleep(1.5) #делаем паузу между действиями
        pyautogui.moveTo(random_x_y(570, 750), random_x_y(619, 635), duration=random_time_duration())
        time.sleep(1.5)
        pyautogui.screenshot(r'C:\Users\m.babczenko\Desktop\photo\photo' + str(index) + '.png')
        print(index, group)
        pyautogui.click()
        pyautogui.hotkey('shift', 'alt')
        # pyautogui.moveTo(455, 490, 1)
        # time.sleep(1)
        # pyautogui.click()
        # pyautogui.moveTo(615, 490, 1)
        # time.sleep(0.5)
        # pyautogui.click()
        # pyautogui.moveTo(455, 490, 1)
        # time.sleep(1)
        # pyautogui.click()
    elif selected_style == 2:
        pyautogui.click(random_x_y(550, 800), random_x_y(240, 250), duration=random_time_duration())
        time.sleep(1)
        time.sleep(2)
        pyautogui.hotkey('shift', 'alt')
        pyautogui.click(random_x_y(470, 850), random_x_y(370, 450), duration=random_time_duration())
        time.sleep(1)
        pyautogui.typewrite(
            "Gjvjuf. dctv erhfbywfv ,tcgkfnyj\n yfqnb hf,jne b ;bkmt d Gjkmit Dfq,th +48576438617",
            interval=random_time_interval())
        time.sleep(1.5)  # делаем паузу между действиями
        pyautogui.moveTo(455, 490, 1)
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(615, 490, 1)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(455, 490, 1)
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(random_x_y(570, 750), random_x_y(619, 635), duration=random_time_duration())
        time.sleep(1.5)
        pyautogui.screenshot(r'C:\Users\m.babczenko\Desktop\photo\photo' + str(index) + '.png')
        print(index, group)
        pyautogui.click()
        pyautogui.hotkey('shift', 'alt')
    elif selected_style == 3:
    #660 720 290
        pyautogui.click(random_x_y(660, 720), random_x_y(290, 299), duration=random_time_duration())
        time.sleep(2)
        #470 840 410 450
        pyautogui.click(random_x_y(470, 851), random_x_y(410, 481), duration=random_time_duration())
        time.sleep(4)
        pyautogui.moveTo(240, 180, duration=random_time_duration())
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(1.5)  # делаем паузу между действиями
        pyautogui.moveTo(615, 620, 1)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.screenshot(r'C:\Users\m.babczenko\Desktop\photo' + str(index) + '.png')
        time.sleep(2)
        print(index, group)
    #570 750 630 640
        pyautogui.moveTo(random_x_y(570, 750), random_x_y(619, 635), duration=random_time_duration())
        time.sleep(1.5)
        pyautogui.click()

    time.sleep(2)
    random_scroll()
