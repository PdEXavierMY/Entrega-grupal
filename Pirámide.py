def piramide():
    #Esto recorre las n filas de la pirámide poniendo los espacios y hastags en el lugar correspondiente para formar la pirámide
    for i in range(n):
        print(" " * (n - i - 1) + "# " * (i + 1))
        print("\n")
        
if __name__ == "__main__":
    #Esto pedirá al usuario un número para definir la altura y base que tendrá nuestra pirámide
    n = int(input("Introduce la altura de la pirámide: ")) 
    print("\n")
    piramide()
