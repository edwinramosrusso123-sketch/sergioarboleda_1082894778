# Programa para registrar estudiantes y encontrar calificaciones extremas

estudiantes = []

for i in range(5):
    print(f"\nEstudiante {i+1}:")
    
    nombre = input("Ingrese nombre del estudiante: ")
    
    # Validar edad
    while True:
        try:
            edad = int(input("Ingrese edad (5-100): "))
            if 5 <= edad <= 100:
                break
            else:
                print("La edad debe estar entre 5 y 100 años.")
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
    
    # Validar calificación
    while True:
        try:
            calificacion = float(input("Ingrese calificación (0-5): "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("La calificación debe estar entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un número válido para la calificación.")
    
    # Agregar estudiante a la lista
    estudiantes.append({
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion
    })

# Encontrar estudiante con calificación más alta
max_est = max(estudiantes, key=lambda x: x['calificacion'])

# Encontrar estudiante con calificación más baja
min_est = min(estudiantes, key=lambda x: x['calificacion'])

# Calcular calificación promedio
promedio = sum(est['calificacion'] for est in estudiantes) / len(estudiantes)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Estudiante con la calificación más alta: {max_est['nombre']} con {max_est['calificacion']}")
print(f"Estudiante con la calificación más baja: {min_est['nombre']} con {min_est['calificacion']}")
print(f"Calificación promedio: {promedio:.2f}")
