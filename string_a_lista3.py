'''Datos que hay que pedir: nombre, DNI, Nota1, Nota2, Nota3'''

#--preguntamos primero cuantos alumnos va a introducir
total_alumnos=int(input("Cuantos alumnos vas a introducir:"))
#--creamos la tabla donde se ven a guardar los datos
datos=[]
#--creamos un bucle que vaya metiendo los datos del alumno conforme el formato que nos dan
for i in range(total_alumnos):
    info=[input("Nombre: "), input("DNI: "),float(input("Nota1: ")),
        float(input("Nota2: ")), float(input("Nota3: "))]
    datos.append(info)

print(datos)
#--creamos bucle para sacar el dni y la media del listado general

for i in range(len(datos)):
    media=0
    suma=0
    for j in range(2,5):
        suma+=datos[i][j]
    media=suma/3
    print(f"El alumno con DNI {datos[i][0]} tiene una media de {round(media,2)}")
    #print(f"El alumno con DNI {datos[i][0]} tiene una media de {media:.2f}")   otra forma de redondear a 2