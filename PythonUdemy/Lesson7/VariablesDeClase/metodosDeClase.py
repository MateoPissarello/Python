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
        print(cls.variable_clase)


MiClase.metodo_clase()