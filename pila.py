class Pila:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad
        self.tope = 0

    def esta_vacia(self):
        return self.tope == 0

    def esta_llena(self):
        return self.tope == self.capacidad

    def insertar(self, elemento):
        if not self.esta_llena():
            self.items.append(elemento)
            self.tope += 1
            print(f"Insertar {elemento} - Pila: {self.items} - Tope: {self.tope}")
        else:
            print("La pila está llena, no se puede insertar.")

    def eliminar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            self.tope -= 1
            print(f"Eliminar {elemento} - Pila: {self.items} - Tope: {self.tope}")
        else:
            print("La pila está vacía, no se puede eliminar.")


pila = Pila(8)

pila.insertar('X')
pila.insertar('Y')
pila.eliminar()
pila.eliminar()
pila.eliminar()
pila.insertar('V')
pila.insertar('W')
pila.eliminar()
pila.insertar('R')
