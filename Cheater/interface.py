from tkinter import *
from tkinter.ttk import *
from pprint import pprint

from finder import Finder

screen = Tk()
screen.geometry("750x320")

word_length = 5
finder = Finder(word_length)

global leters_discarted
global leters_found
global leters_correct

leters_discarted = ""
leters_found = {} # {letra : [posiciones]}
leters_correct = {} # {letra : [posicion(0-4)]}

def init_widgets():
    margen_int_x = 8
    margen_int_y = 4

    first_leter.grid(column=0, row=0, padx=margen_int_x, pady=margen_int_y)
    second_leter.grid(column=1, row=0, padx=margen_int_x, pady=margen_int_y)
    third_leter.grid(column=2, row=0, padx=margen_int_x, pady=margen_int_y)
    fourth_leter.grid(column=3, row=0, padx=margen_int_x, pady=margen_int_y)
    fifth_leter.grid(column=4, row=0, padx=margen_int_x, pady=margen_int_y)

    first_discarted.grid(column=0, row=1, padx=margen_int_x, pady=margen_int_y)
    first_found.grid(column=0, row=2, padx=margen_int_x, pady=margen_int_y)
    first_correct.grid(column=0, row=3, padx=margen_int_x, pady=margen_int_y)

    second_discarted.grid(column=1, row=1, padx=margen_int_x, pady=margen_int_y)
    second_found.grid(column=1, row=2, padx=margen_int_x, pady=margen_int_y)
    second_correct.grid(column=1, row=3, padx=margen_int_x, pady=margen_int_y)

    third_discarted.grid(column=2, row=1, padx=margen_int_x, pady=margen_int_y)
    third_found.grid(column=2, row=2, padx=margen_int_x, pady=margen_int_y)
    third_correct.grid(column=2, row=3, padx=margen_int_x, pady=margen_int_y)

    fourth_discarted.grid(column=3, row=1, padx=margen_int_x, pady=margen_int_y)
    fourth_found.grid(column=3, row=2, padx=margen_int_x, pady=margen_int_y)
    fourth_correct.grid(column=3, row=3, padx=margen_int_x, pady=margen_int_y)

    fifth_discarted.grid(column=4, row=1, padx=margen_int_x, pady=margen_int_y)
    fifth_found.grid(column=4, row=2, padx=margen_int_x, pady=margen_int_y)
    fifth_correct.grid(column=4, row=3, padx=margen_int_x, pady=margen_int_y)

    okButton.grid(column=5, row=2, padx=margen_int_x, pady=margen_int_y)

    posible_words.grid(column=5, row=3, padx=margen_int_x, pady=margen_int_y)

    word_list.grid(column=5, row=4, padx=margen_int_x, pady=margen_int_y)
    scroll_lista.grid(column=6, row=4, ipady=6, sticky='ns')
    word_count.grid(column=5, row=5, ipady=6, sticky='ns')

def found_leter(leter_entry, position):
    leter = leter_entry.get()[0]
    leter_entry.delete(0, END)
    if not leter:
        return
    leter = leter.lower()

    try:
        leters_found[leter].append(position)
    except:
        leters_found[leter] = [position]
    
    # DEV
    print(f"Found: {leters_found}")

def discarted_leter(leter_entry):
    global leters_discarted
    leter = leter_entry.get()
    leter_entry.delete(0, END)
    if not leter:
        return
        
    leter = leter[0].lower()

    leters_discarted += leter
    
    # DEV
    print(f"Discarted: '{leters_discarted}'")

def positioned_leter(leter_entry, position):
    leter = leter_entry.get()[0]
    leter_entry.delete(0, END)
    if not leter:
        return
    leter = leter.lower()

    try:
        leters_correct[leter].append(position)
    except:
        leters_correct[leter] = [position]
    
    # DEV
    print(f"Positioned: {leters_correct}")

def asign_leters(finder: Finder, leters_found={}, leters_correct={}, leters_discarted=""):
    for leter in leters_found:
        for position in leters_found[leter]:
            finder.found_leter(leter, position)

    for leter in leters_correct:
        for position in leters_correct[leter]:
            finder.positioned_leter(leter, position)

    for leter in leters_discarted:
        finder.discarted_leter(leter)

def find_posibles(finder: Finder):
    words = finder.find_posibles()
    word_count.config(text = f"Palabras: {len(words)}")
    #pprint(words)
    word_list.delete(*word_list.get_children())
    i = 0
    for word in words:
        word_list.insert(parent='', index=i, iid=i, text='', values=(str(i + 1), word))
        i += 1

def first_leter_tab(P):
    if len(P) == 1:
        second_leter.focus_set()
    return True
    
def second_leter_tab(P):
    if len(P) == 1:
        third_leter.focus_set()
    return True
    
def third_leter_tab(P):
    if len(P) == 1:
        fourth_leter.focus_set()
    return True
    
def fourth_leter_tab(P):
    if len(P) == 1:
        fifth_leter.focus_set()
    return True
    
def fifth_leter_tab(P):
    if len(P) > 1:
        fifth_leter.delete(0, END)
        fifth_leter.insert(0, P[0])
    return True

word_count = Label(screen)

first_leter = Entry(screen, width=3, validate="key")
first_leter['validatecommand'] = (first_leter.register(first_leter_tab), '%P')

second_leter = Entry(screen, width=3, validate="key")
second_leter['validatecommand'] = (second_leter.register(second_leter_tab), '%P')

third_leter = Entry(screen, width=3, validate="key")
third_leter['validatecommand'] = (third_leter.register(third_leter_tab), '%P')

fourth_leter = Entry(screen, width=3, validate="key")
fourth_leter['validatecommand'] = (fourth_leter.register(fourth_leter_tab), '%P')

fifth_leter = Entry(screen, width=3, validate="key")
fifth_leter['validatecommand'] = (fifth_leter.register(fifth_leter_tab), '%P')

first_discarted = Button(screen, text = "Contiene", command = lambda: found_leter(first_leter, 0))
first_found = Button(screen, text = "Descartar", command = lambda: discarted_leter(first_leter))
first_correct = Button(screen, text = "Correcta", command = lambda: positioned_leter(first_leter, 0))

second_discarted = Button(screen, text = "Contiene", command = lambda: found_leter(second_leter, 1))
second_found = Button(screen, text = "Descartar", command = lambda: discarted_leter(second_leter))
second_correct = Button(screen, text = "Correcta", command = lambda: positioned_leter(second_leter, 1))

third_discarted = Button(screen, text = "Contiene", command = lambda: found_leter(third_leter, 2))
third_found = Button(screen, text = "Descartar", command = lambda: discarted_leter(third_leter))
third_correct = Button(screen, text = "Correcta", command = lambda: positioned_leter(third_leter, 2))

fourth_discarted = Button(screen, text = "Contiene", command = lambda: found_leter(fourth_leter, 3))
fourth_found = Button(screen, text = "Descartar", command = lambda: discarted_leter(fourth_leter))
fourth_correct = Button(screen, text = "Correcta", command = lambda: positioned_leter(fourth_leter, 3))

fifth_discarted = Button(screen, text = "Contiene", command = lambda: found_leter(fifth_leter, 4))
fifth_found = Button(screen, text = "Descartar", command = lambda: discarted_leter(fifth_leter))
fifth_correct = Button(screen, text = "Correcta", command = lambda: positioned_leter(fifth_leter, 4))

okButton = Button(screen, text = "OK", command = lambda: asign_leters(finder, leters_found, leters_correct, leters_discarted))

posible_words = Button(screen, text = "Posibles Palabras", command = lambda: find_posibles(finder))

word_list = Treeview(screen, height = 6, selectmode='browse')
word_list['columns']=('Position', 'Palabras')
word_list.column('#0', width=0, stretch=NO)
word_list.column('Position', minwidth=0, width=40, anchor=CENTER)
word_list.column('Palabras', minwidth=0, width=200, anchor=CENTER)
word_list.heading('#0', text='', anchor=CENTER)
word_list.heading('Position', text='', anchor=CENTER)
word_list.heading('Palabras', text='Palabras', anchor=CENTER)

scroll_lista = Scrollbar(screen, orient="vertical", command=word_list.yview)

screen.title("Buscar Palabras (ES)")
print("OK!")
init_widgets()
word_count.config(text = "Palabras: 0")
screen.mainloop()