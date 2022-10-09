print("Proporcione los siguientes datos del libro: ")
nombreDeLibro = input("Proporcione el nombre: ")
Id = int(input("Proporciona el ID: "))
precioLibro = float(input("Proporcione el precio: "))
envioGratuito = input("Indique si el envio es gratuito (True/false): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe escribir (True/False)"

#print(f"Nombre: {nombreDeLibro} \nId: {Id} \nPrecio: {precioLibro} \nEnvio Gratuito?: {envioGratuito}")
print(f'''
    Nombre: {nombreDeLibro}
    Id: {Id}
    Precio: {precioLibro}
    Envio Gratuito?: {envioGratuito}
''')