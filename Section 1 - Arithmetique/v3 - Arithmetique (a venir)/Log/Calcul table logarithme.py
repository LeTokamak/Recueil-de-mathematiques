from openpyxl import Workbook

from math import log

wb = Workbook()
ws = wb.active

Nmax = 9999
base = 10
nbDecimal = 9

Prem = int(10**(log(Nmax + 1,10) - 1))

### Mise en Page

ws.append([None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

### Calculs

def tronque(n, nbDecimal):
    return float(int(n*(10**nbDecimal)))/(10**nbDecimal)

def tronqueB(n, nbDecimal):
    return int(n/(10**nbDecimal))*(10**nbDecimal)
   
def logArrondi (n, nbDecimal):
    logExact = log(n,base)
    logMin = tronque(logExact, nbDecimal)
    logMaj = logMin + 10**(-1 * nbDecimal)
    
    if n - base**logMin < base**logMaj - n :
        return logMin
            
    else :
        return logMaj

def ajoutZeros(n, nbDecimal):
    for i in range(1, nbDecimal+1):
        if tronqueB(n, i) == 0 :
            return (nbDecimal-i)*'0' + str(n)
    return str(n)

def espace(n):
    r = ''
    
    for i in range(len(n)):
        if (i+1) % 3 == 0:
            r = r + n[i-2:i+1] + ' '
            
    return r


for a in range(Prem,Nmax+1):
    L = [a]
    for b in range(10):
        n = (a*10+b)/(Prem*10)
        logN = int(logArrondi(n, nbDecimal)*10**nbDecimal)
        
        L.append(espace(ajoutZeros(logN,nbDecimal)))
    ws.append(L)
    
    if (a + 1) % 50 == 0:
        ws.append([None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

wb.save("sample.xlsx")


"""
0,51
1,70

from decimal import Decimal
from decimal import localcontext

for n in range(3) :
    moy = Decimal(0)
    for a in range(10**n,10**(n+1)) :
        for b in range(a,10**(n+1)) :
            with localcontext() as ctx:
                ctx.prec = 2
                A = Decimal(a)
                B = Decimal(b)
                L = Decimal(log(A,10)) + Decimal(log(B,10))
                
                moy += Decimal((Decimal(A*B) - Decimal(10**L))/Decimal(A*B))
    
    N = Decimal(10**(n+1)-10**n)
    N2 = int(N)
    R = Decimal(Decimal(2)*moy/(N*(N+Decimal(1))))
    R2 = float(R)
    print(R)"""
