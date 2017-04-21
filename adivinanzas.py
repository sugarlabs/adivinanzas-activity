# -*- coding: utf-8 -*-
import narrativa
import sys

# Definimos una funcion que usaremos varias veces
def leer(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    
    # Ahora tenemos todo el contenido del archivo en la variable "cuerpo".
    cuerpo = unicode(archivo.read())
    cuerpo.decode("utf-8")
    # unicode() transforma el string en un string con soporte de acentos
    # decode() descifra los acentos desde los archivos

    # "lineas" es una lista de strings representando cada linea del archivo.
    lineas = cuerpo.splitlines()

    return lineas 

# Vamos a leer los datos que necesitamos
adivinanza = leer("data/adivinanzas.txt")
correctas = leer("data/correctas.txt")
infodato = leer("data/infodatos.txt")
fondo = leer("data/fondo.txt")
musica = leer("data/musica.txt")

# Este es el objeto encargado de pintar en la pantalla
nv = narrativa.Visual()

aviso = "\n\n\n --- Presiona cualquier tecla para continuar ---"

# "i" va a ser el numero de linea que estamos usando, entre 0 y el total.
for i in range(0, len(adivinanza)):
    
    # primero dibujamos la imagen de fondo
    nv.fondo(fondo[i])

    # ponemos musica
    nv.reproducir(musica[i])

    # colocamos la adivinanza
    nv.imprimir(adivinanza[i])

    while True:
        respuesta = nv.preguntar(u"¿quien soy? ")

        if respuesta in correctas[i].split(","):
            nv.silencio()
            nv.imprimir(u"¡Acertaste!" + aviso)
            nv.esperar()
            nv.imprimir(infodato[i] + aviso, mini=True, 
                        fondo=narrativa.GRIS_CLARO, color=narrativa.GRIS_OSCURO)
            nv.esperar()
            break
        else:
            nv.imprimir(u"¡Intenta otra vez!" + aviso)
            nv.esperar()
            nv.limpiar()
            nv.imprimir(adivinanza[i])

nv.imprimir(u"¡Gracias por jugar!\n\nPresiona una tecla para terminar el juego.")
nv.esperar()
sys.exit()
