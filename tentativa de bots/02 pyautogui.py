import pyautogui
import time

'''a = input("Operação\na - Bloco de notas\nb - Navegador\nc - Desligar computador\n: ")

if a == "a":
   pyautogui.press("win")
   time.sleep(0)
   pyautogui.write("bloco de notas")
   time.sleep(1)
   pyautogui.press("enter")
   time.sleep(1)

elif a == "b":
    pyautogui.press("win")
    time.sleep(0)
    pyautogui.write("opera")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

elif a == "c":
    pyautogui.press("win")
    time.sleep(0)
    pyautogui.write("cmd")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write("shutdown -s -t 0")
    pyautogui.press("enter")


else:
    print("seleção invalida!!")'''

'''pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")'''

'''pyautogui.hotkey("ctrl", "shift", "esc")'''

'''pyautogui.alert(text='Peporipo', title='Alerta?', button='OK')'''

#pyautogui.prompt(text='', title='' , default='')

pyautogui.password(text='Adrielflix', title='Senha', default='', mask='*')

