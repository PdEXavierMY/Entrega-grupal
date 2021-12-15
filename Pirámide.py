#Esto pedirá al usuario un número para definir la altura y base que tendrá nuestra pirámide
n = int(input("Introduce la altura de la pirámide: ")) 

def piramide():
    for fila in range(n):
        print("." * (n - fila -1), end="")
        

piramide()