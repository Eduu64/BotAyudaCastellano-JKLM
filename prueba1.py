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

    global coordenada_x,coordenada_y

    if tecla == Key.ctrl_l:
        coordenada_x,coordenada_y = pyautogui.position()
        #print(coordenada)
    
    if tecla == Key.alt_gr:
        # Mueve el cursor a la posición almacenada en la variable 'coordenada'
        pyautogui.moveTo(coordenada_x,coordenada_y)
        # Hace un doble clic en la posición actual del cursor
        pyautogui.doubleClick()
        #ctrl+c
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.01)
        pyautogui.moveTo(coordenada_x-100,coordenada_y)
        pyautogui.click()
        silaba = pyperclip.paste().lower().strip()
        #print(silaba)

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

# Configuramos el listener para que detecte las teclas
with Listener(on_press=on_press) as listener:
    while True:
        pass
   
#Eduardo
