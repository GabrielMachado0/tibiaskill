import pyautogui, time

pyautogui.hotkey('alt', 'tab')
time.sleep(3)

while True:

    pyautogui.hotkey('ctrl', 'down')
    time.sleep(3)
    pyautogui.hotkey('F4')
    time.sleep(3)
    pyautogui.hotkey('F6')
    time.sleep(500)
    pyautogui.hotkey('ctrl', 'up')
    time.sleep(500)
    pyautogui.hotkey('ctrl', 'left')
    time.sleep(500)
    pyautogui.hotkey('ctrl', 'right')
    time.sleep(500)
