def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10

def validar_email(email):
    return "@" in email and "." in email

def validar_calificaciones(calificaciones):
    return all(0 <= c <= 5 for c in calificaciones)

def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)

def clasificar_desempeño(promedio):
    if promedio >= 4.5: return "Excelente"
    elif promedio >= 4.0: return "Muy bueno"
    elif promedio >= 3.5: return "Bueno"
    elif promedio >= 3.0: return "Satisfactorio"
    else: return "Necesita mejorar"

def main():
    estudiantes = []

    while True:
        print("\n1. Agregar estudiante\n2. Ver estudiantes\n3. Buscar por cédula\n4. Salir")
        op = input("Opción: ")

        if op == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            notas = [float(n) for n in input("Notas: ").split(",")]
            if validar_cedula(cedula) and validar_email(email) and validar_calificaciones(notas):
                promedio = calcular_promedio(notas)
                estudiantes.append({"cedula": cedula, "nombre": nombre, "promedio": promedio})
                print(f"Promedio: {promedio} | {clasificar_desempeño(promedio)}")
            else:
                print("Datos inválidos")

        elif op == "2":
            for e in estudiantes:
                print(e["cedula"], "|", e["nombre"], "|", e["promedio"], "|", clasificar_desempeño(e["promedio"]))

        elif op == "3":
            c = input("Cédula: ")
            for e in estudiantes:
                if e["cedula"] == c:
                    print(e["nombre"], "|", e["promedio"], "|", clasificar_desempeño(e["promedio"]))

        elif op == "4":
            break

main()