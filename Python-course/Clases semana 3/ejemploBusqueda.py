import random 

#agregar 10 numeros aleatorios a una lista

#hacer una funcion que reciba un numero N 
#y devuelva una lista con N numeros aleatorios
#entre 0 y 100

def BuildListOfRandomNumbers(amountOfRandomNumbers, inferiorRange, superiorRange):
    listOfRandomNumbers = []
    for randomNumber in range(0,amountOfRandomNumbers):
        listOfRandomNumbers.append(random.randint(inferiorRange, superiorRange))
    return listOfRandomNumbers

def searchNumberInRandomList(numberToFind,listToSearch):
    found = False
    for index,element in enumerate(listToSearch):
        if element == numberToFind:
            return index
    return found


randomList = BuildListOfRandomNumbers(50, 0, 100)
found = searchNumberInRandomList(19, randomList)
print(randomList)
print(found)
    

