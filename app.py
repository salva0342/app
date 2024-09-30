import streamlit as st

# 1. Función de saludo simple
def saludar(nombre):
    return f"Hola, {nombre}"

# 2. Suma de dos números
def sumar(a, b):
    return a + b

# 3. Área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# 4. Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * (descuento / 100))
    precio_final = precio_descuento + (precio_descuento * (impuesto / 100))
    return precio_final

# 5. Suma de una lista de números
def sumar_lista(lista):
    return sum(lista)

# 6. Función con valores predeterminados (Producto)
def producto(nombre, cantidad=1, precio=10):
    return cantidad * precio

# 7. Números pares e impares
def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

# 8. Multiplicación con *args
def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# 9. Información personal con **kwargs
def informacion_personal(**kwargs):
    return kwargs

# 10. Calculadora flexible
def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "No se puede dividir por cero"

# Interfaz de la Aplicación con Streamlit
st.sidebar.title("Ejercicios de Funciones")
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", 
                                 ["Saludo Simple", "Suma de dos números", "Área de un triángulo", 
                                  "Calculadora de descuento", "Suma de una lista", 
                                  "Producto con valores predeterminados", "Números pares e impares", 
                                  "Multiplicación con *args", "Información personal con **kwargs", 
                                  "Calculadora flexible"])

# 1. Saludo Simple
if ejercicio == "Saludo Simple":
    st.title("Saludo Simple")
    nombre = st.text_input("Ingresa tu nombre")
    if nombre:
        st.write(saludar(nombre))

# 2. Suma de dos números
elif ejercicio == "Suma de dos números":
    st.title("Suma de dos números")
    num1 = st.number_input("Número 1", value=0)
    num2 = st.number_input("Número 2", value=0)
    st.write("La suma es:", sumar(num1, num2))

# 3. Área de un triángulo
elif ejercicio == "Área de un triángulo":
    st.title("Área de un Triángulo")
    base = st.number_input("Base", value=0.0)
    altura = st.number_input("Altura", value=0.0)
    st.write("El área del triángulo es:", calcular_area_triangulo(base, altura))

# 4. Calculadora de descuento
elif ejercicio == "Calculadora de descuento":
    st.title("Calculadora de Descuento")
    precio = st.number_input("Precio del producto", value=0.0)
    descuento = st.number_input("Porcentaje de descuento", value=10)
    impuesto = st.number_input("Porcentaje de impuesto", value=16)
    st.write("El precio final es:", calcular_precio_final(precio, descuento, impuesto))

# 5. Suma de una lista de números
elif ejercicio == "Suma de una lista":
    st.title("Suma de una Lista de Números")
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if numeros:
        lista = [float(num) for num in numeros.split(",")]
        st.write("La suma de los números es:", sumar_lista(lista))

# 6. Producto con valores predeterminados
elif ejercicio == "Producto con valores predeterminados":
    st.title("Producto con Valores Predeterminados")
    nombre_producto = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10)
    st.write("El precio total es:", producto(nombre_producto, cantidad, precio))

# 7. Números pares e impares
elif ejercicio == "Números pares e impares":
    st.title("Números Pares e Impares")
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if numeros:
        lista = [int(num) for num in numeros.split(",")]
        pares, impares = numeros_pares_e_impares(lista)
        st.write("Números pares:", pares)
        st.write("Números impares:", impares)

# 8. Multiplicación con *args
elif ejercicio == "Multiplicación con *args":
    st.title("Multiplicación con *args")
    numeros = st.text_input("Ingresa números separados por comas")
    if numeros:
        lista = [int(num) for num in numeros.split(",")]
        st.write("El resultado de la multiplicación es:", multiplicar_todos(*lista))

# 9. Información personal con **kwargs
elif ejercicio == "Información personal con **kwargs":
    st.title("Información Personal con **kwargs")
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if nombre and direccion:
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
        st.write(info)

# 10. Calculadora flexible
elif ejercicio == "Calculadora flexible":
    st.title("Calculadora Flexible")
    num1 = st.number_input("Número 1", value=0.0)
    num2 = st.number_input("Número 2", value=0.0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicacion", "division"])
    st.write("El resultado es:", calculadora_flexible(num1, num2, operacion))
