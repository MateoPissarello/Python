def conteo_de_materias(nombre_materia_1:str,nombre_materia_2:str,nombre_materia_3:str) -> int:
    count = 0
    materia1,materia2,materia3,materia4 = "programacion","matematica","filosofia","literatura"
    if (materia1 in nombre_materia_1) or (materia2 in nombre_materia_1) or (materia3 in nombre_materia_1) or (materia4 in nombre_materia_1):
        count +=1
    if (materia1 in nombre_materia_2) or (materia2 in nombre_materia_2) or (materia3 in nombre_materia_2) or (materia4 in nombre_materia_2):
        count +=1
    if (materia1 in nombre_materia_3) or (materia2 in nombre_materia_3) or (materia3 in nombre_materia_3) or (materia4 in nombre_materia_3): 
        count +=1
    return count

