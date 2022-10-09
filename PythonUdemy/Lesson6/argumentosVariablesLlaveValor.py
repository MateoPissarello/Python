 #con dos asteriscos se reciben diccionarios en forma de argumentos
def listar_terminos(**kwargs): #kwarfs es "Keyword arguments" pero se puede reemplazar por cualquier palabra
    for llave,valor in kwargs.items():
        print(f"{llave}:{valor}")

listar_terminos(IDE = "Integrated development Environment", PK = "Primary Key")
listar_terminos(DBMS = "Database Management System")
