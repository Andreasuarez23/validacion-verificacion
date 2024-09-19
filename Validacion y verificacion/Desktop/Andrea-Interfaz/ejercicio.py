from urllib.request import urlopen 
from bs4 import BeautifulSoup


def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read()) 
   
def leeLinea(linea):
   lista = []
   for dato in linea.find_all('td'):
      lista.append(dato.get_text())
   return lista
   
def leeTabla(tabla):
    filas = []
    for fila in tabla.find_all('tr'):
       filas.append(leeLinea(fila))
    return filas
    
    
miDir = "https://es.wikipedia.org/wiki/Honolulu"
laSopa = bajar(miDir)
lasTablas = laSopa.find_all("table")
#
tablaClima = lasTablas[2]
tabla = leeTabla(tablaClima)
print (tabla)
#print(tabla[1])
lista_dicc=[{"nom":"Salta","ptabla":1,"tmax":1, "tmin":4},
    {"nom":"Kasgar","ptabla":1,"tmax":2, "tmin":3},
    {"nom":"Honolulu","ptabla":1,"tmax":2, "tmin":3}
    ]

def EncontrarTemperaturaMaxima(temperaturas=[]):
   maxima= float(temperaturas[0])
   for temp in temperaturas:
      if float(temp)>maxima:
         maxima=float(temp)
   return maxima


def EncontrarTemperaturaMinima(temperaturas=[]):
   minima= float(temperaturas[0])
   for temp in temperaturas:
      if float(temp)<minima:
         minima=float(temp)
   return minima

def Calcular_Diferencia_Temperatura(ciudad:any):
    miDir = f"https://es.wikipedia.org/wiki/{ciudad['nom']}"
    laSopa = bajar(miDir)
    todasLasTablas = laSopa.find_all("table")
    tablaClima = todasLasTablas[ciudad['ptabla']]
    temperaturas = leeTabla(tablaClima)
    maximaMedia=EncontrarTemperaturaMaxima(temperaturas[ciudad['tmax']])
    minimaMedia=EncontrarTemperaturaMinima(temperaturas[ciudad['tmin']])
    diferencia= maximaMedia-minimaMedia
    print(f"La diferencia de temperaturas en {ciudad['nom']} es de {round(diferencia,1)}")


for ciudad in lista_dicc:
   Calcular_Diferencia_Temperatura(ciudad)

