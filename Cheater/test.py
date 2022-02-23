from gettext import find
from pprint import pprint
from finder import Finder

def asign_leters(finder: Finder, leters_found={}, leters_correct={}, leters_discarted=""):
    '''
    leters_found = {letra : [posiciones]}
    leters_correct = {letra : posicion}
    leters_discarted = ""
    '''
    for leter in leters_found:
        for position in leters_found[leter]:
            finder.found_leter(leter, position)

    for leter in leters_correct:
        finder.positioned_leter(leter, leters_correct[leter])

    for leter in leters_discarted:
        finder.discarted_leter(leter)

'''
tarro *

seudo
plato
tacho
tarro
'''

finder = Finder(5)

leters_discarted = "seudplch"
leters_found = {"a" : [2], "t" : [3]} # {letra : [posiciones]}
leters_correct = {"o" : 4, "t" : 0, "a" : 1, "r" : 3} # {letra : posicion[0-4]}

asign_leters(finder, leters_found, leters_correct, leters_discarted)

res = finder.find_posibles()
pprint(res)
print(f"{len(res)} words")

print(f"\nFind: {finder.get_found_leters()}")
print(f"Positioned: {finder.get_positioned_leters()}")
print(f"Discarted: {finder.get_discarted_leters()}")