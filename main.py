import os.path
import shutil
import urllib.request
from getpass import getuser


def pathCarpetaDomini(url):
    global domini
    # SEPARAR LA URL EN '/'
    nomCarpetaURLBarra = url.split("/")

    # EL 3 LLOC SEMPRE SERÀ EL NOM DEL DOMINI
    try:
        domini = nomCarpetaURLBarra[2]
    except:
        # MISSATGE SI LA URL NO TÉ 3r LLOC, PER TANT, NO ÉS UNA URL
        print("URL incorrecta")

    # RETORNEM EL PATH DE LA CARPETA DEL DOMINI
    return "/home/" + getuser() + "/URLDownloaderRiba/" + domini


def generarCarpetaDomini(url):
    # DEFINIR EL PATH DE LA CARPETA DEL PROGRAMA
    pathCarpetaPrograma = "/home/" + getuser() + "/URLDownloaderRiba"
    existeixPathCarpetaPrograma = os.path.exists(pathCarpetaPrograma)

    # SI LA CARPETA NO ESTA CREADA, LA CREEM
    if not existeixPathCarpetaPrograma:
        os.mkdir(pathCarpetaPrograma)

    # DEFINIR EL PATH DE LA CARPETA DEL DOMINI
    pathCarpetaWeb = pathCarpetaDomini(url)
    existeixPathCarpetaWeb = os.path.exists(pathCarpetaWeb)

    # SI LA CARPETA NO ESTA CREADA, LA CREEM
    if not existeixPathCarpetaWeb:
        os.mkdir(pathCarpetaWeb)


def nomPartFinalUrl(url):
    # SEPAREM LA URL EN '/'
    urlArray = url.split("/")

    # LA PART FINAL DE LA URL SERÀ LA LLARGADA -1
    numeroPartFinal = (len(urlArray) - 1)

    # DEFINIM QUINA SERÀ LA APRT FINAL DE LA URL
    partFinal = urlArray[numeroPartFinal]

    # RETORNEM LA PART FINAL
    return partFinal


def generarFitxer(url):
    # DEFINIM EL PATH DEL FITXER QUE GENERAREM AMB EL NOM CORRECTE
    pathFitxer = pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + ".html"

    # CONTINGUT QUE VOLEM ESCRIURE
    connexio = urllib.request.urlopen(url)
    contingut = connexio.read().decode('UTF-8')

    # CREEM EL FITXER
    if not existeixFitxer(url):
        fEscriure = open(pathFitxer, "w")
        fEscriure.write(contingut)
        fEscriure.close()


def actualitzarFitxer(url):
    # DEFINIM EL PATH DEL FITXER
    pathFitxer = pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + ".html"
    # SI EL FITXER EXISTEIX
    if os.path.exists(pathFitxer):
        # BORREM LA CARPETA DEL DOMINI
        shutil.rmtree(pathCarpetaDomini(url))
        # GENEREM LA CARPETA DEL DOMINI
        generarCarpetaDomini(url)
        # CREEM EL FITXER
        generarFitxer(url)
        print("URL actualitzada")
        print()
    # SI EL FITXER NO EXISTEIX
    else:
        # INFORMEM QUE LA URL NO HA ESTAT DESCARREGADA
        print("URL no descarregada")


def existeixFitxer(url):
    # DEFINIM EL PATH DEL FITXER
    pathFitxer = pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + ".html"
    # RETORNEM SI EL PATH EXISTEIX
    return os.path.exists(pathFitxer)


def generarCopiafitxerActual(url):
    # DEFINIM EL FITXER QUE VOLEM COPIAR
    fitxerAntic = open(pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + ".html")
    # DEFINIM LA COPIA DEL FITXER
    fitxerNouE = open(pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + "-OLD-" + getValorOLD(url) + ".html", "w")
    # ESCRIVIM AL NOU FITXER
    fitxerNouE.write(fitxerAntic.read())
    # TANQUEM ELS FITXERS
    fitxerAntic.close()
    fitxerNouE.close()
    # BORREM EL FITXER ANTIC
    os.remove(pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + ".html")


def getValorOLD(url):
    # DEFINIM EL VALOR DE OLD QUE TINDRÀ LA COPIA
    valorDeOLD = 1

    while True:
        # DEFINIM EL PATH DEL FITXER
        pathFitxerOLD = pathCarpetaDomini(url) + "/" + nomPartFinalUrl(url) + "-OLD-" + str(valorDeOLD) + ".html"
        # SI EL PATH NO EXISTEIX, VOL DIR QUE EL VALOR ES CORRECTE
        if not os.path.exists(pathFitxerOLD):
            # RETORNEM EL VALOR DE OLD
            return str(valorDeOLD)
        # AUGMENTAR EL VALOR DE OLD PER A QUE PUGUI TROBAR QUAN NO ESTA CREAT
        valorDeOLD += 1


def descarregarURL():
    # PREGUNTAR LA URL QUE VOLEM DESCARERGAR
    urlDescarregar = input("Posa la URL a descarregar: ")
    print()
    # SI EL FITXER JA EXISTEIX
    if existeixFitxer(urlDescarregar):
        # GENERAR UNA COPIA DEL FITXER I BORRAR L'ANTERIOR
        generarCopiafitxerActual(urlDescarregar)
        print("El fitxer '" + nomPartFinalUrl(urlDescarregar) + ".html' ara s'anomena '" + nomPartFinalUrl(urlDescarregar) + "-OLD-" + getValorOLD(urlDescarregar) + ".html")
        print()
        # GENERAR EL NOU FITXER
        generarFitxer(urlDescarregar)
        print("S'ha creat el fitxer '" + nomPartFinalUrl(urlDescarregar) + ".html'")
        print()
    # SI EL FITXER NO EXISTEIX
    else:
        # CREAR CARPETA DEL DOMINI, JA QUE NO ESTARÀ CREADA

        generarCarpetaDomini(urlDescarregar)
        print("S'ha generat la carpeta del domini '" + urlDescarregar.split("/")[2]+"'")
        print()
        # GENEREM EL FITXER
        generarFitxer(urlDescarregar)
        print("S'ha creat el fitxer '" + nomPartFinalUrl(urlDescarregar) + ".html'")
        print()



def menuInicial():
    # BUCLE ACABAR EL PROGRAMA
    bucleInicial = 5
    # MENU INICIAL
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
            descarregarURL()

        if opcio == 3:
            urlActualitzar = input("Posa la URL a actualitzar: ")
            actualitzarFitxer(urlActualitzar)


""""MAIN"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
menuInicial()
