def gradingStudents(nota):

    #Bucle para recorrer todos los elementos de la lista
    for nota in lista:

        #Primero comparamos si la nota es un suspenso o un aprobado
        if nota < 40:
            #Si es suspenso simplemente devuelve la nota tal y como se introdujo
            print("Su nota es un suspenso: " + str(nota))
        
        else:
            #Si es aprobado puede ser redondeada o no
            n = 0

            #Este bucle  calculara el múltiplo de 5 siguiente a la nota
            while n < nota:
                n = n + 5
            
            #Aquí calculamos la diferencia entre el múltiplo de 5 y la nota introducida
            diferencia = n - nota

            #Si la diferencia es mayor que 3 la nota se queda igual
            if diferencia > 3:
                nota = nota
                print("Su nota es un aprobado, pero no fue redondeada: " + str(nota))
            
            #Si es menor que 3 la nota se redondea sumando la diferencia previamente calculada
            else:
                nota = nota + diferencia
                print("Su nota es un aprobado y fue redondeada a un: " + str(nota))


if __name__ == "__main__":

    n = int(input("¿Cuántas notas vas a introducir?: "))
    lista = []
    
    for i in range(n):
        nota = int(input("Introduce tu nota: "))
        lista.append(nota)

    gradingStudents(nota)



