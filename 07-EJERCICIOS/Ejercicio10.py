"""
Pedir por pantalla las notas de 15 alumnos
y mostrar cuantos aprobaron y cuantos no
"""

cont = 1
contAprobados = 0
contDesaprobados = 0

cantalumnos = int(input("Ingrese la cantdad de alumnos a evaluar: "))
for cont in range(1, (cantalumnos + 1)):

    nota = int(input(f"Ingresar nota del alumno {cont}: "))
    if nota >= 6:
        contAprobados += 1
    else:
        contDesaprobados += 1

print(f"\n Los alumnos que aprobaron son: {contAprobados} \nLos alumunos que desaprobaron son : {contDesaprobados}")