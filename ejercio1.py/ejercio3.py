"""
La secuencia de Fibonacci se usa tradicionalmente para explicar la recursividad del árbol.
function fibonacci(n) {
 if(n==0 || n == 1)
 return n;
 return fibonacci(n-1) + fibonacci(n-2);
}
Este algoritmo cumple bien su propósito educativo pero es tremendamente ineficiente , no
solo por la recursividad, sino porque invocamos la función de Fibonacci dos veces, y la rama
derecha de la recursividad (ie fibonacci(n-2)) recalcula todos los números de Fibonacci ya
calculados por la rama izquierda (ie fibonacci(n-1)) .
Este algoritmo es tan ineficiente que el tiempo para calcular cualquier número de Fibonacci
por encima de 50 es simplemente demasiado. Puedes ir por una taza de café o ir a dormir una
siesta mientras esperas la respuesta. Pero si lo intenta aquí en Code Wars, lo más probable es
que obtenga un código de tiempo de espera antes de cualquier respuesta.
Para este Kata en particular, queremos implementar la solución de memorización . Esto será
genial porque nos permitirá seguir usando el algoritmo de recursión de árbol mientras lo
mantenemos lo suficientemente optimizado para obtener una respuesta muy rápidamente.
El truco de la versión memorizada es que mantendremos una estructura de datos de caché
(probablemente una matriz asociativa) donde almacenaremos los números de Fibonacci a
medida que los calculamos. Cuando se calcula un número de Fibonacci, primero lo buscamos
en el caché, si no está allí, lo calculamos y lo ponemos en el caché, de lo contrario, devolvemos
el número almacenado en caché.
Refactorice la función en una función de Fibonacci recursiva que, al usar una estructura de
datos memorizada, evita las deficiencias de la recursividad del árbol. ¿Puedes hacer que la
memoria caché sea privada para esta función?
"""
from ast import main

def fibonacci(n):
    "n es el numero de la secuencia de fibonacci"
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        if n == 0 or n == 1:
            return n
        else:
            cache[n] = fib(n-1) + fib(n-2)
            return cache[n]
    return fib(n)

print(fibonacci(100))

if __name__ == '__main__':
    main()