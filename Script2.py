# Funciones relacionadas con el conteo de valles
def contar_valles(recorrido):
    nivel_actual = 0
    valles = 0
    en_valle = False

    for paso in recorrido:
        if paso == 'U':
            nivel_actual += 1
        elif paso == 'D':
            nivel_actual -= 1

        if nivel_actual < 0 and not en_valle:
            en_valle = True
            valles += 1
        if nivel_actual >= 0 and en_valle:
            en_valle = False

    return valles

# Funciones relacionadas con el árbol binario
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

    def pre_orden(self):
        return self._pre_orden_recursivo(self.raiz)

    def _pre_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        resultado = [nodo.valor]
        resultado += self._pre_orden_recursivo(nodo.izquierdo)
        resultado += self._pre_orden_recursivo(nodo.derecho)
        return resultado

    def in_orden(self):
        return self._in_orden_recursivo(self.raiz)

    def _in_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        resultado = self._in_orden_recursivo(nodo.izquierdo)
        resultado.append(nodo.valor)
        resultado += self._in_orden_recursivo(nodo.derecho)
        return resultado

    def post_orden(self):
        return self._post_orden_recursivo(self.raiz)

    def _post_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        resultado = self._post_orden_recursivo(nodo.izquierdo)
        resultado += self._post_orden_recursivo(nodo.derecho)
        resultado.append(nodo.valor)
        return resultado

# Código principal
if __name__ == "__main__":
    while True:
        try:
            # Ejercicio de Conteo de Valles
            print("------ Ejercicio de Conteo de Valles ------")
            recorrido = input("Ingrese el recorrido del caminante (solo 'U' y 'D'): ")
            # Validar que solo se ingresen 'U' y 'D'
            if not all(paso in ('U', 'D') for paso in recorrido):
                raise ValueError("El recorrido solo puede contener 'U' y 'D'.")

            print("Número de valles:", contar_valles(recorrido))
            print()

            # Ejercicio de Árbol Binario
            print("------ Ejercicio de Árbol Binario ------")
            while True:
                try:
                    num_nodos = int(input("Ingrese el número de nodos del árbol: "))
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")

            print("Ingrese los valores de los nodos separados por espacios:")
            while True:
                try:
                    valores = list(map(int, input().split()))
                    if len(valores) != num_nodos:
                        raise ValueError("La cantidad de valores ingresados no coincide con el número de nodos especificado.")
                    break
                except ValueError:
                    print("Error: Por favor, ingrese valores numéricos separados por espacios.")

            arbol = ArbolBinarioOrdenado()

            for valor in valores:
                arbol.agregar(valor)

            print("Recorrido pre-orden:", arbol.pre_orden())
            print("Recorrido in-orden:", arbol.in_orden())
            print("Recorrido post-orden:", arbol.post_orden())

            # Si todo se ejecuta correctamente, salir del bucle while
            break

        except ValueError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.\n")
