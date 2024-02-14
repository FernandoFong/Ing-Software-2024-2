def contarValles(recorrido):
    nivelActual = 0
    valles = 0

    for paso in recorrido:
        if paso == 'U':
            nivelActual += 1
        elif paso == 'D':
            nivelActual -= 1

        # Aca esta la magia padre, si regresamos al nivel de mar y estamos en U quiere decir que hay un valle
        if nivelActual == 0 and paso == 'U':
            valles += 1

    return valles


recorrido_1 = ['U', 'D', 'D', 'U', 'U', 'D', 'U', 'D']
print("Recorrido:", recorrido_1)
print("Número de valles:", contarValles(recorrido_1))

recorrido_1 = ['D', 'U', 'D', 'U', 'D', 'U', 'D', 'U']
print("Recorrido:", recorrido_1)
print("Número de valles:", contarValles(recorrido_1))


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor <= nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.derecho, valor)

    def preorden(self):
        return self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo):
        if nodo is not None:
            resultado = [nodo.valor]
            resultado.extend(self._preorden_recursivo(nodo.izquierdo))
            resultado.extend(self._preorden_recursivo(nodo.derecho))
            return resultado
        else:
            return []

    def inorden(self):
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            resultado = self._inorden_recursivo(nodo.izquierdo)
            resultado.append(nodo.valor)
            resultado.extend(self._inorden_recursivo(nodo.derecho))
            return resultado
        else:
            return []

    def postorden(self):
        return self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo):
        if nodo is not None:
            resultado = self._postorden_recursivo(nodo.izquierdo)
            resultado.extend(self._postorden_recursivo(nodo.derecho))
            resultado.append(nodo.valor)
            return resultado
        else:
            return []


# Ejemplo de uso:
arbol = ArbolBinarioOrdenado()
arbol.agregar(5)
arbol.agregar(3)
arbol.agregar(7)
arbol.agregar(2)
arbol.agregar(4)
arbol.agregar(6)
arbol.agregar(8)

print("Preorden:", arbol.preorden())
print("Inorden:", arbol.inorden())
print("Postorden:", arbol.postorden())

