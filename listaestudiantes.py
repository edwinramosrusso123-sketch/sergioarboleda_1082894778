estudiantes = ["Juan", "Maria", "Pedro" , "Luisa" , "Carlos" , "Sofia", "Diego", "Valentina", "Andres", "Camila"]

# Agregar un nuevo estudiante al final
estudiantes.append("Ana")
print(estudiantes)  # ['Juan', 'Maria', 'Pedro', 'Ana' , 'Luisa', 'Carlos', 'Sofia', 'Diego', 'Valentina', 'Andres', 'Camila']

# Obtener la cantidad de estudiantes
print(len(estudiantes))  # 11

# Buscar si un estudiante está en la lista
if "Maria" in estudiantes:
    print("Maria está en la lista")

# Eliminar un estudiante de la lista
estudiantes.remove("Pedro")
print(estudiantes)  # ['Juan', 'Maria', 'Ana' , 'Luisa', 'Carlos', 'Sofia', 'Diego', 'Valentina', 'Andres', 'Camila']

# Mostrar la cantidad actualizada
print("Ahora hay", len(estudiantes), "estudiantes en la lista")