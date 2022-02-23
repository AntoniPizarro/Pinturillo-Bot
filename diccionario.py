from pprint import pprint

def diccionario():
    f = open("listado-general.txt", "r", encoding="utf-8")
    content = f.read()
    palabra = ""
    palabras = []
    for char in content:
        if char != "\n":
            palabra += char
        else:
            palabras.append(palabra)
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

class Buscador:

    def __init__(self, lista) -> None:
        self.lista = lista
        self.letras_encontradas = {}
        self.letras_descartadas = set()
        self.letras_posicionadas = {}
    
    def letra_encontrada(self, letra, posicion):
        try:
            self.letras_encontradas[letra].append(posicion)
        except:
            self.letras_encontradas[letra] = [posicion]
    
    def letra_descartada(self, letra):
        self.letras_descartadas.add(letra)
    
    def letra_posicionada(self, letra, posicion):
        self.letras_posicionadas[posicion] = letra
        self.letra_encontrada(letra)
    
    def segun_encontradas(self, palabra):
        for letra in palabra:
            if letra in self.letras_encontradas:
                for posicion in self.letras_encontradas[letra]:
                    if palabra[posicion] == letra:
                        return False
            
        return True
    
    def segun_descartadas(self, palabra):
        for letra in palabra:
            if letra in self.letras_descartadas:
                print(f"La palabra {palabra} no pasa el filtro segun_descartadas")
                return False
        
        return True
    
    def segun_posicionadas(self, palabra):
        for i in range(len(palabra)):
            if i in self.letras_posicionadas and palabra[i] != self.letras_posicionadas[i]:
                print(f"La palabra {palabra} no pasa el filtro segun_posicionadas")
                return False
        
        return True
    
    def buscar_posibles(self):
        res = []
        for palabra in self.lista:
            if not self.segun_descartadas(palabra):
                continue
            elif not self.segun_encontradas(palabra):
                continue
            elif not self.segun_posicionadas(palabra):
                continue

            res.append(palabra)

        return res

buscador = Buscador(diccionario()["cinco"])

encontradas = {"z":[0]}
descartadas = ""
posicionadas = {}

for letra in encontradas:
    for posicion in encontradas[letra]:
        buscador.letra_encontrada(letra, posicion)
for letra in descartadas:
    buscador.letra_descartada(letra)
for posicion in posicionadas:
    buscador.letra_posicionada(posicionadas[posicion], posicion)

res = buscador.buscar_posibles()
pprint(res)