import time
from pynput.keyboard import Key, Controller

def diccionario():
    keyboard = Controller()
    f = open("listado-general.txt", "r", encoding="utf-8")
    content = f.read()
    palabra = ""
    palabras = []
    for char in content:
        if char != "\n":
            palabra += char
        else:
            palabras.append(palabra)
            keyboard.type(palabra)
            palabra = ""
    pocas = []
    tres = []
    cuatro = []
    cinco = []
    seis = []
    siete = []
    ocho = []
    nueve = []
    diez = []
    once = []
    doce = []
    trece = []
    catorce = []
    quince = []
    dieciseis = []
    muchas = []
    for word in palabras:
        if len(word) < 3:
            pocas.append(word)
        elif len(word) == 3:
            tres.append(word)
        elif len(word) == 4:
            cuatro.append(word)
        elif len(word) == 5:
            cinco.append(word)
        elif len(word) == 6:
            seis.append(word)
        elif len(word) == 7:
            siete.append(word)
        elif len(word) == 8:
            ocho.append(word)
        elif len(word) == 9:
            nueve.append(word)
        elif len(word) == 10:
            diez.append(word)
        elif len(word) == 11:
            once.append(word)
        elif len(word) == 12:
            doce.append(word)
        elif len(word) == 13:
            trece.append(word)
        elif len(word) == 14:
            catorce.append(word)
        elif len(word) == 15:
            quince.append(word)
        elif len(word) == 16:
            dieciseis.append(word)
        elif len(word) > 16:
            muchas.append(word)
    '''
    print("Pocas: " + str(len(pocas)))
    print("Tres: " + str(len(tres)))
    print("Cuatro: " + str(len(cuatro)))
    print("Cinco: " + str(len(cinco)))
    print("Seis: " + str(len(seis)))
    print("Siete: " + str(len(siete)))
    print("Ocho: " + str(len(ocho)))
    print("Nueve: " + str(len(nueve)))
    print("Diez: " + str(len(diez)))
    print("Once: " + str(len(once)))
    print("Doce: " + str(len(doce)))
    print("Trece: " + str(len(trece)))
    print("Catorce: " + str(len(catorce)))
    print("Quince: " + str(len(quince)))
    print("Dieciseis: " + str(len(dieciseis)))
    print("Muchas: " + str(len(muchas)))
    print("Comprobación:  " + str(len(palabras)) + " = " + str(len(pocas) + len(tres) + len(cuatro) + len(cinco) + len(seis) + len(siete) + len(ocho) + len(nueve) + len(diez) + len(once) + len(doce) + len(trece) + len(catorce) + len(quince) + len(dieciseis) + len(muchas)))
    '''
    diccionario = {
        "pocas" : pocas,
        "tres" : tres,
        "cuatro" : cuatro,
        "cinco" : cinco,
        "seis" : seis,
        "siete" : siete,
        "ocho" : ocho,
        "nueve" : nueve,
        "diez" : diez,
        "once" : once,
        "doce" : doce,
        "trece" : trece,
        "catorce" : catorce,
        "quince" : quince,
        "dieciseis" : dieciseis,
        "muchas" : muchas,
    }
    f.close()
    return diccionario

def typer(longPalabra, diccionario):
    keyboard = Controller()
    time.sleep(4)
    if longPalabra == "pocas":
        for i in range(len(diccionario["pocas"])):
            keyboard.type(diccionario["pocas"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 3:
        for i in range(len(diccionario["tres"])):
            keyboard.type(diccionario["tres"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 4:
        for i in range(len(diccionario["cuatro"])):
            keyboard.type(diccionario["cuatro"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 5:
        for i in range(len(diccionario["cinco"])):
            keyboard.type(diccionario["cinco"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 6:
        for i in range(len(diccionario["seis"])):
            keyboard.type(diccionario["seis"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 7:
        for i in range(len(diccionario["siete"])):
            keyboard.type(diccionario["siete"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 8:
        for i in range(len(diccionario["ocho"])):
            keyboard.type(diccionario["ocho"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 9:
        for i in range(len(diccionario["nueve"])):
            keyboard.type(diccionario["nueve"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 10:
        for i in range(len(diccionario["diez"])):
            keyboard.type(diccionario["diez"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 11:
        for i in range(len(diccionario["once"])):
            keyboard.type(diccionario["once"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 12:
        for i in range(len(diccionario["doce"])):
            keyboard.type(diccionario["doce"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 13:
        for i in range(len(diccionario["trece"])):
            keyboard.type(diccionario["trece"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 14:
        for i in range(len(diccionario["catorce"])):
            keyboard.type(diccionario["catorce"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 15:
        for i in range(len(diccionario["quince"])):
            keyboard.type(diccionario["quince"][i])
            keyboard.press(Key.enter)
    elif longPalabra == 16:
        for i in range(len(diccionario["dieciseis"])):
            keyboard.type(diccionario["dieciseis"][i])
            keyboard.press(Key.enter)
    elif longPalabra == "muchas":
        for i in range(len(diccionario["muchas"])):
            keyboard.type(diccionario["muchas"][i])
            keyboard.press(Key.enter)
            
l = input("numero de letras   ")
typer(l, diccionario())