productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0],
}

def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if(datos[0].lower() == marca.lower()):
            total += stock[codigo][1]
    print(f"El stock total para '{marca}' es: {total}")

def busqueda_por_precio(precio_min, precio_max):
    resultados = [];
    for codigo, datos in productos.items():
        precio = stock[codigo][0]
        if precio >= precio_min and precio <= precio_max and stock[codigo][1] > 0:
            resultados.append(datos[0] + '---' + codigo)
    if resultados:
        resultados.sort();
        print('Productos encontrados: ', resultados)
    else:
        print('no hay productos en ese rango de precio')

def actualizar_precio(codigo, nuevo_precio):
    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    return False
        
def main():
    while True:
        try:
            print('---Menu---\n1.- Stock marca\n2.- Busqueda por precio\n3.- Actualizar precio\n4.- Salir')
            opc = int(input('Ingrese opcion: '))
            if opc == 1:
                marca = input('Ingrese modelo: ')
                stock_marca(marca)
            elif opc == 2:
                precio_minimo = int(input('Ingrese precio minimo: '))
                precio_maximo = int(input('Ingrese precio maximo: '))
                busqueda_por_precio(precio_minimo, precio_maximo)
            elif opc == 3:
                while True:
                    codigo = input('Ingrese modelo: ')
                    nuevo_precio = int(input('Ingrese nuevo valor: '))
                    if actualizar_precio(codigo, nuevo_precio):
                        print('Precio actualizado')
                    else:
                        print('El modelo no existe')
                    repetir = input('Desea actualizar otro precio (s/n)?: ')
                    if repetir != 's':
                        break
            elif opc == 4:
                print('Programa finalizado.')
                break
            else:
                print('Debe ingresar una opcion del menu')
        except ValueError:
            print('debe ingresar numeros enteros')

if __name__ == '__main__':
    main()