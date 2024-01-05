from openpyxl import Workbook

import math as m


wb = Workbook()
ws = wb.active

nPrem = -1800
nDern = 1800

baseLog = 10
nbDecimal = 9

derNbPremier = 2000



### Mise en Page

Intro = ["Degré", "Rad", None, None, "sin (x)", "cos (x)", "tan (x)", None,  "log |sin (x)|", "log |cos (x)|", "log |tan (x)|"]

ws.append(Intro)
ws.merge_cells(start_row=1, start_column=2, end_row=1, end_column=3)


### Fonctions


def tronque(n, nbDecimal):
    return float(int(n*(10**nbDecimal)))/(10**nbDecimal)



def tronqueEntier(x, nbChiffre):
    #Coupe un Réel x avec nbChiffre chiffres 
    
    return int(x/(10**nbChiffre))*(10**nbChiffre)


   
def FonctArrondie (n, fonct, fonctReciproque, nbDecimal):
    try :
        fonctExact = fonct(n)
        fonctMin = tronque(fonctExact, nbDecimal)
        fonctMaj = fonctMin + 10**(-1 * nbDecimal)
    
        if fonctReciproque(fonctMin) - n < fonctReciproque(fonctMaj) - n :
            return fonctMin
        else :
            return fonctMaj
    except : 
        return 404



def MiseEnPage(nb, nbChiffre, nbDecimal, Espace = True, Signe = False, Int = False):
    if "e" in str(nb) : return str(nb) ;
    
    x = round(nb,nbDecimal)
    nb = abs(nb)
    
    if Espace :
        
        nbZAv = nbChiffre - len (str(int(nb)))
        if nbZAv < 0 : return "ERREUR ! Apprend à programmer ptit con !!! nbZAv < 0" ;
        
        nbGroAv = ( nbZAv + len(str(int(nb))) ) % 3
        if nbGroAv == 0 : nbGroAv = 3 ;    
    
        strNbInt = nbZAv * "0" + str(int(nb))
        strNbFinal = strNbInt[:nbGroAv] 
        if len(str(int(nb))) != nbGroAv : strNbFinal += " " ;
        
        for i in range(len(strNbInt[nbGroAv:]) ):
            strNbFinal += strNbInt[nbGroAv + i]
            if (i+1) % 3 == 0 and i != len(strNbInt[nbGroAv:])-1:
                strNbFinal += " "
            
        if not Int :
            strNbFinal += "."
           
            decimales = str(nb)[len(str(int(nb)))+1:]
            
            for i in range (nbDecimal):
                if i < len(decimales) :
                    if i % 3 == 0 and i != 0:
                        strNbFinal += " "
                    strNbFinal += decimales[i]
                else :
                    strNbFinal += "0"
            
            
            """ 
            nbZAr = len(str(nb)[len(str(int(nb)))+1:]) - nbDecimal
            if nbZAr < 0 : return "ERREUR ! Apprend à programmer ptit con !!! nbZAr < 0" ;
            
            strNbDec = str(nb)[len(str(int(nb)))+1:] + nbZAr * "0"
            
            strNbFinal += strNbDec[0]
    
            for i in range(1, len(strNbDec)):
                strNbFinal += strNbDec[i]
                if (i+1) % 3 == 0 and i != nbDecimal-1:
                    strNbFinal += " "
            """
    
    else :
        strNbFinal = nbZAv * "0" + str(nb) + nbZAr * "0"
        
    if Signe and x < 0:
        strNbFinal = "- " + strNbFinal
    
    return strNbFinal
        

def EstPremier(n):
    d = 2
    while d*d <= n :
        if n % d == 0 :
            return False
        d += 1
    return True



def ListeNbPremierJusqua(nMax):
    n = 2
    L = []
    
    while n < nMax :
        if EstPremier(n):
            L.append(n)
        n += 1
    return L

LPremier = ListeNbPremierJusqua(derNbPremier)

def Simplification(n,d):
    
    if n == 0 : return "0",1,1,1,1 ;    
    
    nFact = []
    nNbTest = LPremier[:]
    dFact = []
    dNbTest = LPremier[:]
    
    while len(nNbTest) != 0 : #Nominateur
        for i in nNbTest:
            if n % i == 0 :
                nFact.append(i)
                n = n / i
            else :
                nNbTest.remove(i)
                
    while len(dNbTest) != 0 : #Denominateur
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

### Programme

nomi = 1
deno = 2

b = 1

nbChiffre = 1
nbDecimal = 9

for a in range(nPrem,nDern):
    
    angleDeg = a/10
    angleRad = angleDeg * m.pi/180
    strFract,nomi,deno,x,y = Simplification(a, 1800)
    
    #print(strFract)
    
    L = [angleDeg, MiseEnPage(angleRad,1,9, Signe = True),strFract, None]
    L.append( MiseEnPage( FonctArrondie(angleRad,m.sin,m.asin,12),nbChiffre, nbDecimal, Signe = True))
    L.append( MiseEnPage( FonctArrondie(angleRad,m.cos,m.acos,12),nbChiffre, nbDecimal, Signe = True))
    L.append( MiseEnPage( FonctArrondie(angleRad,m.tan,m.atan,12),3, nbDecimal, Signe = True))
    L.append( None )
    L.append( MiseEnPage( FonctArrondie(abs(m.sin(angleRad)),m.log10,exp10,12),nbChiffre, nbDecimal, Signe = True))
    L.append( MiseEnPage( FonctArrondie(abs(m.cos(angleRad)),m.log10,exp10,12),nbChiffre, nbDecimal, Signe = True))
    L.append( MiseEnPage( FonctArrondie(abs(m.tan(angleRad)),m.log10,exp10,12),3, nbDecimal, Signe = True))

    ws.append(L)
    
    if (a + 1) % 50 == 0:
        ws.append(Intro)
        b += 51
        ws.merge_cells(start_row=b, start_column=2, end_row=b, end_column=3)
 

wb.save("sample.xlsx")
