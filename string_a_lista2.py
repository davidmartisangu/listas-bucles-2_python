input_pc = '''David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n'''

#--creo una lista del string con la función split
lista_pc=input_pc.split("\n")

#--si hago len de lista veo que son 6 ya que la lista sale con vacios entre los datos de los alumnos, se quitan y se añade  a una nueva lista
lista_pc2=[]
for i in lista_pc:
    if i !="":      #--solo incluyo lo que tenga contenido
        lista_pc2.append(i)

#--crear un bucle que recorra los datos dentro de cada alumno
media=0
notas=[]
datos_total=[]

for i in lista_pc2:
    #--separar los elementos de cada dato del alumno por separado, sino lo daria a lista_pc2[0] y me daria D, quiero que me de David
    elementos=i.split()
    #--le indico que el elemento 3 es el dni
    dni=elementos[2]
    #--los numeros los entiende como strings no como floats, los paso a floats metiendolos en otra lista
    notas=[float(media) for media in elementos[5:]]
    media=round(sum(notas)/len(notas),2) #--redondeo a dos decimilas
    #--lo que piden es el dni y la media
    print(f"El alumno con DNI: {elementos[2]} tiene una nota media de {media}")
