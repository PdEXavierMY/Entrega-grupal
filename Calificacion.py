def gradingStudents():
    if nota < 40:
        print("Su nota es un suspenso: " + str(nota))
    
    else:
        n = 0
        while n < nota:
            n = n + 5
        
        diferencia = n - nota

        if diferencia > 3:
            nota = nota
            print("Su nota es un aprovado, pero no fue redondeada: " + str(nota))
        
        else:
            nota = nota + diferencia
            print("Su nota es un aprovado y fue redondeada a un: " + str(nota))

if __name__ == "__main__":
    nota = int(input("Introduce tu nota: "))
    gradingStudents()



