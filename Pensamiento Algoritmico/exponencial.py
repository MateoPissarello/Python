def exponencial(x,n):
  suma=0
  for i in range(n+1):
    suma+=(x**i)/factorial(i)
  return suma

def factorial(n):
  producto=1
  for i in range(1,n+1):
    producto*=i
  return producto

def main():
  x=0
  n=0
  x=float(input("Por favor ingrese el valor al cual desea calcular la exponencial\n"))
  n=int(input("ingrese el numero de repeteciones que desea\n"))
  print("La exponencial de: "+str(x)+" es: "+str(exponencial(x,n)))

main()