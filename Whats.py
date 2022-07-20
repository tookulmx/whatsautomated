import pywhatkit
import time
import pyautogui
import keyboard as k

i=99

# Introduce number
pywhatkit.sendwhatmsg_instantly("introduce_number", str(i))

for i in range (98,3,-1):
        try:
            Numbers = str(i)
            largo = len(Numbers)

            if largo == 2:
                num1, num2 = [int(i) for i in str(Numbers)][0], [int(i) for i in str(Numbers)][1]
                print(i)
                pyautogui.click(759,984)

                if i>=10:
                    k.press_and_release(str(num1))
                    k.press_and_release(str(num2))
                    time.sleep(.5)
                    k.press_and_release("enter")
                    print("Mensaje enviado")

            if largo == 1: 

                num1 = [int(i) for i in str(Numbers)][0]
                print(i)
                pyautogui.click(759,984)

                if i<10:
                    k.press_and_release(str(num1))
                    time.sleep(.5)
                    k.press_and_release("enter")
                    print("Mensaje enviado")
       
        except:
            print("Sorry, revisa qué sucede")