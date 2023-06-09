from pynput.keyboard import Listener, Key
import pyautogui
import pyperclip
import time
import random


with open('Diccionario.txt', encoding='utf-8') as diccionario:
    # Separar las palabras de la línea
    palabras = diccionario.read().split()

palabras_encontradas = []
silaba = ""
escritor = True

   

def on_press(tecla):

    if tecla == Key.ctrl_l:
         coordenada = pyautogui.position()
         print(coordenada.x,coordenada.y)

    if tecla == Key.alt_gr:
        # Mueve el cursor a la posición almacenada en la variable 'coordenada'
        pyautogui.moveTo(774,559) #cambiar en función de resolución
        # Hace un doble clic en la posición actual del cursor
        pyautogui.doubleClick()
        #ctrl+c
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.01)
        pyautogui.move(100,0)
        pyautogui.click()
        silaba = pyperclip.paste().lower().strip()
        print(silaba)

        palabra = ""

        # Iterar sobre cada palabra en la línea
        for palabra in palabras:
             # Verificar si la sílaba está presente en la palabra
             
             if silaba in palabra and palabra not in palabras_encontradas:

                print(palabra)

                if escritor:
                    pyautogui.write(palabra)
                    pyautogui.press('Enter')     
                else:
                     pyperclip.copy(palabra)

               
                palabras_encontradas.append(palabra) # Agregar la palabra al conjunto de palabras encontradas
                break # Detener la búsqueda después de encontrar la primera palabra
                time.sleep(0.1)

# Configuramos el listener para que detecte las teclas
with Listener(on_press=on_press) as listener:
    while True:
        pass
   
#Eduardo