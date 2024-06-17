import excel as fExc

import math as m
from datetime import datetime, timedelta

derNbPremier = 2000

# %% Fonctions

def tronque(n, nbDecimal):
    """
    Coupe un réel n avec nbDecimal chiffres après la virgule
    """
    return float(int(n*(10**nbDecimal)))/(10**nbDecimal)

def tronqueEntier(x, nbChiffre):
    """
    Coupe un réel x avec nbChiffre chiffres significatifs
    """    
    return int(x/(10**nbChiffre))*(10**nbChiffre)
   
def FonctArrondie(n, fonct, fonctReciproque, nbDecimal):
    """
    Renvoie la valeur de la fonction fonct(n) arrondie à nbDecimal près
    Cet arrondi est le plus proche possible de la valeur exacte
    """
    try :
        yExact = fonct(n)
        yMin = tronque(yExact, nbDecimal)
        yMaj = yMin + 10**(-1 * nbDecimal)
    
        if fonctReciproque(yMin) - n < fonctReciproque(yMaj) - n :
            return yMin
        else :
            return yMaj
    except : 
        return 404

def MiseEnPage(nb, nbChiffre, nbDecimal, Espace = True, affichageSigne = False, retourneEntier = False):
    """
    Met en page un nombre en : 
        - ajoutant des 0 devant le nombre pour que le nb de chiffres devant la virgule soit égal à nbChiffre
        - ajoutant des 0 après la virgule pour que le nb de chiffres après la virgule soit égal à nbDecimal
        - ajoutant des espaces de séparation entre les groupes de chiffres (Espace = True)
        - ajoutant un signe devant le nombre (affichageSigne = True)
        - retournant un nombre entier (retourneEntier = True)
    """
    if "e" in str(nb) : 
        return str(nb)
    
    if nb == -1 : return "- 1"
    if nb == 0  : return "0"
    if nb == 1  : return "1"
    
    if nb == 404 or nb > 1_000_000_000 or nb < -1_000_000_000: return "⨉"
    
    
    
    x  = round(nb, nbDecimal)
    nb = abs(nb)
    
    if Espace :
        # Détermination du nombre de 0 à écrire devant le nombre
        nbZeroAv = nbChiffre - len(str(int(nb)))
        if nbZeroAv < 0 :
            print(nb)
            return "ERREUR ! nbZeroAv < 0"
        
        # Détermination de la taille du groupe de poids le plus fort (en se basant sur la convention d'écriture "12 054")
        nbChiffreGroupeAv = nbChiffre % 3
        if nbChiffreGroupeAv == 0 :
            nbChiffreGroupeAv = 3 

        # Écriture du nombre avec ses espaces de séparation
        strNbInt = nbZeroAv * "0" + str(int(nb))
        strNbFinal = strNbInt[:nbChiffreGroupeAv] 
        if len(str(int(nb))) != nbChiffreGroupeAv :
            strNbFinal += " "
        
        for i in range(len(strNbInt[nbChiffreGroupeAv:]) ):
            strNbFinal += strNbInt[nbChiffreGroupeAv + i]
            if (i+1) % 3 == 0 and i != len(strNbInt[nbChiffreGroupeAv:])-1:
                strNbFinal += " "
            
        if not retourneEntier :
            strNbFinal += "."
           
            decimales = str(nb)[len(str(int(nb)))+1:]
            
            for i in range (nbDecimal):
                if i < len(decimales) :
                    if i % 3 == 0 and i != 0:
                        strNbFinal += " "
                    strNbFinal += decimales[i]
                else :
                    strNbFinal += "0"
    
    else :
        strNbFinal = nbZeroAv * "0" + str(nb) + nbDecimal * "0"
        
    if affichageSigne and x < 0:
        strNbFinal = "- " + strNbFinal
    
    strNbFinal = strNbFinal.replace(" .", ".")
    strNbFinal = strNbFinal.replace(".", ",")
    
    return strNbFinal
        
def EstPremier(n):
    """
    Renvoie True si n est premier, False sinon
    """
    d = 2
    while d*d <= n :
        if n % d == 0 :
            return False
        d += 1
    return True

def ListeNbPremierJusqua(nMax):
    """
    Renvoie la liste des nombres premiers jusqu'à nMax
    """
    n = 2
    L = []
    
    while n < nMax :
        if EstPremier(n):
            L.append(n)
        n += 1
    return L

LPremier = ListeNbPremierJusqua(derNbPremier)

def Simplification(n,d):
    """
    Simplifie une fraction n/d
    Renvoie une chaîne de caractère, le numérateur et le dénominateur simplifiés, les facteurs premiers du numérateur et du dénominateur
    """
    if n == 0 : return "0",1,1,1,1 ;    
    
    nFact = []
    nNbTest = LPremier[:].copy()
    dFact = []
    dNbTest = LPremier[:].copy()
    
    while len(nNbTest) != 0 : # Nominateur
        for i in nNbTest:
            if n % i == 0 :
                nFact.append(i)
                n = n / i
            else :
                nNbTest.remove(i)
                
    while len(dNbTest) != 0 : # Dénominateur
        for i in dNbTest:
            if d % i == 0 :
                dFact.append(i)
                d = d / i
            else :
                dNbTest.remove(i)
                
    for i in nFact :
        if i in dFact:
            nFact.remove(i)
            dFact.remove(i)

    for i in dFact :
        if i in nFact:
            nFact.remove(i)
            dFact.remove(i)
    
    for i in nFact :
        if i in dFact:
            nFact.remove(i)
            dFact.remove(i)

    for i in dFact :
        if i in nFact:
            nFact.remove(i)
            dFact.remove(i)
    
    nomi,deno = 1,1
    
    for i in nFact:
        nomi = nomi * i

    for i in dFact:
        deno = deno * i
    
    if nomi == 1 :
        strNomi = ""
    else :
        strNomi = str(nomi)
        
    if n < 0 :
        signe = "- "
    else :
        signe = ""
    
    if nomi == deno :
        strFract = signe + "π"
    else : 
        strFract = signe + strNomi + " π / " + str(deno)
        
    return strFract,n,d,nFact,dFact

def exp10 (x):
    return 10**x

# %% Programme

# nPrem = -1800
# nDern = 1800

nPrem = 0
nDern = 1800

baseLog = 10

nomi = 1
deno = 2

nbChiffre = 1
nbDecimal = 9

COLONNE_DEGRE      = 1
COLONNE_RADIAN     = 2
COLONNE_FRACTION_1 = 3
COLONNE_FRACTION_2 = 4
COLONNE_FRACTION_3 = 5
COLONNE_SIN        = 6
COLONNE_COS        = 7
COLONNE_TAN        = 8
COLONNE_LOG_SIN    = 9
COLONNE_LOG_COS    = 10
COLONNE_LOG_TAN    = 11

Intro = ["Degré", "Rad", None, None, None, "sin (x)", "cos (x)", "tan (x)", "log |sin (x)|", "log |cos (x)|", "log |tan (x)|"]

wb = fExc.creation_fichier_excel()
ws = wb.active

# Premiere ligne
for e in Intro :
    cellule = ws.cell(row = 1, column = Intro.index(e) + 1)
    cellule.value = e
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_entete)
    cellule.font = fExc.police(est_en_gras = True, couleur=fExc.blanc)

ws.merge_cells(start_row=1, start_column=COLONNE_RADIAN, end_row=1, end_column=COLONNE_FRACTION_3)

angles = range(nPrem, nDern)

angles = [-1800, -1750, -1700, -1650, -1600, -1550, -1500, -1450, -1400, -1350, -1300, -1250, -1200, -1150, -1100, -1050, -1000, -950, -900, -850, -800, -750, -700, -650, -600, -550, -500, -450, -400, -350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800] 

for a in angles:
    
    angleDeg = a/10
    angleRad = angleDeg * m.pi/180
    strFract,nomi,deno,x,y = Simplification(a, 1800)

    i = angles.index(a)
    
    numLigne = 2 + a % 50 + 51*(a // 50)
    numLigne = 2 + i % 50 + 51*(i // 50)
    
    # Angle en degré
    cellule = ws.cell(row = numLigne, column = COLONNE_DEGRE)
    if str(angleDeg)[-2:] == ".0":
        cellule.value = "  "+str(angleDeg)[:-2]
    else :
        cellule.value = "  "+str(angleDeg).replace(".", ",")
        
    cellule.alignment = fExc.alignement(alignement_horizontal="l", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_degre)
    cellule.font = fExc.police(couleur=fExc.blanc, est_en_gras=True)
    
    # Angle en radian
    cellule = ws.cell(row = numLigne, column = COLONNE_RADIAN)
    cellule.value = MiseEnPage(angleRad,1,9, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_rad)
    cellule.border = fExc.bordure(style="dashed", couleur=fExc.noir, a_droite=True)
    cellule.font = fExc.police(est_en_gras=True)
    
    # Fraction
    if "/" in strFract :
        cellule = ws.cell(row = numLigne, column = COLONNE_FRACTION_1)
        cellule.value = strFract.split(" / ")[0]
        cellule.alignment = fExc.alignement(alignement_horizontal="r", alignement_vertical="c")
        cellule.fill = fExc.couleur_fond(fExc.fond_rad)
        cellule.font = fExc.police(est_en_gras=True)
        
        cellule = ws.cell(row = numLigne, column = COLONNE_FRACTION_2)
        cellule.value = "/"
        cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
        cellule.fill = fExc.couleur_fond(fExc.fond_rad)
        cellule.font = fExc.police(est_en_gras=True)
        
        cellule = ws.cell(row = numLigne, column = COLONNE_FRACTION_3)
        cellule.value = strFract.split(" / ")[1]
        cellule.alignment = fExc.alignement(alignement_horizontal="l", alignement_vertical="c")
        cellule.fill = fExc.couleur_fond(fExc.fond_rad)
        cellule.font = fExc.police(est_en_gras=True)
        cellule.border = fExc.bordure(style="medium", couleur=fExc.noir, a_droite=True)
    else :
        cellule = ws.cell(row = numLigne, column = COLONNE_FRACTION_1)
        cellule.value = strFract
        cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
        cellule.fill = fExc.couleur_fond(fExc.fond_rad)
        cellule.font = fExc.police(est_en_gras=True)
        cellule.border = fExc.bordure(style="medium", couleur=fExc.noir, a_droite=True)
        
        ws.merge_cells(start_row=numLigne, start_column=COLONNE_FRACTION_1, end_row=numLigne, end_column=COLONNE_FRACTION_3)
        
        
    # sin(x)
    cellule = ws.cell(row = numLigne, column = COLONNE_SIN)
    cellule.value = MiseEnPage( FonctArrondie(angleRad,m.sin,m.asin,12),nbChiffre, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_blanc)
    
    # cos(x)
    cellule = ws.cell(row = numLigne, column = COLONNE_COS)
    cellule.value = MiseEnPage( FonctArrondie(angleRad,m.cos,m.acos,12),nbChiffre, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_colonne)
    
    # tan(x)
    cellule = ws.cell(row = numLigne, column = COLONNE_TAN)
    cellule.value = MiseEnPage( FonctArrondie(angleRad,m.tan,m.atan,12),3, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_blanc)
    cellule.border = fExc.bordure(style="double", couleur=fExc.noir, a_droite=True)
    
    # log |sin(x)|
    cellule = ws.cell(row = numLigne, column = COLONNE_LOG_SIN)
    cellule.value = MiseEnPage( FonctArrondie(abs(m.sin(angleRad)),m.log10,exp10,12),nbChiffre, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_blanc)
    
    # log |cos(x)|
    cellule = ws.cell(row = numLigne, column = COLONNE_LOG_COS)
    cellule.value = MiseEnPage( FonctArrondie(abs(m.cos(angleRad)),m.log10,exp10,12),nbChiffre, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_colonne)
    
    # log |tan(x)|
    cellule = ws.cell(row = numLigne, column = COLONNE_LOG_TAN)
    cellule.value = MiseEnPage( FonctArrondie(abs(m.tan(angleRad)),m.log10,exp10,12),nbChiffre, nbDecimal, affichageSigne = True)
    cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
    cellule.fill = fExc.couleur_fond(fExc.fond_blanc)
    
    if (i + 1) % 50 == 0:
        
        for e in Intro :
            cellule = ws.cell(row = numLigne + 1, column = Intro.index(e) + 1)
            cellule.value = e
            cellule.alignment = fExc.alignement(alignement_horizontal="c", alignement_vertical="c")
            cellule.fill = fExc.couleur_fond(fExc.fond_entete)
            cellule.font = fExc.police(est_en_gras = True, couleur=fExc.blanc)
            
        ws.merge_cells(start_row=numLigne + 1, start_column=COLONNE_RADIAN, end_row=numLigne + 1, end_column=COLONNE_FRACTION_3)

#fExc.redimensionnement_colonne_auto_optimal(ws)
ws.column_dimensions["A"].width = 1.45 * (22/4.31)
ws.column_dimensions["B"].width = 2.76 * (22/4.31)
ws.column_dimensions["C"].width = 1.41 * (22/4.31)
ws.column_dimensions["D"].width = 0.27 * (22/4.31)
ws.column_dimensions["E"].width = 1.12 * (22/4.31)

ws.column_dimensions["F"].width = 2.90 * (22/4.31)
ws.column_dimensions["G"].width = 2.90 * (22/4.31)
ws.column_dimensions["H"].width = 3.50 * (22/4.31)
ws.column_dimensions["I"].width = 2.90 * (22/4.31)
ws.column_dimensions["J"].width = 2.90 * (22/4.31)
ws.column_dimensions["K"].width = 2.90 * (22/4.31)
wb.save(f"Section 3 - Trigonometrie/v1 - Trigonometrie/Table Trigo/sample_{str(datetime.now()).replace(':', '_')}.xlsx")