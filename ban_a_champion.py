import pyautogui
from pynput import keyboard
import time


def click_search_field_type_name():
    try:
        x, y = pyautogui.locateCenterOnScreen('images/Search_field.png')
        #Point(x=1559, y=38) test pos
        pyautogui.click(x, y)
        pyautogui.typewrite('brand', interval=0.1)
    except TypeError as identifier:
        print('COULDNT FIND FIELD')
        print(identifier)

def click_brand_icon():
    try:
        x, y = pyautogui.locateCenterOnScreen('images/Brand_icon.png')
        pyautogui.click(x, y)
    except TypeError as identifier:
        print('COULDNT FIND BRAND ICON')
        print(identifier)

def click_ban_icon():
    try:
        x, y = pyautogui.locateCenterOnScreen('images/Ban_button.png')
        pyautogui.click(x, y)
    except TypeError as identifier:
        print('COULDNT FIND BAN BUTTON')
        print(identifier)

########################################
# The key combination to check
WAS_EXECUTED = False
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

# The currently active modifiers
current = set()
def execute():
    WAS_EXECUTED == True
    click_search_field_type_name()
    click_brand_icon()
    click_ban_icon()

    return WAS_EXECUTED

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            WAS_EXECUTED = execute()


while WAS_EXECUTED == False:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        break