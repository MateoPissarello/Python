
class FiguraGeometrica:
    def __init__(self,ancho,alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho= 0
            print(f"Valor erroneo ancho: {ancho}")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo alto: {alto}")

    @property
    def get_ancho(self):
        return self._ancho
    @get_ancho.setter
    def set_ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho: {ancho}")

    @property
    def get_alto(self):
        return self._alto
    @get_alto.setter
    def set_alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo ancho: {alto}")

    def __str__(self):
        return f"Ancho: {self._alto}, Alto: {self._ancho}"
    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False
    