import vgamepad as vg
import time

# 仮想ゲームパッドを作成
gamepad = vg.VX360Gamepad()

print("inputs will start in 10 seconds.")
time.sleep(10) #10秒待機

# 'X'ボタンを押す (ゲーム内でコントローラーを認識させるため)
gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.1)
# 'X'ボタンを離す
gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
print('A button pressed.')
time.sleep(1) #1秒待機

while True:
    # 'X'ボタンを押す
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(0.1)
    # 'X'ボタンを離す
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    print('X button pressed.')

    # 2秒待機
    time.sleep(2)

    # POV↓ボタンを押す
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
    time.sleep(0.1)
    # POV↓ボタンを離す
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    gamepad.update()
    print('POV down pressed.')
    
    # 0.5秒待機
    time.sleep(0.5)