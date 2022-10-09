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
    def metodo_instancua(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_clase()
miObjeto1 = MiClase("variable_instancia")
miObjeto1.metodo_clase()
miObjeto1.metodo_instancua()
