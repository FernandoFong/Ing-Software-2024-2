#Tenemos la solución del problema de los Valles.

def num_de_valles(recorridos):
    vallesRecorridos = 0
    enValle = False
    nivelDelMar = 0

    for paso in recorridos:
        if paso == 'U':
            nivelDelMar += 1
        elif paso == 'D':
            nivelDelMar -= 1

        if paso == 'D' and nivelDelMar == 0:
            enValle = True
        elif paso == 'U' and nivelDelMar == 0 and enValle:
            vallesRecorridos += 1
            enValle = False

    return vallesRecorridos

#Tenemos la solución para el árbol binario solicitado.

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.nodo_izquierdo = None
        self.nodo_derecho = None
        self.nodo_padre = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar_elemento(self, elemento):
        if self.raiz is None:
            self.raiz = Nodo(elemento)
        else:
            self.agregar(elemento, self.raiz)

    def agregar(self, elemento, nodo_actual):
        if elemento <= nodo_actual.elemento:
            if nodo_actual.nodo_izquierdo is None:
                nodo_actual.nodo_izquierdo = Nodo(elemento)
                nodo_actual.nodo_izquierdo.nodo_padre = nodo_actual
            else:
                self.agregar(elemento, nodo_actual.nodo_izquierdo)
        else:
            if nodo_actual.nodo_derecho is None:
                nodo_actual.nodo_derecho = Nodo(elemento)
                nodo_actual.nodo_derecho.nodo_padre = nodo_actual
            else:
                self.agregar(elemento, nodo_actual.nodo_derecho)

    def recorrido_preorden(self):
        return self.preOrden(self.raiz)

    def preOrden(self, nodo):
        if nodo is None:
            return []
        resultado = [nodo.elemento]
        resultado += self.preOrden(nodo.nodo_izquierdo)
        resultado += self.preOrden(nodo.nodo_derecho)
        return resultado

    def recorrido_inorden(self):
        return self.inOrden(self.raiz)

    def inOrden(self, nodo):
        if nodo is None:
            return []
        resultado = self.inOrden(nodo.nodo_izquierdo)
        resultado.append(nodo.elemento)
        resultado += self.inOrden(nodo.nodo_derecho)
        return resultado

    def recorrido_postorden(self):
        return self.postOrden(self.raiz)

    def postOrden(self, nodo):
        if nodo is None:
            return []
        resultado = self.postOrden(nodo.nodo_izquierdo)
        resultado += self.postOrden(nodo.nodo_derecho)
        resultado.append(nodo.elemento)
        return resultado


# Ejemplo de ejercicio de solución para el programa de los valles:
recorridos = "UDDDUDUUUDDDU"
print("Número de valles recorridos:", num_de_valles(recorridos))  # Salida con el anterior ejemplo: 1
print()


# Ejemplo para el ejercicio del arbol binario:
arbol = ArbolBinarioOrdenado()
arbol.agregar_elemento(5)
arbol.agregar_elemento(3)
arbol.agregar_elemento(8)
arbol.agregar_elemento(1)
arbol.agregar_elemento(4)
arbol.agregar_elemento(7)
arbol.agregar_elemento(9)

print("Recorrido preorden:", arbol.recorrido_preorden())
print("Recorrido inorden:", arbol.recorrido_inorden())
print("Recorrido postorden:", arbol.recorrido_postorden())
