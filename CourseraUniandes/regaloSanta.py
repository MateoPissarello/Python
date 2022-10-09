#number = int(input('Enter a number : '))
#if number == int(str(number)[::-1]):
    #print(number, 'is palindrome.')
#else:
   # print(number, 'is not palindrome.')


def clasificar_regalo(id):
    resultado = " "
    if (id == int(str(id)[::-1])) and (id % 2 != 0):
        resultado = "girl"
    elif (id == int(str(id)[::-1])) and (id % 2 == 0):
        resultado = "boy"
    elif (id % 2 == 0) and (id != int(str(id)[::-1])):
        resultado = "man"
    elif (id % 2 != 0) and (id != int(str(id)[::-1])):  
        resultado = "woman"
    return print(resultado)

clasificar_regalo(33)