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
if __name__ == "__main__":
    # Obtén la cadena de la terminal
    cadena_pasos = input("Ingresa la cadena de pasos (por ejemplo, DUDUDUDU): ")

    # Llama a la función y muestra el resultado
    resultado = contar_pasos_negativos(cadena_pasos)
    print(f"El número de valles es: {resultado}")
