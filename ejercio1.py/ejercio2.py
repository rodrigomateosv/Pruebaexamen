"""
El malvado gobierno de programación ha prohibido el uso de números. Su tarea, si elige
aceptarla, es devolver números, sin usar números.
Problemas:
• No puede usar literales numéricos en su código fuente.
• No puede usar la propiedad de longitud directamente en su código.
Meta:
• Tienes que devolver 'Puedo escribir números como 1, 2, 3'.
"""
from ast import main

def number():
    return "Puedo escribir números como " + chr(49) + ", " + chr(50) + ", " + chr(51)
print(number())

if __name__ == '__main__':
    main()