print("Hola mundo. ")
nombre: str = "Fran"
apellido: str = "Alapont"
print("Hola me llamo "+ nombre + apellido)
print(f"Hola me llamo {nombre} {apellido}")
print("---")
edad: int = 22
ciudad: str = "Valencia"
tengo_carnet: bool = True
print("---")
print(nombre.upper()+" "+apellido.lower())
print(len(nombre))
print(nombre[0])
print(nombre[-1])
print("---")
diccionario={
    "nombre": "Fran",
    "edad": 22,
    "ciudad": "Valencia",
    "solterx": True
}
print(diccionario)
print("---")
compra=["pan", "leche", "huevos"]
compra.append("frutas")
compra.insert(1, "verduras")
compra.pop(-1)
print(compra)
print("---")
culpable= True
if culpable==True:
    print("Es culpable")
else:
    print("No es culpable")
