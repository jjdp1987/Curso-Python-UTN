# Se puede utilizar los f-strings para cadenas de múltiples líneas:
valor1=1000
valor2=340
suma=valor1+valor2
cadena=f"""
{valor1:5}
{valor2:5}
-----
{suma:5}
"""
print(cadena)