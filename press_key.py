from pynput.keyboard import Key, Controller

keyboard = Controller()

def press(key: "w"):
    '''
    Stimulates a key press passed in as a param
    '''
    print(f"key pressed is: {key}")
    keyboard.press(key)
    keyboard.release(key)