def count_valleys():
    while True:
        height = 0
        valleys = 0
        path = input("Ingresa el recorrido (debe consistir únicamente de 'U' y 'D') ó 'X' para salir\n")
        path = path.lower()
        for step in path:
            match step:
                case "u":
                    height += 1
                    if height == 0:
                        valleys += 1
                case "d":
                    height -= 1
                case "x":
                    return None
                case _:
                    print("Solo debes ingresar 'U' ó 'D'")
        print(f"El número de valles es {valleys}")


def bst():
    root = None

    # Definimos la clase nodo para los árboles

    class Nodo:
        def __init__(self, val, padre=None, izq=None, der=None):
            self.val = val
            self.padre = padre
            self.izq = izq
            self.der = der

        def insertar_nodo(self, toInsert):
            if self.val > toInsert.val:
                if self.izq is None:
                    self.izq = toInsert
                else:
                    self.izq.insertar_nodo(toInsert)
            else:
                if self.der is None:
                    self.der = toInsert
                else:
                    self.der.insertar_nodo(toInsert)

        def preorden(self, path=[]):
            path.append(self.val)
            if self.izq is not None:
                self.izq.preorden(path)
            if self.der is not None:
                self.der.preorden(path)
            return path

        def inorden(self, path=[]):
            if self.izq is not None:
                self.izq.inorden(path)
            path.append(self.val)
            if self.der is not None:
                self.der.inorden(path)
            return path

        def postorden(self, path=[]):
            if self.izq is not None:
                self.izq.postorden()
            if self.der is not None:
                self.der.postorden()
            path.append(self.val)
            return path

    while True:
        opcion = input("1. Agregar al árbol\n2. Leer árbol\n3. Salir\n")
        match opcion:
            case "1":
                value = input("Ingresa el valor a agregar al árbol:\n")
                if root is None:
                    root = Nodo(value)
                else:
                    root.insertar_nodo(Nodo(value))
            case "2":
                order = input("1. Preorden\n2. Inorden\n3. Postorden\n")
                match order:
                    case "1":
                        if root is not None:
                            print(root.preorden())
                        else:
                            print("Primero debes crear un árbol")
                    case "2":
                        if root is not None:
                            print(root.inorden())
                        else:
                            print("Primero debes crear un árbol")
                    case "3":
                        if root is not None:
                            print(root.postorden())
                        else:
                            print("Primero debes crear un árbol")
                    case "_":
                        print("Este orden no existe")
            case "3":
                return None
            case _:
                print("Caso no reconocido")


if __name__ == '__main__':
    funcion = input('1. Contar valles\n2. Árbol binario\n')
    match funcion:
        case "1":
            count_valleys()
        case "2":
            bst()
        case _:
            print("Opción inválida")
