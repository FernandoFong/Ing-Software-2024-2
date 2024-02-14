def contar_pasos_negativos(cadena):
    try:
        # Validar la entrada
        if not all(paso in ('D', 'U') for paso in cadena):
            raise ValueError("La entrada es incorrecta. Debe contener solo 'D' y 'U'.")

        contador = 0
        nivel_actual = 0

        for paso in cadena:
            if paso == 'D':
                nivel_actual -= 1
            elif paso == 'U':
                nivel_actual += 1

            if nivel_actual == 0 and paso == 'U':
                contador += 1

        return contador

    except ValueError as e:
        print(f"Error: {e}")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, valor):
        self.raiz = Nodo(valor)

    def agregar_nodo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.agregar_nodo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.agregar_nodo(nodo.derecha, valor)

    def recorrido_in_orden(self, nodo):
        if nodo is not None:
            self.recorrido_in_orden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.recorrido_in_orden(nodo.derecha)

    def recorrido_pre_orden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self.recorrido_pre_orden(nodo.izquierda)
            self.recorrido_pre_orden(nodo.derecha)

    def recorrido_post_orden(self, nodo):
        if nodo is not None:
            self.recorrido_post_orden(nodo.izquierda)
            self.recorrido_post_orden(nodo.derecha)
            print(nodo.valor, end=" ")

    # estas son las funciones que se deben llamar para agregar y obtener recorridos.

    def agregar(self, valor):
        self.agregar_nodo(self.raiz, valor)
   
    def pre_orden(self):
        self.recorrido_pre_orden(self.raiz)

    def in_orden(self):
        self.recorrido_in_orden(self.raiz)

    def post_orden(self):
        self.recorrido_post_orden(self.raiz)


