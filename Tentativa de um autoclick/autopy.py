import pyautogui
import sqlite3
import time

# pyautogui.alert("Pão")

b = "OK"

me = ""

print("|---------------------------|")
print("| (1) - Tabela idiota       |")
me = input("|---------------------------|\n:")


if me == "1":

    while True:

        a = pyautogui.confirm(text='Robson ele é gay, o Robson é:', title='Ronaldo fenomeno', buttons=['  Gay  ', 'Homossexual', 'sapatão'])

        if a == "Homossexual":
         b =  pyautogui.alert("EAE GAY TA TÃO SERIO POR QUE ?? HAHAHAHAHA")

        elif a == "Gay":
         b = pyautogui.alert("Sabonete niveamen")

