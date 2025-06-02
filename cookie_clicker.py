import pyautogui


def click_cookie():
    # Find the position of the cookie on the screen
    pyautogui.click(x=135, y=500)


def on_move(x, y):
    print(x, y)
    if x == 135 and y == 500:
        return True
    else:
        return False


if __name__ == "__main__":
    import time
    print("Starting cookie clicker...")
    running = True
    inactive = True

    if inactive:
        time.sleep(2)  # Wait for 2 seconds before starting
        while running:
            try:
                while inactive:
                    click_cookie()
                    inactive = on_move(pyautogui.position().x,
                                       pyautogui.position().y)
                while not inactive:
                    time.sleep(2)
                    click_cookie()
                    inactive = on_move(pyautogui.position().x,
                                       pyautogui.position().y)
            except KeyboardInterrupt:
                print("Exiting cookie clicker...")
                running = False
                break
