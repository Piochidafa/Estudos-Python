import pyautogui
from PIL import Image

while True:
 aa = Image.open('lula malusco.jpg')

 bb = pyautogui.confirm(text='Lula Mosluco', title='Rei du kuduru', buttons=['Sim', 'Não']);

 if bb == "Sim":
     aa.show('lula malusco.jpg');

 elif bb == "Não":
     pyautogui.confirm(title='Vai tomar no cuuuuuu', text='Lula Malusco Supremacy');

 else:
     print("Não entendi a resposta");



