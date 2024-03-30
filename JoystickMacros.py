import vgamepad as vg
import time
import random

strategy = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
aim = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
open_map = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
left = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
up = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
down = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
right = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
weapon = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
use = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
reload = vg.XUSB_BUTTON.XUSB_GAMEPAD_X


gamepad = vg.VX360Gamepad()

mapping = {
    "left": left,
    "right": right,
    "up": up,
    "down": down,
    "влево": left,
    "вправо": right,
    "вверх": up,
    "вниз": down,
    "grenade": right,
    "граната": right,
    "хил": up,
    "heal": up,
    "вызов": strategy,
    "страта": strategy,
    "открыть": strategy,
    "open": strategy,
    "strat": strategy,
    "оружие": weapon,
    "weapon": weapon,
    "gun": weapon,
    "use": use,
    "использовать": use,
    "юзать": use,
    "тык": use,
    "reload": reload,
    "перезарядка": reload,
    "map": open_map,
    "карта": open_map,
    "aim": aim,
    "прицел": aim,
    "пуль": aim,
    "back": None,
    "назад": None,
}

toggle = {strategy, aim, None}


def press(key: str):
    key = key.lower()
    if key not in mapping:
        return
    print(key + " pressed")

    keycode = mapping[key]

    if keycode in toggle:
        time.sleep(random.random() * 0.1 + 0.1)
        for t in toggle:
            if t is not None:
                gamepad.release_button(t)
        gamepad.update()
        time.sleep(random.random() * 0.1 + 0.1)
        if keycode is not None:
            gamepad.press_button(keycode)
        gamepad.update()
        return

    time.sleep(random.random() * 0.1 + 0.1)
    gamepad.press_button(keycode)
    gamepad.update()
    time.sleep(random.random() * 0.1 + 0.1)
    gamepad.release_button(keycode)
    gamepad.update()