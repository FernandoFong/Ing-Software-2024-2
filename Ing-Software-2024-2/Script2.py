def contar_valles(recorrido):
    nivel_del_mar = 0
    en_valle = False
    valles = 0

    for paso in recorrido:
        if paso == 'U':
            nivel_del_mar += 1
        elif paso == 'D':
            nivel_del_mar -= 1

        if nivel_del_mar < 0:
            en_valle = True
        elif nivel_del_mar == 0 and en_valle:
            valles += 1
            en_valle = False

    return valles

recorrido = input(
    "Ingrese el recorrido (utilice 'U' para paso hacia arriba y 'D' para paso hacia abajo) sin dejar espacios entre las letras: ").strip().upper()

# Verificar que el recorrido solo contenga 'U' y 'D'
if all(paso in ['U', 'D'] for paso in recorrido):
    numero_de_valles = contar_valles(recorrido)
    print("El número de valles en el recorrido es:", numero_de_valles)
else:
    print("El recorrido ingresado es inválido. Por favor, utilice solo 'U' y 'D'.")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.padre = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nuevo_nodo = Nodo(valor)
                nodo_actual.izquierdo = nuevo_nodo
                nuevo_nodo.padre = nodo_actual
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nuevo_nodo = Nodo(valor)
                nodo_actual.derecho = nuevo_nodo
                nuevo_nodo.padre = nodo_actual
            else:
                self._agregar_recursivo(valor, nodo_actual.derecho)

    def recorrido_preorden(self):
        return self._recorrido_preorden_recursivo(self.raiz)

    def _recorrido_preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self._recorrido_preorden_recursivo(nodo.izquierdo)
            self._recorrido_preorden_recursivo(nodo.derecho)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._recorrido_inorden_recursivo(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self._recorrido_inorden_recursivo(nodo.derecho)

    def recorrido_postorden(self):
        return self._recorrido_postorden_recursivo(self.raiz)

    def _recorrido_postorden_recursivo(self, nodo):
        if nodo is not None:
            self._recorrido_postorden_recursivo(nodo.izquierdo)
            self._recorrido_postorden_recursivo(nodo.derecho)
            print(nodo.valor, end=' ')

# Ejemplo de uso:
arbol = ArbolBinarioOrdenado()
valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for valor in valores:
    arbol.agregar(valor)

print("Recorrido preorden:", end=' ')
arbol.recorrido_preorden()
print("\nRecorrido inorden:", end=' ')
arbol.recorrido_inorden()
print("\nRecorrido postorden:", end=' ')
arbol.recorrido_postorden()
