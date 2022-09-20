import os.path
import urllib.request
from getpass import getuser

def pathCarpetaDomini(url):
    """SEPARAR LA URL EN '/'"""
    nomCarpetaURLBarra = url.split("/")
    """EL 3r VALOR DE L'ARRAY ES EL NOM DEL DOMINI
        
        POSEM UN TRY PER SI NO HI HA 3ra POSICIO, PER TANT, NO SERA UNA URL"""
    try:
        domini = nomCarpetaURLBarra[2]
    except:
        print("URL incorrecta")
        """RETORNEM LA RUTA DE LA CARPETA AMB EL NOM DEL DOMINI"""
    return "/home/" + getuser() + "/URLDownloaderRiba/" + domini

def generarCarpetaDomini(url):
    """MIRAR SI ESTA LA CARPETA DEL PROGRAMA"""
    pathCarpetaPrograma = "/home/" + getuser() + "/URLDownloaderRiba"
    existeixPathCarpetaPrograma = os.path.exists(pathCarpetaPrograma)
    """LA CREEEM SI NO ESTA CREADA"""
    if not (existeixPathCarpetaPrograma):
        os.mkdir(pathCarpetaPrograma)
        print("S'ha creat el directori del programa")
    """MIRAR SI ESTA LA CARPETA DEL DOMINI"""
    pathCarpetaWeb = pathCarpetaDomini(url)
    existeixPathCarpetaWeb = os.path.exists(pathCarpetaWeb)
    """LA CREEEM SI NO ESTA CREADA"""
    if not (existeixPathCarpetaWeb):
        os.mkdir(pathCarpetaWeb)
        print("S'ha creat el directori del domini")


def nomPartFinalUrl(url):

    urlArray = url.split("/")
    numeroPartFinal = (len(urlArray)-2)
    partFinal = urlArray[numeroPartFinal]
    return partFinal


def generarFitxer(url):
    """GENEREM EL PATH DEL FITXER I AGEFIM LA PART FINAL DE LA URL + '.html'"""
    pathFitxer = pathCarpetaDomini(url) + "/"+nomPartFinalUrl(url)+".html"
    """BUSQUEM EL CONTINGUT QUE VOLEM COPIAR AL FITXER"""
    connexio = urllib.request.urlopen(url)
    contingut = connexio.read().decode('UTF-8')
    """CREEM EL FITXER"""
    if not existeixFitxer(url):
        fEscriure = open(pathFitxer, "w")
        fEscriure.write(contingut)
        fEscriure.close()
        print("S'ha creat el fitxer")


def actualitzarFitxer(url):
    """GENEREM EL PATH DEL FITXER I AGEFIM LA PART FINAL DE LA URL + '.html'"""
    pathFitxer = pathCarpetaDomini(url)+"/"+nomPartFinalUrl(url)+".html"
    """SI EL FITXER EXISTEIX, L'ELIMINEM I GENEREM UN DE NOU"""
    if existeixFitxer(url):
        os.remove(pathFitxer)
        generarFitxer(url, pathCarpetaDomini(url))
        print("El fitxer ha estat actualitzat")
    else:
        print("URL no descarregada")

def existeixFitxer(url):

    pathFitxer= pathCarpetaDomini(url)+"/"+nomPartFinalUrl(url)+".html"
    return os.path.exists(pathFitxer)

def generarCopiafitxerActual(url):
    print()
    fitxerAntic = open(pathCarpetaDomini(url)+"/"+nomPartFinalUrl(url)+".html")
    fitxerNouE = open(pathCarpetaDomini(url)+"/"+nomPartFinalUrl(url)+"-OLD-1.html","w")
    fitxerNouE.write(fitxerAntic.read())
    fitxerAntic.close()
    fitxerNouE.close()
    print("Ha generat la copia")
    os.remove(pathCarpetaDomini(url)+"/"+nomPartFinalUrl(url)+".html")
    print("Ha borrat el fitxer anterior")


def menuInicial():
    bucleInicial = 5
    while bucleInicial > 0:
        print("URL DOWNLOADER")
        print()
        print("1- Sortir del programa")
        print("2- Descarregar URL")
        print("3- Actualitzar URL")
        print()
        opcio = int(input("Opcio: "))

        if opcio == 1:
            bucleInicial = 0

        if opcio == 2:
            urlDescarregar = input("Posa la URL a descarregar: ")

            if existeixFitxer(urlDescarregar):
                print("El fitxer ja existeix")
                generarCopiafitxerActual(urlDescarregar)
                generarFitxer(urlDescarregar)
            else:
                generarCarpetaDomini(urlDescarregar)
                generarFitxer(urlDescarregar)

        if opcio == 3:
            urlActualitzar = input("Posa la URL a actualitzar: ")
            actualitzarFitxer(urlActualitzar)


""""MAIN"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
menuInicial()
