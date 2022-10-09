

def isPrimeNumber(number):
    #retornar True si el numero es primo. False si no es primo.
    if number == 1 or number == 0:
        return False
    isPrime = True
    for divisor in range(2,number):
        if number % divisor == 0:
            isPrime = False
            return isPrime
    
    return isPrime


contPrimeNumber = 0
numberToEvaluate = 1
sumPrimeNumbers = 0
sumPrimeFound = False
while not sumPrimeFound:
    if isPrimeNumber(numberToEvaluate):
        contPrimeNumber = contPrimeNumber  + 1
        sumPrimeNumbers = sumPrimeNumbers + numberToEvaluate
        print(numberToEvaluate, sumPrimeNumbers, isPrimeNumber(sumPrimeNumbers))
        if isPrimeNumber(sumPrimeNumbers) and contPrimeNumber >=2:

            sumPrimeFound = True
    numberToEvaluate = numberToEvaluate + 1


#identificar la primera secuencia de numeros primos cuya suma
#tambien es prima