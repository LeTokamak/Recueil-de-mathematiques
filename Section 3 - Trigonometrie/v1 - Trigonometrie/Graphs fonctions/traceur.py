import numpy as np
import matplotlib.pyplot as plt

# Définir l'intervalle de x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Liste des fonctions à tracer
fonctions = [np.sin, np.cos, np.tan, np.arcsin, np.arccos, np.arctan]
noms = ['sinus', 'cosinus', 'tangente', 'arcsinus', 'arccosinus', 'arctangente']

for fonction, nom in zip(fonctions, noms):
    plt.figure()
    # Tracer la fonction
    plt.plot(x, fonction(x))
    # Définir les limites de l'axe des y pour la tangente
    if fonction == np.tan:
        plt.ylim(-10,10)
    if fonction in [np.sin, np.cos]:
        plt.ylim(-1.1,1.1)
        plt.xlim(-np.pi, np.pi)
        
    # Ajouter des titres et des labels
    plt.title(f'Graphique de la fonction {nom}')
    plt.xlabel('theta')
    plt.ylabel(f'{nom}(x)')
    # Enregistrer le graphique
    plt.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Graphs fonctions/{nom}.png')