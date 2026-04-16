def repetir(n_veces):
    def decorador_real(funcion):
        def envoltura(*args, **kwargs):
            for i in range(n_veces):
                print(f"Ejecución {i+1}:")
            funcion(*args, **kwargs)
        return envoltura
    return decorador_real

@repetir(3)
def decir_hola(nombre):
    print(f"Hola {nombre}!")

decir_hola("Juan")