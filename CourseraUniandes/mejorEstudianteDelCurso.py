def mejor_del_salon(estudiante1:dict, estudiante2:dict, estudiante3:dict, estudiante4:dict, estudiante5:dict) -> str:
    promedioEstudiante1 = promedio(estudiante1["matematicas"],estudiante1["español"],estudiante1["ciencias"],estudiante1["literatura"], estudiante1["arte"])
    promedioEstudiante2 = promedio(estudiante2["matematicas"],estudiante2["español"],estudiante2["ciencias"],estudiante2["literatura"], estudiante2["arte"])
    promedioEstudiante3 = promedio(estudiante3["matematicas"],estudiante3["español"],estudiante3["ciencias"],estudiante3["literatura"], estudiante3["arte"])
    promedioEstudiante4 = promedio(estudiante4["matematicas"],estudiante4["español"],estudiante4["ciencias"],estudiante4["literatura"], estudiante4["arte"])
    promedioEstudiante5 = promedio(estudiante5["matematicas"],estudiante5["español"],estudiante5["ciencias"],estudiante5["literatura"], estudiante5["arte"])

    list = [promedioEstudiante1, promedioEstudiante2, promedioEstudiante3, promedioEstudiante4, promedioEstudiante5]
    
    notaMayor = 0
    for nota in list:
        if nota > notaMayor:
            notaMayor = nota
        elif nota == notaMayor:
            
    

        





def promedio (matematicas,español,ciencias,literatura,arte):
    return (matematicas + español + ciencias + literatura + arte) / 5


    