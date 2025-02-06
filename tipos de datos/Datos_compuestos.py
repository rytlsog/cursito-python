#creacion de lista (se puede modificar)
lista = ["lucas" , "lucas dalto" , 1.79 , True]

#imprimir (0 al 9)
#print(List[3])

#creacion de tupla (no se puede modificar)
tupla = ["lucas" , "lucas dalto" , 1.79 , True]

#esto es valido
lista[3] = "maquinola"

#esto no es valido
#tupla[3] = "maquinola"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"lucas" , "lucas dalto" , 1.79 , True}

#print(conjunto[3]) -> no puede acceder al elemento

#print(conjunto)

#creando un diccionario (dict) (estructura de dict key : value y separamos con coma  )
diccionario = {
    'nombre' : "noe antonio",
    'canal' : "noe antonio",
    'estas feliz' : True,
    'altura' : 1.89,
    'dato_duplicado' : "noe antonio"   
}

print(diccionario['nombre'])