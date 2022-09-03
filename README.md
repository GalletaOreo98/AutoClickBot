# AutoClickBot  

Bot tipo GUI que hace auto click a imagen similar que aparezca en pantalla mientras hace scroll.

## Parametros  

- **tolerancia:** Es el grado de similitud que aceptaras en la imagen (1%-100%). El reconocimiento de imagen es píxel a píxel.  

- **scroll:** Es la acción de desplazamiento en la pantalla (Rueda del mouse), valores negativos harán desplazamiento hacia abajo (recomendado/lo usual), valores positivos harán scroll hacia arriba. 

- **timeSleep1:** Tiempo de espera después del scroll. (Tiempo en segundos).  

- **timeSleep1:** Tiempo de espera antes del scroll. (Tiempo en segundos).  

- **grayscale:** Sirve para acelerar el proceso de reconocimiento en la pantalla, lo que hará consumir menos recursos el programa y ser más eficiente, a cambio de hacer el reconocimiento de imagen a escala de grises. Ingresar valor True para activarlo (el valor esta en False por defecto).

Por defecto:  

- **tolerancia:** 0.8
- **timeSleep1:** 1
- **timeSleep2:** 1
- **scroll:** -500
- **grayscale:** False

Puedes cambiar los parametros en el archivo *parametros.json*  

## Imagen  

Debes tomar una captura de pantalla y recortar exactamente el elemento que quieres que el bot reconozca en la pantalla (es de suma importancia ser exacto con el recorte ya que el reconocimiento es píxel a píxel).  
La imagen a usar se debe guardar con el nombre *img.png* el cual sustituirá a la imagen que viene por defecto.  

## Documentación de herramientas principales usadas  
  
  - [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
