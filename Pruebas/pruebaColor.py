import colorama as cl
import time
from termcolor import colored
cl.init()
#Colocar color al texto
print(colored("Hola me llamo Mateo", "magenta","on_green"))
time.sleep(1)
print(colored("Como te llamas tú?\n", "red"))
nombrePersona = input("")
texto = (f"Un gusto conocerte {nombrePersona}")
print(colored(texto, "yellow"))
time.sleep(2)
#Limpiar terminal
print(cl.ansi.clear_screen())