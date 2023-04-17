'''Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.
Supón ahora que tu input es un string como este:
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string.'''
#--Los inputs son los datos de los alumnos que irán a listas individuales
lista1=[["david_fernandez"],["12311267A"],[43527],[2,9.1,7.6,2.4]]
lista2=[["maria_garcia"],["12316487A"],[43527],[2,7.1,8.6,5.4]]
lista3=[["juan_perez"],["647829236A"],[43527],[2,8.1,8.5,8.4]]
#--Creamos una lista de cada alumno y obtenemos la nota media
notas1=lista1[3]
notamedia1=sum(notas1)/len(notas1)
notas2=lista2[3]
notamedia2=sum(notas2)/len(notas2)
notas3=lista3[3]
notamedia3=sum(notas3)/len(notas3)
#--Añadimos la nota media a cada lista
lista1.append(notamedia1)
lista2.append(notamedia2)
lista3.append(notamedia3)
#--Hacemos una lista general de todos los alumnos de la cual tendremos que sacar la nota media y el dni
lista_general=lista1+lista2+lista3
print(f"{lista_general[1]}, tiene una nota media de: {lista_general[4]}\n {lista_general[6]},tiene una nota media de: {lista_general[9]}\n {lista_general[11]}, tiene una nota media de: {lista_general[14]}")

'''nota=0
notaFinal=0
media=0
for i in range (len(lista1[3])):
    nota=float(lista1[3][i])
    notaFinal+=nota
    media=notaFinal/len(lista1[3])
print(media)'''

'''nota_media1=sum(lista1[3])/len(lista1[3])
nota_media2=sum(lista2[3])/len(lista2[3])
nota_media3=sum(lista3[3])/len(lista3[3])'''


