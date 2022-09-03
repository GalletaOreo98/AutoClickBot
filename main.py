import pyautogui
import time
import json
from pynput import keyboard as kb

isOn = True

# Carga de parametros
file = open('parametros.json')
parametros = json.load(file)
file.close()

# Funciones keyListener
def suelta(tecla):
    print('Se ha soltado la tecla ' + str(tecla))
    if tecla == kb.KeyCode.from_char('q'):
        global isOn
        isOn = False
        return False


# Cuadro de dialogo (Alert)
pyautogui.alert(text='### Estas a punto de iniciar el bot ### \n\nTu configuracion es:\n'
                     + json.dumps(parametros) + '\n\nPresiona q cuando quieras detener el bot.', title='Bot',
                button='OK')

# Crea hilo para escuchar tecla stop bot
escuchador = kb.Listener(on_release=suelta)
escuchador.start()

# Funcion principal
while isOn:
    time.sleep(parametros['timeSleep1'])
    posiciones = pyautogui.locateCenterOnScreen(
        'img.png',
        confidence=parametros['tolerancia'],
        grayscale=parametros['grayscale']
    )
    if posiciones is not None:
        moveToY = posiciones.y
        moveToX = posiciones.x
        print(moveToX, moveToY)
        pyautogui.click(x=moveToX, y=moveToY)
    time.sleep(parametros['timeSleep2'])
    pyautogui.scroll(parametros['scroll'])
