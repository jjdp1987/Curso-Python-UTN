import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def esperar_segundos(segundos):
    time.sleep(segundos)
    return f"Esperé {segundos} segundos"
print(esperar_segundos(2))