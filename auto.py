from pyautogui import click, typewrite
from time import sleep
import os

# OPEN YOUTUBE
def open_browser():
    os.system('start firefox')
    sleep(3)
    click(324, 65)
    sleep(1)
    typewrite('youtube')
    typewrite(['enter'])

def main():
    # OPEN GAME
    click(712, 876) # Choose garena
    positions = [(924, 575), (1027, 299), (694, 755)]
    for pos in positions:
        sleep(10)
        click(pos)

    open_browser()

    click(712, 876) 
    sleep(2)
    click(1213, 97) # Exit garena
    sleep(2)
    click(609, 878) # Choose vscode
    sleep(1)
    click(1424, 6) # Exit vscode

if __name__ == "__main__":
    main()
