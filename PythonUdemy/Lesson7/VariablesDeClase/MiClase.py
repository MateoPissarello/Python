class MiClase:
    variable_clase = "Valor variable clase" #Son variables que comparten todos los objetos creados a partir de una clase, estas variables van a tener el mismo valor para todos los objetos instanciados
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia
    #metodos estáticos
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
    @classmethod #metodo de clase
    def metodo_clase(cls):
        pass 
        #TODO terminar de ver el video

print(MiClase.variable_clase)

miClase = MiClase("Valor variable instancia")
print(miClase.variable_instancia)
print(miClase.variable_clase)
MiClase.variable_clase2 = "Valor variable clase 2" #Añadir variables al vuelo (En el mismo instante)
miClase2 = MiClase("Otro valor de variable instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(miClase.variable_clase2)
print(miClase2.variable_clase2)
MiClase.metodo_estatico()