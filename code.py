# Circuit Playground Capacitive Touch

import time
import board
import touchio

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

while True:
    if touch_A1.value:
        lista_saludo=['Hola.Como estas?']
        print(lista_saludo)
    if touch_A2.value:
        lista_numeros_nac=[16,12,1994]
        print(lista_numeros_nac)
    if touch_A3.value:
        lista_reversed=reversed("ciao")
        print(list(lista_reversed))
    if touch_A4.value:
        lista_mixta=['gatos',8]
        print(lista_mixta)
    if touch_A5.value:
        lista_numeros=(1,2,3,4,5)
        print(lista_numeros)
    if touch_A6.value:
        print(lista_numeros[2])
    if touch_TX.value:
        lista_despedida=['Bye']
        print(lista_despedida)

    time.sleep(0.01)