import numpy as np
import matplotlib.pyplot as plt

moins_au_nominateur = [r'$-\pi$', r'$\frac{-5\pi}{6}$', r'$\frac{-3\pi}{4}$', r'$\frac{-2\pi}{3}$', r'$\frac{-\pi}{2}$', r'$\frac{-\pi}{3}$', r'$\frac{-\pi}{4}$', r'$\frac{-\pi}{6}$', '0', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$', r'$\pi$']

# Définir l'intervalle de x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Liste des fonctions à tracer
fonctions = [np.sin, np.cos, np.tan, np.arcsin, np.arccos, np.arctan]
noms = ['sinus', 'cosinus', 'tangente', 'arcsinus', 'arccosinus', 'arctangente']
colors = ['blue', 'red', 'green', 'blue', 'red', 'green']

plt.rcParams['text.usetex'] = True

for fonction, nom, color in zip(fonctions, noms, colors):
    
    plt.figure()
    # Tracer la fonction
    plt.plot(x, fonction(x), color=color)
    # Définir les limites de l'axe des y pour la tangente
    if fonction == np.tan:
        plt.ylim(-10, 10)
        plt.xlim(-np.pi, np.pi)
    if fonction in [np.sin, np.cos]:
        plt.ylim(-1.1, 1.1)
        plt.xlim(-np.pi, np.pi)
        plt.xticks([-np.pi, -5*np.pi/6, -3*np.pi/4, -2*np.pi/3, -np.pi/2, -np.pi/3, -np.pi/4, -np.pi/6, 0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi],
               [r'$-\pi$', r'$\frac{~}{~}\frac{5\pi}{6}~\frac{~}{~}$', r'$\frac{~}{~}\frac{3\pi}{4}$', r'$\frac{~}{~}~\frac{~}{~}\frac{2\pi}{3}$', r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{3}$', r'$-\frac{\pi}{4}$', r'$-\frac{\pi}{6}$', '0', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$', r'$\pi$'])
    # Ajouter des titres et des labels
    plt.title(f'Graphique de la fonction {nom}')
    plt.xlabel(r'$\theta$')
    if   fonction == np.sin    : plt.ylabel(r'$\sin(\theta)$')
    elif fonction == np.cos    : plt.ylabel(r'$\cos(\theta)$')
    elif fonction == np.tan    : plt.ylabel(r'$\tan(\theta)$')
    elif fonction == np.arcsin : plt.ylabel(r'$\arcsin(\theta)$')
    elif fonction == np.arccos : plt.ylabel(r'$\arccos(\theta)$')
    elif fonction == np.arctan : plt.ylabel(r'$\arctan(\theta)$')
    
    # Enregistrer le graphique
    plt.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Graphs fonctions/{nom}.png', dpi=300)