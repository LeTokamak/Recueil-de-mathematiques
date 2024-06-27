import numpy as np
import matplotlib.pyplot as plt

cm = 1/2.54
epsilon = 0.00001

rapport_mdeg_rad = np.pi / 1800

nPrem = 0
nDern = 1800
x_table = range(nPrem, nDern)
x_complet = np.linspace(0, 1800, 1_000_000)
x_complet = np.linspace(0.5, 1799.5, 1800)

print(x_complet)

nbDigitsTable = 4

def approx(x_table, fct, x):
    """
    Approximation linéaire de fct(x) à partir de x_table
    """
    x_table = np.array(x_table)
    
    try :
        # Recherche des indices des deux points les plus proches de x
        x_inf = x_table[x_table <= x].max()
        x_sup = x_table[x_table >= x].min()
        
        y_inf = round(fct(rapport_mdeg_rad*x_inf),nbDigitsTable)
        y_sup = round(fct(rapport_mdeg_rad*x_sup),nbDigitsTable)

        #print(fct(rapport_mdeg_rad*x_sup), y_sup)
        # Coefficients de la droite passant par les deux points
        nomi_a = (y_sup - y_inf)
        deno_a = (rapport_mdeg_rad*x_sup - rapport_mdeg_rad*x_inf)
        
        #print(x, x_inf, x_sup)
        
        a = nomi_a / deno_a 
        b = y_inf - a * rapport_mdeg_rad*x_inf
        return a * rapport_mdeg_rad*x + b
    
    except :
        return fct(rapport_mdeg_rad*x)
    

def ecart_absolu_approx(x_table, fct, x):
    """
    Écart absolu entre fct(x) et son approximation linéaire à partir de x_table
    """
    return fct(rapport_mdeg_rad*x) - approx(x_table, fct, x)

def ecart_relatif_approx(x_table, fct, x):
    """
    Écart relatif entre fct(x) et son approximation linéaire à partir de x_table
    """
    return ecart_absolu_approx(x_table, fct, x) / fct(rapport_mdeg_rad*x)

def calcul_approximation(x_complet, fct):
    """
    Calcul de l'approximation linéaire de fct(x) à partir de x_table
    """
    return [approx(x_table, fct, x) for x in x_complet]

def calcul_ecart_absolu(x_complet, fct):
    """
    Calcul de l'écart absolu entre fct(x) et son approximation linéaire à partir de x_table
    """
    return [ecart_absolu_approx(x_table, fct, x) for x in x_complet]

def calcul_ecart_relatif(x_complet, fct):
    """
    Calcul de l'écart relatif entre fct(x) et son approximation linéaire à partir de x_table
    """
    return [ecart_relatif_approx(x_table, fct, x) for x in x_complet]

def tracer_approx(fct, label, color,
                  y_lim_1, y_lim_2,
                  x_lim_1, x_lim_2,
                  liste_ticks_x, liste_ticks_y,
                  label_ticks_x, label_ticks_y,
                  titre, nom,
                  hauteur=29.7*cm*1/1.25, largeur=21*cm*1/1.25,
                  entree = x_complet,
                  ticks_y_normal = [-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]):

    fig, ax_normal = plt.subplots(figsize=(hauteur, largeur))
    #ax_trigo = ax_normal.twinx()
    
    ax_normal.vlines(liste_ticks_x, y_lim_1, y_lim_2, color='black',alpha = 0.75, lw=1)
    ax_normal.hlines(liste_ticks_y, x_lim_1, x_lim_2, color='black',alpha = 0.75, lw=1)
    ax_normal.hlines(ticks_y_normal, x_lim_1, x_lim_2, color="black", linestyle='--', alpha=0.5, lw=0.75)
    #ax_normal.hlines(0, x_lim_1, x_lim_2, color="black", alpha=0.75, lw=1.5)
    #ax_normal.vlines(0, y_lim_1, y_lim_2, color="black", alpha=0.75, lw=1.5)
    
    ax_normal.plot(entree, calcul_ecart_absolu(entree, fct), linestyle = "", marker = ".",color = color, label=label)
    ax_normal.legend()
    
    ax_normal.set_xlim(x_lim_1, x_lim_2)
    #ax_trigo.set_ylim(y_lim_1, y_lim_2)
    #ax_normal.set_ylim(y_lim_1, y_lim_2)
    
    #ax_trigo.set_xticks(liste_ticks_x, label_ticks_x)
    #ax_trigo.set_yticks(liste_ticks_y, label_ticks_y)
    #ax_normal.set_yticks(ticks_y_normal)
    
    # Ajouter des titres et des labels
    ax_normal.set_title(titre)
    #ax_trigo.set_xlabel(r'$\theta$')
    
    # Enregistrer le graphique
    fig.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Qualité approx linéaire/{nom}.png', dpi=300, bbox_inches='tight')

tracer_approx(np.sin, r'$\sin(\theta)$', 'blue',
              -0.005, 0.005,
              0,1800,
              [], [],
              [], [],
              'Approximation linéaire de la fonction sinus', 'approximation_sin',
              entree = x_complet,
              ticks_y_normal = [])

#print(calcul_ecart_absolu(x_complet, np.sin))