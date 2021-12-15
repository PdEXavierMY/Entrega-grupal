def gradingStudents():
    if nota < 40:
        print("Su nota es un suspenso: " + str(nota))
    
    else:
        n = 0
        while n < nota:
            n = n + 5
        
        diferencia = n - nota

        if diferencia > 3:
            print("Su nota es un aprovado, pero no fue redondeada: " + str(nota))
        
        else:
            print("Su nota es un aprovado y fue redondeada: " + str(nota))
            

