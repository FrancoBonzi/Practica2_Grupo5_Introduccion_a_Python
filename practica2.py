print("=== LA TRIFECTA ===")

while True:
    numero = input("\nIngrese un número entero positivo (0 para salir): ")

    
    if not numero.isdigit():
        print("Error: debe ingresar un número válido.")
        break

    numero = int(numero)

    
    if numero == 0:
        print("Programa finalizado, ingresó 0.")
        break

    
    palabra = input("Ingrese una palabra o frase: ")
    cantidadDecaracteres = len(palabra)
    print(f"La frase tiene {cantidadDecaracteres} caracteres.")

    
    factorial = 1
    contadorDeCaracteres = 1
    while contadorDeCaracteres <= cantidadDecaracteres:
        factorial = factorial * contadorDeCaracteres
        contadorDeCaracteres = contadorDeCaracteres + 1

    print(f"El factorial de {cantidadDecaracteres} es:{factorial}")

    
    if factorial % 2 == 0:
        print("El resultado es PAR.")
    else:
        print("El resultado es IMPAR.")

   
