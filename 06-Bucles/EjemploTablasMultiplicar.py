#######      Ejemplo tablas de multiplicar

print("\n ############ Ejemplo ##############")


numeroUsuario = input("\nIngresar el número sobre el cual quieres saber la tabla de multiplicar: ")

numeroUsuario = int(numeroUsuario)

if numeroUsuario < 1:
    numeroUsuario = 1


print(f"\n\n######## Tabla de Multiplicar del {numeroUsuario} ##############")

cont = 0
for cont in range(0, 11):
    print(f"{cont} x {numeroUsuario} = {cont*numeroUsuario}")

print("\n\t A estudiar!")