import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

x = np.linspace(-2*np.pi, 2*np.pi, 10_000)
x_2 = np.linspace(-np.pi/2+0.0001, np.pi/2-0.0001, 10_000)

x_arcsin = np.linspace(-1, 1, 10_000)
x_arctan = np.linspace(-10, 10, 10_000)

cm = 1/2.54
epsilon = 0.00001

def tracer_couple_fct(fct_1, fct_2,
                      label_1, label_2, 
                      color_1, color_2,
                      y_lim_1, y_lim_2,
                      x_lim_1, x_lim_2,
                      liste_ticks_x, liste_ticks_y,
                      label_ticks_x, label_ticks_y,
                      titre, nom,
                      hauteur=29.7*cm*1/1.25, largeur=21*cm*1/1.25,
                      entree = x,
                      ticks_y_normal = [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]):

    fig, ax_normal = plt.subplots(figsize=(hauteur, largeur))
    ax_trigo = ax_normal.twinx()
    
    ax_trigo.vlines(liste_ticks_x, y_lim_1, y_lim_2, color='black',alpha = 0.75, lw=1)
    ax_trigo.hlines(liste_ticks_y, x_lim_1, x_lim_2, color='black',alpha = 0.75, lw=1)
    ax_normal.hlines(ticks_y_normal, x_lim_1, x_lim_2, color="black", linestyle='--', alpha=0.5, lw=0.75)
    ax_normal.hlines(0, x_lim_1, x_lim_2, color="black", alpha=1, lw=1.5)
    ax_normal.vlines(0, y_lim_1, y_lim_2, color="black", alpha=1, lw=1.5)
    
    ax_trigo.plot(entree, fct_1(entree), color=color_1, label=label_1)
    ax_trigo.plot(entree, fct_2(entree), color=color_2, label=label_2)
    ax_trigo.legend()
    
    ax_trigo.set_xlim(x_lim_1, x_lim_2)
    ax_trigo.set_ylim(y_lim_1, y_lim_2)
    ax_normal.set_ylim(y_lim_1, y_lim_2)
    
    ax_trigo.set_xticks(liste_ticks_x, label_ticks_x)
    ax_trigo.set_yticks(liste_ticks_y, label_ticks_y)
    ax_normal.set_yticks(ticks_y_normal)
    
    # Ajouter des titres et des labels
    ax_trigo.set_title(titre)
    ax_trigo.set_xlabel(r'$\theta$')
    
    if (titre == 'Graphique des fonctions arcsinus et arccosinus'):
        ax_trigo.plot(entree[0], fct_1(entree[0]), ".", color=color_1, markeredgewidth = 2)
        ax_trigo.plot(entree[-1], fct_1(entree[-1]), ".", color=color_1, markeredgewidth = 2)
        ax_trigo.plot(entree[0], fct_2(entree[0]), ".", color=color_2, markeredgewidth = 2)
        ax_trigo.plot(entree[-1], fct_2(entree[-1]), ".", color=color_2, markeredgewidth = 2)
    
    # Enregistrer le graphique
    fig.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Graphs fonctions/{nom}.png', dpi=300, bbox_inches='tight')
    
def tracer_fct(fct_1,
               label_1, 
               color_1,
               y_lim_1, y_lim_2,
               x_lim_1, x_lim_2,
               liste_ticks_x, liste_ticks_y,
               label_ticks_x, label_ticks_y,
               titre, nom,
               hauteur=29.7*cm*1/1.25, largeur=21*cm*1/1.25,
               entree = x_2,
               ticks_y_normal = [-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]):

    fig, ax_normal = plt.subplots(figsize=(hauteur, largeur))
    ax_trigo = ax_normal.twinx()
    
    ax_trigo.vlines(liste_ticks_x, y_lim_1, y_lim_2, color='black',alpha = 0.75, lw=1)
    ax_trigo.hlines(liste_ticks_y, x_lim_1, x_lim_2, color='black',alpha = 0.75, lw=1)
    ax_normal.hlines(ticks_y_normal, x_lim_1, x_lim_2, color="black", linestyle='--', alpha=0.5, lw=0.75)
    ax_normal.hlines(0, x_lim_1, x_lim_2, color="black", alpha=0.75, lw=1.5)
    ax_normal.vlines(0, y_lim_1, y_lim_2, color="black", alpha=0.75, lw=1.5)
    
    ax_trigo.plot(entree, fct_1(entree), color=color_1, label=label_1)
    ax_trigo.legend()
    
    ax_trigo.set_xlim(x_lim_1, x_lim_2)
    ax_trigo.set_ylim(y_lim_1, y_lim_2)
    ax_normal.set_ylim(y_lim_1, y_lim_2)
    
    ax_trigo.set_xticks(liste_ticks_x, label_ticks_x)
    ax_trigo.set_yticks(liste_ticks_y, label_ticks_y)
    ax_normal.set_yticks(ticks_y_normal)
    
    # Ajouter des titres et des labels
    ax_trigo.set_title(titre)
    ax_trigo.set_xlabel(r'$\theta$')
    
    # Enregistrer le graphique
    fig.savefig(f'Section 3 - Trigonometrie/v1 - Trigonometrie/Graphs fonctions/{nom}.png', dpi=300, bbox_inches='tight')

tracer_couple_fct(np.sin, np.cos,
                  r'$\sin(\theta)$', r'$\cos(\theta)$',
                  'blue', 'red',
                  -1.1, 1.1,
                  -np.pi, np.pi,
                  [-np.pi, -5*np.pi/6, -3*np.pi/4, -2*np.pi/3, -np.pi/2, -np.pi/3, -np.pi/4, -np.pi/6, 0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi],
                  [-1, -((3)**0.5)/2, -((2)**0.5)/2, -0.5, 0, 0.5, ((2)**0.5)/2, ((3)**0.5)/2, 1],
                  [r'$\frac{~}{~}\pi$', r'$\frac{~}{~}\frac{5\pi}{6}$', r'$\frac{~}{~}\frac{3\pi}{4}$', r'$\frac{~}{~}\frac{2\pi}{3}$', r'$\frac{~}{~}\frac{\pi}{2}$', r'$\frac{~}{~}\frac{\pi}{3}$', r'$\frac{~}{~}\frac{\pi}{4}$', r'$\frac{~}{~}\frac{\pi}{6}$', r'$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$', r'$\pi$'],
                  [r"$-1$", r"$-\frac{\sqrt{3}}{2}$", r"$-\frac{\sqrt{2}}{2}$", r"$-\frac{1}{2}$", r"$0$", r"$\frac{1}{2}$", r"$\frac{\sqrt{2}}{2}$", r"$\frac{\sqrt{3}}{2}$", r"$1$"],
                  'Graphique des fonctions sinus et cosinus', 'sinus_cosinus')

tracer_fct(np.tan,
           r'$\tan(\theta)$',
           'green',
           -5, 5,
           -np.pi/2+epsilon, np.pi/2-epsilon,
           [-np.pi/2, -5*np.pi/12, -np.pi/3, -np.pi/4, -np.pi/6, -np.pi/12, 0, np.pi/12, np.pi/6, np.pi/4, np.pi/3, 5*np.pi/12, np.pi/2],
           [-2-(3**0.5), -(3**0.5), -1, -(3**0.5)/3, -2+(3**0.5), 0, 2-(3**0.5), (3**0.5)/3, 1 ,(3**0.5), 2+(3**0.5)],
           [r'$-\frac{\pi}{2}$', r'$-\frac{5\pi}{12}$', r'$-\frac{\pi}{3}$', r'$-\frac{\pi}{4}$', r'$-\frac{\pi}{6}$', r'$-\frac{\pi}{12}$', r'$0$', r'$\frac{\pi}{12}$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{5\pi}{12}$', r'$\frac{\pi}{2}$'],
           [r'$-2-\sqrt{3}$', r'$-\sqrt{3}$', r'$-1$', r'$-\frac{\sqrt{3}}{3}$', r'$-2+\sqrt{3}$', r'$0$', r'$2-\sqrt{3}$', r'$\frac{\sqrt{3}}{3}$', r'$1$', r'$\sqrt{3}$', r'$2+\sqrt{3}$'],
           'Graphique de la fonction tangente', 'tangente')

tracer_couple_fct(np.arcsin, np.arccos,
                  r'$\arcsin(\theta)$', r'$\arccos(\theta)$',
                  'blue', 'red',
                  -np.pi/2 - (3.2-np.pi), 3.2,
                  -1.1, 1.1,
                  [-1, -((3)**0.5)/2, -((2)**0.5)/2, -0.5, 0, 0.5, ((2)**0.5)/2, ((3)**0.5)/2, 1],
                  [-np.pi/2, -np.pi/3, -np.pi/4, -np.pi/6, 0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi],
                  [r"$-1$", r"$-\frac{\sqrt{3}}{2}$", r"$-\frac{\sqrt{2}}{2}$", r"$-\frac{1}{2}$", r"$0$", r"$\frac{1}{2}$", r"$\frac{\sqrt{2}}{2}$", r"$\frac{\sqrt{3}}{2}$", r"$1$"],
                  [r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{3}$', r'$-\frac{\pi}{4}$', r'$-\frac{\pi}{6}$', r'$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$', r'$\pi$'],
                  'Graphique des fonctions arcsinus et arccosinus', 'arcsinus_arccosinus',
                  hauteur=21*cm*1/1.25, largeur=29.7*cm*1/1.25,
                  entree=x_arcsin,
                  ticks_y_normal = [3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0, -0.2, -0.4, -0.6, -0.8, -1.0, -1.2, -1.4, -1.6])

tracer_fct(np.arctan,
            r'$\arctan(\theta)$',
            'green',
            -np.pi/2, np.pi/2,
            -5, 5,
            [-2-(3**0.5), -(3**0.5), -1, -(3**0.5)/3, 0, (3**0.5)/3, 1 ,(3**0.5), 2+(3**0.5)],
            [-np.pi/2, -5*np.pi/12, -np.pi/3, -np.pi/4, -np.pi/6, 0, np.pi/6, np.pi/4, np.pi/3, 5*np.pi/12, np.pi/2],
            [r'$-2-\sqrt{3}$', r'$-\sqrt{3}$', r'$-1$', r'$-\frac{\sqrt{3}}{3}$', r'$0$', r'$\frac{\sqrt{3}}{3}$', r'$~1$', r'$\sqrt{3}$', r'$2+\sqrt{3}$'],
            [r'$-\frac{\pi}{2}$', r'$-\frac{5\pi}{12}$', r'$-\frac{\pi}{3}$', r'$-\frac{\pi}{4}$', r'$-\frac{\pi}{6}$', r'$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{5\pi}{12}$', r'$\frac{\pi}{2}$'],
            'Graphique de la fonction arctangente', 'arctangente',
            hauteur=29.7*cm*1/1.25, largeur=21*cm*1/1.25,
            entree=x_arctan, 
            ticks_y_normal = [1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0, -0.2, -0.4, -0.6, -0.8, -1.0, -1.2, -1.4])