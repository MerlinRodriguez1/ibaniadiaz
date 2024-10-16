import matplotlib.pyplot as plt

# Gráfico de Barras (Ventas de productos electrónicos)
def grafico_barras():
    categorias = ['Teléfonos', 'Laptops', 'Tablets', 'Cámaras']
    ventas = [500, 300, 150, 100]

    plt.bar(categorias, ventas, color='skyblue')
    plt.title('Ventas por Categoría de Producto')
    plt.xlabel('Categoría de Producto')
    plt.ylabel('Cantidad Vendida')
    plt.show()

# Gráfico de Líneas (Precios de la vivienda)
def grafico_lineas():
    años = [2010, 2012, 2014, 2016, 2018, 2020]
    precios = [150000, 160000, 170000, 180000, 195000, 210000]

    plt.plot(años, precios, marker='o', linestyle='-', color='red')
    plt.title('Evolución de Precios de la Vivienda')
    plt.xlabel('Año')
    plt.ylabel('Precio Promedio ($)')
    plt.show()

# Gráfico Circular (Películas populares)
def grafico_circular():
    generos = ['Acción', 'Comedia', 'Drama', 'Ciencia Ficción']
    cantidad_peliculas = [35, 40, 25, 15]

    plt.pie(cantidad_peliculas, labels=generos, autopct='%1.1f%%', startangle=90, 
            colors=['red', 'lightgreen', 'lightcoral', 'lightskyblue'])
    plt.title('Distribución de Géneros de Películas')
    plt.show()

# Llamada a las funciones
grafico_barras()
grafico_lineas()
grafico_circular()
