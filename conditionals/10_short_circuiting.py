# Short circuiting - Corto circuito

# Permite cerrar la ejecución del código basado en validaciones

# OR - Evalúa de izquierda a derecha si alguno es verdadero
# Flujo: si el primero o alguno de la secuencia está en True (el primero que sea True)
# entonces procede a no ejecutar lo demás del lado derecho

True or print(10)

# AND - Evalúa de izquierda a derecha que alguno sea False para entregar False; todos deben ser verdaderos
# Si alguno es False, entonces no ejecutará lo demás de la derecha
False and print(10)


# Ejemplo
name = None
print(
    name and name.upper()
)  # Permite evitar le ejecución de algo que podría llegar vacío (es uno de la cantidad de utilidades)
