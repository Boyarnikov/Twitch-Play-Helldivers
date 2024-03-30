import vgamepad as vg
import time
import random

strategy = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
aim = "left_trigger"
open_map = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
left = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
up = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
down = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
right = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
weapon = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
use = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
reload = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
duck = vg.XUSB_BUTTON.XUSB_GAMEPAD_B


gamepad = vg.VX360Gamepad()


key_mapping = {
    left: ["left", "влево", 'a', 'ф'],
    right: ["right", "вправо", "grenade", "граната", 'd', 'в'],
    up: ["up", "вверх", "heal", "хил", 'w', 'ц'],
    down: ["down", "вниз", 'd', 'ы'],
    strategy: ["strat", "stratagem", "вызов", "страта", "открыть", "lb"],
    weapon: ["weapon", "оружие", "gun", "y"],
    use: ["use", "использовать", "юзать", "тык", "a"],
    reload: ["reload", "перезарядка", "x"],
    open_map: ["map", "карта"],
    aim: ["aim", "прицел", "пуль", "lt"],
    duck: ["duck", "присесть", "b"],
    None: ["back", "назад"]
}

mapping = dict()
for key in key_mapping:
    for st in key_mapping[key]:
        mapping[st] = key

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
                if type(t) is str:
                    gamepad.left_trigger(0)
                else:
                    gamepad.release_button(t)

        gamepad.update()
        time.sleep(random.random() * 0.1 + 0.1)
        if keycode is not None:
            if type(keycode) is str:
                gamepad.left_trigger(1)
            else:
                gamepad.press_button(keycode)

        gamepad.update()
        return

    time.sleep(random.random() * 0.1 + 0.1)
    gamepad.press_button(keycode)
    gamepad.update()
    time.sleep(random.random() * 0.1 + 0.1)
    gamepad.release_button(keycode)
    gamepad.update()


if __name__ == "__main__":
    while True:
        time.sleep(random.random() * 0.1 + 0.1)
        gamepad.left_trigger(1)
        gamepad.update()
        time.sleep(random.random() * 0.1 + 1)
        gamepad.left_trigger(0)
        gamepad.update()
        time.sleep(random.random() * 0.1 + 1)