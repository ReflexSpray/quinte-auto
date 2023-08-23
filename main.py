import pyautogui
import keyboard
import threading

# Define de automatisering functie
def automation(number):
    pyautogui.press('f2')
    pyautogui.write(str(number))
    pyautogui.press('space', presses=6)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab', presses=3)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 's')
    print("Automatisering klaar")

# Flag om te kijken of de automatisering al bezig is
is_automation_running = False

def start_automation(e):
    global is_automation_running
    if not is_automation_running:
        is_automation_running = True
        print("F11 gedrukt - Automatisering start...")
        with open("number.txt", "r") as number_file:
            number = int(number_file.read().strip())
            automation_thread = threading.Thread(target=automation, args=(number,))
            automation_thread.start()
            is_automation_running = False  #! Zet de flag terug naar False
            with open("number.txt", "w") as number_file:
                number_file.write(str(number + 1))  # Increment het nummer met 1

keyboard.on_press_key("F11", start_automation)

# Reset nummer naar 1 bij F12
def reset_number(e):
    with open("number.txt", "w") as number_file:
        number_file.write("1")
    print("Nummer gereset naar 1.")

keyboard.on_press_key("F12", reset_number)

print("Druk F11 om de automatisering te starten. - Druk F12 om het nummer te resetten naar 1.")

# Houd de main thread levend
keyboard.wait("esc")  # Wacht op de "esc" key press om het programma te stoppen