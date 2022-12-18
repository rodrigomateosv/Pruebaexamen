"""
En algunos países de la antigua Unión Soviética existía la creencia de los boletos de la
suerte. Se creía que un billete de transporte de cualquier tipo traía suerte si la suma de los
dígitos de la mitad izquierda de su número era igual a la suma de los dígitos de la mitad
derecha. Aquí hay ejemplos de tales números:
003111 # 3 = 1 + 1 + 1
813372 # 8 + 1 + 3 = 3 + 7 + 2
17935 # 1 + 7 = 3 + 5 // si la longitud es impar, debes ignorar el número del medio al
sumar las mitades.
56328116 # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Dichos boletos se comían después de usarlos o se recolectaban para fanfarronear.
Su tarea es escribir una función luck_check(str), que devuelve true/True si el argumento es una
representación decimal de cadena de un número de boleto de la suerte, o false/False para
todos los demás números. Debería arrojar errores para cadenas vacías o cadenas que no
representan un número decimal.
"""

from ast import main
def luck_check(string):
    if string == "":
        raise print("No se puede ingresar una cadena vacia")
    if not string.isdigit():
        raise ValueError("No se puede ingresar una cadena que no represente un numero")
    if len(string) % 2 == 0:
        return sum([int(i) for i in string[:len(string)//2]]) == sum([int(i) for i in string[len(string)//2:]])
    if len(string) % 2 == 1:
        return sum([int(i) for i in string[:len(string)//2]]) == sum([int(i) for i in string[len(string)//2+1:]])
    else:
        return print("Error, no se puede calcular la suma de los digitos")

print("003111",luck_check("003111"))
print("813372",luck_check("813372"))
print("17935",luck_check("17935"))
print("56328116",luck_check("56328116"))
print("5632811",luck_check("5632811")) 

if __name__ == '__main__':
    main()

