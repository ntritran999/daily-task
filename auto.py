import pyautogui, time, os

# OPEN GAME
pyautogui.click(712, 876)
def click(pos):
    time.sleep(10)
    pyautogui.click(pos)

# OPEN YOUTUBE
def open_browser():
    os.system('start firefox')
    time.sleep(1)
    pyautogui.click(324, 65)
    pyautogui.typewrite('youtube')
    pyautogui.typewrite(['enter'])

def main():
    positions = [(924, 575), (1027, 299), (694, 755)]
    for pos in positions:
        click(pos)

    open_browser()

if __name__ == "__main__":
    main()
